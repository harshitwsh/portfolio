with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Let's search for text creation in stage1
pos1 = js_code.find("id:`stage1`")
print("stage1 pos:", pos1)
print(js_code[pos1 : pos1 + 3500])

print("\n" + "="*80 + "\n")

# Let's search for text creation in stage2
pos2 = js_code.find("id:`stage2`")
print("stage2 pos:", pos2)
print(js_code[pos2 : pos2 + 3500])

print("\n" + "="*80 + "\n")

# Let's search for text creation in stage3
pos3 = js_code.find("id:`stage3`")
print("stage3 pos:", pos3)
print(js_code[pos3 : pos3 + 3500])
