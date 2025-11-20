import re

# Read the generated HTML tables
with open('domain_tables_html.txt', 'r') as f:
    content = f.read()

# Extract each domain section
domains_html = {}
pattern = r'DOMAIN: (\w+)\n={80}\n(.*?)(?=\n={80}|$)'
matches = re.findall(pattern, content, re.DOTALL)

for domain_name, tbody_content in matches:
    domains_html[domain_name.lower()] = tbody_content.strip()

# Read the current HTML file
with open('index.html', 'r') as f:
    html_content = f.read()

# Update Document domain
document_tbody = domains_html['document']
html_content = re.sub(
    r'(<div id="document-board".*?<tbody>)(.*?)(</tbody>)',
    f'\\1\n{document_tbody}\n                  \\3',
    html_content,
    flags=re.DOTALL
)

# Update E-commerce domain
ecommerce_tbody = domains_html['ecommerce']
html_content = re.sub(
    r'(<div id="ecommerce-board".*?<tbody>)(.*?)(</tbody>)',
    f'\\1\n{ecommerce_tbody}\n                  \\3',
    html_content,
    flags=re.DOTALL
)

# Update Embodied AI domain
embodiedai_tbody = domains_html['embodiedai']
html_content = re.sub(
    r'(<div id="embodiedai-board".*?<tbody>)(.*?)(</tbody>)',
    f'\\1\n{embodiedai_tbody}\n                  \\3',
    html_content,
    flags=re.DOTALL
)

# Write updated HTML
with open('index.html', 'w') as f:
    f.write(html_content)

print("Successfully updated all domain tables!")
print(f"- Document: {len(document_tbody.split('<tr>')) - 1} rows")
print(f"- E-commerce: {len(ecommerce_tbody.split('<tr>')) - 1} rows")
print(f"- Embodied AI: {len(embodiedai_tbody.split('<tr>')) - 1} rows")
