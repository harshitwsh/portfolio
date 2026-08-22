import re

def inspect_stage_text_creation():
    with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
        js_code = f.read()

    # Stage 1 text layout
    p1 = js_code.find("u=new vb(r,")
    print("Stage 1 text layout at:", p1)
    if p1 != -1:
        print(js_code[p1-50 : p1+500])

    # Stage 2 text layout
    p2 = js_code.find("s=new vb(i,")
    print("\nStage 2 text layout at:", p2)
    if p2 != -1:
        print(js_code[p2-50 : p2+500])

    # Stage 3 text layout
    p3 = js_code.find("let h=e.assetLoader.getAsset(`textsAtlas`);if(h)")
    print("\nStage 3 text layout at:", p3)
    if p3 != -1:
        print(js_code[p3-50 : p3+1200])

inspect_stage_text_creation()
