def apply_hands_integration():
    files = [
        'public/assets/main-B9-HtP-f.js',
        'main-B9-HtP-f.js'
    ]

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        # 1. Update yx.update camera sync
        target_cam = 'i.handsModel.cameraRef&&(i.handsModel.cameraRef.getWorldPosition(e._tempVec3),i.handsModel.cameraRef.getWorldQuaternion(e._tempQuat),e.camera.position.lerp(e._tempVec3,Pg.CAMERA_LERP),e.camera.quaternion.slerp(e._tempQuat,Pg.CAMERA_LERP))'
        replace_cam = 'i.handsModel.cameraRef&&(i.handsModel.cameraRef.getWorldPosition(e.camera.position),i.handsModel.cameraRef.getWorldQuaternion(e.camera.quaternion))'
        if target_cam in code:
            code = code.replace(target_cam, replace_cam)

        # 2. Update initial camera alignment in bx
        target_bx_cam = 'i.cameraRef&&(i.cameraRef.updateWorldMatrix(!0,!1),i.cameraRef.getWorldPosition(e._tempVec3),i.cameraRef.getWorldQuaternion(e._tempQuat),e.camera.position.copy(e._tempVec3),e.camera.quaternion.copy(e._tempQuat))'
        replace_bx_cam = 'i.cameraRef&&(i.cameraRef.updateWorldMatrix(!0,!1),i.cameraRef.getWorldPosition(e.camera.position),i.cameraRef.getWorldQuaternion(e.camera.quaternion))'
        if target_bx_cam in code:
            code = code.replace(target_bx_cam, replace_bx_cam)

        # 3. Ensure hands stay visible in Kv constructor
        code = code.replace('this.group.visible=!1,this._mixers=[]', 'this.group.visible=!0,this._mixers=[]')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Integrated hands directly in', filepath)

if __name__ == '__main__':
    apply_hands_integration()
