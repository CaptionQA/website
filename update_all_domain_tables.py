import re

# Read the generated domain tables HTML
with open('domain_tables_html.txt', 'r') as f:
    content = f.read()

# Split by domain sections
sections = re.split(r'={80}\nDOMAIN: (\w+)\n={80}', content)

# Extract tbody content for each domain
domain_tables = {}
for i in range(1, len(sections), 2):
    domain = sections[i].lower()
    tbody_content = sections[i+1].strip()
    domain_tables[domain] = tbody_content

# Read the current HTML file
with open('index.html', 'r') as f:
    html_content = f.read()

# Update each domain table
domains_config = {
    "natural": {
        "columns": ["Action & Interaction", "Attribute", "Hallucination", "Object Existence", "Scene-Level", "Spatial"]
    },
    "document": {
        "columns": ["Chart-Specific", "Content-Level", "Diagram-Specific", "Domain-Specific", "Structural", "Table-Specific"]
    },
    "ecommerce": {
        "columns": ["Brand & Marketing", "Contextual & Scene", "Functional Info", "Packaging & Accessories", "Product-Level", "Textual Elements", "Visual Appearance"]
    },
    "embodiedai": {
        "columns": ["Activity & Task", "Functional & Semantic", "Perception", "Scene Dynamics", "Sensor & Embodiment", "Spatial & Environment"]
    }
}

for domain, tbody_content in domain_tables.items():
    # First, update the table header to add Size and Overall columns if not present
    header_pattern = rf'(<div id="{domain}-board".*?<thead class="thead-light">.*?<tr>)'

    # Find and update header
    header_match = re.search(header_pattern, html_content, re.DOTALL)
    if header_match:
        header_section = header_match.group(0)

        # Add Size column after Type if not present
        if 'th class="align-middle text-center">Size</th>' not in header_section:
            header_replacement_pattern = rf'(<th class="align-middle text-center">Type</th>)(\s*<th class="align-middle text-center">Prompt</th>)'
            header_section = re.sub(
                header_replacement_pattern,
                r'\1\n                      <th class="align-middle text-center">Size</th>\2',
                header_section
            )

        # Add Overall column after Prompt if not present
        if 'th class="align-middle text-center' in header_section and 'Overall</th>' not in header_section:
            prompt_pattern = rf'(<th class="align-middle text-center">Prompt</th>)(\s*<th class="align-middle text-center sortable")'
            header_section = re.sub(
                prompt_pattern,
                r'\1\n                      <th class="align-middle text-center sortable" onclick="sortTable(\'' + domain + r'-table\', 5)">Overall</th>\2',
                header_section
            )

        html_content = html_content.replace(header_match.group(0), header_section)

    # Update sortable column indices
    # Find all sortTable calls for this domain's table
    table_id = f"{domain}-table"

    # Column layout after updates:
    # Rank=0, Model=1, Type=2, Size=3, Prompt=4, Overall=5, Categories start at 6

    old_indices = list(range(5, 5 + len(domains_config[domain]["columns"])))  # Old indices starting at 5
    new_indices = list(range(6, 6 + len(domains_config[domain]["columns"])))  # New indices starting at 6

    for old_idx, new_idx in zip(old_indices, new_indices):
        html_content = html_content.replace(
            f'sortTable(\'{table_id}\', {old_idx})',
            f'sortTable(\'{table_id}\', {new_idx})'
        )

    # Update tbody content
    tbody_pattern = rf'(<div id="{domain}-board".*?<tbody>)(.*?)(</tbody>)'
    html_content = re.sub(
        tbody_pattern,
        f'\\1\n{tbody_content}\n                  \\3',
        html_content,
        flags=re.DOTALL
    )

# Write updated HTML
with open('index.html', 'w') as f:
    f.write(html_content)

print("Successfully updated all domain leaderboards!")
for domain in domain_tables.keys():
    num_models = len([line for line in domain_tables[domain].split('\n') if '<tr>' in line])
    print(f"{domain.capitalize()}: {num_models} models")
