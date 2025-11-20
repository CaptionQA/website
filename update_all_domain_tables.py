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
    # First, update the table header to add Size column
    header_pattern = rf'(<div id="{domain}-board".*?<thead class="thead-light">.*?<tr>)'
    header_replacement_pattern = rf'(<th class="align-middle text-center">Type</th>)(\s*<th class="align-middle text-center">Prompt</th>)'

    # Find and update header
    header_match = re.search(header_pattern, html_content, re.DOTALL)
    if header_match:
        header_section = header_match.group(0)
        # Add Size column after Type
        updated_header = re.sub(
            header_replacement_pattern,
            r'\1\n                      <th class="align-middle text-center">Size</th>\2',
            header_section
        )
        html_content = html_content.replace(header_section, updated_header)

    # Update sortable column indices (shift by 1 after adding Size column)
    # Find all sortTable calls for this domain's table
    table_id = f"{domain}-table"

    # Update onclick handlers - need to increment column index by 1 for columns after Size
    # The pattern is onclick="sortTable('domain-table', N)"
    # Columns before Size (Rank=0, Model=1, Type=2) stay the same
    # Size is now 3
    # Prompt is now 4
    # Category columns start at 5

    old_indices = list(range(4, 4 + len(domains_config[domain]["columns"])))  # Old indices starting at 4
    new_indices = list(range(5, 5 + len(domains_config[domain]["columns"])))  # New indices starting at 5

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
