def fix_var_vb():
    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        # Clean up the insertion spot
        old_piece = r''';function createEditorialTextTexture(e,t=""){let n=document.createElement(`canvas`);n.width=2048,n.height=800;let r=n.getContext(`2d`);r.clearRect(0,0,n.width,n.height),r.fillStyle=`#ffffff`,r.textAlign=`center`,r.textBaseline=`middle`,r.shadowColor=`rgba(0,0,0,0.4)`,r.shadowBlur=16;if(t){r.font=`italic 400 90px "Bethany Elingston", "STK Bureau Serif", Georgia, serif`,r.fillText(t,1024,310),r.font=`700 160px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,490)}else{r.font=`700 170px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,400)}let i=new dc(n);return i.colorSpace=W,i.generateMipmaps=!0,i.minFilter=v,i.magFilter=v,i.needsUpdate=!0,i};vb=class{'''
        new_piece = r''',vb=class{'''
        code = code.replace(old_piece, new_piece)

        # Now put function createEditorialTextTexture cleanly at top level
        helper = r'''function createEditorialTextTexture(e,t=""){let n=document.createElement(`canvas`);n.width=2048,n.height=800;let r=n.getContext(`2d`);r.clearRect(0,0,n.width,n.height),r.fillStyle=`#ffffff`,r.textAlign=`center`,r.textBaseline=`middle`,r.shadowColor=`rgba(0,0,0,0.4)`,r.shadowBlur=16;if(t){r.font=`italic 400 90px "Bethany Elingston", "STK Bureau Serif", Georgia, serif`,r.fillText(t,1024,310),r.font=`700 160px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,490)}else{r.font=`700 170px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,400)}let i=new dc(n);return i.colorSpace=W,i.generateMipmaps=!0,i.minFilter=v,i.magFilter=v,i.needsUpdate=!0,i};'''
        
        # Place helper right after vb class definition ends
        if "function createEditorialTextTexture" not in code:
            vb_end = code.find("this.group.clear()}}") + len("this.group.clear()}}")
            code = code[:vb_end] + ";" + helper + code[vb_end:]

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print("Fixed var vb in:", filepath)

fix_var_vb()
