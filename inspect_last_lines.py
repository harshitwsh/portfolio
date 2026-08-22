with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("Total lines:", len(lines))
print("Last 15 lines:")
for l in lines[-15:]:
    print(repr(l))
