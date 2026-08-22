import re

def update_h_recognition_and_demo():
    new_ng_class = """Ng=class{constructor(e,t,n,r){this.scene=e,this.camera=t,this.assetLoader=n,this.ui=r,this.isReady=!1,this.isComplete=!1,this.strokePoints=[],this.strokes=[],this.currentStroke=[],this.circleCenterUV=null,this.onStageComplete=null,this.onNearComplete=null,this._nearFired=!1,this._resetTimer=null}setReady(){this.isReady=!0}handleInput(e,t,n){if(!(!this.isReady||this.isComplete))if(n){this._resetTimer&&(clearTimeout(this._resetTimer),this._resetTimer=null),this.strokePoints.push(e,t),this.currentStroke.push(e,t),this._checkHGesture()}else{if(this.currentStroke.length>0&&(this.strokes.push([...this.currentStroke]),this.currentStroke=[]),this._checkHGesture(),!this._resetTimer&&!this.isComplete){this._resetTimer=setTimeout(()=>{this.isComplete||(this.strokePoints=[],this.strokes=[],this.currentStroke=[],this._nearFired=!1),this._resetTimer=null},1800)}}}_checkHGesture(){let e=this.strokePoints,t=e.length>>1;if(t<10)return;let n=Infinity,r=-Infinity,i=Infinity,a=-Infinity;for(let t=0;t<e.length;t+=2){let o=e[t],s=e[t+1];o<n&&(n=o),o>r&&(r=o),s<i&&(i=s),s>a&&(a=s)}let o=r-n,s=a-i;if(o<.05||s<.07)return;let c=s/o;if(c<.45||c>3.5)return;let l=n+o*.38,u=r-o*.38,d=i+s*.22,f=a-s*.22,p=[],m=[],h=[],g=[],_=[];for(let t=0;t<e.length;t+=2){let c=e[t],v=e[t+1];c<=l&&p.push(v),c>=u&&m.push(v),c>=n+o*.18&&c<=r-o*.18&&(v>=d&&v<=f?h.push(c):v>a-s*.15?g.push(c):v<i+s*.15&&_.push(c))}if(p.length<3||m.length<3)return;let v=Math.max(...p)-Math.min(...p),y=Math.max(...m)-Math.min(...m);if(v<s*.45||y<s*.45)return;if(h.length<1)return;if(g.length>=4&&_.length>=4&&h.length<2)return;!this._nearFired&&(this._nearFired=!0,this.onNearComplete&&this.onNearComplete());let b=(n+r)*.5,x=(i+a)*.5;this.circleCenterUV={x:(b+1)*.5,y:(x+1)*.5},this._onHComplete()}_onHComplete(){this.isComplete||(this.isComplete=!0,this._resetTimer&&(clearTimeout(this._resetTimer),this._resetTimer=null),this.onStageComplete&&this.onStageComplete())}}"""

    new_co_class = """CO=class{constructor(e=null,t=document.getElementById(`ui-container`)||document.body){this._canvas=e,this._cursorState=`none`,this._container=document.createElement(`div`),this._container.className=`loader-circle-hint`,this._container.setAttribute(`aria-hidden`,`true`);let n=document.createElement(`div`);n.className=`loader-circle-stage`,this._stage=n;let r=document.createElement(`div`);r.className=`loader-circle-ring`,r.style.display=`none`,n.appendChild(r);let i=document.createElement(`div`);i.className=`loader-circle-handle`,n.appendChild(i),this._handle=i,this._container.appendChild(n),t.appendChild(this._container),this._demoActive=!1,this._demoTween=null,this._progress={t:0}}show(){this._container.classList.add(`is-visible`),this._setCursor(`grab`),this._startDemo()}hide(){this._container.classList.remove(`is-visible`),this._stopDemo(),this._setCursor(`none`)}setPointer(e,t,n){n?(this._stopDemo(),this._container.classList.add(`is-dragging`),this._setCursor(`grabbed`)):(this._container.classList.remove(`is-dragging`),this._demoActive||this._startDemo(),this._setCursor(`grab`))}_startDemo(){this._demoActive||(this._demoActive=!0,this._container.classList.add(`is-demo`),this._demoSweep())}_stopDemo(){this._demoActive=!1,this._container.classList.remove(`is-demo`),this._demoTween&&(this._demoTween.kill(),this._demoTween=null)}_getHPoint(e){let t=.18,n=.22;if(e<.32){let r=e/.32;return{x:-t,y:-n+2*n*r,down:!0}}if(e<.42){let r=(e-.32)/.1;return{x:-t,y:0,down:!1}}if(e<.68){let r=(e-.42)/.26;return{x:-t+2*t*r,y:0,down:!0}}if(e<.78){let r=(e-.68)/.1;return{x:t,y:-n,down:!1}}if(e<=1){let r=(e-.78)/.22;return{x:t,y:-n+2*n*r,down:!0}}return{x:t,y:n,down:!1}}_demoSweep(){if(!this._demoActive)return;this._progress.t=0,this._demoTween=Y.to(this._progress,{t:1,duration:2.4,ease:`linear`,onUpdate:()=>{let e=this._getHPoint(this._progress.t),t=this._stage.offsetWidth||window.innerHeight*.4,n=this._stage.offsetHeight||window.innerHeight*.4;this._handle.style.transform=`translate3d(${e.x*t*1.6}px, ${e.y*n*1.6}px, 0)`,Ck&&!Mk&&Ck.setCursor(e.x*1.1,-e.y*1.1)},onComplete:()=>{this._demoActive&&(this._demoTween=Y.delayedCall(1.2,()=>{this._demoActive&&this._demoSweep()}))}})}resize(){}_setCursor(e){e!==this._cursorState&&(this._cursorState=e,this._canvas&&(e===`grabbed`?this._canvas.style.cursor=AC():e===`grab`?this._canvas.style.cursor=kC():this._canvas.style.cursor=``))}dispose(){this._stopDemo(),this._container.parentNode&&this._container.parentNode.removeChild(this._container),this._setCursor(`none`)}}"""

    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        # Replace Ng class
        ng_start = code.find("Ng=class{")
        ng_end = code.find("Pg={", ng_start)
        if ng_start != -1 and ng_end != -1:
            code = code[:ng_start] + new_ng_class + "," + code[ng_end:]
            print("Replaced Ng class in:", filepath)

        # Replace CO class
        co_start = code.find("CO=class{")
        co_end = code.find("wO=`assets/videos/", co_start)
        if co_start != -1 and co_end != -1:
            code = code[:co_start] + new_co_class + "," + code[co_end:]
            print("Replaced CO class in:", filepath)
        else:
            print("Could not find CO class in:", filepath)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print("Updated file:", filepath)

update_h_recognition_and_demo()
