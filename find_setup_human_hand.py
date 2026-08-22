with open('public/assets/main-B9-HtP-f.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('_setupHumanHand(e,t){')
if pos == -1:
    pos = code.find('_setupHumanHand(')
    pos = code.find('_setupHumanHand(', pos + 20)
print('pos:', pos)
print(code[pos:pos+2500])
