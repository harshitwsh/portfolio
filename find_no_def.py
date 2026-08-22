with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re

for match in re.finditer(r'nO\s*=\s*\[', js_code):
    pos = match.start()
    print("Match at pos:", pos)
    print(js_code[pos : pos + 1500])
    print("="*60)
