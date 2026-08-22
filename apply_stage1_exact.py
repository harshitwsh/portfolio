def apply_stage1_exact():
    target_files = [
        'public/assets/main-B9-HtP-f.js',
        'main-B9-HtP-f.js'
    ]

    # Clean text texture helper using STK Bureau Serif with exact styling of "YOU BELIEVED."
    helper_code = '''function createEditorialTextTexture(e,t=""){let n=document.createElement("canvas");n.width=2048,n.height=800;let r=n.getContext("2d");r.clearRect(0,0,n.width,n.height),r.fillStyle="#ffffff",r.textAlign="center",r.textBaseline="middle",r.shadowColor="rgba(0,0,0,0.45)",r.shadowBlur=18;if(t){r.font='italic 400 90px "Bethany Elingston", "STK Bureau Serif", Georgia, serif',r.fillText(t,1024,300),r.font='700 170px "STK Bureau Serif", "Bethany Elingston", Georgia, serif',r.fillText(e,1024,490)}else{r.font='700 175px "STK Bureau Serif", "Bethany Elingston", Georgia, serif',r.fillText(e,1024,400)}let i=new dc(n);return i.colorSpace=W,i.generateMipmaps=!0,i.minFilter=v,i.magFilter=v,i.needsUpdate=!0,i};'''

    for filepath in target_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        # 1. Update createEditorialTextTexture helper
        if 'function createEditorialTextTexture(' in code:
            pos_h = code.find('function createEditorialTextTexture(')
            pos_h_end = code.find('function _x(e){', pos_h)
            if pos_h != -1 and pos_h_end != -1:
                code = code[:pos_h] + helper_code + code[pos_h_end:]

        # 2. Update Stage 1 setup (function bx) to completely remove coinRing and preserve hands & typography
        # Look for function bx(e)
        pos_bx = code.find('function bx(e){')
        pos_bx_end = code.find('var xx=1', pos_bx)
        if pos_bx != -1 and pos_bx_end != -1:
            bx_code = '''function bx(e){let{scene:t,assetLoader:n,textScene:r}=e,i=e.preWarmed?.handsModel||new Jv(n);t.add(i.group),i.group.visible=!0,i.group.position.set(0,0,0),i.group.rotation.set(0,0,0),i.group.scale.set(1,1,1),i.scrub(0),i.update(0),i.cameraRef&&(i.cameraRef.updateWorldMatrix(!0,!1),i.cameraRef.getWorldPosition(e._tempVec3),i.cameraRef.getWorldQuaternion(e._tempQuat),e.camera.position.copy(e._tempVec3),e.camera.quaternion.copy(e._tempQuat));let s=e.preWarmed?.petalParticles||null;if(!s){let e=n.getAsset(`spcAtlas`);e&&(s=new tb(e))}s&&(s.group.visible=!1,t.add(s.group));let c=e.preWarmed?.portalMaterial||xb(null,{direction:`in2out`,emberColor:[.651,1,.835],emberTip:[1,1,1],charColor:[.525,1,.706],seed:0,burnDelay:0,burnSpeed:1});e.preWarmed?.portalMaterial||(c.uniforms.uTexture.value=e.whiteTex),e.preWarmed&&(e.preWarmed.handsModel=null,e.preWarmed.coinRing=null,e.preWarmed.petalParticles=null,e.preWarmed.portalMaterial=null);let l=new Cr(new fc(.5,64),c);l.position.set(.5643,.947,.4),l.rotation.y=Math.PI/2,l.scale.set(1.5,1.5,1.5),t.add(l),e.fgPass&&(e.fgPass.uniforms.uGodRaysOpacity.value=0),e.bgPass&&(Yg(e.bgPass,`A`,`stage1Background1`,n,!0),Yg(e.bgPass,`B`,`stage1Background2`,n,!0),e.bgPass.uniforms.uProgress.value=0),_x(e);let u=null,d=n.getAsset(`textsAtlas`);d&&e.renderer&&(d.anisotropy=e.renderer.capabilities.getMaxAnisotropy(),d.needsUpdate=!0),(()=>{let t1=createEditorialTextTexture(`YOU HAVE AN IDEA.`),t2=createEditorialTextTexture(`NOW MAKE IT REAL.`);u=new vb(r,[{texture:t1,aspect:2.56,baseScale:.44,anchor:`center-center`,appearAt:.04,disappearAt:.44},{texture:t2,aspect:2.56,baseScale:.44,anchor:`center-center`,appearAt:.50,disappearAt:.94}]),u.resize(e._vw,e._vh)})(),e.components={handsModel:i,coinRing:null,petalParticles:s,portalMaterial:c,portalPlane:l,_bgPhase:1,textLayout:u}}'''
            code = code[:pos_bx] + bx_code + code[pos_bx_end:]

        # 3. In preWarmed setup: make sure coinRing is null
        code = code.replace('preWarmed={handsModel:t,handsModel2:null,coinRing:n,', 'preWarmed={handsModel:t,handsModel2:null,coinRing:null,')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Updated', filepath)

    # 4. Make sure CSS font-face supports all weights for STK Bureau Serif
    with open('public/assets/main-yeWZtezw.css', 'r', encoding='utf-8') as f:
        css = f.read()

    css = css.replace('@font-face{font-family:STK Bureau Serif;src:url(/assets/fonts/STKBureau-SerifBook.otf)format("opentype");font-weight:400;', '@font-face{font-family:STK Bureau Serif;src:url(/assets/fonts/STKBureau-SerifBook.otf)format("opentype");font-weight:100 900;')
    with open('public/assets/main-yeWZtezw.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print('Updated font-face in main-yeWZtezw.css')

if __name__ == '__main__':
    apply_stage1_exact()
