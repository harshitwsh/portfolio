with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

line = lines[5179] # line 5180 (0-indexed 5179)
print("Length of line 5180:", len(line))
print("'{' count in line 5180:", line.count("{"))
print("'}' count in line 5180:", line.count("}"))
