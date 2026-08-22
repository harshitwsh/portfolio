with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

import re
# Find where v, x, etc are defined in three.js constants
pos = code.find("LinearFilter")
if pos != -1:
    print("Found LinearFilter around:", code[max(0, pos-200):min(len(code), pos+200)])
else:
    print("LinearFilter not found as string")

# Let's check the texture constants definition
pos2 = code.find("1006")
print("1006 around:", code[max(0, pos2-100):min(len(code), pos2+100)])
