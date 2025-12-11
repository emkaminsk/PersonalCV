# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**PersonalCV** is a monorepo containing two distinct CV presentation formats:

1. **HTML CV Website** (root directory) - A responsive, modern web-based CV with theme switching and optimized performance
2. **Awesome CV LaTeX Template** (`awesome-CV/` directory) - A LaTeX-based template for professional résumés and cover letters

The projects share the same content but target different delivery methods: web presentation vs. PDF documents.

## Architecture & Technology

### HTML CV Website (Root)
**Tech Stack**: HTML5, CSS3, ES6+ JavaScript, Pico CSS Framework
**Purpose**: Public-facing web CV with responsive design, dark/light theme switching, and social media integration

- **Entry Point**: `index.html` - Main CV webpage with semantic markup
- **Styling**: `custom.css` - Custom styles with CSS Grid/Flexbox, CSS variables, and responsive breakpoints
- **Interactivity**: `js/minimal-theme-switcher.js` - Theme persistence using localStorage
- **Assets**: `img/` (images), `icons/` (SVG social media icons)
- **Image Optimization**: `optimize-images.js` - Node.js script using Sharp library for batch image processing

**Key Architectural Features**:
- **Two-column layout**: Hero + navigation (sticky), main content with right sidebar (desktop only)
- **Responsive breakpoints**: Desktop → Tablet → Mobile (sidebar hidden on mobile)
- **CSS Variables**: Color theme defined in `:root` for consistent theming
- **Accessibility**: Semantic HTML, ARIA attributes, focus styles, sufficient color contrast
- **Performance**: External CSS/JS, image optimization pipeline, minimal dependencies via CDN

### Awesome CV LaTeX (awesome-CV/)
**Purpose**: LaTeX template for PDF-based résumés, CVs, and cover letters
**Build System**: Makefile with xelatex compilation

- **Main Class**: `awesome-cv.cls` - LaTeX document class (30KB) defining all styles and commands
- **Examples**: `examples/` directory with modular content structure
- **Personal Documents**: `myCV/` directory for user-specific CV files
- **Build Artifacts**: Generated PDFs stored alongside source `.tex` files

## Common Development Commands

### HTML CV Website
```bash
# Start local development server (port 8080)
npm run start

# Optimize all images in img/ directory
npm run optimize-images

# Run placeholder test (no actual tests configured)
npm test
```

### Awesome CV LaTeX
```bash
# Compile all examples (resume.pdf, cv.pdf, coverletter.pdf)
cd awesome-CV && make examples

# Compile single document
cd awesome-CV && xelatex -output-directory=examples examples/resume.tex

# Clean generated PDFs
cd awesome-CV && make clean

# Docker-based build (no TeX installation needed)
cd awesome-CV && docker run --rm --user $(id -u):$(id -g) -i -w "/doc" -v "$PWD":/doc texlive/texlive:latest make
```

## Project Structure

```
PersonalCV/
├── index.html                          # Main CV webpage
├── error404.html                       # Custom 404 page
├── custom.css                          # Main stylesheet with responsive design
├── optimize-images.js                  # Image optimization script
├── package.json                        # Dependencies: sharp, http-server
├── sandbox.config.json                 # CodeSandbox configuration
│
├── js/
│   └── minimal-theme-switcher.js      # Dark/light theme toggle with localStorage
│
├── icons/
│   ├── facebook.svg, github.svg, linkedin.svg, x.svg
│
├── img/
│   ├── MK03.jpg                        # Profile photo
│   └── sascha-eremin-*.jpg             # Hero background image
│
├── awesome-CV/                         # LaTeX template subdirectory
│   ├── awesome-cv.cls                  # LaTeX document class
│   ├── Makefile                        # Build automation
│   ├── README.md                       # Template documentation
│   ├── examples/
│   │   ├── resume.tex, cv.tex, coverletter.tex
│   │   ├── resume/, cv/                # Modular content sections
│   │   └── (symlink to awesome-cv.cls)
│   ├── myCV/
│   │   └── cv.tex                      # Personal CV document
│   └── .github/workflows/              # CI/CD for LaTeX compilation
│
├── .cursor/rules/                      # Cursor IDE rules (HTML, CSS, accessibility, etc.)
├── .ai/                                # Documentation from previous implementation sessions
│
└── .github/
    └── workflows/                      # (If present) GitHub Actions for deployment
```

## Key Customization Points

### HTML CV - Styling & Theme
**CSS Variables** (in `custom.css` `:root`):
- `--text-color` / `--bg-color` - Text and background colors
- `--accent-color` - Primary highlight color for links, buttons, hover states
- Light/dark theme variants defined in separate rule sets activated by `data-theme` attribute

**Responsive Breakpoints** (media queries in `custom.css`):
- Desktop: 1024px+ (2-column with sidebar)
- Tablet: 768px-1023px (reduced sidebar, adjusted spacing)
- Mobile: <768px (hidden sidebar, stacked layout)

### HTML CV - Content Structure
Edit `index.html` sections:
- **Hero Section**: Name, title, navigation links, background image
- **About Me**: Summary, contact information
- **Experience**: Work history with job titles, dates, responsibilities
- **Education**: Academic background and certifications
- **Sidebar** (desktop): Technical skills, trainings, languages, interests

### HTML CV - Social Links
SVG icons in `icons/` directory linked from `index.html`. Update href attributes in social media section.

### LaTeX CV - Document Customization
**Colors** in any `.tex` document:
```latex
\colorlet{awesome}{awesome-emerald}   % Available: emerald, skyblue, red, pink, orange, nephritis, concrete, darknight
\definecolor{awesome}{HTML}{CA63A8}    % Custom hex color
```

**Personal Information** (in `.tex` documents):
```latex
\name{First}{Last}
\position{Job Title}
\email{email@example.com}
\github{username}
\linkedin{username}
```

## Development Workflow

### Working on HTML CV
1. **Local Development**: `npm run start` starts server on port 8080
2. **Editing Content**: Modify sections in `index.html` directly
3. **Styling**: Update `custom.css` (follows BEM naming conventions, uses CSS variables)
4. **Theme Testing**: Use browser DevTools to test dark/light theme switching
5. **Responsive Testing**: Use browser responsive mode or physical devices for different screen sizes
6. **Image Optimization**: Run `npm run optimize-images` before committing large images

### Working on LaTeX CV
1. **Edit Content**: Modify `.tex` files in `awesome-CV/examples/` or `awesome-CV/myCV/`
2. **Local Compile**: Use `make examples` to generate PDFs
3. **View Output**: Check generated PDFs for formatting and layout
4. **Docker Build**: Use Docker container if TeX Live not installed locally

### Image Assets
- **Profile photo** (`img/MK03.jpg`): Referenced in HTML, should be square for best appearance
- **Hero background** (`img/sascha-eremin-*.jpg`): Full-width background image, 3000x1000px recommended
- **Optimization**: Use `npm run optimize-images` to batch process before committing

## Performance Optimization

### HTML CV
- **External Resources**: Pico CSS loaded via CDN (jsdelivr), no render-blocking resources
- **Theme Switcher**: Minimal JavaScript (300 lines), runs synchronously on page load to prevent flash of unstyled content
- **Image Optimization**: Sharp library batch processes images with quality tuning
- **CSS Delivery**: Single `custom.css` file inlined or minimized in production

### Key Performance Considerations
- Sidebar hidden on mobile (reduces layout shift)
- SVG icons used instead of image files (smaller, scalable)
- CSS variables leverage browser native support (no polyfills needed)
- Focus on CSS Grid/Flexbox for modern browsers (IE11 excluded)

## Accessibility Standards

### HTML CV Compliance
- **Semantic HTML**: `<header>`, `<main>`, `<footer>`, `<nav>`, `<section>`, `<article>` landmarks
- **Color Contrast**: WCAG AA minimum (4.5:1 for text), verified in both light and dark themes
- **Keyboard Navigation**: All interactive elements accessible via Tab key
- **Focus Indicators**: Clear focus styles on links and buttons
- **ARIA Attributes**: Used where semantic HTML insufficient (e.g., nav dropdowns, theme switcher)
- **Image Alt Text**: Profile photo and background image have meaningful alt attributes

### Cursor Rules Integration
Cursor IDE rules in `.cursor/rules/` enforce:
- **HTML Semantics**: Use `<button>` for interactive elements, not `<div>`
- **CSS Best Practices**: Use external stylesheets, avoid `!important`, prefer class selectors
- **Accessibility**: Minimum color contrast, ARIA roles for complex components
- **Responsive Design**: Mobile-first media queries, flexible touch targets (48px minimum)

## Deployment & CI/CD

### GitHub Actions (LaTeX)
Located in `awesome-CV/.github/workflows/`:
- **main.yml**: Compiles LaTeX examples on every push/PR using texlive/texlive container
- **integration.yaml**: Lints YAML files using yamllint
- Generated PDFs available as workflow artifacts

### Production Deployment
According to `.ai/tech-stack.md`: Changes to main branch auto-deploy to Mikr.us server via GitHub Actions (details in workflow configuration)

## Common Editing Tasks

### Update CV Content (HTML)
1. Open `index.html` in editor
2. Find relevant section (Experience, Education, Skills, etc.)
3. Update text content, keeping HTML structure intact
4. Test responsive display at different breakpoints
5. Commit with meaningful message

### Update CV Styling (HTML)
1. Edit `custom.css` directly (no build process)
2. Use CSS variables for colors (defined at top of file)
3. Update media query breakpoints if layout needs adjustment
4. Test theme switching functionality (light/dark mode)
5. Verify accessibility with contrast checker

### Optimize Images (HTML)
1. Add new images to `img/` directory
2. Run `npm run optimize-images` to batch process
3. Commit only optimized versions (originals can be excluded via .gitignore)

### Create New LaTeX Document
1. Copy template `.tex` file from `examples/`
2. Place in new directory (e.g., `myCV/`)
3. Include desired content sections using `\input{}`
4. Run `xelatex -output-directory=<output_dir> <file>.tex`
5. Verify PDF output

## Browser & Device Support

### HTML CV
- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ⚠️ IE11 (limited theme switcher support)

**Required Features**: CSS Grid/Flexbox, CSS Custom Properties, localStorage, ES6 JavaScript

### LaTeX CVs
- Modern TeX Live distribution with xelatex
- Generated PDFs compatible with all PDF readers
- Fonts: Roboto (body), Source Sans Pro (fallback)
