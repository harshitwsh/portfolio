with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

line = lines[5058] # line 5059 (0-indexed 5058)
print("Length of line 5059:", len(line))
# Search where createEditorialTextTexture is
pos = line.find("createEditorialTextTexture")
print("createEditorialTextTexture pos:", pos)
if pos != -1:
    print(line[max(0, pos-200) : min(len(line), pos+800)])
