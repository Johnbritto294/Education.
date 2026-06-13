import os

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\about.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if "gsap.fromTo" in line or "filter: 'blur" in line:
        start = max(0, idx - 15)
        end = min(len(lines), idx + 25)
        print(f"=== about.html line {idx+1} ===")
        with open("C:\\Users\\jason\\.gemini\\antigravity\\brain\\3112bf68-b1f7-4c4b-8537-5bfd31b050c5\\scratch\\gsap_lines.txt", "w", encoding="utf-8") as out:
            for i in range(start, end):
                out.write(f"  {i+1}: {lines[i]}")
        break
