import os
import re

html_files = ["index.html", "about.html", "blog.html", "contact.html", "courses.html", "features.html"]
workspace_dir = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy"

for name in html_files:
    path = os.path.join(workspace_dir, name)
    if os.path.exists(path):
        print(f"=== 'blur' references in {name} scripts ===")
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        scripts = re.findall(r'<script.*?>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
        for i, s in enumerate(scripts):
            lines = s.split('\n')
            for line_no, line in enumerate(lines):
                if "blur" in line.lower():
                    print(f"  Script {i+1} Line {line_no+1}: {line.strip()}")
