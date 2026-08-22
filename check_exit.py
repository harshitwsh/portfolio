import subprocess

res = subprocess.run(["node", "--check", "public/assets/main-B9-HtP-f.js"], capture_output=True, text=True)
print("Exit code:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)
