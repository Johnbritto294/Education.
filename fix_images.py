import os
root = r'C:\Users\jason\OneDrive - Stackly\Desktop\Online'
for name in os.listdir(root):
    if not name.endswith('.html'):
        continue
    path = os.path.join(root, name)
    try:
        text = open(path, 'rb').read().decode('utf-8', errors='ignore')
    except Exception as e:
        print('Skip', name, e)
        continue
    new = text.replace('.webp"', '.png"').replace(".webp'", ".png'")
    if new != text:
        open(path, 'w', encoding='utf-8').write(new)
        print('Updated', name)
    else:
        print('No change', name)
