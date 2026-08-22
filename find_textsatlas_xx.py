with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Find the existing textsAtlas usage in Xx enter where we can inject text layout
# Look for textsAtlas in stage3/Xx
pos = js_code.find("textsAtlas`);", 918443)
print("textsAtlas in Xx:", pos)
if pos != -1:
    print(js_code[pos : pos + 600])
