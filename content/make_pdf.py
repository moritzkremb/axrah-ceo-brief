from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
from reportlab.lib.enums import TA_LEFT, TA_CENTER

INPUT = "/home/user/axrah-ceo-brief/content/2026-06-18-fda-pbm-carousel.md"
OUTPUT = "/home/user/axrah-ceo-brief/content/2026-06-18-axrah-carousel-brief.pdf"

AXRAH_RED = colors.HexColor("#C8102E")
DARK_BG   = colors.HexColor("#1A1A1A")
MID_GREY  = colors.HexColor("#555555")
LIGHT_GREY= colors.HexColor("#AAAAAA")

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=2.2*cm, rightMargin=2.2*cm,
    topMargin=2.2*cm, bottomMargin=2.2*cm,
    title="AXRAH × Alere MD — Instagram Carousel Brief",
    author="AXRAH"
)

styles = getSampleStyleSheet()

def style(name, **kw):
    s = ParagraphStyle(name, **kw)
    return s

S_doc_title = style("doc_title",
    fontName="Helvetica-Bold", fontSize=20, leading=26,
    textColor=AXRAH_RED, spaceAfter=4)

S_doc_sub = style("doc_sub",
    fontName="Helvetica", fontSize=10, leading=14,
    textColor=LIGHT_GREY, spaceAfter=2)

S_meta = style("meta",
    fontName="Helvetica", fontSize=8, leading=12,
    textColor=MID_GREY, spaceAfter=16)

S_slide_num = style("slide_num",
    fontName="Helvetica-Bold", fontSize=9, leading=12,
    textColor=AXRAH_RED, spaceBefore=18, spaceAfter=2)

S_slide_title = style("slide_title",
    fontName="Helvetica-Bold", fontSize=15, leading=20,
    textColor=colors.HexColor("#111111"), spaceAfter=6)

S_label = style("label",
    fontName="Helvetica-Bold", fontSize=8, leading=10,
    textColor=AXRAH_RED, spaceBefore=10, spaceAfter=3)

S_body = style("body",
    fontName="Helvetica", fontSize=10, leading=16,
    textColor=colors.HexColor("#222222"), spaceAfter=6)

S_editor = style("editor",
    fontName="Helvetica-Oblique", fontSize=9, leading=13,
    textColor=colors.HexColor("#0055AA"), spaceAfter=4,
    borderPad=6, backColor=colors.HexColor("#EEF3FA"),
    borderColor=colors.HexColor("#0055AA"), borderWidth=0.5)

S_prompt = style("prompt",
    fontName="Helvetica-Oblique", fontSize=9, leading=13,
    textColor=colors.HexColor("#333333"), spaceAfter=4,
    backColor=colors.HexColor("#F5F5F5"),
    borderColor=colors.HexColor("#CCCCCC"), borderWidth=0.5,
    borderPad=6)

S_caption_head = style("caption_head",
    fontName="Helvetica-Bold", fontSize=12, leading=16,
    textColor=colors.HexColor("#111111"), spaceBefore=20, spaceAfter=6)

S_hashtag = style("hashtag",
    fontName="Helvetica", fontSize=9, leading=14,
    textColor=MID_GREY, spaceAfter=4)

def rule(color=AXRAH_RED, thickness=1.5):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=10, spaceBefore=4)

def thin_rule():
    return HRFlowable(width="100%", thickness=0.4, color=colors.HexColor("#DDDDDD"), spaceAfter=8, spaceBefore=2)

story = []

# ── Document header ──────────────────────────────────────────────────────────
story.append(Paragraph("AXRAH × Alere MD", S_doc_title))
story.append(Paragraph("Instagram Carousel — Creative Brief", S_doc_sub))
story.append(Paragraph(
    "Date: June 18, 2026   ·   Version: v3   ·   Audience: Clinic owners, medical directors, medspa operators",
    S_meta))
story.append(rule())

# ── Slides ───────────────────────────────────────────────────────────────────
slides = [
    {
        "num": "SLIDE 1 — HOOK / COVER",
        "headline": "AXRAH × Alere MD.",
        "subhead": "Clinical photobiomodulation just landed in Houston.\nAnd the FDA just validated every reason why.",
        "visual": "Split logo lockup — AXRAH × Alere MD on dark background. Red accent line between names. Houston, TX below. Partnership drop aesthetic.",
        "prompt": (
            "A stark typographic partnership announcement card on a near-black background. "
            "Left: 'AXRAH' in bold modern white sans-serif. Center: a thin vertical red glowing line. "
            "Right: 'Alere MD' in matching weight. Below both: 'Houston, TX' in small spaced caps. "
            "Bottom micro-text: 'Clinical photobiomodulation.' No photography. No icons. "
            "Aesthetic: Supreme × Nike collab drop crossed with a medical device press release. Confident. Minimal. Premium."
        ),
        "editor": "If there is a title card or logo reveal moment in today's video, grab that frame. Otherwise use the AI prompt for a designed card.",
    },
    {
        "num": "SLIDE 2 — THE CONTEXT (FDA as setup)",
        "headline": "This week, the FDA authorized photobiomodulation as medicine.",
        "subhead": "Not wellness. Not alternative therapy. Medicine.",
        "body": (
            "The FDA cleared PBM as the first non-invasive treatment for dry AMD — "
            "age-related macular degeneration affecting 20 million Americans.\n\n"
            "The same technology. The same wavelengths. The same mechanism AXRAH has been delivering to clinics since day one.\n\n"
            "Alere MD didn't wait for the FDA to say yes."
        ),
        "visual": "Editorial slide. 'FDA AUTHORIZED' stamp graphic top corner. Body text left-aligned. Clinical white on dark.",
        "prompt": (
            "Documentary-style editorial layout on deep charcoal. Upper right corner: circular red stamp graphic "
            "reading 'FDA AUTHORIZED' in block caps, slightly rotated like a government document seal. "
            "Left-aligned white text body on dark. Faint red horizontal rule separating headline from body. "
            "Serious, authoritative, slightly urgent. AXRAH wordmark bottom right."
        ),
        "editor": "No video frame needed here — designed typographic slide works best.",
    },
    {
        "num": "SLIDE 3 — WHO IS ALERE MD",
        "headline": "Alere MD isn't a wellness boutique.",
        "body": (
            "They're a clinical practice in Houston — one of the largest medical markets in the United States, "
            "home to the Texas Medical Center, the world's largest medical complex.\n\n"
            "When a Houston clinic adopts a technology, the medical community notices.\n\n"
            "AXRAH is their photobiomodulation partner."
        ),
        "visual": "Houston map with glowing red pin. Alere MD name prominent. Credibility signals, not branding.",
        "prompt": (
            "Sleek data-card layout with dark map background showing Houston, Texas, single glowing red location pin. "
            "Foreground: clean white card with 'Alere MD — Houston, TX' in bold. Below: 'Texas Medical Center. "
            "World's largest medical complex.' Pitch deck company profile aesthetic. "
            "Understated. Geographic. Medical. Faint AXRAH red line element bottom left corner."
        ),
        "editor": "If today's video includes any footage at Alere MD's location, or any exterior/interior clinic shots — grab a clean still frame here. This is the strongest slide for real-world footage.",
    },
    {
        "num": "SLIDE 4 — THE SCIENCE (AXRAH owns this)",
        "headline": "Why wavelength selection is everything.",
        "body": (
            "Red and near-infrared light penetrate tissue and activate cytochrome c oxidase — "
            "the enzyme that drives ATP production in your mitochondria.\n\n"
            "More ATP. Less inflammation. Faster repair.\n\n"
            "AXRAH Pod Ultra delivers 5 clinical wavelengths:\n"
            "633 · 660 · 810 · 850 · 940nm\n\n"
            "Not chosen for marketing. Chosen because the clinical literature says these are the frequencies "
            "that trigger the biological response.\n\n"
            "This is what Alere MD is now delivering to their patients."
        ),
        "visual": "Wavelength spectrum visualization. 5 labeled lines at exact nm positions. Dark, scientific. AXRAH × Alere MD co-branded strip at bottom.",
        "prompt": (
            "Precise scientific data visualization on pure black. The EM spectrum from 600nm–1000nm as a horizontal gradient bar — "
            "deep crimson at 600nm fading to invisible near-infrared on the right. "
            "Five sharp white vertical lines at 633nm, 660nm, 810nm, 850nm, 940nm — each labeled in monospaced white type, "
            "each with a small glowing halo in the corresponding color. "
            "Aesthetic: spectrometer readout / oscilloscope display. Clinical. Data-driven. Authoritative. Zero decorative elements."
        ),
        "editor": "If today's video shows the Pod Ultra interior with LEDs active, grab a close-up frame of the red light array — layer it as a background with the wavelength data overlaid as text. Otherwise use the AI prompt.",
    },
    {
        "num": "SLIDE 5 — MARKET SIGNAL",
        "headline": "32% of US adults have tried or plan to try red light therapy.",
        "subhead": "They've already listened to Huberman. They know Bryan Johnson's protocol.",
        "body": (
            "They're walking into clinics and asking for it by name.\n\n"
            "The clinics with AXRAH have the answer.\n"
            "The ones without it are sending patients somewhere else."
        ),
        "visual": "'32%' dominant. Patient-demand flow below: Patient asks → Clinic has AXRAH → Session booked. AXRAH red throughout.",
        "prompt": (
            "Bold infographic poster on dark charcoal. '32%' massive in upper two-thirds, glowing gradient deep red to white "
            "as if the number itself emits red light. Below in clean white sans-serif: "
            "'of US adults have tried or plan to try red light therapy.' "
            "Bottom: three-step horizontal flow diagram in red — person icon → clinic with red cross icon → calendar booking icon — "
            "connected by thin red arrows. No stock photography. Minimal. Data-first."
        ),
        "editor": "No specific video frame needed here — designed stat card works best for this slide.",
    },
    {
        "num": "SLIDE 6 — THE HARDWARE",
        "headline": "This is what Alere MD is running.",
        "body": (
            "AXRAH Pod Ultra\n"
            "→ 43,200 LEDs\n"
            "→ 5 wavelengths (633 / 660 / 810 / 850 / 940nm)\n"
            "→ 6,000W output\n"
            "→ 129 mW/cm² irradiance\n\n"
            "Priced at approximately 1/3 of NovoTHOR and TheraLight.\n\n"
            "Clinical-grade output. Without the clinical-grade price tag."
        ),
        "visual": "Pod Ultra product shot from within, glowing red. Spec list overlaid left. 'This is what Alere MD is running' turns the spec sheet into proof, not a brochure.",
        "prompt": (
            "High-end product launch photograph of the AXRAH Pod Ultra. Open, shot from 3/4 angle in a dark clinical studio. "
            "Interior glows with deep red and crimson light, casting a soft halo on polished floor. "
            "Left side: semi-transparent dark panel with spec lines in monospaced white text — "
            "'43,200 LEDs / 5 Wavelengths / 6,000W / 129 mW/cm²', each separated by fine red rules. "
            "Pod hardware is the visual hero. Shot quality: Apple product reveal. Cinematic. Zero lifestyle elements."
        ),
        "editor": "PRIORITY slide for real footage. Pull the cleanest, most cinematic frame of the Pod Ultra from today's video — ideally a slow push-in or overhead shot of the pod interior lit up. If there's a beauty shot of the LED array, use that. Overlay the spec list as text on the left side.",
    },
    {
        "num": "SLIDE 7 — THE FOMO SLIDE",
        "headline": "Alere MD is first in Houston.",
        "subhead": "Who's first in your market?",
        "body": (
            "The FDA just gave every medical director in the country cover to say yes to PBM.\n\n"
            "The clinics moving now — before their competitors do — are the ones that will own this "
            "category locally for years.\n\n"
            "AXRAH works with medical spas, PT practices, chiropractic offices, sports performance "
            "facilities, and hotels across the USA, Germany, and Austria."
        ),
        "visual": "US map, Houston glowing red, other major cities shown as dim unlit dots. 'Your city next?' implied. Urgency without pressure.",
        "prompt": (
            "Dark minimal map of the continental United States. Dark charcoal with subtle state borders. "
            "Single intense red glow pulses from Houston, Texas — signal radiating outward. "
            "Surrounding major cities (NY, LA, Chicago, Miami, Dallas, Phoenix, Denver, Atlanta) as small dim white dots — unlit. "
            "Feels like a satellite network map or breaking-news geographic alert. "
            "Clean label: 'Houston — DONE' in red beneath the glow. Other city dots unlabeled. "
            "Implication: this is spreading and these spots are open."
        ),
        "editor": "No video frame needed — designed map graphic. If you have footage of Tiger or the team with Alere MD leadership (handshake, walkthrough, anything collaborative), that's a strong alternate for this slide.",
    },
    {
        "num": "SLIDE 8 — CTA",
        "headline": "Book your clinic consultation.",
        "body": (
            "We'll walk you through the Pod Ultra specs, floor plan requirements, ROI model, and financing options.\n\n"
            "No fluff. One call.\n\n"
            "→ Link in bio"
        ),
        "visual": "Pod Ultra in a clinical room, open, ready. AXRAH wordmark centered. CTA button readable. Landing page feel, not a social post.",
        "prompt": (
            "Architectural interior photograph of a premium medical wellness room. White walls, polished concrete floor, "
            "recessed ceiling lighting. AXRAH Pod Ultra open in center, glowing deep red, casting crimson pool on floor. "
            "Wide slightly elevated angle — room looks ready, operational. "
            "Mood: real clinic space, not a render. 'Book your consultation.' in clean white type at bottom. "
            "AXRAH wordmark above it. Subtle 'Link in bio →' CTA. No people. No lifestyle. Serious business."
        ),
        "editor": "Best slide for a wide establishing shot from today's video — any frame showing the Pod Ultra in situ inside a clinical space. If there's a slow dolly or walk-through in the video, grab the frame where the pod is most prominently framed in the room. This is your closing visual — make it the best frame from the shoot.",
    },
]

for slide in slides:
    block = []
    block.append(Paragraph(slide["num"], S_slide_num))
    block.append(rule(AXRAH_RED, 1.2))
    block.append(Paragraph(slide["headline"], S_slide_title))
    if slide.get("subhead"):
        for line in slide["subhead"].split("\n"):
            if line.strip():
                block.append(Paragraph(line.strip(), style("sub2", fontName="Helvetica-BoldOblique",
                    fontSize=10, leading=14, textColor=colors.HexColor("#444444"), spaceAfter=4)))
    if slide.get("body"):
        block.append(Spacer(1, 4))
        for para in slide["body"].split("\n\n"):
            lines = para.strip()
            if lines:
                block.append(Paragraph(lines.replace("\n", "<br/>"), S_body))

    block.append(Paragraph("VISUAL DIRECTION", S_label))
    block.append(Paragraph(slide["visual"], S_body))

    block.append(Paragraph("AI IMAGE PROMPT", S_label))
    block.append(Paragraph(slide["prompt"], S_prompt))

    block.append(Paragraph("✏  EDITOR NOTE", S_label))
    block.append(Paragraph(slide["editor"], S_editor))

    block.append(thin_rule())
    story.append(KeepTogether(block[:4]))  # keep num + rule + headline together
    story.extend(block[4:])
    story.append(Spacer(1, 6))

# ── Caption ───────────────────────────────────────────────────────────────────
story.append(rule())
story.append(Paragraph("CAPTION", S_slide_num))
story.append(rule(AXRAH_RED, 1.2))
caption_text = (
    "Announcing our clinical partnership with Alere MD in Houston, Texas.<br/><br/>"
    "The same week the FDA authorized photobiomodulation as the first non-invasive treatment for dry AMD — "
    "one of the most credibility-defining moments in the history of this technology — Alere MD moved first "
    "in one of the largest medical markets in the country.<br/><br/>"
    "That's not coincidence. That's what it looks like when a clinic stops waiting and starts leading.<br/><br/>"
    "43,200 LEDs. 5 wavelengths. 129 mW/cm² irradiance. Clinical-grade PBM at approximately 1/3 the price "
    "of the closest competitor.<br/><br/>"
    "If you run a clinic, medspa, sports performance facility, or hotel wellness program and you've been "
    "thinking about full-body photobiomodulation — this is the moment.<br/><br/>"
    "Link in bio → book a consultation."
)
story.append(Paragraph(caption_text, S_body))

# ── Hashtags ──────────────────────────────────────────────────────────────────
story.append(Spacer(1, 10))
story.append(Paragraph("HASHTAGS", S_label))
story.append(Paragraph(
    "#AXRAH #AlereMD #Photobiomodulation #PBM #RedLightTherapy #FDAauthorized #ClinicalPBM "
    "#HoustonTX #TexasMedicalCenter #MedicalSpa #SportsMedicine #RecoveryTech #WellnessTech "
    "#PodUltra #BiohackingScience #LightTherapy #ClinicalWellness #HealthTech #MedSpa #Partnership",
    S_hashtag))

doc.build(story)
print(f"PDF created: {OUTPUT}")
