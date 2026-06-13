import os
import re

path = r"c:\Users\jason\OneDrive - Stackly\Desktop\Online - Copy\index.html"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

# 1. Update CSS to set .hero-title opacity to 0 initially
old_css_title = ".hero-title{font-family:'Sora',sans-serif;font-size:clamp(2.4rem,5vw,3.8rem);font-weight:800;line-height:1.1;letter-spacing:-2px;margin-bottom:20px;opacity:1}"
new_css_title = ".hero-title{font-family:'Sora',sans-serif;font-size:clamp(2.4rem,5vw,3.8rem);font-weight:800;line-height:1.1;letter-spacing:-2px;margin-bottom:20px;opacity:0}"

if old_css_title in content:
    content = content.replace(old_css_title, new_css_title)
    print("Updated CSS hero title opacity to 0")
else:
    # Try with spaces
    old_css_title_space = ".hero-title { font-family:'Sora',sans-serif;font-size:clamp(2.4rem,5vw,3.8rem);font-weight:800;line-height:1.1;letter-spacing:-2px;margin-bottom:20px;opacity:1 }"
    if old_css_title_space in content:
        content = content.replace(old_css_title_space, new_css_title)
        print("Updated CSS hero title opacity to 0 (spaced version)")
    else:
        print("CSS hero title style not found for replacement, will do a regex match")
        content = re.sub(r'\.hero-title\s*\{([^}]*?)opacity:\s*1([^}]*?)\}', r'.hero-title{\1opacity:0\2}', content)

# 2. Inject helper function splitTextIntoWords and custom hero animation script
# Let's place it right at the beginning of initGSAP()
old_init_gsap = "function initGSAP() {\n\n\n  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;\n\n\n  gsap.registerPlugin(ScrollTrigger);"

new_init_gsap = """function initGSAP() {


  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;


  gsap.registerPlugin(ScrollTrigger);

  // --- Helper to split text nodes into animatable words ---
  function splitTextIntoWords(element) {
    const nodes = Array.from(element.childNodes);
    nodes.forEach(node => {
      if (node.nodeType === 3) { // Text node
        const text = node.textContent.trim();
        if (text) {
          const words = text.split(/\\s+/);
          const frag = document.createDocumentFragment();
          words.forEach((word, index) => {
            const wrapper = document.createElement('span');
            wrapper.className = 'word-wrapper';
            wrapper.style.cssText = 'display:inline-block; overflow:hidden; vertical-align:bottom; margin-right:0.18em;';
            
            const inner = document.createElement('span');
            inner.className = 'word';
            inner.style.cssText = 'display:inline-block; transform:translateY(115%) rotate(5deg); will-change:transform;';
            inner.textContent = word;
            
            wrapper.appendChild(inner);
            frag.appendChild(wrapper);
          });
          element.replaceChild(frag, node);
        } else {
          node.textContent = ' ';
        }
      } else if (node.nodeType === 1) { // Element node
        splitTextIntoWords(node);
      }
    });
  }

  // --- Unique Hero Entrance Animation ---
  const heroTitle = document.querySelector('.hero-title');
  if (heroTitle) {
    splitTextIntoWords(heroTitle);
    heroTitle.style.opacity = '1';
    
    gsap.to('.hero-title .word', {
      y: '0%',
      rotate: 0,
      duration: 1.1,
      ease: 'power4.out',
      stagger: 0.05,
      delay: 0.1
    });
  }

  gsap.fromTo('.hero-badge',
    { scale: 0.8, opacity: 0 },
    { scale: 1, opacity: 1, duration: 0.8, ease: 'back.out(1.5)', delay: 0.05 }
  );

  gsap.fromTo('.hero-desc',
    { y: 20, opacity: 0, filter: 'blur(3px)' },
    { y: 0, opacity: 1, filter: 'blur(0px)', duration: 0.9, ease: 'power3.out', delay: 0.45 }
  );

  gsap.fromTo('.hero-actions',
    { y: 15, opacity: 0 },
    { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out', delay: 0.65 }
  );

  gsap.fromTo('.hero-stats .stat-item',
    { y: 30, opacity: 0 },
    { y: 0, opacity: 1, duration: 0.8, ease: 'power3.out', stagger: 0.08, delay: 0.75 }
  );

  gsap.fromTo('.hero-card-main',
    { x: 40, opacity: 0, rotateY: 10 },
    { x: 0, opacity: 1, rotateY: -6, duration: 1.2, ease: 'power3.out', delay: 0.35 }
  );

  gsap.fromTo('.floating-card-1',
    { x: -30, y: 20, opacity: 0 },
    { x: 0, y: 0, opacity: 1, duration: 1.0, ease: 'back.out(1.2)', delay: 0.75 }
  );

  gsap.fromTo('.floating-card-2',
    { x: 30, y: -20, opacity: 0 },
    { x: 0, y: 0, opacity: 1, duration: 1.0, ease: 'back.out(1.2)', delay: 0.95 }
  );
"""

if old_init_gsap in content:
    content = content.replace(old_init_gsap, new_init_gsap)
    print("Injected custom hero animation block into initGSAP()")
else:
    # Try matching without newlines
    old_init_gsap_normalized = "function initGSAP() { if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return; gsap.registerPlugin(ScrollTrigger);"
    # Let's search with regex
    content = re.sub(r'function initGSAP\(\)\s*\{\s*if\s*\(typeof gsap\s*===\s*\'undefined\'\s*\|\|\s*typeof ScrollTrigger\s*===\s*\'undefined\'\)\s*return;\s*gsap\.registerPlugin\(ScrollTrigger\);', new_init_gsap, content)
    print("Injected custom hero animation block using regex search")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("Successfully modified index.html")
