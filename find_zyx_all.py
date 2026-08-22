with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

import re
matches = [m.start() for m in re.finditer(r'case`ZYX`:', code)]
print("Matches:", matches)
for pos in matches:
    print("--- at", pos)
    print(code[pos : pos + 250])
