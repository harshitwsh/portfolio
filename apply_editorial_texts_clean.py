def apply_editorial_texts_clean():
    helper_code = """function createEditorialTextTexture(e,t=""){let n=document.createElement(`canvas`);n.width=2048,n.height=800;let r=n.getContext(`2d`);r.clearRect(0,0,n.width,n.height),r.fillStyle=`#ffffff`,r.textAlign=`center`,r.textBaseline=`middle`,r.shadowColor=`rgba(0,0,0,0.4)`,r.shadowBlur=16;if(t){r.font=`italic 400 90px "Bethany Elingston", "STK Bureau Serif", Georgia, serif`,r.fillText(t,1024,310),r.font=`700 160px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,490)}else{r.font=`700 170px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,400)}let i=new dc(n);return i.colorSpace=W,i.generateMipmaps=!0,i.minFilter=v,i.magFilter=v,i.needsUpdate=!0,i};"""

    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        if "function createEditorialTextTexture" not in code:
            vb_pos = code.find("vb=class{")
            code = code[:vb_pos] + helper_code + code[vb_pos:]
            print("Inserted helper in:", filepath)

        # Stage 1: replace textsAtlas layout with "YOU HAVE AN IDEA." -> "NOW MAKE IT REAL."
        s1_start = code.find("d&&(u=new vb(r,[{texture:d,atlasUV:Nv(0,0,775.26,371.64)")
        if s1_start != -1:
            s1_end = code.find("u.resize(e._vw,e._vh))", s1_start) + len("u.resize(e._vw,e._vh))")
            new_s1 = "(()=>{let t1=createEditorialTextTexture(`YOU HAVE AN IDEA.`),t2=createEditorialTextTexture(`NOW MAKE IT REAL.`);u=new vb(r,[{texture:t1,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.04,disappearAt:.44},{texture:t2,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.50,disappearAt:.94}]),u.resize(e._vw,e._vh)})()"
            code = code[:s1_start] + new_s1 + code[s1_end:]
            print("Replaced Stage 1 text layout in:", filepath)

        # Stage 1: remove coinRing (brand logos)
        code = code.replace("coinRing:o,petalParticles:s", "coinRing:null,petalParticles:s")

        # Stage 2: remove text overlay so middle-finger visual speaks for itself
        s2_start = code.find("s=new vb(i,[{texture:c,atlasUV:Nv(1092.93,558.45,945.23,371.64)")
        if s2_start != -1:
            s2_end = code.find("s.resize(e._vw,e._vh))", s2_start) + len("s.resize(e._vw,e._vh))")
            new_s2 = "s=new vb(i,[]),s.resize(e._vw,e._vh)"
            code = code[:s2_start] + new_s2 + code[s2_end:]
            print("Replaced Stage 2 text layout in:", filepath)

        # Gate 1 to 2: remove text overlay
        gate_start = code.find("e._gateTextLayout=new vb(e.textScene,[{texture:t,atlasUV:Nv(257.75,558.45")
        if gate_start != -1:
            gate_end = code.find("e._gateTextLayout.resize(e._vw,e._vh))", gate_start) + len("e._gateTextLayout.resize(e._vw,e._vh))")
            new_gate = "e._gateTextLayout=new vb(e.textScene,[]),e._gateTextLayout.resize(e._vw,e._vh)"
            code = code[:gate_start] + new_gate + code[gate_end:]
            print("Replaced Gate1to2 text in:", filepath)

        # Stage 3: "NO LIMITS." -> "JUST BUILD."
        s3_start = code.find("let t=[{texture:h,atlasUV:Nv(0,371.64,365.21,186.82),aspect:Pv(365.21,186.82)")
        if s3_start != -1:
            s3_end = code.find("anchor:`bottom-right`,appearAt:.87,disappearAt:.99}];", s3_start) + len("anchor:`bottom-right`,appearAt:.87,disappearAt:.99}];")
            new_s3 = "let t3_1=createEditorialTextTexture(`NO LIMITS.`),t3_2=createEditorialTextTexture(`JUST BUILD.`);let t=[{texture:t3_1,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.05,disappearAt:.45},{texture:t3_2,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.50,disappearAt:.92}];"
            code = code[:s3_start] + new_s3 + code[s3_end:]
            print("Replaced Stage 3 text layout in:", filepath)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print("Written successfully:", filepath)

apply_editorial_texts_clean()
