import os
import json
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = r"C:\scripts\linkedin_autopilot"
VAULT_PATH = os.path.join(BASE_DIR, "content_vault.json")
GRAPHICS_DIR = os.path.join(BASE_DIR, "graphics")
os.makedirs(GRAPHICS_DIR, exist_ok=True)

# Color themes per category
CATEGORY_COLORS = {
    "ENDPOINT AUTOMATION": {"accent": (56, 189, 248), "pill_bg": (12, 74, 110)},
    "IDENTITY & SECURITY": {"accent": (244, 63, 94), "pill_bg": (136, 19, 55)},
    "CLOUD & VIRTUALIZATION": {"accent": (96, 165, 250), "pill_bg": (30, 58, 138)},
    "DEVOPS & RELEASE MANAGEMENT": {"accent": (52, 211, 153), "pill_bg": (6, 78, 59)},
    "OPEN SOURCE & ARCHITECTURE": {"accent": (251, 146, 60), "pill_bg": (124, 45, 18)},
    "CONTAINERS & KUBERNETES": {"accent": (168, 85, 247), "pill_bg": (88, 28, 135)},
    "CLOUD MIGRATION": {"accent": (14, 165, 233), "pill_bg": (3, 105, 161)},
    "MONITORING & RELIABILITY": {"accent": (234, 179, 8), "pill_bg": (113, 63, 18)},
    "AUTOMATION & POWERSHELL": {"accent": (59, 130, 246), "pill_bg": (29, 78, 216)},
    "CAREER & ENGINEERING": {"accent": (16, 185, 129), "pill_bg": (4, 120, 87)}
}

# Load standard Windows system fonts
def get_font(size, bold=False):
    font_names = ["segoeui.ttf", "arial.ttf", "calibri.ttf"]
    if bold:
        font_names = ["segoeuib.ttf", "arialbd.ttf", "calibrib.ttf"]
    for fn in font_names:
        p = os.path.join(os.environ.get("WINDIR", "C:\\Windows"), "Fonts", fn)
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except:
                pass
    return ImageFont.load_default()

font_title = get_font(42, bold=True)
font_category = get_font(20, bold=True)
font_bullet = get_font(24, bold=False)
font_metric = get_font(24, bold=True)
font_footer = get_font(20, bold=False)
font_footer_bold = get_font(20, bold=True)

with open(VAULT_PATH, "r", encoding="utf-8") as f:
    posts = json.load(f)

for post in posts:
    pid = post["id"]
    category = post.get("category", "CLOUD ARCHITECTURE")
    title = post.get("card_title", "Engineering Case Study")
    takeaways = post.get("card_takeaways", [])
    metric = post.get("metric", "Enterprise Case Study")
    
    colors = CATEGORY_COLORS.get(category, {"accent": (56, 189, 248), "pill_bg": (12, 74, 110)})
    accent = colors["accent"]
    pill_bg = colors["pill_bg"]
    
    # 1200x675 canvas
    img = Image.new("RGB", (1200, 675), color=(11, 17, 32)) # Deep slate
    draw = ImageDraw.Draw(img)
    
    # Gradient accent bar at top
    draw.rectangle([(0, 0), (1200, 8)], fill=accent)
    
    # Outer frame
    draw.rounded_rectangle([(30, 30), (1170, 645)], radius=20, outline=(30, 41, 59), width=2)
    
    # Category Pill Badge (Top Left)
    bbox = draw.textbbox((0, 0), category, font=font_category)
    text_w = bbox[2] - bbox[0]
    pill_x = 60
    pill_y = 50
    pill_h = 44
    pill_w = text_w + 44
    draw.rounded_rectangle([(pill_x, pill_y), (pill_x + pill_w, pill_y + pill_h)], radius=14, fill=pill_bg, outline=accent, width=2)
    draw.text((pill_x + 22, pill_y + 10), category, fill=accent, font=font_category)
    
    # Metric Badge (Top Right)
    m_bbox = draw.textbbox((0, 0), metric, font=font_metric)
    m_w = m_bbox[2] - m_bbox[0] + 40
    m_h = 44
    m_x = 1140 - m_w
    m_y = 50
    draw.rounded_rectangle([(m_x, m_y), (1140, m_y + m_h)], radius=14, fill=(30, 41, 59), outline=(71, 85, 105), width=2)
    draw.text((m_x + 20, m_y + 9), metric, fill=(248, 250, 252), font=font_metric)
    
    # Main Title
    # Simple line-wrap for long titles
    words = title.split(" ")
    lines = []
    cur = ""
    for w in words:
        test = (cur + " " + w).strip()
        t_box = draw.textbbox((0, 0), test, font=font_title)
        if t_box[2] - t_box[0] > 1050:
            lines.append(cur)
            cur = w
        else:
            cur = test
    if cur:
        lines.append(cur)
        
    title_y = 125
    for l in lines:
        draw.text((60, title_y), l, fill=(255, 255, 255), font=font_title)
        title_y += 50
        
    # Takeaway Cards
    card_y = max(title_y + 20, 235)
    for i, t in enumerate(takeaways[:3]):
        # Background card panel
        draw.rounded_rectangle([(60, card_y), (1140, card_y + 80)], radius=14, fill=(20, 30, 48), outline=(35, 48, 71), width=1)
        
        # Indicator check/dot
        draw.ellipse([(85, card_y + 28), (105, card_y + 48)], fill=accent)
        draw.ellipse([(91, card_y + 34), (99, card_y + 42)], fill=(11, 17, 32))
        
        # Text
        draw.text((125, card_y + 25), t, fill=(226, 232, 240), font=font_bullet)
        card_y += 98
        
    # Footer Divider & Branding
    draw.line([(60, 585), (1140, 585)], fill=(30, 41, 59), width=2)
    
    # Footer Left: Author & Role
    draw.text((60, 600), "Efrain Rivas", fill=(255, 255, 255), font=font_footer_bold)
    draw.text((195, 600), "|   Senior Cloud & Systems Architect", fill=(148, 163, 184), font=font_footer)
    
    # Footer Right: GitHub Handle
    draw.text((950, 600), "github.com/digdast", fill=accent, font=font_footer)
    
    # Save Image
    out_filename = f"post_day_{pid:02d}.png"
    out_path = os.path.join(GRAPHICS_DIR, out_filename)
    img.save(out_path, "PNG")
    print(f"[OK] Generated {out_filename}")

print(f"Successfully generated all {len(posts)} social graphics in {GRAPHICS_DIR}")
