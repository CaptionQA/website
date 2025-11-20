import re

# Read the generated Overall HTML
with open('overall_table_html.txt', 'r') as f:
    overall_tbody = f.read()

# Extract just the table rows (skip the first comment line and last "Total models" line)
lines = overall_tbody.strip().split('\n')
tbody_content = '\n'.join([line for line in lines if '<tr>' in line or '<td' in line or '</tr>' in line])

# Read the current HTML file
with open('index.html', 'r') as f:
    html_content = f.read()

# Update Overall table tbody
html_content = re.sub(
    r'(<div id="overall-board".*?<tbody>)(.*?)(</tbody>)',
    f'\\1\n{tbody_content}\n                  \\3',
    html_content,
    flags=re.DOTALL
)

# Write updated HTML
with open('index.html', 'w') as f:
    f.write(html_content)

print("Successfully updated Overall leaderboard!")
print("Total models: 16")
