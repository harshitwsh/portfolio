with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

pos = 2166474
print(js_code[pos-200 : pos+2000])
