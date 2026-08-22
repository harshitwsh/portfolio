import re

def update_ng_refined():
    new_ng_class = """Ng=class{constructor(e,t,n,r){this.scene=e,this.camera=t,this.assetLoader=n,this.ui=r,this.isReady=!1,this.isComplete=!1,this.strokePoints=[],this.strokes=[],this.currentStroke=[],this.circleCenterUV=null,this.onStageComplete=null,this.onNearComplete=null,this._nearFired=!1,this._resetTimer=null}setReady(){this.isReady=!0}handleInput(e,t,n){if(!(!this.isReady||this.isComplete))if(n){this._resetTimer&&(clearTimeout(this._resetTimer),this._resetTimer=null),this.strokePoints.push(e,t),this.currentStroke.push(e,t),this._checkHGesture()}else{if(this.currentStroke.length>0&&(this.strokes.push([...this.currentStroke]),this.currentStroke=[]),this._checkHGesture(),!this._resetTimer&&!this.isComplete){this._resetTimer=setTimeout(()=>{this.isComplete||(this.strokePoints=[],this.strokes=[],this.currentStroke=[],this._nearFired=!1),this._resetTimer=null},2500)}}}_checkHGesture(){let e=this.strokePoints,t=e.length>>1;if(t<12)return;let n=0,r=0;for(let t=0;t<e.length;t+=2)n+=e[t],r+=e[t+1];n/=t,r/=t;let i=0,a=0,o=0;for(let s=0;s<e.length;s+=2){let c=e[s]-n,l=e[s+1]-r;i+=c*c,a+=l*l,o+=c*l}if(i>1e-5&&a>1e-5){let e=o*o/(i*a);if(e>.78)return}let s=Infinity,c=-Infinity,l=Infinity,u=-Infinity;for(let t=0;t<e.length;t+=2){let n=e[t],r=e[t+1];n<s&&(s=n),n>c&&(c=n),r<l&&(l=r),r>u&&(u=r)}let d=c-s,f=u-l;if(d<.06||f<.08)return;let p=f/d;if(p<.4||p>3.5)return;let m=s+d*.35,h=c-d*.35,g=l+f*.18,_=u-f*.18,v=[],y=[],b=[];for(let t=0;t<e.length;t+=2){let n=e[t],r=e[t+1];n<=m&&v.push(r),n>=h&&y.push(r),n>=s+d*.2&&n<=c-d*.2&&r>=g&&r<=_&&b.push(n)}if(v.length<4||y.length<4)return;let x=Math.max(...v)-Math.min(...v),S=Math.max(...y)-Math.min(...y);if(x<f*.48||S<f*.48)return;let C=Math.max(Math.min(...v),Math.min(...y)),w=Math.min(Math.max(...v),Math.max(...y));if(Math.max(0,w-C)<f*.35)return;if(b.length<1)return;!this._nearFired&&(this._nearFired=!0,this.onNearComplete&&this.onNearComplete());let T=(s+c)*.5,E=(l+u)*.5;this.circleCenterUV={x:(T+1)*.5,y:(E+1)*.5},this._onHComplete()}_onHComplete(){this.isComplete||(this.isComplete=!0,this._resetTimer&&(clearTimeout(this._resetTimer),this._resetTimer=null),this.onStageComplete&&this.onStageComplete())}}"""

    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        ng_start = code.find("Ng=class{")
        ng_end = code.find("Pg={", ng_start)
        if ng_start != -1 and ng_end != -1:
            code = code[:ng_start] + new_ng_class + "," + code[ng_end:]
            print("Replaced refined Ng class in:", filepath)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print("Updated file:", filepath)

update_ng_refined()
