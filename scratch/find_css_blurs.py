import os
import re

html_files = ["index.html", "about.html", "blog.html", "contact.html", "courses.html", "features.html"]
workspace_dir = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy"

for name in html_files:
    path = os.path.join(workspace_dir, name)
    if os.path.exists(path):
        print(f"=== 'blur' styling in {name} ===")
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        # Find selectors with blur in their rules
        style_blocks = re.findall(r'<style.*?>(.*?)</style>', content, re.DOTALL | re.IGNORECASE)
        for i, style in enumerate(style_blocks):
            # find all rules with blur
            blur_rules = re.findall(r'([^{}]*?\{[^{}]*?blur[^{}]*?\})', style, re.DOTALL | re.IGNORECASE)
            for rule in blur_rules:
                print(f"  {rule.strip()}")
