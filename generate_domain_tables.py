import json
import os
from collections import defaultdict

# Path to qa_results
qa_results_path = "/Users/yunongliu/Github/CaptionQA/qa_results"

# Domains and prompts
domains = ["natural", "document", "ecommerce", "embodiedai"]
prompts = ["long", "simple"]

# Model name mapping with affiliations and types
model_info = {
    "gpt-5_Qwen2.5-72B-Instruct": {"name": "GPT-5", "affiliation": "OpenAI", "type": "Proprietary"},
    "gemini-2.5-pro_Qwen2.5-72B-Instruct": {"name": "Gemini 2.5 Pro", "affiliation": "Google", "type": "Proprietary"},
    "gemini-2.5-flash_Qwen2.5-72B-Instruct": {"name": "Gemini 2.5 Flash", "affiliation": "Google", "type": "Proprietary"},
    "Qwen3-VL-30B-A3B-Instruct_Qwen2.5-72B-Instruct": {"name": "Qwen3-VL", "affiliation": "Alibaba", "type": "Open-Source"},
    "GLM-4.1V-9B-Thinking_Qwen2.5-72B-Instruct": {"name": "GLM-4.1V", "affiliation": "Zhipu AI", "type": "Open-Source"},
    "Qwen2.5-VL-32B-Instruct_Qwen2.5-72B-Instruct": {"name": "Qwen2.5-VL", "affiliation": "Alibaba", "type": "Open-Source"},
    "Claude-Sonnet-4.5_Qwen2.5-72B-Instruct": {"name": "Claude Sonnet 4.5", "affiliation": "Anthropic", "type": "Proprietary"},
    "InternVL3_5-38B_Qwen2.5-72B-Instruct": {"name": "InternVL3.5", "affiliation": "Shanghai AI Lab", "type": "Open-Source"}
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
                category = q["category"][0]
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

# Category ordering for each domain
category_order = {
    "natural": ["Action and Interaction", "Attribute", "Hallucination", "Object Existence", "Scene-Level Evaluation", "Spatial"],
    "document": ["Chart-Specific Elements", "Content-Level Evaluation", "Diagram-Specific Elements", "Domain-Specific Evaluation", "Structural Elements", "Table-Specific Elements"],
    "ecommerce": ["Brand and Marketing Information", "Contextual and Scene Information", "Functional Information", "Packaging and Accessories", "Product-Level Information", "Textual Elements in Image", "Visual Appearance and Presentation"],
    "embodiedai": ["Activity and Task Context", "Functional and Semantic Understanding", "Perception", "Scene Dynamics", "Sensor and Embodiment Information", "Spatial and Environment Context"]
}

# Collect all model data for each domain
domain_data = {}
for domain in domains:
    domain_data[domain] = []

    for prompt in prompts:
        for model_key, info in model_info.items():
            model_file = f"{model_key}.json"
            scores = calculate_category_scores(domain, prompt, model_file)

            if scores:
                row_data = {
                    "model": info["name"],
                    "affiliation": info["affiliation"],
                    "type": info["type"],
                    "prompt": prompt.capitalize(),
                    "scores": scores
                }
                domain_data[domain].append(row_data)

# Generate HTML for each domain
for domain in domains:
    print(f"\n{'='*80}")
    print(f"DOMAIN: {domain.upper()}")
    print('='*80)

    rank = 1
    for row in domain_data[domain]:
        badge_class = "badge-primary" if row["type"] == "Proprietary" else "badge-success"

        print(f'''                    <tr>
                      <td class="align-middle text-center">{rank}</td>
                      <td class="align-middle text-center">{row["model"]}<br><span class="affiliation">{row["affiliation"]}</span></td>
                      <td class="align-middle text-center"><span class="badge {badge_class}">{row["type"]}</span></td>
                      <td class="align-middle text-center">{row["prompt"]}</td>''', end='')

        # Add category scores in order
        for cat in category_order[domain]:
            score = row["scores"].get(cat, "-")
            if isinstance(score, float):
                print(f'''
                      <td class="align-middle text-center">{score}</td>''', end='')
            else:
                print(f'''
                      <td class="align-middle text-center">-</td>''', end='')

        print('''
                    </tr>''')

        rank += 1

    print()
