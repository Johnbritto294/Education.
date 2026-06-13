import os

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\index.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

# Search for the script tags towards the end
script_start = -1
for idx, line in enumerate(lines):
    if "gsap.registerPlugin" in line:
        script_start = idx
        break

if script_start != -1:
    print(f"=== Script starts at line {script_start+1} ===")
    with open("C:\\Users\\jason\\.gemini\\antigravity\\brain\\3112bf68-b1f7-4c4b-8537-5bfd31b050c5\\scratch\\index_script_dump.txt", "w", encoding="utf-8") as out:
        for i in range(max(0, script_start - 10), min(len(lines), script_start + 180)):
            out.write(f"  {i+1}: {lines[i]}")
else:
    print("No script block with gsap.registerPlugin found")
