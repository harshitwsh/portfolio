with open('public/assets/main-B9-HtP-f.js', 'r', encoding='utf-8') as f:
    code = f.read()

import re
print('=== new Jv calls ===')
for m in re.finditer(r'new\s+Jv\b', code):
    print(code[max(0, m.start()-100):min(len(code), m.end()+250)])
    print('---')

print('=== Ey / coinRing calls ===')
for m in re.finditer(r'coinRing', code):
    print(code[max(0, m.start()-100):min(len(code), m.end()+250)])
    print('---')
