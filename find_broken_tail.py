with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Fix: after the restored ORIGINAL_BLOCK, the code now has:
# ...e.components.textLayout=n}let g=Math.PI/180;.getOwnPropertyDescriptor,...
# Need to remove the ".getOwnPropertyDescriptor..." part up to the next sensible code
# The ".getOwnPropertyDescriptor,r=Object.getOwnPropertyNames,..." sequence was from our earlier corrupt injection

# Let's look for the exact broken transition and what comes after
BROKEN_TAIL = ";.getOwnPropertyDescriptor,r=Object.getOwnPropertyNames,i=Object.getPrototypeOf,a=Object.prototype.hasOwnProperty"
pos = js_code.find(BROKEN_TAIL, 920000, 925000)
print("Broken tail pos:", pos)

if pos != -1:
    # What comes after the broken tail?
    print("Context around broken tail:")
    print(js_code[pos-50 : pos+400])
