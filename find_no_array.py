with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re

pos = js_code.find("nO=[{id:`stage1`")
if pos == -1:
    pos = js_code.find("nO=[")
print("nO array at:", pos)
if pos != -1:
    print(js_code[pos : pos + 10000])
