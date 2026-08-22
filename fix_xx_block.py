with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Replace the broken Xx block with the correct original content from the 2nd copy
OLD = """textsAtlas`);if(h){e.renderer&&(h.anisotropy=e.renderer.capabilities.getMaxAnisotropy());.getOwnPropertyDescriptor"""

# The CORRECT original content (from 2nd copy)
NEW = """textsAtlas`);if(h){e.renderer&&(h.anisotropy=e.renderer.capabilities.getMaxAnisotropy());let t=[{texture:h,atlasUV:Nv(0,371.64,365.21,186.82),aspect:Pv(365.21,186.82),baseScale:.25,anchor:`bottom-left`,appearAt:.05,disappearAt:.3},{texture:h,atlasUV:Nv(505.51,604.41,594.62,355.65),aspect:Pv(594.62,355.65),baseScale:.4,anchor:`center-center`,appearAt:.3,disappearAt:.4},{texture:h,atlasUV:Nv(363.64,371.64,337.74,186.82),aspect:Pv(337.74,186.82),baseScale:.25,anchor:`top-left`,appearAt:.4,disappearAt:.6},{texture:h,atlasUV:Nv(0,1023,482.83,168.84),aspect:Pv(482.83,168.84),baseScale:.25,anchor:`bottom-right`,appearAt:.5,disappearAt:.6},{texture:h,atlasUV:Nv(0,744.27,472.68,278.73),aspect:Pv(472.68,278.73),baseScale:.25,anchor:`center-center`,appearAt:.6,disappearAt:.7},{texture:h,atlasUV:Nv(775.24,0,521.92,325.68),aspect:Pv(521.92,325.68),baseScale:.38,anchor:`center-center`,appearAt:.7,disappearAt:.8},{texture:h,atlasUV:Nv(771,1542,667,221),aspect:Pv(667,221),baseScale:.38,anchor:`center-center`,appearAt:.8,disappearAt:.87},{texture:h,atlasUV:Nv(700.32,371.64,331.52,232.77),aspect:Pv(331.52,232.77),baseScale:.25,anchor:`top-left`,appearAt:.87,disappearAt:.99},{texture:h,atlasUV:Nv(1030.99,325.68,334.61,232.77),aspect:Pv(334.61,232.77),baseScale:.25,anchor:`bottom-right`,appearAt:.93,disappearAt:.99}],n=new vb(e.textScene,t);n.resize(e._vw,e._vh),e.components.textLayout=n}let g=Math.PI/180""" + """;.getOwnPropertyDescriptor"""

print("OLD found:", OLD in js_code)
count = js_code.count(OLD)
print("Count:", count)
