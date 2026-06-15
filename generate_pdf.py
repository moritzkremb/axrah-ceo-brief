from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

OUTPUT = "/home/user/axrah-ceo-brief/AXRAH_Carousel_Script.pdf"

DARK   = colors.HexColor("#0a0a0a")
RED    = colors.HexColor("#c0392b")
WHITE  = colors.HexColor("#ffffff")
GREY   = colors.HexColor("#888888")
LGREY  = colors.HexColor("#cccccc")
BGPAGE = colors.HexColor("#0f0f0f")

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=22*mm,
    rightMargin=22*mm,
    topMargin=20*mm,
    bottomMargin=20*mm,
)

W, H = A4

def page_bg(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(BGPAGE)
    canvas.rect(0, 0, W, H, fill=1, stroke=0)
    canvas.restoreState()

styles = getSampleStyleSheet()

def s(name, parent="Normal", **kw):
    return ParagraphStyle(name, parent=styles[parent], **kw)

cover_title  = s("cover_title",  fontSize=26, leading=32, textColor=WHITE,  fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=4)
cover_sub    = s("cover_sub",    fontSize=11, leading=16, textColor=RED,     fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=2)
cover_meta   = s("cover_meta",   fontSize=9,  leading=14, textColor=GREY,    fontName="Helvetica",      alignment=TA_CENTER)

slide_num    = s("slide_num",    fontSize=8,  leading=12, textColor=RED,     fontName="Helvetica-Bold", spaceBefore=18, spaceAfter=2)
slide_title  = s("slide_title",  fontSize=16, leading=22, textColor=WHITE,   fontName="Helvetica-Bold", spaceAfter=6)
body         = s("body",         fontSize=10, leading=16, textColor=LGREY,   fontName="Helvetica",      spaceAfter=4)
body_bold    = s("body_bold",    fontSize=10, leading=16, textColor=WHITE,   fontName="Helvetica-Bold", spaceAfter=4)
img_label    = s("img_label",    fontSize=8,  leading=12, textColor=RED,     fontName="Helvetica-Bold", spaceBefore=10, spaceAfter=2)
img_body     = s("img_body",     fontSize=9,  leading=14, textColor=GREY,    fontName="Helvetica-Oblique", spaceAfter=2)
caption_hd   = s("caption_hd",  fontSize=13, leading=18, textColor=WHITE,   fontName="Helvetica-Bold", spaceBefore=14, spaceAfter=6)
caption_body = s("caption_body", fontSize=10, leading=16, textColor=LGREY,   fontName="Helvetica",      spaceAfter=4)
hashtag      = s("hashtag",      fontSize=9,  leading=14, textColor=GREY,    fontName="Helvetica",      spaceAfter=2)
section_hd   = s("section_hd",  fontSize=11, leading=16, textColor=RED,     fontName="Helvetica-Bold", spaceBefore=20, spaceAfter=6)

def rule():
    return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#333333"), spaceAfter=6, spaceBefore=6)

def red_rule():
    return HRFlowable(width="100%", thickness=1, color=RED, spaceAfter=8, spaceBefore=0)

story = []

# ── COVER PAGE ───────────────────────────────────────────────────────────────
story.append(Spacer(1, 30*mm))
story.append(Paragraph("AXRAH", cover_title))
story.append(Paragraph("Instagram Carousel Script", cover_sub))
story.append(Spacer(1, 4*mm))
story.append(red_rule())
story.append(Spacer(1, 2*mm))
story.append(Paragraph("“They’re All Using It. Here’s What Actually Delivers.”", s("qt", fontSize=13, leading=18, textColor=WHITE, fontName="Helvetica-BoldOblique", alignment=TA_CENTER)))
story.append(Spacer(1, 6*mm))
story.append(Paragraph("8 Slides · Copy + Image Prompts · June 2026", cover_meta))
story.append(Spacer(1, 8*mm))
story.append(rule())
story.append(Spacer(1, 4*mm))

meta_data = [
    ["FORMAT",   "8-slide Instagram carousel"],
    ["ANGLE",    "Social proof → science → spec reality → AXRAH wins"],
    ["ICP",      "Gym owners · Clinic directors · Sports performance teams"],
    ["PRODUCT",  "AXRAH Chamber · AXRAH Chamber Ultra"],
]
tbl = Table(meta_data, colWidths=[40*mm, 120*mm])
tbl.setStyle(TableStyle([
    ("TEXTCOLOR",   (0,0), (-1,-1), GREY),
    ("TEXTCOLOR",   (0,0), (0,-1), RED),
    ("FONTNAME",    (0,0), (0,-1), "Helvetica-Bold"),
    ("FONTNAME",    (1,0), (1,-1), "Helvetica"),
    ("FONTSIZE",    (0,0), (-1,-1), 9),
    ("LEADING",     (0,0), (-1,-1), 14),
    ("ROWBACKGROUNDS", (0,0), (-1,-1), [colors.HexColor("#161616"), colors.HexColor("#111111")]),
    ("LEFTPADDING",  (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ("TOPPADDING",   (0,0), (-1,-1), 6),
    ("BOTTOMPADDING",(0,0), (-1,-1), 6),
]))
story.append(tbl)

# ── SLIDES ───────────────────────────────────────────────────────────────────
slides = [
    {
        "num": "SLIDE 01",
        "title": "COVER",
        "copy": [
            ("normal", "Bryan Johnson. Andrew Huberman. Dave Asprey."),
            ("normal", ""),
            ("normal", "Three of the most followed names in human optimization all use red light therapy."),
            ("normal", ""),
            ("bold",   "Here's what they're using it for — and what device actually delivers."),
        ],
        "img": "Minimalist dark background (#0a0a0a). Three names stacked vertically in bold white sans-serif type, large. A single narrow vertical beam of deep red light (#c0392b) running down the center of the frame. No photos, no faces. Bottom-right corner: AXRAH logo in small white. Cinematic, editorial feel.",
    },
    {
        "num": "SLIDE 02",
        "title": "THE SCIENCE",
        "copy": [
            ("normal", "2026 peer-reviewed research confirmed it:"),
            ("normal", ""),
            ("bold",   "Athletes recover 47% faster with photobiomodulation."),
            ("normal", ""),
            ("normal", "Faster return to peak performance. Less soreness. Accelerated tissue repair."),
            ("normal", ""),
            ("normal", "This isn't biohacking. It's mitochondrial biology."),
        ],
        "img": "Dark background. The number \"47%\" in oversized bold white type, centered and dominant — takes up most of the frame. Below it in smaller type: \"faster recovery.\" Subtle red glow emanating from behind the text. Clean, no clutter. Scientific but bold. AXRAH logo small bottom-right.",
    },
    {
        "num": "SLIDE 03",
        "title": "BRYAN JOHNSON",
        "copy": [
            ("normal", "Bryan Johnson uses full-body red light therapy"),
            ("bold",   "3x per week. 12 minutes per session."),
            ("normal", ""),
            ("normal", "It's part of his non-negotiable recovery stack — alongside sleep, nutrition, and biomarker tracking."),
            ("normal", ""),
            ("normal", "He doesn't guess. He protocols."),
        ],
        "img": "Dark background. Top label in small caps: \"BRYAN JOHNSON / BLUEPRINT PROTOCOL\". Center of frame: \"3x per week. 12 min.\" in oversized white type — the stat is the visual. Below in smaller grey type: \"Full-body photobiomodulation.\" Thin red horizontal rule separating the stat from the label. Minimal, data-card aesthetic.",
    },
    {
        "num": "SLIDE 04",
        "title": "HUBERMAN",
        "copy": [
            ("normal", "Andrew Huberman has dedicated multiple podcast episodes to photobiomodulation — covering how red and near-infrared light supports neuronal function, tissue repair, and cellular energy output."),
            ("normal", ""),
            ("normal", "9 million people heard it."),
            ("bold",   "The category exploded."),
        ],
        "img": "Dark background. Abstract audio waveform graphic in muted red across the center of the frame, like a podcast soundwave. Above it in small caps: \"HUBERMAN LAB.\" Below it, large white type: \"9 million listeners.\" Clean editorial layout. No faces. AXRAH logo small bottom-right.",
    },
    {
        "num": "SLIDE 05",
        "title": "THE PROBLEM",
        "copy": [
            ("bold",   "Most red light devices on the market deliver 40–60 mW/cm²."),
            ("normal", ""),
            ("normal", "The clinical research behind the 47% recovery stat was conducted at"),
            ("bold",   "100 mW/cm² and above."),
            ("normal", ""),
            ("normal", "You're not getting the protocol. You're getting the aesthetic."),
        ],
        "img": "Dark background, split layout. Left side: \"40–60 mW/cm²\" in large grey type with a red diagonal strikethrough. Right side: \"100+ mW/cm²\" in bright white type, clean. Small label above left: \"consumer devices.\" Small label above right: \"clinical threshold.\" A thin vertical red line divides the two halves. Bold, confrontational contrast.",
    },
    {
        "num": "SLIDE 06",
        "title": "AXRAH CHAMBER ULTRA",
        "copy": [
            ("bold",   "129 mW/cm²"),
            ("normal", "43,200 LEDs"),
            ("normal", "5 wavelengths: 633 · 660 · 810 · 850 · 940nm"),
            ("normal", "Full body. One session."),
            ("normal", ""),
            ("normal", "Built for clinics. Priced for reality."),
        ],
        "img": "Full-bleed dramatic product shot of the AXRAH Chamber Ultra — low angle, dark studio environment, deep red light emanating from inside the chamber. Specs overlaid in clean white type on the left side: \"129 mW/cm² · 43,200 LEDs · 5 Wavelengths.\" Bottom-left: \"AXRAH Chamber Ultra.\" No background noise — just the product and the numbers. Premium, clinical, powerful.",
    },
    {
        "num": "SLIDE 07",
        "title": "THE PRICE ARGUMENT",
        "copy": [
            ("normal", "NovoTHOR — approx. $65,000"),
            ("normal", "TheraLight — approx. $45,000–$85,000"),
            ("normal", ""),
            ("bold",   "AXRAH Chamber Ultra — $24,999"),
            ("normal", ""),
            ("normal", "Same clinical irradiance threshold."),
            ("normal", "One third of the price."),
            ("bold",   "The math is the pitch."),
        ],
        "img": "Dark background. Three-line price comparison stacked vertically, centered. \"NovoTHOR — ~$65,000\" in small grey type. \"TheraLight — ~$45,000–$85,000\" in small grey type. \"AXRAH Chamber Ultra — $24,999\" in large bold white type with a solid red underline beneath it. Below in small italic grey: \"Same clinical irradiance. One third of the price.\" Nothing else on the slide.",
    },
    {
        "num": "SLIDE 08",
        "title": "CTA",
        "copy": [
            ("normal", "Your clients are already looking for this."),
            ("normal", "Bryan Johnson proved the demand. Huberman built the audience. The research validated the outcomes."),
            ("normal", ""),
            ("bold",   "You just need the right device."),
            ("normal", ""),
            ("bold",   "→ Book a spec call. Link in bio."),
        ],
        "img": "Clean dark background with a very subtle deep red gradient vignette at the edges. Center: AXRAH logo, larger than usual. Below it: \"Book a spec call.\" in white. Below that in smaller grey: \"Link in bio.\" Bottom of frame: website URL. Calm, premium close — feels like a luxury brand card, not a sales slide.",
    },
]

for i, slide in enumerate(slides):
    story.append(Spacer(1, 6*mm))
    story.append(rule())
    story.append(Paragraph(slide["num"], slide_num))
    story.append(Paragraph(slide["title"], slide_title))

    story.append(Paragraph("COPY", section_hd))
    for kind, line in slide["copy"]:
        if line == "":
            story.append(Spacer(1, 2*mm))
        elif kind == "bold":
            story.append(Paragraph(line, body_bold))
        else:
            story.append(Paragraph(line, body))

    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("IMAGE PROMPT", img_label))
    story.append(Paragraph(slide["img"], img_body))

# ── CAPTION ──────────────────────────────────────────────────────────────────
story.append(Spacer(1, 8*mm))
story.append(rule())
story.append(Paragraph("CAPTION", caption_hd))

caption_paras = [
    "Bryan Johnson uses it 3x a week. Huberman spent multiple episodes explaining why. Dave Asprey's been ahead of it for years.",
    "",
    "The science isn't new. The pricing finally is.",
    "",
    "AXRAH Chamber Ultra. 129 mW/cm². 43,200 LEDs. 5 wavelengths. Full-body coverage.",
    "",
    "$24,999 — where the competition starts at $45,000.",
    "",
    "Built for clinics, gyms, and performance facilities. Book a spec call → link in bio.",
]
for p in caption_paras:
    if p == "":
        story.append(Spacer(1, 2*mm))
    else:
        story.append(Paragraph(p, caption_body))

story.append(Spacer(1, 6*mm))
story.append(Paragraph("HASHTAGS", img_label))
story.append(Paragraph(
    "#RedLightTherapy #Photobiomodulation #BryanJohnson #HubermanLab #AXRAH "
    "#RecoveryScience #PBM #PerformanceClinic #ClinicalRecovery #MedSpa #GymOwner #BiohackingScience",
    hashtag
))

# ── BUILD ─────────────────────────────────────────────────────────────────────
doc.build(story, onFirstPage=page_bg, onLaterPages=page_bg)
print(f"PDF written to {OUTPUT}")
