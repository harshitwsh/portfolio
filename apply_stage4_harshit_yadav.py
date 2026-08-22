def apply_stage4_harshit_yadav():
    target_files = [
        'public/assets/main-B9-HtP-f.js',
        'main-B9-HtP-f.js'
    ]

    stage4_helper = '''function createStage4BrandTexture(e="Harshit",t="Yadav"){let n=document.createElement("canvas");n.width=2400,n.height=1400;let r=n.getContext("2d");r.clearRect(0,0,n.width,n.height);let i=r.createLinearGradient(0,250,0,1150);i.addColorStop(0,"#5b8493"),i.addColorStop(.35,"#7198a6"),i.addColorStop(.65,"#9cbcc8"),i.addColorStop(.88,"rgba(200,225,235,0.45)"),i.addColorStop(1,"rgba(255,255,255,0)"),r.fillStyle=i,r.textAlign="center",r.textBaseline="alphabetic",r.font='800 360px "Cabinet Grotesk", "STK Bureau Serif", -apple-system, sans-serif',r.letterSpacing="-0.04em",r.fillText(e,1200,620),r.fillText(t,1200,1020);let a=new dc(n);return a.colorSpace=W,a.generateMipmaps=!0,a.minFilter=v,a.magFilter=v,a.needsUpdate=!0,a};'''

    for filepath in target_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        # 1. Add createStage4BrandTexture helper
        pos_h = code.find('function createShardTextTexture(')
        if pos_h != -1:
            code = code[:pos_h] + stage4_helper + code[pos_h:]

        # 2. Update Stage 4 s mapping to use createStage4BrandTexture for i === 0
        old_map = 's=t.map(([e,t,n,r],i)=>({texture:h,atlasUV:Nv(e,t,n,r),aspect:Pv(n,r),baseScale:.35,anchor:`center-center`,appearAt:o[i][0],disappearAt:o[i][1]}))'
        new_map = 's=t.map(([e,t,n,r],i)=>i===0?{texture:createStage4BrandTexture(`Harshit`,`Yadav`),aspect:1.71,baseScale:.65,anchor:`center-center`,appearAt:o[i][0],disappearAt:o[i][1]}:{texture:h,atlasUV:Nv(e,t,n,r),aspect:Pv(n,r),baseScale:.35,anchor:`center-center`,appearAt:o[i][0],disappearAt:o[i][1]})'

        if old_map in code:
            code = code.replace(old_map, new_map)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Applied Stage 4 Harshit Yadav branding to', filepath)

if __name__ == '__main__':
    apply_stage4_harshit_yadav()
