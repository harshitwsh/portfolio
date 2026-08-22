import re

def fix_all_city_blur():
    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        # 1. Fix LensBlurPass render() to strictly respect _forcedOff
        old_lens_render = 'render(e,t,n){let r=this._compositeMat.uniforms,i=r.uEnabled.value>=.5&&r.uMaxBlur.value>=.01;if(this.needsSwap=i,!i)return;'
        new_lens_render = 'render(e,t,n){if(this._forcedOff){this.needsSwap=!1;return}let r=this._compositeMat.uniforms,i=r.uEnabled.value>=.5&&r.uMaxBlur.value>=.01;if(this.needsSwap=i,!i)return;'
        if old_lens_render in code:
            code = code.replace(old_lens_render, new_lens_render)
            print("Fixed LensBlurPass render in", filepath)
        else:
            print("LensBlurPass render pattern not found directly, checking regex...")
            code = re.sub(
                r'render\(e,t,n\)\{let r=this\._compositeMat\.uniforms,i=r\.uEnabled\.value>=?\.5&&r\.uMaxBlur\.value>=?\.01;if\(this\.needsSwap=i,!i\)return;',
                'render(e,t,n){if(this._forcedOff){this.needsSwap=!1;return}let r=this._compositeMat.uniforms,i=r.uEnabled.value>=.5&&r.uMaxBlur.value>=.01;if(this.needsSwap=i,!i)return;',
                code,
                count=1
            )

        # 2. Fix stage5 enter & update to completely ensure lensBlurPass is off and stays off
        # Remove backdrop-filter blur from resume-backdrop and map-panel-backdrop
        code = re.sub(
            r'\.resume-backdrop\s*\{([^}]*?)backdrop-filter:\s*blur\([^)]*\);\s*-webkit-backdrop-filter:\s*blur\([^)]*\);',
            r'.resume-backdrop {\1',
            code
        )
        code = re.sub(
            r'\.map-panel-backdrop\s*\{([^}]*?)backdrop-filter:\s*blur\([^)]*\);\s*-webkit-backdrop-filter:\s*blur\([^)]*\);',
            r'.map-panel-backdrop {\1',
            code
        )

        # 3. Make the ringHit mesh purely transparent (no milky white overlay)
        # Find: let p=new Cr(new fc(d,64),new Gn({color:16777215,transparent:!0,opacity:.1,depthWrite:!1}));
        code = re.sub(
            r'let p=new Cr\(new fc\(d,64\),new Gn\(\{color:16777215,transparent:!0,opacity:\.1,depthWrite:!1\}\)\);',
            r'let p=new Cr(new fc(d,64),new Gn({color:16777215,transparent:!0,opacity:0,depthWrite:!1}));',
            code
        )

        # 4. In stage5 update loop, keep lensBlurPass forced off
        code = re.sub(
            r'e\.lensBlurPass&&\((e\._stage5LensBlurWasEnabled=[^;]+;)?e\.lensBlurPass\.uniforms\.uEnabled\.value=0,e\.lensBlurPass\._forcedOff=!0\);',
            r'e.lensBlurPass&&(e.lensBlurPass._forcedOff=!0,e.lensBlurPass.uniforms.uEnabled.value=0,e.lensBlurPass.uniforms.uMaxBlur.value=0);',
            code
        )

        # 5. In stage4 teardown, don't re-enable lensBlur if transitioning to stage5
        code = re.sub(
            r'e\.lensBlurPass\)\{let t=y_\.preset;e\.lensBlurPass\.uniforms\.uEnabled\.value=t\.lensBlur\.enabled,e\.lensBlurPass\.uniforms\.uMaxBlur\.value=t\.lensBlur\.maxBlur\}',
            r'e.lensBlurPass&&!e._stage5LensBlurWasEnabled&&!e.lensBlurPass._forcedOff){let t=y_.preset;e.lensBlurPass.uniforms.uEnabled.value=t.lensBlur.enabled,e.lensBlurPass.uniforms.uMaxBlur.value=t.lensBlur.maxBlur}',
            code
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(code)
        print("Updated file:", filepath)

fix_all_city_blur()
