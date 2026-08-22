with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Find the Xx (stage3) enter function
# Look for the stage3 id
pos = js_code.find("id:`stage3`")
if pos == -1:
    pos = js_code.find('id:"stage3"')
print("stage3 id pos:", pos)
if pos != -1:
    print(js_code[pos-50 : pos+800])
