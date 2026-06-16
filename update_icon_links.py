from pathlib import Path
import re
root = Path('billing/templates')
pattern = re.compile(r'<link rel="stylesheet"\s*href="https://cdn\.jsdelivr\.net/npm/bootstrap-icons@1\.11\.3/font/bootstrap-icons\.min\.css">', re.MULTILINE)
for path in root.rglob('*.html'):
    text = path.read_text(encoding='utf-8')
    new_text = pattern.sub('<link rel="stylesheet" href="{% static \'billing/css/bootstrap-icons.min.css\' %}">', text)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        print('updated', path)
