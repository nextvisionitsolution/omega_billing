from pathlib import Path
import re
root = Path('billing/templates')
pattern = re.compile(r'<link href="https://cdn\.jsdelivr\.net/npm/bootstrap@5\.3\.0/dist/css/bootstrap\.min\.css" rel="stylesheet">\s*<link rel="stylesheet" href="https://cdn\.jsdelivr\.net/npm/bootstrap-icons@1\.11\.3/font/bootstrap-icons\.min\.css">\s*(<link href="https://fonts\.googleapis\.com[^>]+>\s*)?', re.MULTILINE)
replacement = '{% load static %}\n<link rel="stylesheet" href="{% static \'billing/css/bootstrap.min.css\' %}">\n<link rel="stylesheet" href="{% static \'billing/css/bootstrap-icons.min.css\' %}">\n'
for path in root.rglob('*.html'):
    text = path.read_text(encoding='utf-8')
    if pattern.search(text):
        new_text = pattern.sub(replacement, text)
        if '{% load static %}' not in new_text:
            new_text = '{% load static %}\n' + new_text
        path.write_text(new_text, encoding='utf-8')
        print('updated', path)
