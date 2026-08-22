with open("public/assets/main-B9-HtP-f.js", "r", encoding="utf-8") as f:
    code = f.read()

start = code.find("function injectResumeModalStyles()")
end = code.find('window.addEventListener("zero:openResume", openResumeModal);')
print("start:", start)
print("end:", end)
if start != -1 and end != -1:
    print("Start context:")
    print(code[start : start + 150])
    print("End context:")
    print(code[end : end + 100])
