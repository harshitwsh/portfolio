with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Find the problematic segment
pos = js_code.find("let t3_1=createEditorialTextTexture(`NO LIMITS.`)")
print("Stage 3 injection pos:", pos)
# Let's inspect 500 chars around it
print(js_code[pos-300 : pos+500])
