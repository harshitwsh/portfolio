with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re

# Search for CanvasTexture assignment
matches = list(re.finditer(r'CanvasTexture', js_code))
print("CanvasTexture mentions:", [(m.start(), js_code[m.start()-10 : m.start()+40]) for m in matches[:5]])

# dc could be assigned as dc=SomeClass where SomeClass is CanvasTexture
# Let's find how dc is used in the code
dc_usages = list(re.finditer(r'\bdc\b', js_code))
print("dc usages count:", len(dc_usages))

# Find where dc appears near 'new dc('
new_dc = list(re.finditer(r'new dc\(', js_code))
print("new dc( positions:", [(m.start(), js_code[max(0,m.start()-30) : m.start()+20]) for m in new_dc[:3]])
