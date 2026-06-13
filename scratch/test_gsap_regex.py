import os
import re

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\about.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Pattern to match: gsap.utils.toArray(targets).forEach(...)
pattern = r'gsap\.utils\.toArray\(targets\)\.forEach\(el\s*=>\s*\{.*?\n\s*\}\);'
match = re.search(pattern, content, re.DOTALL)
if match:
    print("MATCH FOUND:")
    print(match.group(0)[:400])
else:
    print("NO MATCH FOUND")
