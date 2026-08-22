with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Find the Xx (stage3) object — typically has id + scrollVh + enter function
# Search for stage3 context in the actual stage configs
import re

# Look for Xx= pattern or the stage3 enter function
matches = list(re.finditer(r'Xx=\{', js_code))
print("Xx= matches:")
for m in matches[:5]:
    print("  pos:", m.start(), js_code[m.start() : m.start()+300])
