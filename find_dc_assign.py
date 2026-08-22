with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re

# Find all dc= assignments
dc_assigns = list(re.finditer(r'[,;{]\s*dc\s*=', js_code))
print("dc= assignments:")
for m in dc_assigns[:10]:
    print("  pos:", m.start(), js_code[m.start() : m.start()+80])
