with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

line = lines[4779] # 0-indexed 4779 = line 4780
print("Length of line 4780:", len(line))
pos = line.find("Ey=class")
print("Ey pos:", pos)
if pos != -1:
    print(line[max(0, pos-300) : min(len(line), pos+400)])
