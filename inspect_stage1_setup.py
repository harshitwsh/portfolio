with open('test_slice.js', 'r', encoding='utf-8') as f:
    code = f.read()

pos = 915565
print('Code before stage 1 setup in test_slice.js:')
print(code[pos-2500:pos])
