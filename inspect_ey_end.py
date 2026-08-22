with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

line = lines[4779]
pos = line.find("this.group.clear()")
print("this.group.clear pos:", pos)
if pos != -1:
    print(line[pos : pos + 100])
