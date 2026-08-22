with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re
# Find uD, dD, gD, _D, mD, hD, yD definitions
pos = js_code.find("cD={")
print("cD and shaders around:", pos)
print(js_code[pos : pos + 3000])
