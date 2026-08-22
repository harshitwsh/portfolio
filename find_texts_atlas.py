with open('test_slice.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re
pos = code.find('textsAtlas')
print('textsAtlas in test_slice.js pos:', pos)
for m in re.finditer(r'textsAtlas', code):
    print(code[max(0, m.start()-100):min(len(code), m.end()+300)])
    print('---')
