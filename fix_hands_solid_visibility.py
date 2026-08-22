def fix_hands_solid_visibility():
    files = ['public/assets/main-B9-HtP-f.js', 'main-B9-HtP-f.js']

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        # 1. In Iv shader, guarantee solid alphaMask = 1.0
        target_mask = 'float alphaMask = texture2D(uAlphaMap, vUv * uAlphaScale + uAlphaOffset).r;'
        replace_mask = 'float alphaMask = 1.0;'
        if target_mask in code:
            code = code.replace(target_mask, replace_mask)

        # 2. In _setupEthHand, make fancy hand solid matcap material
        old_eth_mat = 'let l=new _c({matcap:i||null,alphaMap:o||null,normalMap:s||null,transparent:!0,depthWrite:!0,depthTest:!0,side:0,toneMapped:!1});'
        new_eth_mat = 'let l=new _c({matcap:i||null,normalMap:s||null,transparent:!1,depthWrite:!0,depthTest:!0,side:2,toneMapped:!1});'
        if old_eth_mat in code:
            code = code.replace(old_eth_mat, new_eth_mat)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Fixed hands solid rendering in', filepath)

if __name__ == '__main__':
    fix_hands_solid_visibility()
