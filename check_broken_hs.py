with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# The issue is in the join: "hS={=e.components" 
# This happened because CORRECT_TAIL ended with ",hS={" but 
# and AFTER starts from p2_xx which INCLUDES another Xx= declaration
# So there's duplication. Let's find and fix the join

broken_hs = "hS={=e.components"
pos = js_code.find(broken_hs)
print("Broken hS join pos:", pos)
if pos != -1:
    print("Context before:", js_code[pos - 100 : pos + 200])

# Also check general code around 940000 
print("\nCode around 940000:")
print(js_code[939900 : 940200])
