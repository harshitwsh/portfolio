with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re
matches = [m.start() for m in re.finditer(r'onStageComplete|isComplete|_onHComplete|_onZeroComplete', js_code)]
print("Matches:", matches)
for pos in matches:
    print("--- at", pos)
    print(js_code[max(0, pos-100) : min(len(js_code), pos+150)])
