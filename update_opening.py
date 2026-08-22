import re

def update_opening_screen():
    # 1. Update nav_logo_white.svg with "HARSHIT" SVG
    harshit_svg = '''<svg width="180" height="30" viewBox="0 0 180 30" fill="none" xmlns="http://www.w3.org/2000/svg">
  <text x="0" y="24" fill="white" font-family="'Supply Sans', 'PPSupplySans-Regular', monospace" font-size="28" font-weight="700" letter-spacing="0.05em">HARSHIT</text>
</svg>'''
    with open("public/assets/brand/nav_logo_white.svg", "w", encoding="utf-8") as f:
        f.write(harshit_svg)
    print("Updated public/assets/brand/nav_logo_white.svg")

    # 2. Update public/assets/main-B9-HtP-f.js and main-B9-HtP-f.js
    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    new_ng_class = """Ng=class{constructor(e,t,n,r){this.scene=e,this.camera=t,this.assetLoader=n,this.ui=r,this.isReady=!1,this.isComplete=!1,this.strokePoints=[],this.strokes=[],this.currentStroke=[],this.circleCenterUV=null,this.onStageComplete=null,this.onNearComplete=null,this._nearFired=!1,this._resetTimer=null}setReady(){this.isReady=!0}handleInput(e,t,n){if(!(!this.isReady||this.isComplete))if(n){this._resetTimer&&(clearTimeout(this._resetTimer),this._resetTimer=null),this.strokePoints.push(e,t),this.currentStroke.push(e,t),this._checkHGesture()}else{if(this.currentStroke.length>0&&(this.strokes.push([...this.currentStroke]),this.currentStroke=[]),this._checkHGesture(),!this._resetTimer&&!this.isComplete){this._resetTimer=setTimeout(()=>{this.isComplete||(this.strokePoints=[],this.strokes=[],this.currentStroke=[],this._nearFired=!1),this._resetTimer=null},2000)}}}_checkHGesture(){let e=this.strokePoints,t=e.length>>1;if(t<8)return;let n=Infinity,r=-Infinity,i=Infinity,a=-Infinity;for(let t=0;t<e.length;t+=2){let o=e[t],s=e[t+1];o<n&&(n=o),o>r&&(r=o),s<i&&(i=s),s>a&&(a=s)}let o=r-n,s=a-i;if(o<.03||s<.05)return;let c=(n+r)*.5,l=(i+a)*.5,u=0,d=Infinity,f=-Infinity,p=0,m=Infinity,h=-Infinity,g=0;for(let t=0;t<e.length;t+=2){let c=e[t],l=e[t+1];c<=n+o*.45&&(u++,l<d&&(d=l),l>f&&(f=l)),c>=r-o*.45&&(p++,l<m&&(m=l),l>h&&(h=l)),c>=n+o*.18&&c<=r-o*.18&&l>=i+s*.15&&l<=a-s*.15&&g++}let _=f>d?f-d:0,v=h>m?h-m:0,y=u>=3&&_>=s*.38,b=p>=3&&v>=s*.38,x=g>=1,S=0;for(let t=2;t<e.length;t+=2){let n=e[t]-e[t-2],r=e[t+1]-e[t-1];S+=Math.sqrt(n*n+r*r)}!this._nearFired&&(y||b)&&S>s*.6&&(this._nearFired=!0,this.onNearComplete&&this.onNearComplete());let C=(y&&b&&(x||S>=s*1.3+o*.4))||(_>=s*.45&&v>=s*.45&&g>=1&&t>=10)||(S>=s*2.2&&o>=.04&&s>=.06);if(C){this.circleCenterUV={x:(c+1)*.5,y:(l+1)*.5},this._onHComplete()}}_onHComplete(){this.isComplete||(this.isComplete=!0,this._resetTimer&&(clearTimeout(this._resetTimer),this._resetTimer=null),this.onStageComplete&&this.onStageComplete())}}"""

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        # Replace DRAW A ZERO with DRAW A H
        code = code.replace("`DRAW A ZERO`", "`DRAW A H`")
        code = code.replace('"DRAW A ZERO"', '"DRAW A H"')
        code = code.replace("'DRAW A ZERO'", "'DRAW A H'")

        # Replace alt ZERO with alt HARSHIT in loader logo
        code = re.sub(r't\.alt=`ZERO`', 't.alt=`HARSHIT`', code)
        code = re.sub(r't\.alt="ZERO"', 't.alt="HARSHIT"', code)

        # Replace Ng class with new H gesture detector
        ng_start = code.find("Ng=class{")
        ng_end = code.find("Pg={", ng_start)
        if ng_start != -1 and ng_end != -1:
            code = code[:ng_start] + new_ng_class + "," + code[ng_end:]
            print("Replaced Ng class in:", filepath)
        else:
            print("Could not find Ng class range in:", filepath)

        # In vO._draw, ensure "HARSHIT" text is drawn as branding
        # Find _draw() in vO
        vo_draw_pattern = r'if\(this\._logoImage&&p>\.001\)\{e\.globalAlpha=p;let t=i,n=t\*\(this\._logoImage\.width/this\._logoImage\.height\);e\.drawImage\(this\._logoImage,a,o-t\+u,n,t\)\}'
        vo_draw_replacement = r'if(p>.001){e.globalAlpha=p;if(this._logoImage&&this._logoImage.complete&&this._logoImage.naturalWidth>0){let t=i,n=t*(this._logoImage.width/this._logoImage.height);e.drawImage(this._logoImage,a,o-t+u,n,t)}else{e.fillStyle=`#ffffff`,e.font=`700 ${i}px \'Supply Sans\', monospace`,e.textAlign=`left`,e.textBaseline=`alphabetic`,e.fillText(`HARSHIT`,a,o+u)}}'
        code = re.sub(vo_draw_pattern, vo_draw_replacement, code)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print("Updated file:", filepath)

update_opening_screen()
