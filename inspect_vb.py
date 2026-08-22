with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

pos = js_code.find("class vb")
if pos == -1:
    pos = js_code.find("var vb=class")
if pos == -1:
    pos = js_code.find("vb=class")
print("vb pos:", pos)
if pos != -1:
    print(js_code[pos : pos + 2500])
