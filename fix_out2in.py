with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

pos = code.find("direction:out2in")
if pos != -1:
    print("Found unquoted out2in at:", pos)
    print(code[pos-20 : pos+40])
    code = code.replace("direction:out2in", "direction:`out2in`")
    with open("public/assets/main-B9-HtP-f.js", "w", encoding="utf-8") as f:
        f.write(code)
    with open("main-B9-HtP-f.js", "w", encoding="utf-8") as f:
        f.write(code)
    print("Fixed unquoted out2in")
