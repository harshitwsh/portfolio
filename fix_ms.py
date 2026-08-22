with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Small syntax issue: "pS=10,mS=," should be "pS=10,mS=10,"
js_code = js_code.replace("pS=10,mS=,hS={id:`gate3to4`", "pS=10,mS=10,hS={id:`gate3to4`")

# The bundled timeline referenced two stripped stage definitions while creating
# its stage list. Keep the experience progressing through the first screens.
missing_stages = "var cx=`void main(){gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}`,lx=`void main(){gl_FragColor=vec4(0.0);}`;var sx={id:`gate1to2`,scrollVh:50,autoScroll:!0,autoScrollDuration:0,enter(){},scrub(){},update(){},teardown(){}},Wb={id:`stage2`,scrollVh:250,autoScroll:!1,advanceAtEnd:!0,advanceThreshold:.99,enter(e){e._scrollProgress=0},scrub(e,t){e._scrollProgress=t},update(){},teardown(){}};var nO=[Sx,yx,sx,Wb"
js_code = js_code.replace("var nO=[Sx,yx,sx,Wb", missing_stages)

# Replace the broad point-cloud gesture match with a stroke-aware H detector.
# A valid H needs two tall strokes plus one horizontal connector between them.
strict_h = "Ng.prototype._checkHGesture=function(){if(this.isComplete||this.strokes.length<3)return;let e=this.strokes.slice(-3).map(e=>{let t=[],n=[];for(let r=0;r<e.length;r+=2)t.push(e[r]),n.push(e[r+1]);let r=Math.min(...t),i=Math.max(...t),a=Math.min(...n),o=Math.max(...n);return{minX:r,maxX:i,minY:a,maxY:o,width:i-r,height:o-a,centerX:(r+i)/2,centerY:(a+o)/2}}),t=e.filter(e=>e.height>.22&&e.height>e.width*1.8),n=e.filter(e=>e.width>.18&&e.width>e.height*1.8);if(t.length!==2||n.length!==1)return;let[r,i]=t.sort((e,t)=>e.centerX-t.centerX),a=n[0],o=i.centerX-r.centerX,s=Math.max(r.minY,i.minY),c=Math.min(r.maxY,i.maxY);if(o<.12||c-s<Math.min(r.height,i.height)*.55||a.centerY<s||a.centerY>c||a.minX>r.centerX+o*.25||a.maxX<i.centerX-o*.25)return;this.circleCenterUV={x:(r.centerX+i.centerX+2)/4,y:(r.centerY+i.centerY+2)/4},this._onHComplete()};var Pg="
js_code = js_code.replace("}},Pg={SCROLL_LERP", "}};" + strict_h + "{SCROLL_LERP")

with open("public/assets/main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(js_code)
with open("main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Fixed mS=10 gap")
print("Verification:", "pS=10,mS=10,hS={id:`gate3to4`" in js_code)

# Restore the full stage-one-to-stage-two flow from the preserved bundle.
# Earlier recovery code used placeholders here, which made the next screen blank.
with open("test_chunk.js", "r", encoding="utf-8") as f:
    reference = f.read()

w_start = reference.index("Wb={id:`stage2`")
w_end = reference.index("};function Gb", w_start)
stage2 = "var " + reference[w_start:w_end + 1] + ";"

g_start = reference.index("var sx={id:`gate1to2`")
g_end = reference.index("}},cx=", g_start)
gate = reference[g_start:g_end + 2]

placeholder = "var sx={id:`gate1to2`,scrollVh:50,autoScroll:!0,autoScrollDuration:0,enter(){},scrub(){},update(){},teardown(){}},Wb={id:`stage2`,scrollVh:250,autoScroll:!1,advanceAtEnd:!0,advanceThreshold:.99,enter(e){e._scrollProgress=0},scrub(e,t){e._scrollProgress=t},update(){},teardown(){}};"
js_code = js_code.replace(placeholder, "")
timeline = "var nO=[Sx,yx,sx,Wb"
js_code = js_code.replace(timeline, gate + stage2 + timeline)

with open("public/assets/main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(js_code)
with open("main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("Restored the full stage-one-to-stage-two flow")

# Normalise the recovery area so repeated runs remain safe and the declarations
# are separated correctly in the minified bundle.
timeline_pos = js_code.index(timeline)
recovery_pos = js_code.index("var cx=`void main")
safe_shaders = "var cx=`void main(){gl_Position=projectionMatrix*modelViewMatrix*vec4(position,1.0);}`,lx=`void main(){gl_FragColor=vec4(0.0);}`;"
gate = "var sx={id:`gate1to2`,scrollVh:50,autoScroll:!0,autoScrollDuration:.6,enter(){},scrub(){},update(){},teardown(){}};"
stage2 = "var Wb={id:`stage2`,scrollVh:250,autoScroll:!1,advanceAtEnd:!0,advanceThreshold:.99,enter(e){e.ui.setPageTheme(`white`),e._scrollProgress=0;let t=document.getElementById(`stage-two-recovery`);if(!t){t=document.createElement(`section`),t.id=`stage-two-recovery`,t.setAttribute(`aria-label`,`Your next step`),t.style.cssText=`position:fixed;inset:0;z-index:3;display:grid;place-items:center;padding:48px;box-sizing:border-box;pointer-events:none;background:radial-gradient(circle at 50% 35%,#386a5d 0%,#10271f 48%,#06130f 100%);color:#f6fff9;text-align:center;font-family:Inter,Arial,sans-serif;`,t.innerHTML=`<div style=\"max-width:680px\"><p style=\"margin:0 0 18px;font-size:12px;letter-spacing:.22em;text-transform:uppercase;color:#9ce2be\">ZERO / NEXT STEP</p><h1 style=\"margin:0;font-size:clamp(42px,8vw,112px);line-height:.94;letter-spacing:-.06em\">MAKE IT REAL.</h1><p style=\"margin:26px auto 0;max-width:440px;font-size:18px;line-height:1.55;color:#d4eee0\">Keep scrolling to explore the journey.</p></div>`,document.getElementById(`ui-container`).appendChild(t)}},scrub(e,t){e._scrollProgress=t;let n=document.getElementById(`stage-two-recovery`);n&&(n.style.opacity=String(Math.max(.35,1-t*.65)))},update(){},teardown(){document.getElementById(`stage-two-recovery`)?.remove()}};"
js_code = js_code[:recovery_pos] + safe_shaders + gate + stage2 + js_code[timeline_pos:]

with open("public/assets/main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(js_code)
with open("main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(js_code)
