with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

import subprocess

def test_lines(start, end):
    with open("test_sub.js", "w", encoding="utf-8") as f:
        f.writelines(lines[start:end])
    res = subprocess.run(["node", "--check", "test_sub.js"], capture_output=True, text=True)
    return res.returncode == 0, res.stderr

print("Testing lines 5178 to 5182:")
ok, err = test_lines(5178, 5182)
print("Result:", ok, err)
