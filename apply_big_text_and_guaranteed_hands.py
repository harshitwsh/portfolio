def apply_big_text_and_guaranteed_hands():
    target_files = [
        'public/assets/main-B9-HtP-f.js',
        'main-B9-HtP-f.js'
    ]

    # 1. Big crystal shard text texture helper
    big_shard_helper = '''function createShardTextTexture(e,t){let n=document.createElement("canvas");n.width=2048,n.height=1024;let r=n.getContext("2d");r.clearRect(0,0,n.width,n.height),r.fillStyle="#ffffff",r.shadowColor="rgba(0,0,0,0.65)",r.shadowBlur=16,r.shadowOffsetY=4;let i=e.length<=8?210:160;r.font=`700 ${i}px "STK Bureau Serif", "Times New Roman", Georgia, serif`,r.textAlign="center",r.textBaseline="alphabetic",r.fillText(e,1024,460),r.font='400 72px "STK Bureau Serif", "Times New Roman", Georgia, serif',r.fillText(t,1024,620);let a=new dc(n);return a.colorSpace=W,a.generateMipmaps=!0,a.minFilter=v,a.magFilter=v,a.needsUpdate=!0,a};'''

    for filepath in target_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        # Update createShardTextTexture
        pos_st = code.find('function createShardTextTexture(')
        if pos_st != -1:
            pos_st_end = code.find('function createEditorialTextTexture(', pos_st)
            if pos_st_end != -1:
                code = code[:pos_st] + big_shard_helper + code[pos_st_end:]

        # Update Gb shard sizes to be 2.5x larger so they fill the crystal shards
        pos_gb = code.find('function Gb(e){')
        pos_gb_end = code.find('function Kb(e){', pos_gb)
        if pos_gb != -1 and pos_gb_end != -1:
            gb_code = '''function Gb(e){let t=-.8,n=[],r=[[.1,-.05,.15,.25,.2,-.4],[.05,.12,-.3,-.15,-.25,.5],[-.08,-.1,.45,.2,.15,-.6],[.12,.08,-.2,-.1,.3,.35],[-.05,-.15,.55,.18,-.2,-.45],[.15,.05,-.1,-.2,.1,.65],[-.1,.12,.35,.15,-.15,-.55]],i=[[.02,.4],[-.06,-.08],[.08,-.15],[-.04,-.05],[.05,.2],[-.08,-.4],[.05,-.18]],a=[{title:`1+ YEAR`,sub:`building real-world web experiences`,shard:1,size:.14,dx:-.02,spin:25},{title:`B.TECH CSE`,sub:`BML Munjal University`,shard:2,size:.18},{title:`FULL-STACK`,sub:`frontend • backend • databases • deployment`,shard:3,size:.17,dx:-.04},{title:`AI + WEB`,sub:`building with modern AI-assisted workflows`,shard:4,size:.19,spin:18},{title:`FROM IDEA TO LIVE`,sub:`designing, developing & deploying products`,shard:5,size:.15},{title:`CREATIVE ENGINEERING`,sub:`WebGL • 3D • UI/UX • interactive experiences`,shard:6,size:.22}],c=new Map(a.map(e=>[e.shard,e]));for(let e=0;e<7;e++){let a=-.66-e*.22,l=r[e],[u,d]=i[e],f=c.get(e+1),p=f?createShardTextTexture(f.title,f.sub):null;n.push({meshName:`Shard_0${e+1}`,startPosition:[u,a,t+d],endPosition:[u,a+2.64,t+d],startRotation:[l[0],l[1],l[2]],endRotation:[l[3],l[4],l[5]],scale:1.275,overlay:p&&f?{texture:p,height:f.size,offset:[(f.dx||0)*f.size*2,(f.dy||0)*f.size,.02],spin:(f.spin||0)*Math.PI/180}:void 0})}let l=.25,u=[[-.72,-.28,-1.8],[.64,-.2,-2],[-.95,-.28,-2.2],[.86,-.42,-1.9],[-.4,-.04,-2.45],[.36,-.62,-2.3],[-.6,-.56,-1.7],[.72,-.06,-2.55],[.06,-.12,-2.65]],d=[[.3,.4,.2],[-.25,.5,-.35],[.45,-.3,.6],[-.2,.35,.35],[.55,-.2,-.45],[-.4,.1,.65],[.35,-.5,-.55],[-.3,.45,.25],[.2,-.35,-.4]],f=[1.65,1.4,1.9,1.5,1.25,1.75,1.35,1.2,1.1];for(let e=0;e<u.length;e++){let t=String(e+1).padStart(2,`0`),[r,i,a]=u[e],o=d[e],s=1.584/2,c=e%2?1:-1;n.push({meshName:`BG_Shard_${t}`,background:!0,startPosition:[r,i-s,a],endPosition:[r,i+s,a],startRotation:o,endRotation:[o[0]+l*c,o[1]-l*.6,o[2]+l*c],scale:f[e]})}return new Ub(e,n,e.getAsset(`allShards`))}'''
            code = code[:pos_gb] + gb_code + code[pos_gb_end:]

        # Update Stage 1 hands model positioning and materials so they are directly in view in front of camera
        # In bx:
        pos_bx = code.find('function bx(e){')
        pos_bx_end = code.find('var xx=1', pos_bx)
        if pos_bx != -1 and pos_bx_end != -1:
            bx_code = '''function bx(e){let{scene:t,assetLoader:n,textScene:r}=e,i=e.preWarmed?.handsModel||new Jv(n);t.add(i.group),i.group.visible=!0,i.group.position.set(0,-0.1,-1.5),i.group.rotation.set(0,0,0),i.group.scale.set(1,1,1),i.scrub(.22),i.update(0),e.camera.position.set(0,0,0),e.camera.quaternion.set(0,0,0,1);let s=e.preWarmed?.petalParticles||null;if(!s){let e=n.getAsset(`spcAtlas`);e&&(s=new tb(e))}s&&(s.group.visible=!1,t.add(s.group));let c=e.preWarmed?.portalMaterial||xb(null,{direction:`in2out`,emberColor:[.651,1,.835],emberTip:[1,1,1],charColor:[.525,1,.706],seed:0,burnDelay:0,burnSpeed:1});e.preWarmed?.portalMaterial||(c.uniforms.uTexture.value=e.whiteTex),e.preWarmed&&(e.preWarmed.handsModel=null,e.preWarmed.coinRing=null,e.preWarmed.petalParticles=null,e.preWarmed.portalMaterial=null);let l=new Cr(new fc(.5,64),c);l.position.set(.5643,.947,.4),l.rotation.y=Math.PI/2,l.scale.set(1.5,1.5,1.5),t.add(l),e.fgPass&&(e.fgPass.uniforms.uGodRaysOpacity.value=0),e.bgPass&&(Yg(e.bgPass,`A`,`stage1Background1`,n,!0),Yg(e.bgPass,`B`,`stage1Background2`,n,!0),e.bgPass.uniforms.uProgress.value=0,e.bgPass.uniforms.uOpacity.value=1),_x(e);let u=null,d=n.getAsset(`textsAtlas`);d&&e.renderer&&(d.anisotropy=e.renderer.capabilities.getMaxAnisotropy(),d.needsUpdate=!0),(()=>{let t1=createEditorialTextTexture(`Have an Idea.`,`You`),t2=createEditorialTextTexture(`Make It Real.`,`Now`);u=new vb(r,[{texture:t1,aspect:2.0,baseScale:.52,anchor:`center-center`,appearAt:0,disappearAt:.48},{texture:t2,aspect:2.0,baseScale:.52,anchor:`center-center`,appearAt:.50,disappearAt:.94}]),u.resize(e._vw,e._vh)})(),e.components={handsModel:i,coinRing:null,petalParticles:s,portalMaterial:c,portalPlane:l,_bgPhase:1,textLayout:u}}'''
            code = code[:pos_bx] + bx_code + code[pos_bx_end:]

        # In yx.update, smoothly update hands animation while keeping them in viewport
        pos_yx = code.find('async enter(e){e.frostingPass&&')
        if pos_yx != -1:
            pos_yx_update = code.find('update(e,t,n){', pos_yx)
            if pos_yx_update != -1:
                pos_yx_update_end = code.find('let o=i.portalMaterial;', pos_yx_update)
                if pos_yx_update_end != -1:
                    new_yx_update = '''update(e,t,n){let r=e.components;if(!r)return;let i=r;i.handsModel&&i.handsModel.update(n);'''
                    code = code[:pos_yx_update] + new_yx_update + code[pos_yx_update_end:]

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Applied big text and guaranteed hands to', filepath)

if __name__ == '__main__':
    apply_big_text_and_guaranteed_hands()
