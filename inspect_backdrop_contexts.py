with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re
matches = [m.start() for m in re.finditer(r'backdrop-filter', js_code)]
for pos in matches:
    print("=== Backdrop filter at pos", pos, "===")
    print(js_code[max(0, pos-200) : min(len(js_code), pos+200)])
