"""
All the text on the site lives here. Edit, save, refresh.
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

PORTFOLIO = {
    "name": "Peter Mutethia",
    "nickname": "Helpertesh",
    "initials": "PM",
    "title": "Full-Stack Web Developer",
    "role_line": "Full-stack web developer based in Nairobi, Kenya",
    "tagline": "I build fast, responsive websites and web apps from the database to the pixel. Python and JavaScript on the back end, React and clean CSS on the front, shipped with Git and Docker.",
    "availability": "Available for freelance & full-time work",
    "location": "Nairobi, Kenya",
    "location_short": "Nairobi, KE",
    "email": "mutethiap25@gmail.com",
    "phone": "+254 712 919 229",
    "whatsapp": "254712919229",
    "whatsapp_message": "Hi Peter, I found your portfolio and would like to talk about a project.",
    "resume": "Peter-Mutethia-Resume.pdf",
    "about_image": "assets/peter.jpg",
    "coding_since": 2018,
    "years_badge": "5+",
    "code_stack": ["Python", "JavaScript", "React", "FastAPI"],

    # Social links. Add e.g. "linkedin": "https://linkedin.com/in/..." and an entry in SOCIAL_ICONS below.
    "social": {
        "github": "https://github.com/helpertesh",
    },

    "ticker": [
        {"icon": "fab fa-python", "label": "Python"},
        {"icon": "fab fa-js", "label": "JavaScript"},
        {"icon": "fab fa-react", "label": "React"},
        {"icon": "fas fa-bolt", "label": "FastAPI"},
        {"icon": "fab fa-node-js", "label": "Node.js"},
        {"icon": "fas fa-database", "label": "PostgreSQL"},
        {"icon": "fab fa-docker", "label": "Docker"},
        {"icon": "fab fa-git-alt", "label": "Git"},
        {"icon": "fas fa-wind", "label": "Tailwind CSS"},
        {"icon": "fas fa-plug", "label": "REST APIs"},
        {"icon": "fab fa-linux", "label": "Linux"},
    ],

    "about_heading": "Front-end roots, full-stack today",
    "about": [
        "I started building for the web in 2018 with HTML and CSS, and I've been hooked ever since. Those front-end roots still show: I care about layouts that work on every screen and interfaces that feel obvious to use.",
        "These days I work across the whole stack. I design REST APIs with FastAPI and Node.js, model data in PostgreSQL and MySQL, build React front-ends, and ship it all with Git, Docker and a proper deployment workflow.",
    ],
    "currently": "Deepening my FastAPI and React skills, and open to freelance projects and full-time roles.",
    "highlights": [
        "Mobile-first layouts that work on every screen",
        "Clean, tested APIs with clear documentation",
        "Honest communication and reliable delivery",
    ],

    # Skill groups. "size" is wide / normal / full. "hot": True highlights a chip.
    "stack": [
        {"size": "wide", "icon": "fas fa-code", "name": "Programming", "sub": "Languages I write every week", "items": [
            {"icon": "fab fa-python", "label": "Python", "hot": True},
            {"icon": "fab fa-js", "label": "JavaScript (ES6+)", "hot": True},
            {"icon": "fas fa-c", "label": "C++"},
            {"icon": "fab fa-html5", "label": "HTML5"},
            {"icon": "fab fa-css3-alt", "label": "CSS3"},
        ]},
        {"size": "wide", "icon": "fas fa-window-maximize", "name": "Front-end", "sub": "Interfaces people actually enjoy", "items": [
            {"icon": "fab fa-react", "label": "React", "hot": True},
            {"icon": "fas fa-layer-group", "label": "Redux"},
            {"icon": "fas fa-wind", "label": "Tailwind CSS", "hot": True},
            {"icon": "fab fa-bootstrap", "label": "Bootstrap"},
            {"icon": "fas fa-mobile-screen", "label": "Responsive design"},
        ]},
        {"size": "normal", "icon": "fas fa-server", "name": "Back-end & APIs", "sub": "Where the logic lives", "items": [
            {"icon": "fas fa-bolt", "label": "FastAPI", "hot": True},
            {"icon": "fas fa-flask", "label": "Flask"},
            {"icon": "fab fa-node-js", "label": "Node.js"},
            {"icon": "fas fa-route", "label": "Express.js"},
            {"icon": "fas fa-plug", "label": "REST APIs"},
            {"icon": "fas fa-shield-halved", "label": "Pydantic"},
            {"icon": "fas fa-book", "label": "Swagger / OpenAPI"},
        ]},
        {"size": "normal", "icon": "fas fa-database", "name": "Databases", "sub": "Structured and document stores", "items": [
            {"icon": "fas fa-database", "label": "PostgreSQL", "hot": True},
            {"icon": "fas fa-database", "label": "MySQL"},
            {"icon": "fas fa-database", "label": "SQLite"},
            {"icon": "fas fa-leaf", "label": "MongoDB (fundamentals)"},
        ]},
        {"size": "normal", "icon": "fas fa-toolbox", "name": "Tools", "sub": "Daily drivers", "items": [
            {"icon": "fab fa-git-alt", "label": "Git", "hot": True},
            {"icon": "fab fa-github", "label": "GitHub"},
            {"icon": "fas fa-code", "label": "VS Code"},
            {"icon": "fas fa-paper-plane", "label": "Postman"},
            {"icon": "fab fa-docker", "label": "Docker", "hot": True},
            {"icon": "fas fa-cubes", "label": "Docker Compose"},
            {"icon": "fab fa-linux", "label": "Linux"},
        ]},
        {"size": "full", "icon": "fas fa-list-check", "name": "How I work", "sub": "Practices that keep projects healthy", "items": [
            {"icon": "fas fa-pen-to-square", "label": "CRUD design"},
            {"icon": "fas fa-vial", "label": "API testing"},
            {"icon": "fas fa-bug", "label": "Debugging"},
            {"icon": "fas fa-sliders", "label": "Environment configuration"},
            {"icon": "fas fa-rocket", "label": "Deployment workflows"},
            {"icon": "fas fa-code-branch", "label": "Version control"},
            {"icon": "fas fa-universal-access", "label": "Accessibility"},
        ]},
    ],

    "services": [
        {"title": "Websites & landing pages",
         "desc": "Fast, responsive, search-friendly sites built from scratch or from your design, with a contact form that actually reaches you.",
         "points": ["Business and portfolio sites", "Landing pages for campaigns", "Hosting and domain setup"]},
        {"title": "Web apps & APIs",
         "desc": "Full-stack applications with a React front-end, a Python or Node back-end, a real database and documented REST endpoints.",
         "points": ["Booking and dashboard systems", "FastAPI / Express back-ends", "Auth, CRUD and reporting"]},
        {"title": "Fixes & improvements",
         "desc": "Already have a site? I'll make it faster, fix the mobile layout, squash bugs and add the features you've been putting off.",
         "points": ["Performance and SEO tune-ups", "Mobile responsiveness", "New features on existing code"]},
    ],

    # Projects. Leave live_url / repo_url empty ("") if there is no link yet.
    "projects": [
        {
            "title": "StudyFlow — Learning Automation",
            "description": "An AI-powered study assistant for university students. Organise units, notes, past papers and assignments, plan a timetable and calendar, log study time, and let the built-in AI generate summaries, quizzes and exam prep.",
            "image": "assets/learning-automation.jpg",
            "image_align": "left top",
            "tags": ["React", "Express.js", "Node.js", "OpenAI API", "Railway"],
            "live_url": "https://learningautomation-production.up.railway.app/",
            "repo_url": "https://github.com/helpertesh/learning-automation",
            "featured": True,
        },
        {
            "title": "Hostel Booking Platform",
            "description": "Booking platform for Dedan Kimathi University students to browse hostels, check availability and reserve rooms.",
            "image": "assets/hostel-booking.jpg",
            "tags": ["HTML", "CSS", "JavaScript", "Chart.js"],
            "live_url": "https://cool-arithmetic-8f3db7.netlify.app/",
            "repo_url": "https://github.com/helpertesh/hostel-bookin",
        },
        {
            "title": "Restaurant Booking System",
            "description": "Online reservations with table management, customer notifications and an admin dashboard.",
            "image": "https://images.unsplash.com/photo-1552566626-52f8b828add9?w=900&q=80",
            "tags": ["HTML", "CSS", "JavaScript", "Firebase"],
            "live_url": "", "repo_url": "",
            "status": "In progress — demo coming soon",
        },
        {
            "title": "Weather Forecast App",
            "description": "Real-time weather with geolocation detection, a five-day forecast and interactive maps.",
            "image": "https://images.unsplash.com/photo-1504608524841-42fe6f032b4b?w=900&q=80",
            "tags": ["HTML", "CSS", "JavaScript", "Weather API"],
            "live_url": "", "repo_url": "",
            "status": "In progress — demo coming soon",
        },
    ],

    # Timeline, newest first. "tags" is optional.
    "journey": [
        {"date": "2026 — now", "title": "Going full-stack",
         "text": "Shipped StudyFlow, an AI study assistant with a React front-end and an Express back-end on Railway, and now building REST APIs with FastAPI, PostgreSQL and Docker.",
         "tags": ["React", "Express.js", "OpenAI API", "FastAPI", "Docker"]},
        {"date": "2025", "title": "Hostel Booking Platform",
         "text": "Shipped a booking platform for university students with authentication, a booking flow and a Chart.js dashboard. Deployed on Netlify.",
         "tags": ["JavaScript", "Chart.js", "Netlify"]},
        {"date": "2019 — 2024", "title": "Freelance web developer",
         "text": "Built responsive websites and small web apps, from landing pages to booking systems, and learned to turn a vague brief into something that works.",
         "tags": ["HTML", "CSS", "JavaScript", "Python"]},
        {"date": "2018", "title": "First website",
         "text": "Wrote my first HTML page, broke it, fixed it, and got hooked on building things for the web."},
    ],
}

# Font Awesome icon for each key in PORTFOLIO["social"]
SOCIAL_ICONS = {
    "github": "fab fa-github",
    "linkedin": "fab fa-linkedin-in",
    "twitter": "fab fa-x-twitter",
    "instagram": "fab fa-instagram",
    "youtube": "fab fa-youtube",
}

CONTACTS_FILE = BASE_DIR / "data" / "messages.json"
