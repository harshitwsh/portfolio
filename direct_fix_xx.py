with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# DIRECT FIX: 
# The first Xx enter function is corrupted after position ~922554
# The second Xx (at 1859224) is intact. 
# Strategy: find the garbage range in the first Xx and replace with the correct chunk from 2nd Xx

# Garbage starts right after the restored textLayout block closes:
# ";e._stage3QuatA..." is only in the 2nd copy
# The FIRST copy's garbage starts at ";.getOwnPropertyDescriptor"

# Find the first Xx's enter function end (before garbage) 
FIRST_XX_GARBAGE_START = ";.getOwnPropertyDescriptor,r=Object.getOwnPropertyNames"
# Find the NEXT gate/stage declaration after this garbage
# The garbage ends when we hit hS (gate from stage3 to stage4)
FIRST_XX_END_MARKER = ",hS={"  # the gate that follows Xx

p_garbage = js_code.find(FIRST_XX_GARBAGE_START, 918443, 930000)
p_next = js_code.find(FIRST_XX_END_MARKER, 918443, 1000000)

print("Garbage start:", p_garbage)
print("Next gate (hS) pos:", p_next)

# Get the CORRECT Xx enter/scrub/teardown/update tail from the 2nd copy
# In the 2nd copy, after textLayout, the stage3 QuatA starts the tail
# We need: e._stage3QuatA... (tail of enter) + scrub + update + teardown  
# But actually we just need the tail of the enter function + close of Xx object

# Find this from 2nd Xx  
p2_xx = 1859224
xx2_str = js_code[p2_xx:]
p2_quat = xx2_str.find("e._stage3QuatA=new Ct()")
p2_hs = xx2_str.find(",hS=")  # end of second Xx

CORRECT_TAIL = xx2_str[p2_quat : p2_hs + len(",hS={")]

print("Correct tail length:", len(CORRECT_TAIL))
print("Correct tail start:", CORRECT_TAIL[:200])
print("Correct tail end:", CORRECT_TAIL[-200:])
