"""
Builds a clean "deploy" folder containing only what the live site needs.
Run:  python make_deploy.py
Then drag the "deploy" folder onto https://app.netlify.com/drop
"""
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "deploy"

FILES = ["index.html", "Peter-Mutethia-Resume.pdf"]
FOLDERS = ["assets"]

if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

for name in FILES:
    shutil.copy2(ROOT / name, OUT / name)
for name in FOLDERS:
    shutil.copytree(ROOT / name, OUT / name)

# Tell Netlify to serve index.html for any unknown path (nice for sharing links)
(OUT / "_redirects").write_text("/*  /index.html  200\n", encoding="utf-8")

total = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file())
print(f"deploy/ ready: {total/1024:.0f} KB")
for f in sorted(OUT.rglob("*")):
    if f.is_file():
        print("  ", f.relative_to(OUT))
