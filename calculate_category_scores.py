import json
import os
from collections import defaultdict

# Path to qa_results
qa_results_path = "/Users/yunongliu/Github/CaptionQA/qa_results"

# Domains and prompts
domains = ["natural", "document", "ecommerce", "embodiedai"]
prompts = ["long", "short", "simple", "taxonomy_default"]

# Model name mapping
model_mapping = {
    "gpt-5_Qwen2.5-72B-Instruct": "GPT-5",
    "gpt-4o_Qwen2.5-72B-Instruct": "GPT-4o",
    "o4-mini_Qwen2.5-72B-Instruct": "o4-mini",
    "gemini-2.5-pro_Qwen2.5-72B-Instruct": "Gemini 2.5 Pro",
    "gemini-2.5-flash_Qwen2.5-72B-Instruct": "Gemini 2.5 Flash",
    "Claude-Sonnet-4.5_Qwen2.5-72B-Instruct": "Claude Sonnet 4.5",
    "Mistral-Small-3.1-24B-Instruct-2503_Qwen2.5-72B-Instruct": "Mistral Small 3.1",
    "Qwen3-VL-30B-A3B-Instruct_Qwen2.5-72B-Instruct": "Qwen3-VL-30B-A3B",
    "Qwen3-VL-8B-Instruct_Qwen2.5-72B-Instruct": "Qwen3-VL-8B",
    "Qwen3-VL-4B-Instruct_Qwen2.5-72B-Instruct": "Qwen3-VL-4B",
    "Qwen2.5-VL-72B-Instruct_Qwen2.5-72B-Instruct": "Qwen2.5-VL-72B",
    "Qwen2.5-VL-32B-Instruct_Qwen2.5-72B-Instruct": "Qwen2.5-VL-32B",
    "Qwen2.5-VL-7B-Instruct_Qwen2.5-72B-Instruct": "Qwen2.5-VL-7B",
    "GLM-4.1V-9B-Thinking_Qwen2.5-72B-Instruct": "GLM-4.1V-9B",
    "InternVL3_5-38B_Qwen2.5-72B-Instruct": "InternVL3.5-38B",
    "InternVL3_5-30B-A3B_Qwen2.5-72B-Instruct": "InternVL3.5-30B-A3B",
    "InternVL3_5-8B_Qwen2.5-72B-Instruct": "InternVL3.5-8B",
    "InternVL3_5-1B_Qwen2.5-72B-Instruct": "InternVL3.5-1B",
    "InternVL3-78B_Qwen2.5-72B-Instruct": "InternVL3-78B",
    "InternVL3-14B_Qwen2.5-72B-Instruct": "InternVL3-14B",
    "InternVL3-8B_Qwen2.5-72B-Instruct": "InternVL3-8B",
    "nvidia_NVLM-D-72B_Qwen2.5-72B-Instruct": "NVLM-D-72B",
    "llava-onevision-qwen2-7b-ov-hf_Qwen2.5-72B-Instruct": "LLaVA-OneVision-7B",
    "llava-1.5-7b-hf_Qwen2.5-72B-Instruct": "LLaVA-1.5-7B"
}

def calculate_category_scores(domain, prompt, model_file):
    """Calculate scores for each category from a model's results"""
    file_path = os.path.join(qa_results_path, domain, prompt, model_file)

    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as f:
        data = json.load(f)

    # Aggregate scores by category
    category_scores = defaultdict(lambda: {"correct": 0, "total": 0})

    for image_id, questions in data.items():
        for q in questions:
            if "category" in q and len(q["category"]) > 0:
                category = q["category"][0]  # Take first category
                # Extract top-level category
                top_category = category.split(" - ")[0] if " - " in category else category

                category_scores[top_category]["total"] += 1
                if q.get("is_correct", False):
                    category_scores[top_category]["correct"] += 1

    # Calculate percentages
    results = {}
    for cat, scores in category_scores.items():
        if scores["total"] > 0:
            results[cat] = round(100 * scores["correct"] / scores["total"], 2)

    return results

# Calculate for all domains
print("Calculating category-level scores...\n")

for domain in domains:
    print(f"\n{'='*60}")
    print(f"DOMAIN: {domain.upper()}")
    print(f"{'='*60}")

    for prompt in prompts:
        print(f"\nPrompt: {prompt}")
        print("-" * 60)

        # Get all available models
        all_models = list(model_mapping.keys())
        model_files = [f"{model}.json" for model in all_models]

        for model_file in model_files:
            model_name = model_mapping.get(model_file.replace(".json", ""), model_file)
            scores = calculate_category_scores(domain, prompt, model_file)

            if scores:
                print(f"\n{model_name}:")
                for cat, score in sorted(scores.items()):
                    print(f"  {cat}: {score}%")

print("\n" + "="*60)
print("Done!")
