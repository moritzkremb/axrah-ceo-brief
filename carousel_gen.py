from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import textwrap

# Square slide dimensions — Instagram 1:1
W = 6.5 * inch
H = 6.5 * inch

OUTPUT = "/home/user/axrah-ceo-brief/AXRAH_IG_Carousel_2026-06-21.pdf"

# Brand colors
BLACK      = colors.HexColor("#0A0A0A")
WHITE      = colors.HexColor("#FFFFFF")
RED        = colors.HexColor("#D63B2F")
LIGHT_GRAY = colors.HexColor("#AAAAAA")
DARK_GRAY  = colors.HexColor("#1C1C1C")
MID_GRAY   = colors.HexColor("#333333")
CREAM      = colors.HexColor("#F5F0EB")

c = canvas.Canvas(OUTPUT, pagesize=(W, H))

def bg(fill=BLACK):
    c.setFillColor(fill)
    c.rect(0, 0, W, H, fill=1, stroke=0)

def rule(y, color=RED, width=W*0.08, thickness=2):
    c.setStrokeColor(color)
    c.setLineWidth(thickness)
    c.line(0.45*inch, y, 0.45*inch + width, y)

def label(text, x, y, size=7, color=RED, tracking=2.5):
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", size)
    c.drawString(x, y, text.upper())

def headline(text, x, y, size=28, color=WHITE, width=W - 0.9*inch, leading=34):
    lines = []
    words = text.split()
    line = ""
    for w in words:
        test = (line + " " + w).strip()
        c.setFont("Helvetica-Bold", size)
        if c.stringWidth(test, "Helvetica-Bold", size) <= width:
            line = test
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)

    c.setFillColor(color)
    for i, l in enumerate(lines):
        c.setFont("Helvetica-Bold", size)
        c.drawString(x, y - i * leading, l)
    return y - len(lines) * leading

def body(text, x, y, size=12, color=LIGHT_GRAY, width=W - 0.9*inch, leading=18):
    lines = text.split("\n")
    c.setFillColor(color)
    c.setFont("Helvetica", size)
    cur_y = y
    for line in lines:
        if line.strip() == "":
            cur_y -= leading * 0.6
            continue
        # wrap
        wrapped = []
        words = line.split()
        cur = ""
        for w in words:
            test = (cur + " " + w).strip()
            if c.stringWidth(test, "Helvetica", size) <= width:
                cur = test
            else:
                wrapped.append(cur)
                cur = w
        if cur:
            wrapped.append(cur)
        for wl in wrapped:
            c.drawString(x, cur_y, wl)
            cur_y -= leading
    return cur_y

def stat_line(text, x, y, size=13, color=WHITE):
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", size)
    c.drawString(x, y, text)
    return y - 22

def image_prompt_box(prompt_text, y_top):
    # Draw a subtle box for the image prompt
    margin = 0.45 * inch
    box_h = 1.15 * inch
    box_y = y_top - box_h
    c.setFillColor(DARK_GRAY)
    c.setStrokeColor(MID_GRAY)
    c.setLineWidth(0.5)
    c.roundRect(margin, box_y, W - 2*margin, box_h, 6, fill=1, stroke=1)

    label("IMAGE DIRECTION", margin + 10, box_y + box_h - 14, size=6, color=RED)

    # wrap prompt text
    c.setFillColor(LIGHT_GRAY)
    c.setFont("Helvetica-Oblique", 8)
    x = margin + 10
    y = box_y + box_h - 26
    words = prompt_text.split()
    line = ""
    lines = []
    max_w = W - 2*margin - 20
    for w in words:
        test = (line + " " + w).strip()
        if c.stringWidth(test, "Helvetica-Oblique", 8) <= max_w:
            line = test
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    for l in lines[:5]:
        c.drawString(x, y, l)
        y -= 11

def slide_number(n, total=8):
    c.setFillColor(LIGHT_GRAY)
    c.setFont("Helvetica", 7.5)
    c.drawRightString(W - 0.45*inch, 0.32*inch, f"{n} / {total}")

def axrah_bug(corner="br"):
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 8)
    if corner == "br":
        c.drawRightString(W - 0.45*inch, H - 0.38*inch, "AXRAH")
    else:
        c.drawString(0.45*inch, H - 0.38*inch, "AXRAH")

# ─────────────────────────────────────────────
# SLIDE 1 — HOOK
# ─────────────────────────────────────────────
bg()
axrah_bug()
slide_number(1)

label("Red Light Therapy", 0.45*inch, H - 0.75*inch)

y = H - 1.15*inch
y = headline("Bryan Johnson spends $2M/year optimizing his body.", 0.45*inch, y, size=23, leading=30)
y -= 0.18*inch
y = headline("Red light therapy is in his daily protocol.", 0.45*inch, y, size=23, leading=30)
y -= 0.28*inch
rule(y + 0.05*inch)
y -= 0.22*inch
body("Here's what it looks like when you scale that\nto clinical grade.", 0.45*inch, y, size=13, color=WHITE, leading=20)

image_prompt_box(
    "Dark cinematic split-screen. Left: single consumer RLT panel, warm red glow, slightly underexposed. "
    "Right: interior of a glowing full-body clinical device, rich red and near-infrared light flooding every surface. "
    "No logos. White sans-serif text overlay, bottom-left. High contrast. Editorial quality.",
    1.55*inch
)

c.showPage()

# ─────────────────────────────────────────────
# SLIDE 2 — BRYAN'S DAILY STACK
# ─────────────────────────────────────────────
bg()
axrah_bug()
slide_number(2)

label("His Protocol", 0.45*inch, H - 0.75*inch)
y = H - 1.1*inch
y = headline("Bryan Johnson's daily\nRLT stack.", 0.45*inch, y, size=26, leading=32)
y -= 0.25*inch
rule(y + 0.05*inch)
y -= 0.28*inch

items = [
    ("○  Laser cap", "6 min  ·  scalp"),
    ("○  Face panel", "Celluma Pro  ·  daily"),
    ("○  Full-body panels", "12 min  ·  3× per week"),
    ("○  FlexBeam", "targeted recovery  ·  as needed"),
]
for title, detail in items:
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.45*inch, y, title)
    c.setFillColor(LIGHT_GRAY)
    c.setFont("Helvetica", 11)
    c.drawString(0.45*inch, y - 14, detail)
    y -= 38

y -= 0.05*inch
body("4 devices. Multiple sessions. Every single day.", 0.45*inch, y, size=11, color=RED, leading=17)

image_prompt_box(
    "Clean flat-lay on matte black. Four devices arranged symmetrically: laser cap at top, small face panel, "
    "two vertical panels flanking center, curved targeted device at bottom. Soft red-toned product lighting. "
    "Minimalist white text labels. High-end editorial — not an ad.",
    1.55*inch
)

c.showPage()

# ─────────────────────────────────────────────
# SLIDE 3 — THE GAP
# ─────────────────────────────────────────────
bg()
axrah_bug()
slide_number(3)

label("The Problem", 0.45*inch, H - 0.75*inch)
y = H - 1.1*inch
y = headline("Consumer panels are built\nfor bedrooms.", 0.45*inch, y, size=26, leading=32)
y -= 0.22*inch
rule(y + 0.05*inch)
y -= 0.28*inch
body("If you're running a clinic, medspa, or gym —\nyou need a different conversation entirely.", 0.45*inch, y, size=13, color=WHITE, leading=20)
y -= 0.65*inch

specs = ["Irradiance.", "Wavelengths.", "Sessions per day.", "Durability."]
for s in specs:
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.45*inch, y, s)
    y -= 20

y -= 0.1*inch
body("These numbers determine your ROI.", 0.45*inch, y, size=12, color=LIGHT_GRAY, leading=18)

image_prompt_box(
    "A lone consumer RLT panel propped against a clinical treatment room wall — slightly out of place, small. "
    "Harsh overhead clinical lighting making it look inadequate. Room is professional — tiled, clean, equipment-ready. "
    "Visual tension intentional. No text overlay.",
    1.55*inch
)

c.showPage()

# ─────────────────────────────────────────────
# SLIDE 4 — WHAT CLINICAL GRADE MEANS
# ─────────────────────────────────────────────
bg()
axrah_bug()
slide_number(4)

label("Clinical Grade", 0.45*inch, H - 0.75*inch)
y = H - 1.1*inch
y = headline("Clinical grade isn't a\nmarketing term.\nIt's a spec sheet.", 0.45*inch, y, size=22, leading=28)
y -= 0.28*inch
rule(y + 0.05*inch)
y -= 0.28*inch

specs = [
    ("43,200", "LEDs"),
    ("5", "wavelengths  ·  633 / 660 / 810 / 850 / 940nm"),
    ("6,000W", "output"),
    ("129 mW/cm²", "irradiance"),
    ("360°", "full-body coverage"),
]
for num, desc in specs:
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 14)
    tw = c.stringWidth(num, "Helvetica-Bold", 14)
    c.drawString(0.45*inch, y, num)
    c.setFillColor(LIGHT_GRAY)
    c.setFont("Helvetica", 11)
    c.drawString(0.45*inch + tw + 8, y, desc)
    y -= 26

y -= 0.1*inch
body("Every cell. Every session.", 0.45*inch, y, size=12, color=RED, leading=18)

image_prompt_box(
    "Dark background, data-visualization aesthetic. Human body silhouette at center glowing faintly with five "
    "colored light rays penetrating at different depths — each wavelength in its actual color. Numbers and "
    "wavelength labels float around the figure in clean type. Clinical, scientific, beautiful.",
    1.55*inch
)

c.showPage()

# ─────────────────────────────────────────────
# SLIDE 5 — THE MATH
# ─────────────────────────────────────────────
bg()
axrah_bug()
slide_number(5)

label("The ROI", 0.45*inch, H - 0.75*inch)
y = H - 1.1*inch
y = headline("The math your\naccountant will like.", 0.45*inch, y, size=26, leading=32)
y -= 0.22*inch
rule(y + 0.05*inch)
y -= 0.3*inch

rows = [
    ("$50 – $200", "per client session"),
    ("8 sessions / day", "standard clinic schedule"),
    ("5 days / week", "operating baseline"),
    ("$104K – $416K", "annual revenue from one device"),
]
for val, desc in rows:
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.45*inch, y, val)
    c.setFillColor(LIGHT_GRAY)
    c.setFont("Helvetica", 10)
    c.drawString(0.45*inch, y - 14, desc)
    y -= 38

# divider line
c.setStrokeColor(MID_GRAY)
c.setLineWidth(0.5)
c.line(0.45*inch, y + 4, W - 0.45*inch, y + 4)
y -= 16

body("Equipment cost pays itself back in weeks, not years.", 0.45*inch, y, size=12, color=RED, leading=18)

image_prompt_box(
    "Minimal white background. Clean table in black and brand-red. Three columns: Sessions/Day, Price/Session, "
    "Annual Revenue. Numbers large and bold. Equipment cost appears small at the bottom as a reference line. "
    "Design: Bloomberg terminal meets luxury spa brochure.",
    1.55*inch
)

c.showPage()

# ─────────────────────────────────────────────
# SLIDE 6 — THE COMPARISON
# ─────────────────────────────────────────────
bg()
axrah_bug()
slide_number(6)

label("Competitor Watch", 0.45*inch, H - 0.75*inch)
y = H - 1.1*inch
y = headline("The market leader just received\nan FDA Class 2 recall.", 0.45*inch, y, size=22, leading=28)
y -= 0.22*inch
rule(y + 0.05*inch)
y -= 0.28*inch

left_x = 0.45*inch
mid = W / 2 + 0.1*inch

# Competitor column
c.setFillColor(LIGHT_GRAY)
c.setFont("Helvetica-Bold", 9)
c.drawString(left_x, y, "COMPETITOR")
c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 17)
c.drawString(left_x, y - 22, "~$75K–$95K")
c.setFillColor(RED)
c.setFont("Helvetica", 10)
c.drawString(left_x, y - 38, "FDA Class 2 Recall")
c.setFillColor(LIGHT_GRAY)
c.setFont("Helvetica", 10)
c.drawString(left_x, y - 52, "Gen 3.0 whole-body pod")

# Divider
c.setStrokeColor(MID_GRAY)
c.setLineWidth(0.8)
c.line(mid - 15, y + 10, mid - 15, y - 65)

# AXRAH column
c.setFillColor(LIGHT_GRAY)
c.setFont("Helvetica-Bold", 9)
c.drawString(mid, y, "AXRAH")
c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 17)
c.drawString(mid, y - 22, "$24,999")
c.setFillColor(colors.HexColor("#4CAF50"))
c.setFont("Helvetica", 10)
c.drawString(mid, y - 38, "No recall")
c.setFillColor(LIGHT_GRAY)
c.setFont("Helvetica", 10)
c.drawString(mid, y - 52, "5 wavelengths  ·  43,200 LEDs")

y -= 90
body("The math writes itself.", 0.45*inch, y, size=13, color=WHITE, leading=18)

image_prompt_box(
    "Two columns, stark contrast. Left: muted gray, silhouetted competing device, small red 'recall' badge, "
    "large price figure. Right: full color AXRAH clinical system interior glowing warm, $24,999 bold and clean. "
    "Balanced composition, right side radiates warmth and authority. No competitor logos.",
    1.55*inch
)

c.showPage()

# ─────────────────────────────────────────────
# SLIDE 7 — MARKET PROOF
# ─────────────────────────────────────────────
bg()
axrah_bug()
slide_number(7)

label("Market Size", 0.45*inch, H - 0.75*inch)
y = H - 1.1*inch
y = headline("Your clients are already\nasking for this.", 0.45*inch, y, size=26, leading=32)
y -= 0.22*inch
rule(y + 0.05*inch)
y -= 0.3*inch

stats = [
    ("32%", "of US adults have tried or plan to try RLT"),
    ("$8.2B", "RLT bed market today"),
    ("$19.3B", "projected by 2032  ·  13% CAGR"),
    ("11.9%", "annual growth in clinical pod segment"),
]
for num, desc in stats:
    c.setFillColor(RED)
    c.setFont("Helvetica-Bold", 20)
    nw = c.stringWidth(num, "Helvetica-Bold", 20)
    c.drawString(0.45*inch, y, num)
    c.setFillColor(LIGHT_GRAY)
    c.setFont("Helvetica", 11)
    c.drawString(0.45*inch + nw + 10, y - 3, desc)
    y -= 32

y -= 0.05*inch
body("The question is whether they find it at your clinic.", 0.45*inch, y, size=12, color=WHITE, leading=18)

image_prompt_box(
    "Editorial lifestyle photography. Diverse range: athlete mid-stretch, woman in medspa robe, older man with "
    "reading glasses — each in a separate minimal frame in a 3-panel grid. Warm red ambient light touches each image. "
    "Bold single-line stat in white text over solid dark band below.",
    1.55*inch
)

c.showPage()

# ─────────────────────────────────────────────
# SLIDE 8 — CTA
# ─────────────────────────────────────────────
bg()
axrah_bug()
slide_number(8)

label("Ready to run the numbers?", 0.45*inch, H - 0.75*inch)
y = H - 1.15*inch
y = headline("If you run a clinic, gym,\nmedspa, or recovery center —", 0.45*inch, y, size=22, leading=28)
y -= 0.22*inch
rule(y + 0.05*inch)
y -= 0.28*inch
body("and you're serious about adding full-body\nred light therapy to your offering —", 0.45*inch, y, size=13, color=WHITE, leading=20)
y -= 0.65*inch

# CTA box
box_h = 0.65*inch
c.setFillColor(RED)
c.roundRect(0.45*inch, y - box_h + 0.15*inch, W - 0.9*inch, box_h, 8, fill=1, stroke=0)
c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 15)
cta = 'DM us "SYSTEM" for your custom ROI breakdown.'
c.drawCentredString(W/2, y - box_h/2 - 3, cta)

y -= box_h + 0.2*inch
body("No pitch. Just numbers.", 0.45*inch, y, size=12, color=LIGHT_GRAY, leading=18)

image_prompt_box(
    "Full-bleed shot from client perspective — lying inside the clinical device, looking up through open canopy "
    "at ceiling of LEDs glowing in red and near-infrared. Intimate, aspirational, slightly cinematic. "
    'The word "SYSTEM" appears in minimal white type, center-bottom. Nothing else.',
    1.45*inch
)

c.showPage()

# ─────────────────────────────────────────────
# CAPTION PAGE
# ─────────────────────────────────────────────
bg(DARK_GRAY)
axrah_bug("tl")

y = H - 0.7*inch
label("Instagram Caption", 0.45*inch, y)
y -= 0.35*inch
rule(y + 0.05*inch, width=W*0.15)
y -= 0.35*inch

caption_lines = [
    "Bryan Johnson built a $2M annual health stack",
    "around red light therapy.",
    "",
    "For clinics, the math looks very different.",
    "",
    "Swipe to see what clinical-grade PBM actually",
    "delivers — and why the market is moving fast. ↓",
]
for line in caption_lines:
    if line == "":
        y -= 10
        continue
    c.setFillColor(WHITE)
    c.setFont("Helvetica", 12)
    c.drawString(0.45*inch, y, line)
    y -= 18

y -= 0.25*inch
hashtags = "#RedLightTherapy #Photobiomodulation #MedSpa #ClinicalWellness"
hashtags2 = "#BiohackingBusiness #WellnessIndustry #RLT #BryanJohnson"
hashtags3 = "#LongevityMedicine #SportsRecovery #AXRAH"
for h in [hashtags, hashtags2, hashtags3]:
    c.setFillColor(LIGHT_GRAY)
    c.setFont("Helvetica", 9)
    c.drawString(0.45*inch, y, h)
    y -= 14

y -= 0.4*inch
label("Posting Notes", 0.45*inch, y)
y -= 0.28*inch
notes = [
    "· Slide 6 (recall) requires legal sign-off before publishing.",
    "· Set up 'SYSTEM' DM auto-reply in ManyChat before going live.",
    "· Best window: Tue–Thu, 8–10am in primary market timezone (EST).",
    "· DM keyword triggers sales qualification sequence.",
]
for note in notes:
    c.setFillColor(LIGHT_GRAY)
    c.setFont("Helvetica", 10)
    c.drawString(0.45*inch, y, note)
    y -= 16

c.save()
print(f"Saved: {OUTPUT}")
