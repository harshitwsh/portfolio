def restore_missing_stage_block():
    with open('test_slice.js', 'r', encoding='utf-8') as f:
        slice_code = f.read()

    pos_sb = slice_code.find('var Sb=`/`,Cb=[')
    pos_x_ = slice_code.find('function _x(e){')
    if pos_sb == -1 or pos_x_ == -1:
        print('Error: Could not find block in test_slice.js')
        return

    missing_block = slice_code[pos_sb : pos_x_]
    print(f'Extracted missing block of size: {len(missing_block)}')

    for path in ['public/assets/main-B9-HtP-f.js', 'main-B9-HtP-f.js']:
        with open(path, 'r', encoding='utf-8') as f:
            code = f.read()

        if 'function _x(e){' not in code:
            print(f'Error: function _x(e) not in {path}')
            continue

        if 'var Sb=`/`,Cb=[' in code:
            print(f'Block already present in {path}')
            continue

        target = 'function _x(e){'
        code = code.replace(target, missing_block + target)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f'Restored missing block to {path}')

if __name__ == '__main__':
    restore_missing_stage_block()
