def apply_hands_visible_fix():
    files = [
        'public/assets/main-B9-HtP-f.js',
        'main-B9-HtP-f.js'
    ]

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        # 1. Update function bx to position hands group directly in front of camera
        old_bx_pos = 'i.group.position.set(0,0,0),i.group.rotation.set(0,0,0),i.group.scale.set(1,1,1)'
        new_bx_pos = 'i.group.position.set(0,-0.15,-1.6),i.group.rotation.set(0,0,0),i.group.scale.set(1.15,1.15,1.15)'
        if old_bx_pos in code:
            code = code.replace(old_bx_pos, new_bx_pos)

        # 2. In Stage 1 update, keep camera stable at [0,0,0] looking forward so hands at [0,-0.15,-1.6] are directly in view
        target_cam_update = 'i.handsModel.cameraRef&&(i.handsModel.cameraRef.getWorldPosition(e.camera.position),i.handsModel.cameraRef.getWorldQuaternion(e.camera.quaternion))'
        replace_cam_update = 'e.camera.position.set(0,0,0),e.camera.quaternion.set(0,0,0,1)'
        if target_cam_update in code:
            code = code.replace(target_cam_update, replace_cam_update)

        # 3. In bx initial camera setup
        target_bx_cam = 'i.cameraRef&&(i.cameraRef.updateWorldMatrix(!0,!1),i.cameraRef.getWorldPosition(e.camera.position),i.cameraRef.getWorldQuaternion(e.camera.quaternion))'
        replace_bx_cam = 'e.camera.position.set(0,0,0),e.camera.quaternion.set(0,0,0,1)'
        if target_bx_cam in code:
            code = code.replace(target_bx_cam, replace_bx_cam)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Updated hands positioning in', filepath)

if __name__ == '__main__':
    apply_hands_visible_fix()
