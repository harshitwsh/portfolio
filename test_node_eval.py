import subprocess

with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

# Let's use node with a small script to find exact syntax error offset
script = """
const fs = require('fs');
const code = fs.readFileSync('public/assets/main-B9-HtP-f.js', 'utf8');
try {
  new Function(code);
  console.log("SYNTAX VALID!");
} catch (e) {
  console.log("ERROR:", e.message);
  console.log(e.stack);
}
"""
with open("test_node.js", "w", encoding="utf-8") as f:
    f.write(script)

res = subprocess.run(["node", "test_node.js"], capture_output=True, text=True)
print(res.stdout)
print(res.stderr)
