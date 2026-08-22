with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Look at the Xx enter function in detail to find where to inject text
pos = 918443
print(js_code[pos : pos + 2000])
