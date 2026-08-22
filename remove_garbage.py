with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Remove the garbage text between positions 922554 and the next sensible code
# The garbage is: ";.getOwnPropertyDescriptor,...[thousands of lines]...e._stage3QuatA=..."
# We need to replace everything from position 922554 to e._stage3QuatA= with just "e._stage3QuatA..."

GARBAGE_START = ";.getOwnPropertyDescriptor,r=Object.getOwnPropertyNames,i=Object.getPrototypeOf,a=Object.prototype.hasOwnProperty"
GARBAGE_END_MARKER = "e._stage3QuatA=new Ct().setFromEuler(new un(Jx.x"

start_pos = js_code.find(GARBAGE_START, 920000, 930000)
end_pos = js_code.find(GARBAGE_END_MARKER, 922000, 1000000)

print("Garbage start:", start_pos)
print("Garbage end:", end_pos)
print("Garbage length:", end_pos - start_pos)

if start_pos != -1 and end_pos != -1 and end_pos > start_pos:
    # Remove the garbage and replace with correct continuation
    # The semicolon at start_pos (the ";") is actually the end of "let g=Math.PI/180;"
    # so we keep the semicolon and just replace what comes after
    fixed_code = js_code[:start_pos + 1] + js_code[end_pos:]
    print("After fix, context:")
    print(fixed_code[start_pos - 100 : start_pos + 400])
    
    with open("public/assets/main-B9-HtP-f.js", "w", encoding="utf-8") as f:
        f.write(fixed_code)
    with open("main-B9-HtP-f.js", "w", encoding="utf-8") as f:
        f.write(fixed_code)
    print("Fixed! Garbage removed.")
