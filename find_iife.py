with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import re

# Find the IIFE that calls createEditorialTextTexture inside bx
# The target code looks like:
# (()=>{let t1=createEditorialTextTexture(`YOU HAVE AN IDEA.`),t2=...
old_block = "(()=>{let t1=createEditorialTextTexture(`YOU HAVE AN IDEA.`),t2=createEditorialTextTexture(`NOW MAKE IT REAL.`);u=new vb(r,[{texture:t1,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.04,disappearAt:.44},{texture:t2,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.50,disappearAt:.94}]),u.resize(e._vw,e._vh)})()"

pos = js_code.find(old_block)
print("IIFE pos:", pos)
if pos != -1:
    print(js_code[pos : pos + 200])
