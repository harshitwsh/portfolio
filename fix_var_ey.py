with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

code = code.replace("function Ty(e){if(e<=0)return 0;if(e>=1)return 1;let t=e*Cy,n=t|0,r=t-n;return wy[n]+(wy[n+1]-wy[n])*r}Ey=class", "function Ty(e){if(e<=0)return 0;if(e>=1)return 1;let t=e*Cy,n=t|0,r=t-n;return wy[n]+(wy[n+1]-wy[n])*r}var Ey=class")

with open("public/assets/main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(code)

with open("main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(code)

print("Added var before Ey")
