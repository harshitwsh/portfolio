with open('test_slice.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re
matches = list(re.finditer(r'id:\s*[`\'"]stage1[`\'"]', code))
print('Matches for stage1 in test_slice.js:', len(matches))
for m in matches:
    print('Match at', m.start())
    print(code[max(0, m.start()-100):min(len(code), m.end()+2500)])
