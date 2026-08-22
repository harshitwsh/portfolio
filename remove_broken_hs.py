with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# There are 2 copies of hS in the file
# The broken one at 943519: "hS={=e.components..."
# The correct one at 969918: ",hS={id:`gate3to4`..."

# The broken one has content belonging to the Ix function mixed in
# Strategy: 
# 1. Remove the broken hS occurrence entirely - just cut from 943516 to 969918
# That's: pS=10,mS=10,hS={...broken garbage...},{correct hS content}
# We want just: pS=10,mS=10,{correct hS content}

# Find boundaries
broken_hS_start = 943519 - 3  # "hS={" starts at 943519, comma is 3 chars before
correct_hS_start = 969918  # starts with ",hS={id:`gate3to4`"

print("Removing chars from", broken_hS_start, "to", correct_hS_start)
print("Removed content length:", correct_hS_start - broken_hS_start)
print("Before:", js_code[broken_hS_start - 50 : broken_hS_start + 50])
print("After:", js_code[correct_hS_start : correct_hS_start + 50])

fixed = js_code[:broken_hS_start] + js_code[correct_hS_start:]
print("\nFixed join:")
print(fixed[broken_hS_start - 50 : broken_hS_start + 150])

with open("public/assets/main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(fixed)
with open("main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(fixed)

print("FIXED!")
