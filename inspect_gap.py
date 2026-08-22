with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Let's inspect the exact gap
pos1 = js_code.find("emberTip:i=[6,1.5,.25")
pos2 = js_code.find("onHoldStart:e=>{e&&(ix(e),ax(e))")
print("Gap between pos1 and pos2:", pos2 - pos1)
print(js_code[pos1-50 : pos2+100])
