with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# The broken part is: 
# getAsset(`textsAtlas`);if(h){e.renderer&&(h.anisotropy=e.renderer.capabilities.getMaxAnisotropy());.getOwnPropertyDescriptor
# which should be:
# getAsset(`textsAtlas`);if(h){e.renderer&&(h.anisotropy=e.renderer.capabilities.getMaxAnisotropy());let t=[...original...];n.resize...n} <then normal code continues>

# Find what the "next part" after the broken injection should be - the original code that followed
# The break point: our injection removed text and then code continues with ".getOwnPropertyDescriptor"
# which is actually the start of another scope
# Let's look at what's exactly at 921146 + len(broken)

broken_str = "textsAtlas`);if(h){e.renderer&&(h.anisotropy=e.renderer.capabilities.getMaxAnisotropy());"
pos = js_code.find(broken_str)
if pos == -1:
    import re
    m = re.search(r'textsAtlas`\);if\(h\)\{e\.renderer&&\(h\.anisotropy=e\.renderer\.capabilities\.getMaxAnisotropy\(\)\);', js_code)
    if m:
        pos = m.start()
print("Broken pos:", pos)

# What comes right after the if block opener?
after = js_code[pos + len(broken_str):]
print("After broken_str:", after[:200])
