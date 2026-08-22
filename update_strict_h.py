def update_strict_h():
    js_h_recognizer = '''Ng=class{constructor(e,t,n,r){this.scene=e,this.camera=t,this.assetLoader=n,this.ui=r,this.isReady=!1,this.isComplete=!1,this.strokePoints=[],this.strokes=[],this.currentStroke=[],this.circleCenterUV=null,this.onStageComplete=null,this.onNearComplete=null,this._nearFired=!1,this._resetTimer=null}setReady(){this.isReady=!0}handleInput(e,t,n){if(!(!this.isReady||this.isComplete))if(n){this._resetTimer&&(clearTimeout(this._resetTimer),this._resetTimer=null),this.strokePoints.push(e,t),this.currentStroke.push(e,t),this._checkHGesture(!1)}else{if(this.currentStroke.length>0&&(this.strokes.push([...this.currentStroke]),this.currentStroke=[]),this._checkHGesture(!0),!this._resetTimer&&!this.isComplete){this._resetTimer=setTimeout(()=>{this.isComplete||(this.strokePoints=[],this.strokes=[],this.currentStroke=[],this._nearFired=!1),this._resetTimer=null},2500)}}}_checkHGesture(e=!1){if(this.isComplete)return;let t=this.strokePoints,n=t.length>>1;if(n<8)return;let r=this.strokes.filter(e=>e.length>=4);if(r.length>=3){let e=r.slice(-3).map(e=>{let t=[],n=[];for(let r=0;r<e.length;r+=2)t.push(e[r]),n.push(e[r+1]);let r=Math.min(...t),i=Math.max(...t),a=Math.min(...n),o=Math.max(...n);return{minX:r,maxX:i,minY:a,maxY:o,w:i-r,h:o-a,cx:(r+i)*.5,cy:(a+o)*.5}}),t=e.filter(e=>e.h>.08&&e.h>=e.w*1.1),n=e.filter(e=>e.w>.06&&e.w>=e.h*.8);if(t.length===2&&n.length===1){let[e,r]=t.sort((e,t)=>e.cx-t.cx),i=n[0],a=r.cx-e.cx;if(a>.05){let o=Math.max(e.minY,r.minY),s=Math.min(e.maxY,r.maxY),c=s-o,l=Math.min(e.h,r.h);if(c>l*.35&&i.cy>=o-l*.25&&i.cy<=s+l*.25&&i.minX<=e.cx+a*.45&&i.maxX>=r.cx-a*.45){this.circleCenterUV={x:(e.cx+r.cx+2)*.25,y:(e.cy+r.cy+2)*.25},this._onHComplete();return}}}}let i=[],a=[];for(let e=0;e<t.length;e+=2)i.push(t[e]),a.push(t[e+1]);let o=Math.min(...i),s=Math.max(...i),c=Math.min(...a),l=Math.max(...a),u=s-o,d=l-c;if(u<.06||d<.08)return;let f=d/u;if(f<.45||f>3)return;let p=i.reduce((e,t)=>e+t,0)/n,m=a.reduce((e,t)=>e+t,0)/n,h=0,g=0,_=0;for(let e=0;e<n;e++){let t=i[e]-p,n=a[e]-m;h+=t*t,g+=n*n,_+=t*n}if(h>1e-5&&g>1e-5&&_*_/ (h*g)>.78)return;let v=o+u*.35,y=s-u*.35,b=c+d*.2,x=l-d*.2,S=[],C=[],w=[],T=[],E=[];for(let e=0;e<n;e++){let t=i[e],n=a[e];t<=v&&S.push(n),t>=y&&C.push(n),t>v&&t<y&&(n>=b&&n<=x&&w.push(t),n>l-d*.15&&T.push(t),n<c+d*.15&&E.push(t))}if(S.length<3||C.length<3)return;let D=Math.max(...S)-Math.min(...S),k=Math.max(...C)-Math.min(...C);if(D<d*.5||k<d*.5||w.length<1)return;if(T.length>=w.length*1.5&&E.length>=w.length*1.5)return;!this._nearFired&&(this._nearFired=!0,this.onNearComplete&&this.onNearComplete());if(e||r.length>=2||w.length>=2){this.circleCenterUV={x:(o+s+2)*.25,y:(c+l+2)*.25},this._onHComplete()}}_onHComplete(){if(!this.isComplete){this.isComplete=!0;this._resetTimer&&(clearTimeout(this._resetTimer),this._resetTimer=null);if(typeof wk!=="undefined"&&wk){try{Y.killTweensOf(wk);wk.dispose();wk=null;}catch{}document.body.classList.remove("webgl-loader-overlay");}this.onStageComplete&&this.onStageComplete();}}};'''

    for path in ['public/assets/main-B9-HtP-f.js', 'main-B9-HtP-f.js']:
        with open(path, 'r', encoding='utf-8') as f:
            code = f.read()

        pos1 = code.find('Ng=class{')
        pos2 = code.find(';var Pg=')
        if pos1 != -1 and pos2 != -1:
            code = code[:pos1] + js_h_recognizer + code[pos2+1:]
            with open(path, 'w', encoding='utf-8') as f:
                f.write(code)
            print(f'Applied strict H recognition in {path}')
        else:
            print(f'Could not find Ng markers in {path}')

if __name__ == '__main__':
    update_strict_h()
