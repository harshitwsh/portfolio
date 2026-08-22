with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

pos = code.find("case`ZYX`:")
print("pos of case ZYX:", pos)
if pos != -1:
    print(code[pos : pos + 300])
