from pathlib import Path

files = [
    Path(r"C:\Users\jason\OneDrive - Stackly\Desktop\Online\index.html"),
    Path(r"C:\Users\jason\OneDrive - Stackly\Desktop\Online\features.html"),
    Path(r"C:\Users\jason\OneDrive - Stackly\Desktop\Online\courses.html"),
    Path(r"C:\Users\jason\OneDrive - Stackly\Desktop\Online\about.html"),
    Path(r"C:\Users\jason\OneDrive - Stackly\Desktop\Online\blog.html"),
    Path(r"C:\Users\jason\OneDrive - Stackly\Desktop\Online\contact.html"),
]

fixes = [
    ('?? Hot', '🔥 Hot'),
    ('?? Bestseller', '🔥 Bestseller'),
    ('?? 12,400 students', '👥 12,400 students'),
    ('❓', '▶'),
    ('? Watch Demo', '▶ Watch Demo'),
    ('Explore Courses ?', 'Explore Courses →'),
    ('Browse All 1,200+ Courses ?', 'Browse All 1,200+ Courses →'),
    ('Get Started ?', 'Get Started →'),
    ('Join Free ?', 'Join Free →'),
    ('Contact Sales ?', 'Contact Sales →'),
    ('Send Message ?', 'Send Message →'),
    ('View All Articles ?', 'View All Articles →'),
    ('Read Article ?', 'Read Article →'),
    ('Loading…', 'Loading…'),
    ('?? ', '🎓 '),
    ('? Browse Courses', '→ Browse Courses'),
    ('? Instructors', '→ Instructors'),
    ('? Certifications', '→ Certifications'),
    ('? Live Classes', '→ Live Classes'),
    ('? Pricing', '→ Pricing'),
    ('? About Us', '→ About Us'),
    ('? Careers', '→ Careers'),
    ('? Press', '→ Press'),
    ('? Blog', '→ Blog'),
    ('? Contact', '→ Contact'),
    ('? Help Center', '→ Help Center'),
    ('? Community Forum', '→ Community Forum'),
    ('? Student Guide', '→ Student Guide'),
    ('? Teach on Elearna', '→ Teach on Elearna'),
    ('? Enterprise', '→ Enterprise'),
    ('?? Jun 5, 2025', '📅 Jun 5, 2025'),
    ('?? May 28, 2025', '📅 May 28, 2025'),
    ('?? May 18, 2025', '📅 May 18, 2025'),
    ('? 5 min read', '📖 5 min read'),
    ('? 7 min read', '📖 7 min read'),
    ('? 6 min read', '📖 6 min read'),
    ('?? 18 courses', '📚 18 courses'),
    ('?? 24K students', '👥 24K students'),
    ('?? 12 courses', '📚 12 courses'),
    ('?? 18K students', '👥 18K students'),
    ('?? 9 courses', '📚 9 courses'),
    ('?? 31K students', '👥 31K students'),
    ('?? 7 courses', '📚 7 courses'),
    ('?? 15K students', '👥 15K students'),
    ('course rate ? triple', 'course rate 3x triple'),
    ('triple the industry average.', 'triple the industry average.'),
]

def clean_placeholders(text: str) -> str:
    lines = text.splitlines(keepends=True)
    out = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('<div class="hero-card-img">'):
            line = line.replace('>??<', '>🎓<').replace('>❓<', '>🎓<')
        if 'class="play-btn"' in stripped and '❓' in stripped:
            line = line.replace('❓', '▶')
        elif 'class="course-badge badge-hot"' in stripped and ('??' in stripped or '❓' in stripped):
            line = line.replace('?? Hot', '🔥 Hot').replace('❓', '🔥')
        if 'class="fc-num"' in stripped and ('❓' in stripped or '??' in stripped):
            line = line.replace('>❓<', '>🎯<').replace('>❓❓<', '>🎯<')
        if 'class="stat-icon"' in stripped and ('❓' in stripped or '??' in stripped):
            line = line.replace('❓', '📈')
        if 'class="step-circle"' in stripped and ('❓' in stripped or '??' in stripped):
            line = line.replace('❓', '1')
        if 'class="contact-icon"' in stripped and ('❓' in stripped or '??' in stripped):
            line = line.replace('❓', '📞')
        if 'class="testi-stars"' in stripped and ('❓' in stripped or '??' in stripped):
            line = line.replace('❓', '★')
        if 'class="blog-thumb"' in stripped and ('❓' in stripped or '??' in stripped):
            line = line.replace('>❓<', '>🖼️<').replace('>❓❓<', '>🖼️<')
        if 'class="instructor-photo"' in stripped and ('❓' in stripped or '??' in stripped):
            line = line.replace('❓', '👤')
        if 'class="course-thumb-bg"' in stripped and ('❓' in stripped or '??' in stripped):
            line = line.replace('>❓<', '>🎓<').replace('>❓❓<', '>🎓<')
        out.append(line)
    return ''.join(out)


for path in files:
    text = path.read_text(encoding="utf-8", errors="replace")
    original = text
    for old, new in fixes:
        text = text.replace(old, new)
    text = clean_placeholders(text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"Fixed: {path.name}")
    else:
        print(f"No change: {path.name}")
