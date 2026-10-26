import os
import sys
import json
import datetime
import subprocess

BASE_DIR = r"C:\scripts\linkedin_autopilot"
VAULT_PATH = os.path.join(BASE_DIR, "content_vault.json")
STATE_PATH = os.path.join(BASE_DIR, "state.json")
GRAPHICS_DIR = os.path.join(BASE_DIR, "graphics")

with open(VAULT_PATH, "r", encoding="utf-8") as f:
    posts = json.load(f)

# Load or initialize state
state = {"current_index": 0, "last_posted_date": None}
if os.path.exists(STATE_PATH):
    try:
        with open(STATE_PATH, "r", encoding="utf-8") as f:
            state = json.load(f)
    except:
        pass

# Determine post: can accept an explicit argument or pick next
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    post_idx = (int(sys.argv[1]) - 1) % len(posts)
else:
    post_idx = state.get("current_index", 0) % len(posts)

cur_post = posts[post_idx]
post_id = cur_post["id"]
post_text = cur_post["text"]
graphic_path = os.path.join(GRAPHICS_DIR, f"post_day_{post_id:02d}.png")

# Advance state for next time
state["current_index"] = (post_idx + 1) % len(posts)
state["last_posted_date"] = str(datetime.date.today())
with open(STATE_PATH, "w", encoding="utf-8") as f:
    json.dump(state, f, indent=2)

# Copy text to Windows clipboard via PowerShell
ps_script = f"""
$txt = @'
{post_text}
'@
Set-Clipboard -Value $txt
"""
subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", ps_script], check=True)

print("=" * 65)
print(f" [AUTOPILOT] Post #{post_id} Loaded: {cur_post['card_title']}")
print(f" Category:   {cur_post['category']}")
print(f" Graphic:    {graphic_path}")
print("=" * 65)
print(" 1. Text copied to your clipboard!")
print(" 2. Graphic selected in Windows Explorer.")
print(" 3. Opening LinkedIn post composer in your browser...")
print("=" * 65)
print(" >> Press [Ctrl + V] in LinkedIn, drag the image in, and click Post! <<")
print("=" * 65)

# Highlight graphic in Explorer for drag-and-drop
if os.path.exists(graphic_path):
    subprocess.Popen(f'explorer.exe /select,"{graphic_path}"')

# Open browser to LinkedIn post composer
subprocess.Popen(["cmd.exe", "/c", "start", "https://www.linkedin.com/feed/?shareActive=true"])
