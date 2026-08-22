with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re

for word in ["Believed", "College", "land", "JOB", "Bullsh", "coins", "brands"]:
    matches = [m.start() for m in re.finditer(re.escape(word), js_code, re.IGNORECASE)]
    print(f"Matches for '{word}':", len(matches))
    for pos in matches[:4]:
        print(f"  at {pos}:", js_code[max(0, pos-80) : min(len(js_code), pos+120)])
