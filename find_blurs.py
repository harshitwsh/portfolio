import re

with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

print("File length:", len(code))

# Find all matches for blur or backdrop or frost or lens
matches = re.finditer(r'([^\n;{}]{0,100}(?:blur|backdrop|frost|filter)[^\n;{}]{0,100})', code, re.IGNORECASE)
count = 0
for m in matches:
    print(f"Match: {m.group(1).strip()}")
    count += 1
    if count > 40:
        break
