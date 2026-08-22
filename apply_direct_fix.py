with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

FIRST_XX_GARBAGE_START = ";.getOwnPropertyDescriptor,r=Object.getOwnPropertyNames"

p2_xx = 1859224
xx2_str = js_code[p2_xx:]
p2_quat = xx2_str.find("e._stage3QuatA=new Ct()")
p2_hs = xx2_str.find(",hS=")
CORRECT_TAIL = xx2_str[p2_quat : p2_hs + len(",hS={")]

p_garbage = js_code.find(FIRST_XX_GARBAGE_START, 918443, 930000)

# Find where the 2nd Xx starts (so we don't include too much)
# The garbage goes from p_garbage to p2_xx (second Xx starts)
# Replace from p_garbage+1 (keep the ";") to p2_xx with CORRECT_TAIL + "hS={"
# Then continue from p2_xx

BEFORE = js_code[:p_garbage + 1]  # keep the ";"
AFTER = js_code[p2_xx:]  # everything from 2nd Xx onwards 

fixed_code = BEFORE + CORRECT_TAIL + AFTER

print("Fixed code length:", len(fixed_code))
print("Context at join:")
idx = len(BEFORE) + len(CORRECT_TAIL) - 50
print(fixed_code[idx : idx + 200])

with open("public/assets/main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(fixed_code)
with open("main-B9-HtP-f.js", "w", encoding="utf-8") as f:
    f.write(fixed_code)

print("DONE - Garbage replaced with correct Xx tail")
