# Mrudu brand kit (lean)

"Mrudu" is a **placeholder** until a trademark search clears it. Everything below survives a rename: the name is one text element in `wordmark.svg`; the icon has no name in it.

**Idea:** the hardness test strip is the brand. Magenta pad = hard, green pad = softer (the colours real total-hardness strips use). We look like a measuring instrument, not a spa.

**Positioning (internal):** For Bangalore homes on hard borewell water, Mrudu is the shower softener you can check with a strip.
**Tagline (public, already approved as A-HL2):** A shower softener you can test.

**Brand words:** Measured · Plain · Local.

## Tone of voice
| Do | Don't |
|---|---|
| "Dip a strip before and after. Compare the colour." | "Transform your shower experience." |
| "₹1,999 incl. all taxes and the first cartridge." | "Just ₹1,999!" / "Only a few left" |
| "Results depend on your water." | "Soft water every day" / "lasts 2–3 months" |
| "That white crust is limescale." | "Do you have hard water damage?" |
| Say the number, or `[TO BE MEASURED]`. | "Softer hair and skin", "No.1", any health outcome |
Sentence case. No exclamation marks. No em dashes in ads.

## Colour (WCAG contrast computed, AA = 4.5:1 normal text, 3:1 large text/graphics)
| Name | Hex | Use | Contrast |
|---|---|---|---|
| Borewell ink | `#14232E` | Text, dark bands | 14.2 on Limestone, 16.0 on white: AA |
| Limestone | `#EEF2F1` | Page background | (background) |
| Slate | `#3E5260` | Secondary text | 7.2 on Limestone: AA |
| Resin teal | `#0D5C63` | Buttons, links, unit end caps | white on it 7.7; on Limestone 6.8: AA |
| Hard pad | `#B4346C` | Strip "hard" colour, accents | 5.1 on Limestone, white on it 5.8: AA |
| Soft pad | `#2F8F6B` | Strip "softer" colour, **graphics only** | 4.0 on white: **fails text AA**; passes 3:1 graphics |
| Soft text | `#1F6B4F` | Green text when needed | 5.7 on Limestone, 6.4 on white: AA |
| Placeholder amber | `#8A4B00` | `[TO BE MEASURED]` tags, internal only | 6.0 on Limestone: AA |
Rules: `#C9D3D2` (light grey, on Ink 10.5). Never put magenta text on Ink (2.8: fails).

## Type (both SIL Open Font License 1.1, Google Fonts `ofl/` repo)
- **Bricolage Grotesque** 700 (600 for subheads): wordmark, headlines, price. Tight tracking (−0.02em).
- **Atkinson Hyperlegible** 400/700: body, captions, labels. Built for legibility; good for ppm numbers on small phones.
- Fallback: `system-ui, 'Segoe UI', sans-serif`. Scale: 17px body, ×1.25 steps (21 / 27 / 34 / 42+).

## Logo usage
- `wordmark.svg` (strip mark + lowercase name), `icon.svg` (strip on Ink, favicon and Meta page profile).
- Clear space = strip width on all sides. Min width: wordmark 96px, icon 16px.
- On dark: change the text fill to Limestone `#EEF2F1`. Keep the strip white with both pads.
- Don't: recolour or reorder the pads, add shadows or gradients, set it on a busy photo without a solid band, or caption the mark as a reading. It is a symbol, not a result.
- Before launch, outline the wordmark text (font-independent) once the name is final.

## Imagery
Our own photos first (`images.md`). `product-render.svg` until then, always labelled "Illustration". Stock only for mood, never as our product or result. No people's skin or hair. No illustrated results.

## Compliance check (`test-plan.md` §9: C1 personal attribute · C2 health · C3 before/after body · C4 measurable only · C5 fake proof · C6 fake urgency · C7 price incl. taxes · C8 substantiation)
| Item | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |
|---|---|---|---|---|---|---|---|---|
| Positioning line | P | P | P | P* | P | P | N/A | P* |
| Tagline "A shower softener you can test." | P | P | P | P | P | P | N/A | P |
| Tone do-lines | P | P | P | P | P | P | P | P |
| Wordmark / icon (strip mark) | P | P | P | P | P | P | N/A | P |
| `product-render.svg` (labelled illustration, unused strip, no result) | P | P | P | P | P | P | N/A | P* |
| Mockup A hook "Same shower. 30 seconds apart." | P | P | P | P* | P | P | P | P* |
| Mockup B hook "Chlorine filter or hardness softener?" | P | P | P | P | P | P | P | P |
| Mockup C hook "Same soap. 10 shakes each." | P | P | P | P* | P | P | P | P* |
| Mockup D hook "That white crust is limescale." + scale drawing | P | P | P | P | P | P | P | P |
| Price band "₹1,999 incl. all taxes. Refundable pre-order." | P | P | P | P | P | P | P | P |
| End card "Ships by [SHIP DATE]" | P | P | P | P | P | P | P | P* |
**0 fails.** P* = passes only once our own measured test fills it (cartridge-capacity curve, real footage, strip quantity in box, ship date). Mockup visuals are placeholders and carry a visible "Placeholder" tag; none may run as an ad. Primary texts and headlines are unchanged from `creatives.md` and keep their §9 results.
