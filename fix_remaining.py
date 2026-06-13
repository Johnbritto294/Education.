from pathlib import Path

files = [
    Path(r"C:\Users\jason\OneDrive - Stackly\Desktop\Online\index.html"),
    Path(r"C:\Users\jason\OneDrive - Stackly\Desktop\Online\features.html"),
    Path(r"C:\Users\jason\OneDrive - Stackly\Desktop\Online\courses.html"),
    Path(r"C:\Users\jason\OneDrive - Stackly\Desktop\Online\about.html"),
    Path(r"C:\Users\jason\OneDrive - Stackly\Desktop\Online\blog.html"),
    Path(r"C:\Users\jason\OneDrive - Stackly\Desktop\Online\contact.html"),
]

replacements = {
    # Fix broken lazy attribute (corrupted from loading="lazy")
    '" "lazy"': ' loading="lazy"',
    # Course badge hot
    '?? Hot': '🔥 Hot',
    # Play button
    'class="play-btn">?</div>': 'class="play-btn">▶</div>',
    # Course meta icons
    '<span>? ': '<span>⏱ ',
    '<span> ?? ': '<span> 📚 ',
    '<span> ? ': '<span> ★ ',
    # Button/link arrows
    'Get Started ?': 'Get Started →',
    'Browse All 1,200+ Courses ?': 'Browse All 1,200+ Courses →',
    'Contact Sales ?': 'Contact Sales →',
    'Join Free ?': 'Join Free →',
    'Read Article ?': 'Read Article →',
    'Send Message ?': 'Send Message →',
    'View All Articles ?': 'View All Articles →',
    'Explore Courses ?': 'Explore Courses →',
    # Footer menu arrows
    '? Browse Courses': '→ Browse Courses',
    '? Instructors': '→ Instructors',
    '? Certifications': '→ Certifications',
    '? Live Classes': '→ Live Classes',
    '? Pricing': '→ Pricing',
    '? About Us': '→ About Us',
    '? Careers': '→ Careers',
    '? Press': '→ Press',
    '? Blog': '→ Blog',
    '? Contact': '→ Contact',
    '? Help Center': '→ Help Center',
    '? Community Forum': '→ Community Forum',
    '? Student Guide': '→ Student Guide',
    '? Teach on Elearna': '→ Teach on Elearna',
    '? Enterprise': '→ Enterprise',
    # Blog meta
    '?? Jun 5, 2025': '📅 Jun 5, 2025',
    '?? May 28, 2025': '📅 May 28, 2025',
    '?? May 18, 2025': '📅 May 18, 2025',
    '? 5 min read': '⏱ 5 min read',
    '? 7 min read': '⏱ 7 min read',
    '? 6 min read': '⏱ 6 min read',
    # Blog excerpt
    'workflow ? and what': 'workflow — and what',
    # Instructor stats
    '?? 18 courses': '📚 18 courses',
    '?? 24K students': '👥 24K students',
    '?? 12 courses': '📚 12 courses',
    '?? 18K students': '👥 18K students',
    '?? 9 courses': '📚 9 courses',
    '?? 31K students': '👥 31K students',
    '?? 7 courses': '📚 7 courses',
    '?? 15K students': '👥 15K students',
    # Loading text
    'Loading?': 'Loading…',
    # CTA footer
    'No spam \xa0?\xa0 ? Cancel anytime \xa0?\xa0 ? Free forever plan': 'No spam  ·  Cancel anytime  ·  Free forever plan',
}

for path in files:
    text = path.read_text(encoding="utf-8", errors="replace")
    original = text
    for old, new in replacements.items():
        text = text.replace(old, new)
    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"Fixed: {path.name}")
    else:
        print(f"No change: {path.name}")
