with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# The Xx stage3 textsAtlas block at 921146 is:
# textsAtlas`);if(h){e.renderer&&(h.anisotropy=e.renderer.capabilities.getMaxAnisotropy());
# [OUR REMOVED INJECTION WAS HERE]
# .getOwnPropertyDescriptor,...  <- this is clearly NOT related code, it's cut code

# The original code was likely:
# textsAtlas`);if(h){e.renderer&&(h.anisotropy=e.renderer.capabilities.getMaxAnisotropy(),h.needsUpdate=!0)};let s=...textLayout...
# We need to find what came after the if block originally

# Let's look at the SAME Xx in the second copy (there are 2 copies of all stages)
pos2 = 1859224  # second Xx= position
js_after_2 = js_code[pos2:]
ta_pos = js_after_2.find("textsAtlas`);")
print("Second Xx textsAtlas offset:", ta_pos)
print(js_after_2[ta_pos : ta_pos + 600])
