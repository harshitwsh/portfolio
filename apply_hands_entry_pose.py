def apply_hands_entry_pose():
    files = ['public/assets/main-B9-HtP-f.js', 'main-B9-HtP-f.js']

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()

        # 1. In bx initial setup, scrub to 0.22 so hands are immediately in-frame on enter
        code = code.replace('i.scrub(0),i.update(0)', 'i.scrub(.22),i.update(0)')
        code = code.replace('i.scrub(.12),i.update(0)', 'i.scrub(.22),i.update(0)')

        # 2. In yx.scrub, map progress so hands start in-frame at 0.22 and animate to 0.70
        old_scrub1 = 'n.handsModel.scrub(hv(t,.01,1)*.7)'
        old_scrub2 = 'n.handsModel.scrub(.12+hv(t,0,1)*.58)'
        new_scrub = 'n.handsModel.scrub(.22+hv(t,0,1)*.48)'

        if old_scrub1 in code:
            code = code.replace(old_scrub1, new_scrub)
        if old_scrub2 in code:
            code = code.replace(old_scrub2, new_scrub)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(code)
        print('Updated hands entry pose in', filepath)

if __name__ == '__main__':
    apply_hands_entry_pose()
