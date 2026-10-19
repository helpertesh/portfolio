"""
Generates Peter-Mutethia-Resume.pdf from the data below.

Edit the dictionaries, then run:   python make_resume.py
The portfolio's "Download resume" button serves the file this script writes.
Sections with an empty list (e.g. EDUCATION) are left out of the PDF.
"""
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (HRFlowable, Paragraph, SimpleDocTemplate, Spacer,
                                Table, TableStyle, KeepTogether)

# ====================== EDIT ME ======================
PERSON = {
    "name": "Peter Mutethia",
    "title": "Full-Stack Web Developer",
    "location": "Nairobi, Kenya",
    "email": "mutethiap25@gmail.com",
    "phone": "+254 712 919 229",
    "github": "github.com/helpertesh",
    "website": "",          # e.g. "petermutethia.netlify.app" once deployed
    "linkedin": "",         # e.g. "linkedin.com/in/your-handle"
}

SUMMARY = (
    "Full-stack web developer with front-end roots, building for the web since 2018. "
    "I design and ship responsive websites and web applications end to end: React and clean CSS "
    "on the front, Python (FastAPI, Flask) and Node.js on the back, PostgreSQL for data, and Git "
    "and Docker for delivery. I care about accessible interfaces, well-documented APIs and "
    "reliable deployment."
)

SKILLS = [
    ("Programming", "Python, JavaScript (ES6+), C++, HTML5, CSS3"),
    ("Front-end", "React, Redux, Tailwind CSS, Bootstrap, responsive web design"),
    ("Back-end & APIs", "FastAPI, Flask, Node.js, Express.js, REST APIs, Pydantic, Swagger/OpenAPI"),
    ("Databases", "PostgreSQL, MySQL, SQLite; MongoDB fundamentals"),
    ("Tools", "Git, GitHub, VS Code, Postman, Docker, Docker Compose, Linux fundamentals"),
    ("Practices", "CRUD design, API testing, debugging, environment configuration, deployment workflows"),
]

PROJECTS = [
    {
        "name": "Hostel Booking Platform",
        "year": "2025",
        "link": "cool-arithmetic-8f3db7.netlify.app",
        "repo": "github.com/helpertesh/hostel-bookin",
        "stack": "HTML, CSS, JavaScript, Chart.js",
        "bullets": [
            "Built a booking platform for Dedan Kimathi University of Technology students to browse hostels, check availability and reserve rooms.",
            "Implemented login and sign-up flows, a booking workflow and a Chart.js dashboard.",
            "Deployed on Netlify with a responsive layout that works on phones and desktops.",
        ],
    },
    {
        "name": "Restaurant Booking System",
        "year": "In progress",
        "link": "", "repo": "",
        "stack": "HTML, CSS, JavaScript, Firebase",
        "bullets": [
            "Online table reservations with customer notifications and an admin dashboard.",
        ],
    },
    {
        "name": "Weather Forecast App",
        "year": "In progress",
        "link": "", "repo": "",
        "stack": "JavaScript, Weather API, Geolocation",
        "bullets": [
            "Real-time weather with geolocation detection and a five-day forecast.",
        ],
    },
]

EXPERIENCE = [
    {
        "role": "Freelance Web Developer",
        "org": "Self-employed",
        "dates": "2019 – present",
        "bullets": [
            "Design and build responsive websites and small web applications for clients, from landing pages to booking systems.",
            "Handle the full delivery cycle: requirements, design, development, testing, deployment and hand-over.",
        ],
    },
]

# Add entries like: {"degree": "BSc Computer Science", "school": "Dedan Kimathi University of Technology", "dates": "2021 – 2025"}
EDUCATION = []

# Add entries like: {"name": "Meta Front-End Developer", "issuer": "Coursera", "year": "2025"}
CERTIFICATIONS = []
# ====================== END EDIT ======================


ACCENT = colors.HexColor("#2563eb")
INK = colors.HexColor("#0f172a")
MUTED = colors.HexColor("#475569")
RULE = colors.HexColor("#cbd5e1")

BASE = "Helvetica"
BOLD = "Helvetica-Bold"

st_name = ParagraphStyle("name", fontName=BOLD, fontSize=22, leading=26, textColor=INK, spaceAfter=2)
st_title = ParagraphStyle("title", fontName=BASE, fontSize=11.5, leading=14, textColor=ACCENT, spaceAfter=4)
st_contact = ParagraphStyle("contact", fontName=BASE, fontSize=9, leading=12, textColor=MUTED)
st_h = ParagraphStyle("h", fontName=BOLD, fontSize=10.5, leading=13, textColor=ACCENT, spaceBefore=10, spaceAfter=3)
st_body = ParagraphStyle("body", fontName=BASE, fontSize=9.6, leading=13.2, textColor=INK)
st_item = ParagraphStyle("item", fontName=BOLD, fontSize=10, leading=13, textColor=INK)
st_meta = ParagraphStyle("meta", fontName=BASE, fontSize=9, leading=12, textColor=MUTED)
st_bullet = ParagraphStyle("bullet", parent=st_body, leftIndent=10, bulletIndent=0, spaceAfter=1)
st_skill_k = ParagraphStyle("sk", fontName=BOLD, fontSize=9.3, leading=12.5, textColor=INK)
st_skill_v = ParagraphStyle("sv", fontName=BASE, fontSize=9.3, leading=12.5, textColor=INK)


def heading(text):
    return [Paragraph(text.upper(), st_h), HRFlowable(width="100%", thickness=0.8, color=RULE, spaceAfter=5)]


def bullets(items):
    return [Paragraph(b, st_bullet, bulletText="•") for b in items]


def build():
    doc = SimpleDocTemplate(
        "Peter-Mutethia-Resume.pdf", pagesize=A4,
        leftMargin=16 * mm, rightMargin=16 * mm, topMargin=14 * mm, bottomMargin=14 * mm,
        title=f"{PERSON['name']} – Resume", author=PERSON["name"],
    )
    story = []

    # Header
    contact_bits = [PERSON["location"], PERSON["email"], PERSON["phone"], PERSON["github"]]
    for k in ("website", "linkedin"):
        if PERSON.get(k):
            contact_bits.append(PERSON[k])
    story += [
        Paragraph(PERSON["name"], st_name),
        Paragraph(PERSON["title"], st_title),
        Paragraph("  ·  ".join(contact_bits), st_contact),
        Spacer(1, 4),
    ]

    # Summary
    story += heading("Summary")
    story.append(Paragraph(SUMMARY, st_body))

    # Skills table
    story += heading("Technical skills")
    rows = [[Paragraph(k, st_skill_k), Paragraph(v, st_skill_v)] for k, v in SKILLS]
    t = Table(rows, colWidths=[34 * mm, None])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 1.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
    ]))
    story.append(t)

    # Projects
    if PROJECTS:
        story += heading("Projects")
        for p in PROJECTS:
            links = " · ".join(x for x in (p.get("link"), p.get("repo")) if x)
            meta = p["stack"] + (f"  ·  {links}" if links else "")
            block = [
                Table([[Paragraph(p["name"], st_item), Paragraph(p["year"], ParagraphStyle("r", parent=st_meta, alignment=2))]],
                      colWidths=[None, 30 * mm], style=[("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                                       ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]),
                Paragraph(meta, st_meta),
                *bullets(p["bullets"]),
                Spacer(1, 5),
            ]
            story.append(KeepTogether(block))

    # Experience
    if EXPERIENCE:
        story += heading("Experience")
        for e in EXPERIENCE:
            block = [
                Table([[Paragraph(f"{e['role']} — {e['org']}", st_item), Paragraph(e["dates"], ParagraphStyle("r2", parent=st_meta, alignment=2))]],
                      colWidths=[None, 36 * mm], style=[("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                                       ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]),
                *bullets(e["bullets"]),
                Spacer(1, 5),
            ]
            story.append(KeepTogether(block))

    # Education
    if EDUCATION:
        story += heading("Education")
        for ed in EDUCATION:
            story.append(Paragraph(f"<b>{ed['degree']}</b> — {ed['school']}  ·  <font color='#475569'>{ed['dates']}</font>", st_body))

    # Certifications
    if CERTIFICATIONS:
        story += heading("Certifications")
        for c in CERTIFICATIONS:
            story.append(Paragraph(f"<b>{c['name']}</b> — {c['issuer']}, {c['year']}", st_body))

    doc.build(story)
    print("Wrote Peter-Mutethia-Resume.pdf")


if __name__ == "__main__":
    build()
