with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# The bad injection is at position 921235
# It broke the original code that follows. We need to:
# 1. Remove the bad stage3 injection block
# 2. Instead, just find the Xx stage enter function and cleanly patch it

# Find what was there - the broken part
BAD_INJECTION = "let t3_1=createEditorialTextTexture(`NO LIMITS.`),t3_2=createEditorialTextTexture(`JUST BUILD.`);let t=[{texture:t3_1,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.05,disappearAt:.45},{texture:t3_2,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.50,disappearAt:.92}];"

pos = js_code.find(BAD_INJECTION)
print("Bad injection pos:", pos)
print("Context before:", js_code[pos-100 : pos])
print("Context after:", js_code[pos+len(BAD_INJECTION) : pos+len(BAD_INJECTION)+200])
