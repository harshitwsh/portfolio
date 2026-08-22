with open('public/assets/main-B9-HtP-f.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('function bx(e){')
pos_end = code.find('var xx=1', pos)
print('=== function bx in main-B9-HtP-f.js ===')
print(code[pos:pos_end])

pos_s1 = code.find('var yx={id:`stage1`')
pos_s1_end = code.find('var xx=', pos_s1)
if pos_s1_end == -1:
    pos_s1_end = pos_s1 + 2500
print('=== Stage 1 object in main-B9-HtP-f.js ===')
print(code[pos_s1:pos_s1_end])
