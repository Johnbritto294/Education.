import os
import re

workspace_dir = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy"
html_files = ["index.html", "about.html", "blog.html", "contact.html", "courses.html", "features.html"]

# The new JS code we want to insert
replacement_js = """  gsap.utils.toArray(targets).forEach(el => {
    if (el.dataset.gsapInit) return;
    if (el.closest('.hero') || el.closest('.reveal') || el.closest('.reveal-left') || el.closest('.reveal-right')) return;
    el.dataset.gsapInit = 'true';

    const isHero = el.closest('.hero');
    const delay = isHero ? 0 : Math.random() * 0.15;

    // Check if the element is a navbar link, back-to-top button, hamburger, or fixed layout control
    const isLayoutControl = el.closest('#navbar') || el.closest('.navbar') || el.closest('.nav-links') || el.closest('.nav-actions') || el.closest('.back-top') || el.id === 'backTop' || el.closest('.hamburger') || el.id === 'hamburger';

    if (isLayoutControl) {
      // Animate fixed layout controls immediately on page load without ScrollTrigger
      gsap.fromTo(el,
        { y: -10, opacity: 0, filter: 'blur(3px)' },
        { y: 0, opacity: 1, filter: 'blur(0px)', duration: 0.5, ease: 'power2.out', delay: delay }
      );
    } else {
      // Normal scroll trigger animation for other page elements
      gsap.fromTo(el,
        { y: 50, opacity: 0, filter: 'blur(8px)' },
        {
          y: 0, opacity: 1, filter: 'blur(0px)',
          duration: 0.9,
          ease: 'power3.out',
          delay: delay,
          scrollTrigger: {
            trigger: el,
            start: 'top 85%',
            toggleActions: 'play none none none'
          }
        }
      );
    }
  });"""

for name in html_files:
    path = os.path.join(workspace_dir, name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            
        # Regex pattern to match the target code
        pattern = r'gsap\.utils\.toArray\(targets\)\.forEach\(el\s*=>\s*\{.*?\n\s*\}\);'
        
        # Replace the matched block with replacement_js
        new_content, count = re.subn(pattern, replacement_js, content, flags=re.DOTALL)
        if count > 0:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Successfully fixed GSAP scroll trigger blur in {name}")
        else:
            print(f"Failed to match GSAP pattern in {name}!")
