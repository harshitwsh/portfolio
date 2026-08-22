def apply_stage1_polish():
    for filepath in ['public/assets/main-B9-HtP-f.js', 'main-B9-HtP-f.js']:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        # In yx.enter (Stage 1 enter), clear whiteout and set initial hand progress
        target_enter = 'async enter(e){if(e.onStage1Entered&&e.onStage1Entered()'
        replacement_enter = 'async enter(e){e.frostingPass&&(e.frostingPass.material.uniforms.uWhiteout.value=0,e.frostingPass.stopSpread&&e.frostingPass.stopSpread(),e.frostingPass.active=!1);if(e.onStage1Entered&&e.onStage1Entered()'
        if target_enter in code:
            code = code.replace(target_enter, replacement_enter)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Polished Stage 1 enter in', filepath)

if __name__ == '__main__':
    apply_stage1_polish()
