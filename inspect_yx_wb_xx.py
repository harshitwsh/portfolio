with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Let's find where yx is defined and its setup
pos_yx = js_code.find("yx={id:`stage1`")
print("yx definition pos:", pos_yx)
if pos_yx != -1:
    print(js_code[pos_yx : pos_yx + 4000])

print("\n" + "="*80 + "\n")

pos_wb = js_code.find("Wb={id:`stage2`")
print("Wb definition pos:", pos_wb)
if pos_wb != -1:
    print(js_code[pos_wb : pos_wb + 4000])

print("\n" + "="*80 + "\n")

pos_xx = js_code.find("Xx={id:`stage3`")
print("Xx definition pos:", pos_xx)
if pos_xx != -1:
    print(js_code[pos_xx : pos_xx + 4000])
