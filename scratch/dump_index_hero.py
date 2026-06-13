import os
import re

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\index.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

hero_match = re.search(r'<section[^>]*?class=["\'][^"\']*hero[^"\']*["\'][^>]*>(.*?)</section>', content, re.DOTALL | re.IGNORECASE)
with open("C:\\Users\\jason\\.gemini\\antigravity\\brain\\3112bf68-b1f7-4c4b-8537-5bfd31b050c5\\scratch\\index_hero_dump.txt", "w", encoding="utf-8") as out:
    if hero_match:
        out.write(hero_match.group(1).strip())
    else:
        out.write("No hero section found!")
print("Finished. Saved to scratch/index_hero_dump.txt")
