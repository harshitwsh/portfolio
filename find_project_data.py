with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re
pos = js_code.find("Gym Management")
print("Gym Management at:", pos)
if pos != -1:
    print(js_code[pos-200 : pos+2000])
