with open('test_slice.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re
pos = code.find('function Cv(')
print('function Cv in test_slice.js pos:', pos)
if pos != -1:
    print(code[pos:pos+3500])
