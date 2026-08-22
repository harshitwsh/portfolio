with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

pos = js_code.find("Ng=class{")
print("Ng class at:", pos)
print(js_code[pos : pos + 2200])
