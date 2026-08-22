with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Stage 2 pos 1826958 - check context
pos = 1826958
print("Stage 2 context:")
print(js_code[pos-100 : pos+400])
