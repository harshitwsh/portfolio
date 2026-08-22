with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

import re
matches = [m.start() for m in re.finditer("worldMap", code)]
print("worldMap occurrences:", matches)
for pos in matches:
    print("--- Context at", pos)
    print(code[max(0, pos - 150) : min(len(code), pos + 150)])
