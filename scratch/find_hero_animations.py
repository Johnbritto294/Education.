import os
import re

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\index.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Search for hero elements in script blocks
scripts = re.findall(r'<script.*?>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
for idx, s in enumerate(scripts):
    found = False
    for term in ["hero-title", "hero-desc", "hero-badge", "hero-actions", "hero-stats"]:
        if term in s:
            found = True
            break
    if found:
        print(f"=== Found in Script {idx+1} ===")
        lines = s.split('\n')
        for i, line in enumerate(lines):
            if any(term in line for term in ["hero-title", "hero-desc", "hero-badge", "hero-actions", "hero-stats"]):
                print(f"  {i+1}: {line.strip()}")
