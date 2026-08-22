with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Check stage 2 injection (Wb) - it should be empty: s = new vb(i, [])
pos = js_code.find("s = new vb(i, [])")
if pos == -1:
    pos = js_code.find("s=new vb(i,[])")
print("Stage 2 empty textLayout pos:", pos)

# Check stage 1 injection in bx()
pos2 = js_code.find("YOU HAVE AN IDEA.")
print("Stage 1 text pos:", pos2)
if pos2 != -1:
    print(js_code[pos2-200 : pos2+300])
