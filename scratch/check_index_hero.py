import os
import re

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\index.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Search for hero class markup and styling
hero_style = re.findall(r'\.hero[^{]*?\{[^}]*?\}', content, re.DOTALL | re.IGNORECASE)
print("=== Hero style in index.html ===")
for h in hero_style:
    print(h.strip())

hero_markup = re.findall(r'<section[^>]*?class=["\'][^"\']*hero[^"\']*["\'][^>]*>', content, re.IGNORECASE)
print("=== Hero markup in index.html ===")
for hm in hero_markup:
    print(hm.strip())
