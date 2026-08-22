with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

BAD_INJECTION = "let t3_1=createEditorialTextTexture(`NO LIMITS.`),t3_2=createEditorialTextTexture(`JUST BUILD.`);let t=[{texture:t3_1,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.05,disappearAt:.45},{texture:t3_2,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.50,disappearAt:.92}];"

# The bad injection is placed inline where it broke the code
# We remove the bad injection entirely — keep stage3 vanilla for now (no editorial text)
fixed_code = js_code.replace(BAD_INJECTION, "")

with open("public/assets/main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(fixed_code)
with open("main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(fixed_code)

print("Removed bad stage 3 injection")
print("Remaining occurrences:", fixed_code.count(BAD_INJECTION))
