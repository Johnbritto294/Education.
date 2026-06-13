import os
import re

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\courses.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Search for #courses selector inside style
matches = re.findall(r'#courses\s*\{[^}]*?\}', content, re.DOTALL | re.IGNORECASE)
for m in matches:
    print(m)
