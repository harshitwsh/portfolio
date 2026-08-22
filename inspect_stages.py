with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re

# Find stage definitions
for stage_id in ["stage1", "gate1to2", "stage2", "gate2to3", "stage3"]:
    pos = js_code.find(f"id:`{stage_id}`")
    if pos == -1:
        pos = js_code.find(f'id:"{stage_id}"')
    print(f"Stage {stage_id} at pos {pos}")
    if pos != -1:
        print(js_code[pos : pos + 1200])
        print("="*60)
