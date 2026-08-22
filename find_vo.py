with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re

# Find vO class
pos = js_code.find("class vO")
if pos == -1:
    pos = js_code.find("var vO=class")
if pos == -1:
    pos = js_code.find("vO=class")
print("vO class pos:", pos)
if pos != -1:
    print(js_code[pos : pos + 3000])

# Search in html / css
with open("public/index.html", "r", encoding="utf-8") as f:
    html = f.read()
print("index.html contents:", html[:1000])
