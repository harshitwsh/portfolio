import re

def apply_editorial_texts():
    helper_code = """
function createEditorialTextTexture(e,t=""){let n=document.createElement(`canvas`);n.width=2048,n.height=800;let r=n.getContext(`2d`);r.clearRect(0,0,n.width,n.height),r.fillStyle=`#ffffff`,r.textAlign=`center`,r.textBaseline=`middle`,r.shadowColor=`rgba(0,0,0,0.5)`,r.shadowBlur=20;if(t){r.font=`italic 400 90px "Bethany Elingston", "STK Bureau Serif", Georgia, serif`,r.fillText(t,1024,310),r.font=`700 160px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,490)}else{r.font=`700 170px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,400)}let i=new dc(n);return i.colorSpace=W,i.generateMipmaps=!0,i.minFilter=v,i.magFilter=v,i.needsUpdate=!0,i}
"""

    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        # Insert helper_code if not present
        if "createEditorialTextTexture" not in code:
            # Place it before _x or vb
            vb_pos = code.find("vb=class{")
            code = code[:vb_pos] + helper_code + code[vb_pos:]
            print("Inserted createEditorialTextTexture helper in:", filepath)

        # 1. Update Stage 1 text layout and remove coinRing
        # In Stage 1 setup:
        s1_old_pattern = r'd&&\((u=new vb\(r,\[\{texture:d,atlasUV:Nv\(0,0,775\.26,371\.64\).*?\}\]\),u\.resize\(e\._vw,e\._vh\)\)'
        s1_new_code = r'''(()=>{let t1=createEditorialTextTexture(`YOU HAVE AN IDEA.`),t2=createEditorialTextTexture(`NOW MAKE IT REAL.`);u=new vb(r,[{texture:t1,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.04,disappearAt:.42},{texture:t2,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.48,disappearAt:.92}]),u.resize(e._vw,e._vh)})()'''
        code = re.sub(s1_old_pattern, s1_new_code, code)

        # In Stage 1 coinRing: ensure coinRing is hidden
        code = code.replace("coinRing:o", "coinRing:null")

        # 2. Update Stage 2 (Middle-finger scene): remove text overlay so visual speaks for itself
        s2_old_pattern = r's=new vb\(i,\[\{texture:c,atlasUV:Nv\(1092\.93,558\.45,945\.23,371\.64\),aspect:Pv\(945\.23,371\.64\),baseScale:\.4,anchor:`center-center`,appearAt:0,disappearAt:\.2\}\]\)'
        s2_new_code = r's=new vb(i,[])'
        code = re.sub(s2_old_pattern, s2_new_code, code)

        # Also remove gate1to2 text overlay if any
        gate1_old_pattern = r'e\._gateTextLayout=new vb\(e\.textScene,\[\{texture:t,atlasUV:Nv\(257\.75,558\.45,247\.06,165\.84\),aspect:Pv\(247\.06,165\.84\),baseScale:\.15,anchor:`center-center`,appearAt:1,disappearAt:2\}\]\)'
        gate1_new_code = r'e._gateTextLayout=new vb(e.textScene,[])'
        code = re.sub(gate1_old_pattern, gate1_new_code, code)

        # 3. Update Stage 3 text layout: "NO LIMITS." then "JUST BUILD."
        s3_old_pattern = r'let t=\[\{texture:h,atlasUV:Nv\(0,371\.64,365\.21,186\.82\),aspect:Pv\(365\.21,186\.82\),baseScale:\.25,anchor:`bottom-left`,appearAt:\.05,disappearAt:\.3\}.*?anchor:`bottom-right`,appearAt:\.87,disappearAt:\.99\}\];'
        s3_new_code = r'''let t3_1=createEditorialTextTexture(`NO LIMITS.`),t3_2=createEditorialTextTexture(`JUST BUILD.`);let t=[{texture:t3_1,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.05,disappearAt:.45},{texture:t3_2,aspect:2.56,baseScale:.42,anchor:`center-center`,appearAt:.50,disappearAt:.92}];'''
        code = re.sub(s3_old_pattern, s3_new_code, code)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print("Updated file successfully:", filepath)

apply_editorial_texts()
