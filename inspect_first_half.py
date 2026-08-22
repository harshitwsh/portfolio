with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

line = lines[5179]
print(line[:1450])
print("'{' in first half:", line[:1450].count("{"))
print("'}' in first half:", line[:1450].count("}"))
