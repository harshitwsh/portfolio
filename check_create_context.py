with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# The IIFE calls createEditorialTextTexture which needs dc (CanvasTexture) in scope
# But createEditorialTextTexture is a function defined at pos 894555 using dc (pos 465910)
# Since dc is a var in the same top-level scope, it SHOULD be accessible
# unless createEditorialTextTexture was placed INSIDE a block where dc is not visible.

# Let's check what exactly is around position 894555
pos_create = js_code.find("function createEditorialTextTexture")
print("createEditorialTextTexture at:", pos_create)
print("Context before:")
print(js_code[pos_create-200 : pos_create + 100])
