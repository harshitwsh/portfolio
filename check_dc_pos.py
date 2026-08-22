with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Check where dc (CanvasTexture) is declared vs where _x and createEditorialTextTexture are
dc_pos = js_code.find("dc=class{")
if dc_pos == -1:
    dc_pos = js_code.find("var dc=")
if dc_pos == -1:
    import re
    m = re.search(r'dc=\w+Texture', js_code)
    if m:
        dc_pos = m.start()

create_pos = js_code.find("function createEditorialTextTexture")
_x_pos = js_code.find("function _x(e)")
bx_pos = js_code.find("function bx(e)")

print("dc_pos:", dc_pos)
print("create_pos:", create_pos)
print("_x_pos:", _x_pos)
print("bx_pos:", bx_pos)

print("\n--- dc context ---")
print(js_code[dc_pos-20 : dc_pos + 150])
