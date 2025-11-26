# Teahose Design System

Vintage 1950s comic book aesthetic with warm aged paper and bold pop art accents.

## Color Palette

### Base Colors
```css
--background: #f7f4f0        /* Warm aged cream paper */
--card: #fffefa              /* Warm white cards */
--foreground: #1a1a1a        /* True black text */
--border: #1a1a1a            /* Black borders */
```

### Accent Colors (Bold Pop Art)
```css
--comic-red: #c41e3a         /* Cardinal red */
--comic-yellow: #f4c430      /* Golden yellow */
--comic-blue: #2d5a7b        /* Deep blue */
--comic-teal: #457b7b        /* Secondary blue-green */
```

### Tints (Subtle card variants)
```css
--card-red: #fdf5f5          /* Soft red tint */
--card-yellow: #fffcf0       /* Soft yellow tint */
--card-blue: #f5f8fa         /* Soft blue tint */
--card-cream: #f5f0e8        /* Cream */
```

## Typography

### Headings
- **Transform**: UPPERCASE
- **Weight**: 700 (h1, h2), 600 (h3, h4)
- **Letter spacing**: -0.01em
- **Style**: Bold, condensed, newspaper-like

### Body
- **Font**: Geist sans-serif
- **Color**: #1a1a1a (true black)
- **Line height**: 1.75

## Visual Elements

### Borders
- **Width**: 3px
- **Color**: Black (#1a1a1a)
- **Style**: Solid, sharp corners (no border radius)

### Shadows
- **Comic shadow**: 4px 4px 0 #1a1a1a
- **Card hover**: 6px 6px 0 #1a1a1a
- **Button press**: Translates element, reduces shadow

### Background Pattern
- **Halftone dots**: Subtle 4px grid
- **Color**: rgba(0, 0, 0, 0.04)
- **Effect**: Aged newspaper texture

### Interactive States
- **Card hover**: Lifts up (-2px, -2px) with extended shadow
- **Button hover**: Translates (2px, 2px), reduces shadow
- **Button active**: Translates (4px, 4px), removes shadow

## Image Generation

All comic images (daily digest, weekly summary) should use:

### Style Guide
```
BACKGROUND: Warm aged cream paper (#f7f4f0) with subtle halftone dots
BORDERS: Thick black outlines (3px) around all panels
COLORS: Cardinal red (#c41e3a), golden yellow (#f4c430), deep blue (#2d5a7b)
SHADOWS: Black comic drop shadows
TEXTURE: Ben Day halftone dots, stipple patterns
TEXT: UPPERCASE bold sans-serif labels
```

### Color Usage
- **Panel backgrounds**: Rotate soft tints (red/yellow/blue/cream)
- **Main elements**: Use bold accent colors
- **Overall base**: Warm cream throughout
- **Borders**: Always thick black

## Components

### Cards
```css
background: var(--card)
border: 3px solid var(--border)
box-shadow: 4px 4px 0 #1a1a1a
transition: all 0.2s ease
```

### Buttons
```css
Primary: Red background, black border, uppercase
Secondary: White background, black border, uppercase
Both: 3px borders, comic shadow, press effect
```

### Utility Classes
- .dots-pattern - Halftone background
- .text-comic-shadow - Comic text shadow
- .halftone - Image halftone effect
- .card-[red|yellow|blue|cream] - Tinted cards

## Brand Voice

**Aesthetic**: Vintage 1950s newspaper comic section meets modern tech content
**Tone**: Warm, approachable, nostalgic yet sophisticated
**Contrast**: Soft cream base with punchy accent colors when needed

## Files

- app/globals.css - Main stylesheet with all design tokens
- generate_daily_email.py - Daily digest image prompt (line ~205)
- test_daily_email.py - Test email image prompt (line ~211)
- generate_weekly_header_image.py - Weekly summary image prompt (line ~127)

## Consistency

All Nano Banana Pro image generation prompts now match this design system:
- Warm cream background (#f7f4f0)
- Bold red/yellow/blue accents
- Thick black borders
- Halftone texture
- UPPERCASE text

This creates visual consistency between the website and all generated imagery.
