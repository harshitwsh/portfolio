with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

pos = js_code.find("function OD(")
print("OD at:", pos)
if pos != -1:
    print(js_code[pos : pos + 500])
