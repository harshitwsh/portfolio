def apply_master_polish():
    target_files = [
        'public/assets/main-B9-HtP-f.js',
        'main-B9-HtP-f.js'
    ]

    helper_code = '''function createEditorialTextTexture(e="Have an Idea.",t="You"){let n=document.createElement("canvas");n.width=2400,n.height=1200;let r=n.getContext("2d");r.clearRect(0,0,n.width,n.height);let i=r.createLinearGradient(0,300,0,850);i.addColorStop(0,"#6c9b8e"),i.addColorStop(.25,"#527e72"),i.addColorStop(.65,"#385b51"),i.addColorStop(1,"#233e36"),r.fillStyle=i,r.shadowColor="rgba(18,42,35,0.32)",r.shadowBlur=18,r.shadowOffsetY=5,r.font='400 110px "STK Bureau Serif", "Times New Roman", Georgia, serif';let a=r.measureText(t).width;r.font='italic 400 240px "STK Bureau Serif", "Times New Roman", Georgia, serif';let o=r.measureText("H").width;r.font='400 210px "STK Bureau Serif", "Times New Roman", Georgia, serif';let s=r.measureText("ave an Idea.").width,c=o+s,l=(n.width-c)/2,u=720;r.font='400 105px "STK Bureau Serif", "Times New Roman", Georgia, serif',r.textAlign="left",r.textBaseline="alphabetic",r.fillText(t,l+o+15,u-160),r.font='italic 400 240px "STK Bureau Serif", "Times New Roman", Georgia, serif',r.fillText("H",l,u),r.font='400 210px "STK Bureau Serif", "Times New Roman", Georgia, serif',r.fillText("ave an Idea.",l+o-10,u);let d=new dc(n);return d.colorSpace=W,d.generateMipmaps=!0,d.minFilter=v,d.magFilter=v,d.needsUpdate=!0,d};'''

    for filepath in target_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        # 1. Update createEditorialTextTexture
        pos_h = code.find('function createEditorialTextTexture(')
        if pos_h != -1:
            pos_h_end = code.find(';var Sb=`/`', pos_h)
            if pos_h_end != -1:
                code = code[:pos_h] + helper_code + code[pos_h_end+1:]

        # 2. Update function bx
        pos_bx = code.find('function bx(e){')
        pos_bx_end = code.find('var xx=1', pos_bx)
        if pos_bx != -1 and pos_bx_end != -1:
            bx_code = '''function bx(e){let{scene:t,assetLoader:n,textScene:r}=e,i=e.preWarmed?.handsModel||new Jv(n);t.add(i.group),i.group.visible=!0,i.group.position.set(0,0,0),i.group.rotation.set(0,0,0),i.group.scale.set(1,1,1),i.scrub(.12),i.update(0),i.cameraRef&&(i.cameraRef.updateWorldMatrix(!0,!1),i.cameraRef.getWorldPosition(e._tempVec3),i.cameraRef.getWorldQuaternion(e._tempQuat),e.camera.position.copy(e._tempVec3),e.camera.quaternion.copy(e._tempQuat));let s=e.preWarmed?.petalParticles||null;if(!s){let e=n.getAsset(`spcAtlas`);e&&(s=new tb(e))}s&&(s.group.visible=!1,t.add(s.group));let c=e.preWarmed?.portalMaterial||xb(null,{direction:`in2out`,emberColor:[.651,1,.835],emberTip:[1,1,1],charColor:[.525,1,.706],seed:0,burnDelay:0,burnSpeed:1});e.preWarmed?.portalMaterial||(c.uniforms.uTexture.value=e.whiteTex),e.preWarmed&&(e.preWarmed.handsModel=null,e.preWarmed.coinRing=null,e.preWarmed.petalParticles=null,e.preWarmed.portalMaterial=null);let l=new Cr(new fc(.5,64),c);l.position.set(.5643,.947,.4),l.rotation.y=Math.PI/2,l.scale.set(1.5,1.5,1.5),t.add(l),e.fgPass&&(e.fgPass.uniforms.uGodRaysOpacity.value=0),e.bgPass&&(Yg(e.bgPass,`A`,`stage1Background1`,n,!0),Yg(e.bgPass,`B`,`stage1Background2`,n,!0),e.bgPass.uniforms.uProgress.value=0,e.bgPass.uniforms.uOpacity.value=1),_x(e);let u=null,d=n.getAsset(`textsAtlas`);d&&e.renderer&&(d.anisotropy=e.renderer.capabilities.getMaxAnisotropy(),d.needsUpdate=!0),(()=>{let t1=createEditorialTextTexture(`Have an Idea.`,`You`),t2=createEditorialTextTexture(`Make It Real.`,`Now`);u=new vb(r,[{texture:t1,aspect:2.0,baseScale:.50,anchor:`center-center`,appearAt:0,disappearAt:.48},{texture:t2,aspect:2.0,baseScale:.50,anchor:`center-center`,appearAt:.50,disappearAt:.94}]),u.resize(e._vw,e._vh)})(),e.components={handsModel:i,coinRing:null,petalParticles:s,portalMaterial:c,portalPlane:l,_bgPhase:1,textLayout:u}}'''
            code = code[:pos_bx] + bx_code + code[pos_bx_end:]

        # 3. Update yx.scrub for smooth hands progression starting at .12
        pos_scrub = code.find('n.handsModel.scrub(hv(t,.01,1)*.7)')
        if pos_scrub != -1:
            code = code.replace('n.handsModel.scrub(hv(t,.01,1)*.7)', 'n.handsModel.scrub(.12+hv(t,0,1)*.58)')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Applied master polish to', filepath)

if __name__ == '__main__':
    apply_master_polish()
