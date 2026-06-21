# AXRAH CEO Brief

Daily executive intelligence brief for the AXRAH CEO (Tiger).

## What this does

Every morning, produce a concise, actionable brief that synthesizes:
1. Social media trend data (from the scraper repo)
2. Email inbox (Gmail MCP)
3. Web research (industry news, competitor moves)

Then turn it into decisions and team directives — not a data dump.

## How to run

1. Fetch the latest trend data from:
   ```
   https://raw.githubusercontent.com/moritzkremb/axrah-trend-scraper/main/outputs/latest.md
   ```
2. Check Gmail for emails from the last 24 hours — look for client inquiries, order notifications, partnership requests, competitor mentions, anything business-relevant
3. Run web searches for: "red light therapy news", "photobiomodulation industry news", "NovoTHOR", "TheraLight", "AXRAH" — look for breaking developments
4. Synthesize everything into the brief format below
5. Write the brief to `briefs/YYYY-MM-DD.md` (today's date)
6. Also write to `briefs/latest.md` (overwrite)
7. Commit and push with message: "Daily CEO brief — YYYY-MM-DD"
8. Output the full brief in the chat so Tiger can read it immediately

## Brief format

```markdown
# AXRAH CEO Brief — [Date]

## Urgent / Action Required
[Anything needing same-day attention — client issues, time-sensitive opportunities, problems]

## Industry & Market
[Key developments in red light therapy, photobiomodulation, wellness tech, regulatory changes]

## Competitor Intelligence
[NovoTHOR, TheraLight, Prism Light Pod, Joovv, Mito Red — moves, pricing, products, partnerships]

## Content & Social Trends
[What's trending in AXRAH's categories. What angles get engagement. What people ask/complain about]

## Influencer & Creator Signals
[What Huberman, Asprey, Greenfield, Bryan Johnson, etc. are posting. Podcast mentions, collaborations]

## Team Directives

### Marketing
[What to post, respond to, or capitalize on]

### Sales
[Leads to prioritize, objections surfacing, market signals for outreach]

### Product
[Feature requests, unmet needs, development priorities]

### Operations
[Supply chain, fulfillment, support issues]

### Business Development
[Partnership opportunities, events, collaborations to pursue]

## Key Links & Sources
[Links to the most important items mentioned above]
```

## Business context

AXRAH is a red light therapy / photobiomodulation device company.

- **Products:** Panel ($449), Panel Pro ($1,999), Grid ($1,999), Chamber ($14,999), Chamber Ultra ($24,999)
- **Positioning:** Clinical-grade PBM at 1/3 to 1/5 competitor pricing
- **Markets:** USA, Germany, Austria
- **Sales model:** Primarily B2B (clinics, gyms, sports teams, hotels)
- **Key competitors:** NovoTHOR ($65K+), TheraLight ($45-85K+), Prism Light Pod ($35K+), Joovv (panels only)
- **Differentiator:** Chamber Ultra — 43,200 LEDs, 5 wavelengths (633/660/810/850/940nm), 6,000W, 129 mW/cm²
- **Target ICPs:** Medical spas, gyms/fitness, chiropractic/PT, sports teams, hotels/resorts
- **Key metric:** 32% of US adults have tried or plan to try RLT
- **Market:** RLT beds $8.21B (2025) → $19.30B by 2032 (13% CAGR)

### Products in development (do NOT mention to prospects):
- Lounger ($34,999) — luxury reclining system
- Halo ($349) — hair loss cap
- SkinIQ ($69) — skin diagnostic device

### Competitor pricing is estimated — always use "approximately" or "estimated"

## Tone

Direct, concise, CEO-level. No fluff. Lead with what matters, what changed, and what to do about it. Tiger is a founder who wants signal, not noise.

## Required connections

- Gmail MCP (for inbox scanning)
- WebSearch / WebFetch (for industry news)
