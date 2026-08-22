with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Second Xx textsAtlas block - get the full original content
pos2 = 1859224
ta_pos = pos2 + 2703  # absolute position of textsAtlas in 2nd copy
# Find end of the if block 
# The if block ends with something like },t.components.textLayout=... or similar 
print(js_code[ta_pos : ta_pos + 3000])
