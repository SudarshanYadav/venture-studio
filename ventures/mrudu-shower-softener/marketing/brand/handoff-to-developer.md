# Handoff to Developer: apply the Mrudu brand kit to `landing/index.html`

1. Colours: your `:root` tokens already match the kit. Only change: any green **text** uses `#1F6B4F` (`#2F8F6B` is 4.0:1, graphics only). Keep `--cta:#0D5C63`.
2. Fonts: load Google Fonts `Bricolage Grotesque` (600, 700; `opsz` axis) and `Atkinson Hyperlegible` (400, 700) with `display=swap`; both SIL OFL.
3. Apply: `h1, h2, h3, .price strong, .brand` use Bricolage Grotesque, letter-spacing -0.02em; `body` uses Atkinson Hyperlegible; keep `system-ui` fallbacks.
4. Header: replace the text link `.brand` with `<img src="brand/wordmark.svg" alt="Mrudu" height="36">` (copy `wordmark.svg`, `icon.svg`, `product-render.svg` from `marketing/brand/` to `landing/brand/`). Inside an `<img>` the SVG can't load webfonts, so it shows the fallback font until the text is outlined.
5. Favicon: `<link rel="icon" href="brand/icon.svg" type="image/svg+xml">`; also give Razorpay `image:` the icon if it accepts SVG, else skip.
6. Hero: keep your strip illustration and its "not a measured result" caption. Add `product-render.svg` in the "What you get" section with caption "Illustration. Final unit may look different."
7. Replace the render with our own photo (shot list #1 in `images.md`) as soon as it exists.
8. No stock images on the page without CEO approval of a specific URL from `images.md`.
9. Re-check contrast and the 375px screenshot after the font swap (Bricolage is wider than system-ui; watch the h1 wrap).
10. Source files: `marketing/brand/`. Name "Mrudu" is a placeholder; the wordmark has one text element to swap.
