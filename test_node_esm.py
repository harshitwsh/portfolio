import subprocess

script = """
import fs from 'fs';
const code = fs.readFileSync('public/assets/main-B9-HtP-f.js', 'utf8');
try {
  new Function(code);
  console.log("SYNTAX VALID!");
} catch (e) {
  console.log("ERROR:", e.message);
  console.log(e.stack);
}
"""
with open("test_node.mjs", "w", encoding="utf-8") as f:
    f.write(script)

res = subprocess.run(["node", "test_node.mjs"], capture_output=True, text=True)
print(res.stdout)
print(res.stderr)
