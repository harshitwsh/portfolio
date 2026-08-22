def fix_syntax():
    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        code = code.replace("_b=.3,function createEditorialTextTexture", "_b=.3;function createEditorialTextTexture")
        code = code.replace("mb=4,hb=`outExpo`,gb={smoothstep:e=>e*e*(3-2*e),outExpo:e=>e>=1?1:1-2**(-10*e),inExpo:e=>e<=0?0:2**(10*(e-1))},_b=.3,function", "mb=4,hb=`outExpo`,gb={smoothstep:e=>e*e*(3-2*e),outExpo:e=>e>=1?1:1-2**(-10*e),inExpo:e=>e<=0?0:2**(10*(e-1))},_b=.3;function")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print("Fixed syntax in:", filepath)

fix_syntax()
