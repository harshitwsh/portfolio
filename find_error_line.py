with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    lines = f.readlines()

import subprocess

# Binary search the lines to locate the exact error line
low = 0
high = len(lines)

# Write a chunk to test_syntax.js
def test_chunk(n):
    with open("test_chunk.js", "w", encoding="utf-8") as f:
        f.writelines(lines[:n])
    res = subprocess.run(["node", "--check", "test_chunk.js"], capture_output=True, text=True)
    return res.returncode == 0, res.stderr

print("Total lines:", len(lines))
# Let's test lines around 5050 to 5200
for test_line in [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, len(lines)]:
    ok, err = test_chunk(test_line)
    first_err = err.split('\n')[0] if err else "OK"
    print(f"Up to line {test_line}: {ok} | {first_err}")
