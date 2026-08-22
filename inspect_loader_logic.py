with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re

# Find Stage 0 / loader logic
pos = js_code.find("updateLoader(")
print("updateLoader pos:", pos)
if pos != -1:
    print(js_code[pos : pos + 1000])

# Find where assets are loaded at start
pos2 = js_code.find("loadStageAssets(`stage0`)")
if pos2 == -1:
    pos2 = js_code.find("loadStageAssets(`stage1`)")
print("loadStageAssets pos:", pos2)
if pos2 != -1:
    print(js_code[pos2-100 : pos2+1000])
