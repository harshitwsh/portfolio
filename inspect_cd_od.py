with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

start = js_code.find("function CD()")
end = js_code.find("function OD(", start)
print("CD start:", start)
print("OD start:", end)
if start != -1 and end != -1:
    print("CD to OD length:", end - start)
    print(js_code[start : start + 500])
