with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re
# Find CD, TD, DD, OD definitions (the mapPanel functions)
pos = js_code.find("function TD(")
print("TD at:", pos)
if pos != -1:
    print(js_code[pos-200 : pos+2000])

pos2 = js_code.find("function CD()")
print("CD at:", pos2)
if pos2 != -1:
    print(js_code[pos2-200 : pos2+2000])
