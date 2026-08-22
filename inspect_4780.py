with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(4775, 4785):
    if i < len(lines):
        print(f"Line {i+1}: {repr(lines[i])}")
