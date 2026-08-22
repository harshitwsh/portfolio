with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

pos = js_code.find("function ib(")
if pos == -1:
    pos = js_code.find("ib=function(")
if pos == -1:
    pos = js_code.find("var ib=")
print("ib pos:", pos)
if pos != -1:
    print(js_code[pos : pos + 2500])
