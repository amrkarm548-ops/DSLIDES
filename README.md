# Goiter — Complete Medical Presentation

This branch packages the existing presentation so it can be run locally without changing the slide files themselves.

## Run it
1. Download the ZIP archive for the `goiter-presentation-ready` branch and extract it.
2. Open `index.html` in a modern browser (Chrome or Edge recommended).
3. Use **Prev / Next**, the keyboard arrows, Page Up / Page Down, Space, Home / End, or Fullscreen.

## What was preserved
- The slide HTML, stylesheet, manifest, and image files are reused from the original commit as the same Git blobs; only their folder locations are arranged into `slides/` and `assets/` so the relative paths resolve correctly.
- The original `main` branch is unchanged.
- The launcher has navigation only; it does not rewrite the content or styling of the slides.
- The stylesheet imports Google Fonts online; without internet, the presentation falls back to the font families already specified in the stylesheet.
