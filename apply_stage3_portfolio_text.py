def apply_stage3_portfolio_text():
    target_files = [
        'public/assets/main-B9-HtP-f.js',
        'main-B9-HtP-f.js'
    ]

    stage3_helper = '''function createStage3TextTexture(e,t,n=""){let r=document.createElement("canvas");r.width=2400,r.height=1300;let i=r.getContext("2d");i.clearRect(0,0,r.width,r.height);let a=i.createLinearGradient(0,200,0,950);if(a.addColorStop(0,"#ffffff"),a.addColorStop(.3,"#e2faf2"),a.addColorStop(.7,"#c1efe0"),a.addColorStop(1,"#a5e2cf"),i.fillStyle=a,i.shadowColor="rgba(10,35,25,0.5)",i.shadowBlur=20,i.shadowOffsetY=6,n){i.font='400 120px "STK Bureau Serif", "Times New Roman", Georgia, serif',i.textAlign="left",i.textBaseline="alphabetic",i.fillText(e,450,420),i.font='italic 400 240px "Bethany Elingston", "Times New Roman", cursive, serif',i.fillText(t,450,680),i.font='700 160px "STK Bureau Serif", "Times New Roman", Georgia, serif',i.fillText(n,450,880)}else{i.font='400 170px "STK Bureau Serif", "Times New Roman", Georgia, serif',i.textAlign="left",i.textBaseline="alphabetic",i.fillText(e,450,520),i.font='italic 400 290px "Bethany Elingston", "Times New Roman", cursive, serif',i.fillText(t,550,790)}let o=new dc(r);return o.colorSpace=W,o.generateMipmaps=!0,o.minFilter=v,o.magFilter=v,o.needsUpdate=!0,o};'''

    for filepath in target_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        # 1. Add createStage3TextTexture helper
        pos_h = code.find('function createEditorialTextTexture(')
        if pos_h != -1:
            code = code[:pos_h] + stage3_helper + code[pos_h:]

        # 2. Update Stage 3 textLayout in Xx
        pos_s3_text = code.find('let h=e.assetLoader.getAsset(`textsAtlas`);if(h){')
        pos_s3_text_end = code.find('let g=Math.PI/180;e._stage3QuatA', pos_s3_text)

        if pos_s3_text != -1 and pos_s3_text_end != -1:
            new_s3_text = '''(()=>{let t=[
{texture:createStage3TextTexture(`University`,`taught me.`),aspect:1.85,baseScale:.52,anchor:`center-center`,appearAt:.01,disappearAt:.15},
{texture:createStage3TextTexture(`Freelancing`,`shaped me.`),aspect:1.85,baseScale:.52,anchor:`center-center`,appearAt:.14,disappearAt:.27},
{texture:createStage3TextTexture(`but`,`Building`,`changed everything.`),aspect:1.85,baseScale:.54,anchor:`center-center`,appearAt:.26,disappearAt:.39},
{texture:createStage3TextTexture(`I stopped`,`waiting for opportunities.`),aspect:1.85,baseScale:.52,anchor:`center-center`,appearAt:.38,disappearAt:.51},
{texture:createStage3TextTexture(`I started`,`creating them.`),aspect:1.85,baseScale:.52,anchor:`center-center`,appearAt:.50,disappearAt:.63},
{texture:createStage3TextTexture(`Ideas became`,`projects.`),aspect:1.85,baseScale:.52,anchor:`center-center`,appearAt:.62,disappearAt:.75},
{texture:createStage3TextTexture(`Projects became`,`products.`),aspect:1.85,baseScale:.52,anchor:`center-center`,appearAt:.74,disappearAt:.87},
{texture:createStage3TextTexture(`and that's`,`why`,`I build.`),aspect:1.85,baseScale:.55,anchor:`center-center`,appearAt:.86,disappearAt:.99}
],n=new vb(e.textScene,t);n.resize(e._vw,e._vh),e.components.textLayout=n})();'''
            code = code[:pos_s3_text] + new_s3_text + code[pos_s3_text_end:]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Applied Stage 3 portfolio texts to', filepath)

if __name__ == '__main__':
    apply_stage3_portfolio_text()
