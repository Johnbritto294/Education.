import os
import re

html_files = ["index.html", "about.html", "blog.html", "contact.html", "courses.html", "features.html"]
workspace_dir = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy"

for name in html_files:
    path = os.path.join(workspace_dir, name)
    if os.path.exists(path):
        print(f"=== hover selector styling in {name} ===")
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        style_blocks = re.findall(r'<style.*?>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
        for style in style_blocks:
            # Look for hover selectors that contain filter or opacity
            rules = re.findall(r'([^{}]*?:hover[^{}]*?\{[^{}]*?(?:filter|opacity|blur)[^{}]*?\})', style, re.DOTALL | re.IGNORECASE)
            for rule in rules:
                print(f"  {rule.strip()}")
