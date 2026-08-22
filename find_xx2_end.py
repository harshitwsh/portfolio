with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# The QuatA is only in the 2nd copy (1864656). The garbage text in the first copy 
# at 922554 stretches until what was originally the first copy's QuatA position
# 
# We need to remove the garbage block from 922554 to the start of the second Xx stage (1859224)
# Wait, no, that would delete massive amounts of code.
# 
# Let's think differently: the garbage in the first Xx copy starts at 922554
# and is the second half of the file's initialization code that was DUPLICATE-injected.
# 
# Looking at the structure:
# - First Xx at 918443 -> enter function -> textsAtlas block -> GARBAGE (922554 onwards)
# - Second Xx at 1859224 -> enter function -> textsAtlas block -> QuatA (1864656)
# 
# The garbage is code that belongs ELSEWHERE, injected here by previous edits.
# The original first Xx enter function should end with QuatA, scrub, teardown, etc.
# which are all in the second copy.
# 
# The safest fix: just close the enter function properly
# The first Xx's enter function ends at comma before scrub, so we need to close it.
# 
# Let's find the exact boundary: what comes after 922554 in the original?
# We need: e._stage3QuatA,e._stage3QuatB,camera setup,cameraRig,Xx.scrub(e,0)
# then close the enter function
# then have scrub(e,t){...}, update(e,t,n){...}, teardown(e){...} 
# 
# The second Xx has all of this. Let's find the full first Xx from 918443 to its next var declaration
# by finding what normally follows Xx={ in the second copy

pos2 = 1859224
xx2_str = js_code[pos2:]
# Find where Xx} ends in the second copy
import re
# Look for the end of the Xx object
# Actually after Xx, there's Zx={...} or similar
xx2_end_marker = "},Zx={"
xx2_end_pos = xx2_str.find(xx2_end_marker)
if xx2_end_pos == -1:
    xx2_end_marker = "},Zx="
    xx2_end_pos = xx2_str.find(xx2_end_marker)
print("Xx2 end marker pos:", xx2_end_pos)
print(xx2_str[xx2_end_pos - 50 : xx2_end_pos + 200])
