with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

stage5_pos = code.rfind("id:`stage5`")
print("stage5 rfind:", stage5_pos)
print(code[stage5_pos : stage5_pos + 4000])
