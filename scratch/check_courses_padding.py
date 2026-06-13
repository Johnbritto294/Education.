import os
import re

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\courses.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Search for section-padding
matches = re.findall(r'\.section-padding\s*\{[^}]*?\}', content, re.DOTALL | re.IGNORECASE)
for m in matches:
    print(m)
    
# Let's also check the actual section tags in courses.html
section_tags = re.findall(r'<section[^>]*?id=["\']courses["\'][^>]*>', content, re.IGNORECASE)
print("Section tag:")
for t in section_tags:
    print(f"  {t}")
