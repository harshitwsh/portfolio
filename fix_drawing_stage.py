
with open('public/assets/main-B9-HtP-f.js', 'r', encoding='utf-8') as f:
    code = f.read()

old_stage_complete = 'else Ak.onStageComplete=()=>{X.play(),Sk.onCircleComplete(),RO(Ek),Ck&&Ck.exit(),Tk&&Tk.hide(),qk.unpin(),$._stage2VideoPrefetch||=Dv(),'
new_stage_complete = 'else Ak.onStageComplete=()=>{X.play(),Sk.onCircleComplete(),RO(Ek),Ck&&Ck.exit(),Tk&&Tk.hide(),qk.unpin(),wk&&(Y.killTweensOf(wk),wk.dispose(),wk=null,document.body.classList.remove()),$._stage2VideoPrefetch||=Dv(),'

new_ng_code = """Ng=class{constructor(e,t,n,r){this.scene=e,this.camera=t,this.assetLoader=n,this.ui=r,this.isReady=!1,this.isComplete=!1,this.strokePoints=[],this.strokes=[],this.currentStroke=[],this.circleCenterUV=null,this.onStageComplete=null,this.onNearComplete=null,this._nearFired=!1,this._resetTimer=null;window.addEventListener(,e=>{if(this.isReady&&!this.isComplete&&(e.key===||e.key===||e.key===||e.key===||e.key===)){e.preventDefault();this._onHComplete();}})}setReady(){this.isReady=!0}handleInput(e,t,n){if(!(!this.isReady||this.isComplete))if(n){this._resetTimer&&(clearTimeout(this._resetTimer),this._resetTimer=null),this.strokePoints.push(e,t),this.currentStroke.push(e,t),this._checkHGesture(!1)}else{if(this.currentStroke.length>0&&(this.strokes.push([...this.currentStroke]),this.currentStroke=[]),this._checkHGesture(!0),!this._resetTimer&&!this.isComplete){this._resetTimer=setTimeout(()=>{this.isComplete||(this.strokePoints=[],this.strokes=[],this.currentStroke=[],this._nearFired=!1),this._resetTimer=null},3e3)}}}_checkHGesture(e=!1){if(this.isComplete)return;let t=this.strokePoints,n=t.length>>1;if(n<3)return;let r=Infinity,i=-Infinity,a=Infinity,o=-Infinity;for(let e=0;e<t.length;e+=2){let n=t[e],s=t[e+1];n<r&&(r=n),n>i&&(i=n),s<a&&(a=s),s>o&&(o=s)}let s=i-r,c=o-a,l=(r+i)*.5,u=(a+o)*.5;if(this.circleCenterUV={x:(l+1)*.5,y:(u+1)*.5},!this._nearFired&&n>=4&&(this._nearFired=!0,this.onNearComplete&&this.onNearComplete()),this.strokes.length>=2||(this.strokes.length===1&&e)){if(s>.02||c>.02||n>=6){this._onHComplete();return}}if(s>.05||c>.05||n>=8){this._onHComplete();return}if(e&&n>=3){this._onHComplete();return}}_onHComplete(){if(!this.isComplete){this.isComplete=!0;this._resetTimer&&(clearTimeout(this._resetTimer),this._resetTimer=null);if(typeof wk!==&&wk){try{Y.killTweensOf(wk);wk.dispose();wk=null;}catch{}document.body.classList.remove();}this.onStageComplete&&this.onStageComplete();}}};"""

for path in ['public/assets/main-B9-HtP-f.js', 'main-B9-HtP-f.js']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    
    pos1 = c.find('Ng=class{')
    pos2 = c.find(';var Pg=')
    if pos1 != -1 and pos2 != -1:
        c = c[:pos1] + new_ng_code + c[pos2+1:]
    
    if old_stage_complete in c:
        c = c.replace(old_stage_complete, new_stage_complete)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print('Updated', path)
