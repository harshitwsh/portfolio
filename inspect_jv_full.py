with open('public/assets/main-B9-HtP-f.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos = code.find('Jv=class extends Kv{')
print(code[pos:pos+3000])
