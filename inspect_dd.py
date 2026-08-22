with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

pos = js_code.find("function DD(")
print("DD at:", pos)
if pos != -1:
    print(js_code[pos : pos + 2500])

pos2 = js_code.find("var QS=")
if pos2 == -1:
    pos2 = js_code.find("QS=[")
print("QS at:", pos2)
if pos2 != -1:
    print(js_code[pos2 : pos2 + 2000])
