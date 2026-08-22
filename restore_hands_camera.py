def restore_hands():
    files = ['public/assets/main-B9-HtP-f.js', 'main-B9-HtP-f.js']

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        # 1. Reset hands group positioning in bx
        code = code.replace('i.group.position.set(0,-0.15,-1.6),i.group.rotation.set(0,0,0),i.group.scale.set(1.15,1.15,1.15)', 'i.group.position.set(0,0,0),i.group.rotation.set(0,0,0),i.group.scale.set(1,1,1)')

        # 2. Reset initial camera sync in bx
        code = code.replace('i.update(0),e.camera.position.set(0,0,0),e.camera.quaternion.set(0,0,0,1);', 'i.update(0),i.cameraRef&&(i.cameraRef.updateWorldMatrix(!0,!1),i.cameraRef.getWorldPosition(e._tempVec3),i.cameraRef.getWorldQuaternion(e._tempQuat),e.camera.position.copy(e._tempVec3),e.camera.quaternion.copy(e._tempQuat));')

        # 3. Reset continuous camera lerp in yx.update
        code = code.replace('e.camera.position.set(0,0,0),e.camera.quaternion.set(0,0,0,1)', 'i.handsModel.cameraRef&&(i.handsModel.cameraRef.getWorldPosition(e._tempVec3),i.handsModel.cameraRef.getWorldQuaternion(e._tempQuat),e.camera.position.lerp(e._tempVec3,0.08),e.camera.quaternion.slerp(e._tempQuat,0.08))')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Restored original hands camera rig in', filepath)

if __name__ == '__main__':
    restore_hands()
