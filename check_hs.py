with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Fix the broken hS=  
# Context at join shows: "hS={=e.components" which is wrong
# Should be: hS={id:`gate3to4`,...}
# Let's find the hS definition in the 2nd copy
p2_hs_abs = js_code.rfind(",hS=")
print("hS pos from end:", p2_hs_abs)
print("hS context:", js_code[p2_hs_abs : p2_hs_abs + 400])
