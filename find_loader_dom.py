with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re
matches = [m.start() for m in re.finditer(r'loader-container|loader-text|loader-logo', js_code)]
print("Loader DOM matches:", matches)
for pos in matches:
    print("--- at", pos)
    print(js_code[max(0, pos-100) : min(len(js_code), pos+200)])
