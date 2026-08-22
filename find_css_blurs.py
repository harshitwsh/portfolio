import re

with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

with open("public/assets/main-yeWZtezw.css", "r", encoding="utf-8") as f:
    css_code = f.read()

print("--- CSS backdrop-filters ---")
for m in re.finditer(r'([^{}]*\{[^{}]*backdrop-filter[^{}]*\})', css_code):
    print(m.group(1))

print("--- JS backdrop-filters and filters ---")
for m in re.finditer(r'([^\n;`]{0,80}(?:backdrop-filter|filter:\s*blur)[^\n;`]{0,80})', js_code):
    print(m.group(1).strip())
