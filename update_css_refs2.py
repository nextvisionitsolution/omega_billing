from pathlib import Path
import re
root = Path('billing/templates')
for path in root.rglob('*.html'):
    text = path.read_text(encoding='utf-8')
    new = text
    if 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' in new:
        new = new.replace('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">', '{% load static %}\n<link rel="stylesheet" href="{% static \'billing/css/bootstrap.min.css\' %}\">')
    if 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css' in new:
        new = new.replace('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">', '<link rel="stylesheet" href="{% static \'billing/css/bootstrap-icons.min.css\' %}\">')
        if '{% load static %}' not in new:
            new = '{% load static %}\n' + new
    new = re.sub(r'<link href="https://fonts.googleapis.com[^>]+>\s*', '', new)
    if new != text:
        path.write_text(new, encoding='utf-8')
        print('updated', path)
