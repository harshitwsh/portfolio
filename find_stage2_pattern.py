with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# The issue: at position 921146, we have:
# textsAtlas`);if(h){e.renderer&&(h.anisotropy=...);.getOwnPropertyDescriptor,...
# The original code was:
# textsAtlas`);if(h){e.renderer&&(h.anisotropy=...); THEN the textLayout code, then }
# Our bad injection removed part of the if(h){...} block and corrupted the structure

# Let's look at the original xb function that starts textsAtlas and understand the pattern
# Searching for textLayout in Wb (stage2) enter function for comparison
pos = js_code.find("textsAtlas`);c&&(e.renderer")
print("Stage 2 textsAtlas pattern pos:", pos)
print(js_code[pos : pos + 400])
