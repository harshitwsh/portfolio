with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# The code still has "};let g=Math.PI/180;.getOwnPropertyDescriptor" which is broken
# We need to close the if block with } before the semicolon and then the code continues
# Actually looking at the 2nd copy output:
# },e.components.textLayout=n}let g=Math.PI/180; ... e._stage3QuatA...
# Wait the 2nd copy was: n.resize(e._vw,e._vh),e.components.textLayout=n}let g=Math.PI/180
# So after the closing }, the "let g=Math.PI/180" is the NEXT line of code in the enter function
# That means the ".getOwnPropertyDescriptor" part is NOT the next line

# So ".getOwnPropertyDescriptor" is at position 921235 + ORIGINAL_BLOCK 
# and should NOT be there — it's the start of some code that was misplaced by previous edits
# Let me check what correctly follows the if block in the 2nd Xx copy:

pos_2 = 1859224
js_xx2 = js_code[pos_2:]
ta_pos = js_xx2.find("textsAtlas`);")
block_end = js_xx2.find("e.components.textLayout=n}", ta_pos)
print("Block end in 2nd copy:", block_end)
print(js_xx2[block_end : block_end + 200])
