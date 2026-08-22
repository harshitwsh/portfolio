with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re
matches = [m.start() for m in re.finditer(r'function TD\(|function DD\(|function CD\(', js_code)]
print("Matches:", matches)
for pos in matches:
    print("--- Match at", pos)
    print(js_code[pos : pos + 100])
