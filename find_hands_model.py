with open('public/assets/main-B9-HtP-f.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re
matches = list(re.finditer(r'handsModel', code))
print('Total matches for handsModel in main-B9-HtP-f.js:', len(matches))
for m in matches[:10]:
    print('--- at', m.start())
    print(code[max(0, m.start()-100):min(len(code), m.end()+250)])
