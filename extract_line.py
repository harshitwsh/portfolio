with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Write line 4780 to test_line.js
with open("test_line.js", "w", encoding="utf-8") as f:
    f.write(lines[4779])
