with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

start = js_code.find("CO=class{")
end = js_code.find("NO(e){", start)
print("CO start:", start)
print("CO end:", end)
print(js_code[start : end])
