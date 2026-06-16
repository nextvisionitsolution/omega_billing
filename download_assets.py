import os, urllib.request, re
os.makedirs('billing/static/billing/css', exist_ok=True)
os.makedirs('billing/static/billing/fonts', exist_ok=True)
urls = {
    'billing/static/billing/css/bootstrap.min.css': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
    'billing/static/billing/css/bootstrap-icons.min.css': 'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css'
}
for path, url in urls.items():
    print('downloading', url)
    urllib.request.urlretrieve(url, path)
css = open('billing/static/billing/css/bootstrap-icons.min.css', 'r', encoding='utf-8').read()
m = re.search(r'url\(([^)]+)\)', css)
if m:
    font_url = m.group(1).strip("'\"")
    print('downloading', font_url)
    urllib.request.urlretrieve('https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/' + font_url, 'billing/static/billing/fonts/' + os.path.basename(font_url))
print('done')
