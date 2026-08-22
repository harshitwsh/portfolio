with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

pos_ey = code.find("Ey=class")
pos_dy = code.find("Dy=450")

ey_str = code[pos_ey : pos_dy + 20]
print("Ey snippet:")
print(ey_str)

# Let's count '{' and '}' in Ey
print("'{' count:", ey_str.count("{"))
print("'}' count:", ey_str.count("}"))
