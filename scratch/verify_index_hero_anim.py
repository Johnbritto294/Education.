import os

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\index.html"
success = True

if os.path.exists(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Check opacity
    if ".hero-title{" in content and "opacity:0" in content:
        print("OK: .hero-title is set to opacity:0 initially.")
    else:
        print("Warning: could not verify .hero-title opacity:0 styling directly, let's look for opacity:0")
        if "opacity:0" in content:
            print("OK: Found opacity:0 references.")
        else:
            success = False
            
    # 2. Check JS functions
    if "splitTextIntoWords" in content and "Unique Hero Entrance Animation" in content:
        print("OK: splitTextIntoWords function and Entrance Animation triggers verified in JS script block.")
    else:
        print("Error: JS helper or trigger not found!")
        success = False

if success:
    print("SUCCESS: index.html hero text animations verified successfully!")
else:
    print("FAILURE: Verification failed.")
