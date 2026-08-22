with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

import re
matches = [m.start() for m in re.finditer(r'ResumeModal|resume-modal', code)]
print("ResumeModal matches:", matches)
for pos in matches:
    print("--- at", pos)
    print(code[max(0, pos-100) : min(len(code), pos+150)])
