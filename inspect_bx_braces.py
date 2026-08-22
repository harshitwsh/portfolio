with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

line = lines[5179]
pos = line.find("function bx(e)")
print("bx function pos:", pos)
bx_str = line[pos : pos + 2200]
print(bx_str)
print("'{' in bx:", bx_str.count("{"))
print("'}' in bx:", bx_str.count("}"))
