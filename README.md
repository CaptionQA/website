# CaptionQA Leaderboard

Public leaderboard for the CaptionQA benchmark: [captionqa.github.io/website](https://captionqa.github.io/website)

---

## Adding Your Model to the Leaderboard

### Step 1: Get Your Evaluation Results

1. Download the [CaptionQA dataset](https://huggingface.co/datasets/Borise/CaptionQA)
2. Generate captions with your model
3. Email your captions (JSONL or CSV format with `image_id` and `caption` fields) to: **captionqa.team@gmail.com**
4. We will evaluate your captions and email you the results within 3-5 days

### Step 2: Submit a Pull Request

Once you receive your scores and want to add them to the public leaderboard:

1. **Fork this repository**

2. **Edit `index.html`** - Find the main leaderboard table (around line 208) and add your row

3. **Copy and fill the HTML template:**

```html
<tr>
  <td class="align-middle text-center">-<br><span class="eval-date">2025-Dec-02</span></td>
  <td class="align-middle text-center">Your Model<br><span class="affiliation">Your Org</span></td>
  <td class="align-middle text-center"><span class="badge badge-primary">Proprietary</span></td>
  <td class="align-middle text-center">7B</td>
  <td class="align-middle text-center">85.50</td>
  <td class="align-middle text-center">84.20</td>
  <td class="align-middle text-center">86.10</td>
  <td class="align-middle text-center">88.30</td>
  <td class="align-middle text-center">83.40</td>
</tr>
```

**Field Guide:**

| Field | Description | Required | Example |
|-------|-------------|----------|---------|
| Rank | Use `-` (auto-sorts by Overall) | Yes | `-` |
| Date | Evaluation date (YYYY-MMM-DD) | Yes | `2025-Dec-02` |
| Model | Your model name | Yes | `GPT-5` |
| Organization | Your affiliation (optional, use `-` if not provided) | No | `OpenAI` or `-` |
| Type | Proprietary or Open-Source (optional, use `-` if not provided) | No | `badge-primary`, `badge-success`, or `-` |
| Size | Model parameters (optional, use `-` if not provided) | No | `7B`, `72B`, or `-` |
| Overall | Overall score | Yes | `85.50` |
| Natural | Natural domain score | Yes | `84.20` |
| Document | Document domain score | Yes | `86.10` |
| E-comm | E-commerce domain score | Yes | `88.30` |
| Embodied | Embodied AI domain score | Yes | `83.40` |

**Notes:**
- For open-source models, use `<span class="badge badge-success">Open-Source</span>`
- The table auto-sorts by Overall score - just use `-` for rank
- Add your row anywhere in the `<tbody>` section
- Existing entries keep their numeric ranks (1, 2, 3...), new submissions use `-`

4. **Submit your Pull Request**

We will review and merge your PR, and your results will appear on the [public leaderboard](https://captionqa.github.io/website).

---

## Questions or Issues?

- For evaluation questions, email: captionqa.team@gmail.com
- For website issues, open an issue in this repository
- For dataset or code questions, see the [main CaptionQA repository](https://github.com/bronyayang/CaptionQA)

---

## Citation

```bibtex
@misc{yang2025captionqacaptionusefulimage,
      title={CaptionQA: Is Your Caption as Useful as the Image Itself?},
      author={Shijia Yang and Yunong Liu and Bohan Zhai and Ximeng Sun and Zicheng Liu and Emad Barsoum and Manling Li and Chenfeng Xu},
      year={2025},
      eprint={2511.21025},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2511.21025},
}
```
