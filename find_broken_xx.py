with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# The corrupted first Xx textsAtlas block (at 921146) is:
# textsAtlas`);if(h){e.renderer&&(h.anisotropy=e.renderer.capabilities.getMaxAnisotropy());
# [code was removed by our bad injection]
# .getOwnPropertyDescriptor,...

# The original should have been:
BROKEN = """textsAtlas`);if(h){e.renderer&&(h.anisotropy=e.renderer.capabilities.getMaxAnisotropy());.getOwnPropertyDescriptor"""

# Check if it exists as-is
broken_pos = js_code.find("textsAtlas`);if(h){e.renderer&&(h.anisotropy=e.renderer.capabilities.getMaxAnisotropy());.getOwnPropertyDescriptor")
print("Broken pos:", broken_pos)

if broken_pos == -1:
    # Check with unicode escapes
    broken_pos = js_code.find("textsAtlas`);if(h){e.renderer\u0026\u0026(h.anisotropy=e.renderer.capabilities.getMaxAnisotropy());.getOwnPropertyDescriptor")
    print("Broken pos unicode:", broken_pos)

print(js_code[broken_pos-50 : broken_pos+200])
