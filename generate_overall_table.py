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
    "gpt-5_Qwen2.5-72B-Instruct": {"name": "GPT-5", "affiliation": "OpenAI", "type": "Proprietary", "size": "-"},
    "gemini-2.5-pro_Qwen2.5-72B-Instruct": {"name": "Gemini 2.5 Pro", "affiliation": "Google", "type": "Proprietary", "size": "-"},
    "gemini-2.5-flash_Qwen2.5-72B-Instruct": {"name": "Gemini 2.5 Flash", "affiliation": "Google", "type": "Proprietary", "size": "-"},
    "Qwen3-VL-30B-A3B-Instruct_Qwen2.5-72B-Instruct": {"name": "Qwen3-VL", "affiliation": "Alibaba", "type": "Open-Source", "size": "30B-A3B"},
    "GLM-4.1V-9B-Thinking_Qwen2.5-72B-Instruct": {"name": "GLM-4.1V", "affiliation": "Zhipu AI", "type": "Open-Source", "size": "9B"},
    "Qwen2.5-VL-32B-Instruct_Qwen2.5-72B-Instruct": {"name": "Qwen2.5-VL", "affiliation": "Alibaba", "type": "Open-Source", "size": "32B"},
    "Claude-Sonnet-4.5_Qwen2.5-72B-Instruct": {"name": "Claude Sonnet 4.5", "affiliation": "Anthropic", "type": "Proprietary", "size": "-"},
    "InternVL3_5-38B_Qwen2.5-72B-Instruct": {"name": "InternVL3.5", "affiliation": "Shanghai AI Lab", "type": "Open-Source", "size": "38B"}
}

def calculate_overall_score(domain, prompt, model_file):
    """Calculate overall accuracy for a model on a domain"""
    file_path = os.path.join(qa_results_path, domain, prompt, model_file)

    if not os.path.exists(file_path):
        return None

    with open(file_path, 'r') as f:
        data = json.load(f)

    correct = 0
    total = 0

    for image_id, questions in data.items():
        for q in questions:
            total += 1
            if q.get("is_correct", False):
                correct += 1

    if total > 0:
        return round(100 * correct / total, 2)
    return None

# Collect all model data
all_results = []

for prompt in prompts:
    for model_key, info in model_info.items():
        model_file = f"{model_key}.json"

        # Calculate scores for each domain
        domain_scores = {}
        for domain in domains:
            score = calculate_overall_score(domain, prompt, model_file)
            if score is not None:
                domain_scores[domain] = score

        # Only add if we have all 4 domain scores
        if len(domain_scores) == 4:
            overall_score = round(sum(domain_scores.values()) / 4, 2)

            row_data = {
                "model": info["name"],
                "affiliation": info["affiliation"],
                "type": info["type"],
                "size": info["size"],
                "prompt": prompt.capitalize(),
                "overall": overall_score,
                "natural": domain_scores["natural"],
                "document": domain_scores["document"],
                "ecommerce": domain_scores["ecommerce"],
                "embodiedai": domain_scores["embodiedai"]
            }
            all_results.append(row_data)

# Sort by overall score (descending)
all_results.sort(key=lambda x: x["overall"], reverse=True)

# Generate HTML
print("<!-- Overall Leaderboard Table Body -->")
for rank, row in enumerate(all_results, 1):
    badge_class = "badge-primary" if row["type"] == "Proprietary" else "badge-success"

    print(f'''                    <tr>
                      <td class="align-middle text-center">{rank}</td>
                      <td class="align-middle text-center">{row["model"]}<br><span class="affiliation">{row["affiliation"]}</span></td>
                      <td class="align-middle text-center"><span class="badge {badge_class}">{row["type"]}</span></td>
                      <td class="align-middle text-center">{row["size"]}</td>
                      <td class="align-middle text-center">{row["prompt"]}</td>
                      <td class="align-middle text-center">{row["overall"]}</td>
                      <td class="align-middle text-center">{row["natural"]}</td>
                      <td class="align-middle text-center">{row["document"]}</td>
                      <td class="align-middle text-center">{row["ecommerce"]}</td>
                      <td class="align-middle text-center">{row["embodiedai"]}</td>
                    </tr>''')

print(f"\nTotal models: {len(all_results)}")
