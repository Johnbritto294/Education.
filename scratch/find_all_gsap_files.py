import os
import re

workspace_dir = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy"

for name in os.listdir(workspace_dir):
    if name.endswith(".html"):
        path = os.path.join(workspace_dir, name)
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        if "scrollTrigger" in content and "filter: 'blur" in content:
            print(f"Found match in {name}")
