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

| Field | Description | Example |
|-------|-------------|---------|
| Rank | Use `-` (auto-sorts by Overall) | `-` |
| Date | Evaluation date (YYYY-MMM-DD) | `2025-Dec-02` |
| Model | Your model name | `GPT-5` |
| Organization | Your affiliation (optional, use `-` if not provided) | `OpenAI` or `-` |
| Type | Proprietary or Open-Source (optional, use `-` if not provided) | `badge-primary`, `badge-success`, or `-` |
| Size | Model parameters (optional, use `-` if not provided) | `7B`, `72B`, or `-` |
| Overall | Overall score | `85.50` |
| Natural | Natural domain score | `84.20` |
| Document | Document domain score | `86.10` |
| E-comm | E-commerce domain score | `88.30` |
| Embodied | Embodied AI domain score | `83.40` |

**Notes:**
- For open-source models, use `<span class="badge badge-success">Open-Source</span>`
- The table auto-sorts by Overall score - just use `-` for rank
- Add your row anywhere in the `<tbody>` section
- Existing entries keep their numeric ranks (1, 2, 3...), new submissions use `-`

<details>
<summary><b>Optional but recommanded: Adding Category-Level Scores</b> (click to expand)</summary>

If you want to add category-level scores to the "Per Domain" tabs, you'll need to add rows to each domain table. To add category scores, find the corresponding domain table in `index.html` and add a row to each domain table you want to include.

<details>
<summary><b>Natural Domain Template</b></summary>

Search for `id="natural-board"` in `index.html` and add this row:

```html
<tr>
  <td class="align-middle text-center">-<br><span class="eval-date">2025-Dec-02</span></td>
  <td class="align-middle text-center">Your Model<br><span class="affiliation">Your Org</span></td>
  <td class="align-middle text-center"><span class="badge badge-primary">Proprietary</span></td>
  <td class="align-middle text-center">7B</td>
  <td class="align-middle text-center">85.50</td> <!-- Overall -->
  <td class="align-middle text-center">84.20</td> <!-- Action & Interaction -->
  <td class="align-middle text-center">83.50</td> <!-- Attribute -->
  <td class="align-middle text-center">86.30</td> <!-- Hallucination -->
  <td class="align-middle text-center">85.10</td> <!-- Object Existence -->
  <td class="align-middle text-center">84.70</td> <!-- Scene-Level -->
  <td class="align-middle text-center">82.90</td> <!-- Spatial -->
</tr>
```

</details>

<details>
<summary><b>Document Domain Template</b></summary>

Search for `id="document-board"` in `index.html` and add this row:

```html
<tr>
  <td class="align-middle text-center">-<br><span class="eval-date">2025-Dec-02</span></td>
  <td class="align-middle text-center">Your Model<br><span class="affiliation">Your Org</span></td>
  <td class="align-middle text-center"><span class="badge badge-primary">Proprietary</span></td>
  <td class="align-middle text-center">7B</td>
  <td class="align-middle text-center">86.10</td> <!-- Overall -->
  <td class="align-middle text-center">85.20</td> <!-- Chart-Specific -->
  <td class="align-middle text-center">87.30</td> <!-- Content-Level -->
  <td class="align-middle text-center">84.50</td> <!-- Diagram-Specific -->
  <td class="align-middle text-center">86.80</td> <!-- Domain-Specific -->
  <td class="align-middle text-center">85.90</td> <!-- Structural -->
  <td class="align-middle text-center">86.40</td> <!-- Table-Specific -->
</tr>
```

</details>

<details>
<summary><b>E-commerce Domain Template</b></summary>

Search for `id="ecommerce-board"` in `index.html` and add this row:

```html
<tr>
  <td class="align-middle text-center">-<br><span class="eval-date">2025-Dec-02</span></td>
  <td class="align-middle text-center">Your Model<br><span class="affiliation">Your Org</span></td>
  <td class="align-middle text-center"><span class="badge badge-primary">Proprietary</span></td>
  <td class="align-middle text-center">7B</td>
  <td class="align-middle text-center">88.30</td> <!-- Overall -->
  <td class="align-middle text-center">87.40</td> <!-- Brand & Marketing -->
  <td class="align-middle text-center">89.20</td> <!-- Contextual & Scene -->
  <td class="align-middle text-center">88.60</td> <!-- Functional -->
  <td class="align-middle text-center">87.80</td> <!-- Packaging -->
  <td class="align-middle text-center">89.10</td> <!-- Product-Level -->
  <td class="align-middle text-center">88.90</td> <!-- Textual Elements -->
  <td class="align-middle text-center">88.50</td> <!-- Visual Appearance -->
</tr>
```

</details>

<details>
<summary><b>Embodied AI Domain Template</b></summary>

Search for `id="embodiedai-board"` in `index.html` and add this row:

```html
<tr>
  <td class="align-middle text-center">-<br><span class="eval-date">2025-Dec-02</span></td>
  <td class="align-middle text-center">Your Model<br><span class="affiliation">Your Org</span></td>
  <td class="align-middle text-center"><span class="badge badge-primary">Proprietary</span></td>
  <td class="align-middle text-center">7B</td>
  <td class="align-middle text-center">83.40</td> <!-- Overall -->
  <td class="align-middle text-center">82.50</td> <!-- Activity & Task -->
  <td class="align-middle text-center">84.30</td> <!-- Functional & Semantic -->
  <td class="align-middle text-center">83.80</td> <!-- Perception -->
  <td class="align-middle text-center">82.90</td> <!-- Scene Dynamics -->
  <td class="align-middle text-center">83.70</td> <!-- Sensor & Embodiment -->
  <td class="align-middle text-center">84.10</td> <!-- Spatial & Environment -->
</tr>
```

</details>

</details>

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
