with open('public/assets/main-B9-HtP-f.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos_h = code.find('function createEditorialTextTexture(')
print('pos createEditorialTextTexture:', pos_h)
if pos_h != -1:
    print(code[pos_h:pos_h+800])

pos_bx = code.find('function bx(e){')
print('pos bx:', pos_bx)
if pos_bx != -1:
    print(code[pos_bx:pos_bx+1500])
