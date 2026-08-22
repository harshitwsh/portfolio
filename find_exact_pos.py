with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    js_code = f.read()

import subprocess

script = """
import fs from 'fs';
const code = fs.readFileSync('test_slice.js', 'utf8');
try {
  new Function(code);
  process.exit(0);
} catch (e) {
  process.exit(1);
}
"""
with open("test_slice.mjs", "w", encoding="utf-8") as f:
    f.write(script)

# Binary search on js_code length
def check_prefix(n):
    with open("test_slice.js", "w", encoding="utf-8") as f:
        f.write(js_code[:n] + "\n};")
    res = subprocess.run(["node", "test_slice.mjs"])
    return res.returncode == 0

# Check around pos 920000
for pos in range(915000, 945000, 2000):
    with open("test_slice.js", "w", encoding="utf-8") as f:
        f.write(js_code[:pos] + "\n};")
    res = subprocess.run(["node", "test_slice.mjs"], capture_output=True)
    # also test with node --check
    r2 = subprocess.run(["node", "--check", "test_slice.js"], capture_output=True, text=True)
    err = r2.stderr.split('\n')[0] if r2.stderr else "OK"
    print(f"Pos {pos}: {err}")
