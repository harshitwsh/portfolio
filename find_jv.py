with open('public/assets/main-B9-HtP-f.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re
matches = list(re.finditer(r'class\s+Jv\b|Jv\s*=\s*class\b', code))
print('Matches for Jv:', len(matches))
for m in matches:
    print('Match at', m.start())
    print(code[m.start():m.start()+2500])
