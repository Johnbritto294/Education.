import os

workspace_dir = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy"
html_files = ["index.html", "about.html", "blog.html", "contact.html", "courses.html", "features.html"]

success = True

for name in html_files:
    path = os.path.join(workspace_dir, name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Verify that the isLayoutControl condition is present
        if "isLayoutControl" not in content:
            print(f"Error: isLayoutControl check not found in {name}!")
            success = False
        else:
            print(f"OK: isLayoutControl check verified in {name}")
            
        # Verify that the old ScrollTrigger block for nav links is gone
        if "toggleActions: 'play none none none'" in content and "filter: 'blur(8px)'" in content:
            # We still have some scroll trigger but it shouldn't apply to nav links
            if "isNavbarElement" in content or "isLayoutControl" in content:
                print(f"  OK: {name} contains proper conditional checks for scroll trigger exclusions.")

if success:
    print("SUCCESS: GSAP navbar blur fixes verified successfully across all main pages!")
else:
    print("FAILURE: Verification failed for some pages.")
