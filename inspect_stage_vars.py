with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

for var_name in ["Sx=", "yx=", "sx=", "Wb=", "Xx=", "hS="]:
    pos = js_code.find(var_name)
    print(f"Variable {var_name} at pos {pos}")
    if pos != -1:
        print(js_code[pos : pos + 1500])
        print("="*60)
