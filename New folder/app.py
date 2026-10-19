import json
import os
import smtplib
from datetime import datetime, timezone
from email.message import EmailMessage
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request, send_from_directory

from config import BASE_DIR, CONTACTS_FILE, PORTFOLIO, SOCIAL_ICONS

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-change-me-in-production")


def _ensure_data_dir() -> None:
    CONTACTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not CONTACTS_FILE.exists():
        CONTACTS_FILE.write_text("[]", encoding="utf-8")


def _load_messages() -> list:
    _ensure_data_dir()
    try:
        return json.loads(CONTACTS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []


def _save_message(entry: dict) -> None:
    messages = _load_messages()
    messages.append(entry)
    CONTACTS_FILE.write_text(json.dumps(messages, indent=2), encoding="utf-8")


def _send_email(name: str, email: str, subject: str, message: str) -> bool:
    host = os.getenv("SMTP_HOST")
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASSWORD")
    to_addr = os.getenv("CONTACT_TO", PORTFOLIO["email"])

    if not all([host, user, password]):
        return False

    msg = EmailMessage()
    msg["Subject"] = f"[Portfolio] {subject or 'New message'} — {name}"
    msg["From"] = user
    msg["To"] = to_addr
    msg["Reply-To"] = email
    msg.set_content(
        f"Name: {name}\nEmail: {email}\nSubject: {subject}\n\n{message}"
    )

    port = int(os.getenv("SMTP_PORT", "587"))
    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(user, password)
        server.send_message(msg)
    return True


def _media_url(path: str) -> str:
    if path.startswith(("http://", "https://")):
        return path
    if (BASE_DIR / path).is_file():
        return f"/media/{path}"
    return "https://placehold.co/800x500/0c1222/64748b?text=Image"


def wa_link() -> str:
    from urllib.parse import quote
    msg = PORTFOLIO.get("whatsapp_message", "")
    return f"https://wa.me/{PORTFOLIO['whatsapp']}" + (f"?text={quote(msg)}" if msg else "")


@app.context_processor
def inject_media():
    return {"media": _media_url, "wa_link": wa_link()}


@app.route("/media/<path:filename>")
def media_file(filename):
    return send_from_directory(BASE_DIR, filename)


@app.route("/")
def index():
    return render_template("index.html", p=PORTFOLIO, icons=SOCIAL_ICONS)


@app.route("/resume")
def resume():
    return send_from_directory(BASE_DIR, PORTFOLIO["resume"], as_attachment=True)


@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json(silent=True) or {}
    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    subject = (data.get("subject") or "").strip()
    message = (data.get("message") or "").strip()

    if not name or not email or not message:
        return jsonify({"ok": False, "error": "Name, email, and message are required."}), 400

    if "@" not in email:
        return jsonify({"ok": False, "error": "Please enter a valid email."}), 400

    entry = {
        "name": name,
        "email": email,
        "subject": subject,
        "message": message,
        "at": datetime.now(timezone.utc).isoformat(),
    }
    _save_message(entry)

    emailed = False
    try:
        emailed = _send_email(name, email, subject, message)
    except Exception:
        emailed = False

    return jsonify({
        "ok": True,
        "message": "Thanks! Your message was received."
        + (" We'll reply soon." if emailed else ""),
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
