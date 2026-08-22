with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Find first e._stage3QuatA after 922554
pos = js_code.find("e._stage3QuatA=new Ct()", 920000)
print("stage3QuatA pos:", pos)
if pos != -1:
    print("Context:")
    print(js_code[pos - 100 : pos + 200])
