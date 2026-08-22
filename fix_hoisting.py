with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

# Remove from bottom
code = code.replace(r'''window.createEditorialTextTexture=function(e,t=""){let n=document.createElement(`canvas`);n.width=2048,n.height=800;let r=n.getContext(`2d`);r.clearRect(0,0,n.width,n.height),r.fillStyle=`#ffffff`,r.textAlign=`center`,r.textBaseline=`middle`,r.shadowColor=`rgba(0,0,0,0.4)`,r.shadowBlur=16;if(t){r.font=`italic 400 90px "Bethany Elingston", "STK Bureau Serif", Georgia, serif`,r.fillText(t,1024,310),r.font=`700 160px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,490)}else{r.font=`700 170px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,400)}let i=new dc(n);return i.colorSpace=W,i.generateMipmaps=!0,i.minFilter=v,i.magFilter=v,i.needsUpdate=!0,i};''', "")

# Define function createEditorialTextTexture right before _x
helper = r'''function createEditorialTextTexture(e,t=""){let n=document.createElement(`canvas`);n.width=2048,n.height=800;let r=n.getContext(`2d`);r.clearRect(0,0,n.width,n.height),r.fillStyle=`#ffffff`,r.textAlign=`center`,r.textBaseline=`middle`,r.shadowColor=`rgba(0,0,0,0.4)`,r.shadowBlur=16;if(t){r.font=`italic 400 90px "Bethany Elingston", "STK Bureau Serif", Georgia, serif`,r.fillText(t,1024,310),r.font=`700 160px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,490)}else{r.font=`700 170px "STK Bureau Serif", "Bethany Elingston", Georgia, serif`,r.fillText(e,1024,400)}let i=new dc(n);return i.colorSpace=W,i.generateMipmaps=!0,i.minFilter=v,i.magFilter=v,i.needsUpdate=!0,i};'''

pos = code.find("function _x(e)")
if pos != -1:
    code = code[:pos] + helper + code[pos:]
    print("Placed createEditorialTextTexture before _x function")

with open("public/assets/main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(code)
with open("main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated files successfully")
