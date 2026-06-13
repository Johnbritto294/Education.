import os
import re

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\index.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# Find the hero section structure
hero_match = re.search(r'<section[^>]*?class=["\'][^"\']*hero[^"\']*["\'][^>]*>(.*?)</section>', content, re.DOTALL | re.IGNORECASE)
if hero_match:
    print("=== Hero section in index.html ===")
    print(hero_match.group(1).strip()[:1500])
else:
    print("No hero section found!")
