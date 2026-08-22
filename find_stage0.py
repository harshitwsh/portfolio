with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re

print("--- DRAW A ZERO matches ---")
for m in re.finditer(r'DRAW A ZERO', js_code):
    pos = m.start()
    print("Pos:", pos, js_code[max(0, pos-100) : min(len(js_code), pos+100)])

print("\n--- ZERO FOR FREE matches ---")
for m in re.finditer(r'ZERO FOR FREE', js_code, re.IGNORECASE):
    pos = m.start()
    print("Pos:", pos, js_code[max(0, pos-100) : min(len(js_code), pos+100)])

print("\n--- Ng class (stage0 detector) ---")
pos = js_code.find("class Ng")
if pos == -1:
    pos = js_code.find("var Ng=class")
if pos == -1:
    pos = js_code.find("Ng=class")
print("Ng class pos:", pos)
if pos != -1:
    print(js_code[pos : pos + 3000])
