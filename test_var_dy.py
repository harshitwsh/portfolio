with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("this.group.clear()}},Dy=450", "this.group.clear()}};var Dy=450")

with open("public/assets/main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(code)

with open("main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(code)

print("Replaced with };var Dy=450")
