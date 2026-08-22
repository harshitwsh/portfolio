def apply_crystal_panels():
    target_files = [
        'public/assets/main-B9-HtP-f.js',
        'main-B9-HtP-f.js'
    ]

    for filepath in target_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        # 1. Add createShardTextTexture helper
        shard_helper = '''function createShardTextTexture(e,t){let n=document.createElement("canvas");n.width=1024,n.height=512;let r=n.getContext("2d");r.clearRect(0,0,n.width,n.height),r.fillStyle="#ffffff",r.shadowColor="rgba(0,0,0,0.55)",r.shadowBlur=12,r.shadowOffsetY=3,r.font='700 88px "STK Bureau Serif", "Times New Roman", Georgia, serif',r.textAlign="center",r.textBaseline="alphabetic",r.fillText(e,512,225),r.font='400 36px "STK Bureau Serif", "Times New Roman", Georgia, serif',r.fillText(t,512,305);let i=new dc(n);return i.colorSpace=W,i.generateMipmaps=!0,i.minFilter=v,i.magFilter=v,i.needsUpdate=!0,i};'''

        pos_h = code.find('function createEditorialTextTexture(')
        if pos_h != -1:
            code = code[:pos_h] + shard_helper + code[pos_h:]

        # 2. Update Ub overlay material creation to support per-overlay canvas texture
        target_ub_mat = 'this._overlayMaterial||=(e.texture.premultiplyAlpha=!1,new Gn({map:e.texture,transparent:!0,depthWrite:!1,depthTest:!1,side:2,toneMapped:!1}));let d=this._overlayMaterial,f=new Cr(u,d)'
        replace_ub_mat = 'let d=new Gn({map:e.texture,transparent:!0,depthWrite:!1,depthTest:!1,side:2,toneMapped:!1}),f=new Cr(u,d)'
        if target_ub_mat in code:
            code = code.replace(target_ub_mat, replace_ub_mat)

        # 3. Update Gb function with the 6 exact portfolio statements
        pos_gb = code.find('function Gb(e){')
        pos_gb_end = code.find('function Kb(e){', pos_gb)
        if pos_gb != -1 and pos_gb_end != -1:
            gb_code = '''function Gb(e){let t=-.8,n=[],r=[[.1,-.05,.15,.25,.2,-.4],[.05,.12,-.3,-.15,-.25,.5],[-.08,-.1,.45,.2,.15,-.6],[.12,.08,-.2,-.1,.3,.35],[-.05,-.15,.55,.18,-.2,-.45],[.15,.05,-.1,-.2,.1,.65],[-.1,.12,.35,.15,-.15,-.55]],i=[[.02,.4],[-.06,-.08],[.08,-.15],[-.04,-.05],[.05,.2],[-.08,-.4],[.05,-.18]],a=[{title:`1+ YEAR`,sub:`building real-world web experiences`,shard:1,size:.055,dx:-.03,spin:25},{title:`B.TECH CSE`,sub:`BML Munjal University`,shard:2,size:.072},{title:`FULL-STACK`,sub:`frontend • backend • databases • deployment`,shard:3,size:.068,dx:-.05},{title:`AI + WEB`,sub:`building with modern AI-assisted workflows`,shard:4,size:.078,spin:18},{title:`FROM IDEA TO LIVE`,sub:`designing, developing & deploying products`,shard:5,size:.058},{title:`CREATIVE ENGINEERING`,sub:`WebGL • 3D • UI/UX • interactive experiences`,shard:6,size:.092}],c=new Map(a.map(e=>[e.shard,e]));for(let e=0;e<7;e++){let a=-.66-e*.22,l=r[e],[u,d]=i[e],f=c.get(e+1),p=f?createShardTextTexture(f.title,f.sub):null;n.push({meshName:`Shard_0${e+1}`,startPosition:[u,a,t+d],endPosition:[u,a+2.64,t+d],startRotation:[l[0],l[1],l[2]],endRotation:[l[3],l[4],l[5]],scale:1.275,overlay:p&&f?{texture:p,height:f.size,offset:[(f.dx||0)*f.size*2,(f.dy||0)*f.size,.02],spin:(f.spin||0)*Math.PI/180}:void 0})}let l=.25,u=[[-.72,-.28,-1.8],[.64,-.2,-2],[-.95,-.28,-2.2],[.86,-.42,-1.9],[-.4,-.04,-2.45],[.36,-.62,-2.3],[-.6,-.56,-1.7],[.72,-.06,-2.55],[.06,-.12,-2.65]],d=[[.3,.4,.2],[-.25,.5,-.35],[.45,-.3,.6],[-.2,.35,.35],[.55,-.2,-.45],[-.4,.1,.65],[.35,-.5,-.55],[-.3,.45,.25],[.2,-.35,-.4]],f=[1.65,1.4,1.9,1.5,1.25,1.75,1.35,1.2,1.1];for(let e=0;e<u.length;e++){let t=String(e+1).padStart(2,`0`),[r,i,a]=u[e],o=d[e],s=1.584/2,c=e%2?1:-1;n.push({meshName:`BG_Shard_${t}`,background:!0,startPosition:[r,i-s,a],endPosition:[r,i+s,a],startRotation:o,endRotation:[o[0]+l*c,o[1]-l*.6,o[2]+l*c],scale:f[e]})}return new Ub(e,n,e.getAsset(`allShards`))}'''
            code = code[:pos_gb] + gb_code + code[pos_gb_end:]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Applied crystal panels text to', filepath)

if __name__ == '__main__':
    apply_crystal_panels()
