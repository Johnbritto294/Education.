import os
import re

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\index.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Search for backTop or back-top in script
scripts = re.findall(r'<script.*?>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
for idx, s in enumerate(scripts):
    if "backtop" in s.lower() or "back-top" in s.lower():
        print(f"=== Script {idx+1} ===")
        lines = s.split('\n')
        for i, line in enumerate(lines):
            if "back" in line.lower() or "scroll" in line.lower():
                print(f"  {i+1}: {line.strip()}")
