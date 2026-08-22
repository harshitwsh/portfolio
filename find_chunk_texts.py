with open('test_chunk.js', 'r', encoding='utf-8') as f:
    chunk = f.read()

import re
matches = list(re.finditer(r'textsAtlas', chunk))
for m in matches:
    print('Match at', m.start())
    print(chunk[max(0, m.start()-100):min(len(chunk), m.end()+400)])
    print('---')
