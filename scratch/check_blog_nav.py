import os

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\blog.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

idx = content.find("</nav>")
if idx != -1:
    print(content[idx:idx+300])
else:
    print("No nav end found")
