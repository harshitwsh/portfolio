with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

pos = js_code.find("function _x(")
if pos == -1:
    pos = js_code.find("_x=function(")
if pos == -1:
    pos = js_code.find("_x=async function")
if pos == -1:
    pos = js_code.find("async function _x")
print("_x pos:", pos)
if pos != -1:
    print(js_code[pos : pos + 3000])
