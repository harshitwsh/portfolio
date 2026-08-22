with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(max(0, 5055), min(len(lines), 5065)):
    print(f"Line {i+1}: {lines[i][:200]}")
