def fix_helper_placement():
    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        # Remove previous helper insertions
        code = code.replace(";function createEditorialTextTexture", "")
        code = code.replace("function createEditorialTextTexture(e,t=\"\"){let n=document.createElement(`canvas`);n.width=2048,n.height=800;let r=n.getContext(`2d`);r.clearRect(0,0,n.width,n.height),r.fillStyle=`#ffffff`,r.textAlign=`center`,r.textBaseline=`middle`,r.shadowColor=`rgba(0,0,0,0.4)`,r.shadowBlur=16;if(t){r.font=`italic 400 90px \"Bethany Elingston\", \"STK Bureau Serif\", Georgia, serif`,r.fillText(t,1024,310),r.font=`700 160px \"STK Bureau Serif\", \"Bethany Elingston\", Georgia, serif`,r.fillText(e,1024,490)}else{r.font=`700 170px \"STK Bureau Serif\", \"Bethany Elingston\", Georgia, serif`,r.fillText(e,1024,400)}let i=new dc(n);return i.colorSpace=W,i.generateMipmaps=!0,i.minFilter=v,i.magFilter=v,i.needsUpdate=!0,i};", "")

        # Attach to global window or define at top-level safely
        helper = r'''window.createEditorialTextTexture=function(e,t=""){let n=document.createElement(`canvas`);n.width=2048,n.height=800;let r=n.getContext(`2d`);r.clearRect(0,0,n.width,n.height),r.fillStyle=`#ffffff`,r.textAlign=`center`,r.textBaseline=`middle`,r.shadowColor=`rgba(0,0,0,0.4)`,r.shadowBlur=16;if(t){r.font=`italic 400 90px "Bethany Elingston", "STK Bureau Serif", Georgia, serif`,r.fillText(t,1024,310),r.font=`700 160px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,490)}else{r.font=`700 170px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,400)}let i=new dc(n);return i.colorSpace=W,i.generateMipmaps=!0,i.minFilter=v,i.magFilter=v,i.needsUpdate=!0,i};'''

        # Place at end of file
        code = code + "\n" + helper

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print("Fixed helper placement in:", filepath)

fix_helper_placement()
