# View Implementation Plan - Index View (Main CV Page)

## 1. Overview

The Index View is the main landing page and comprehensive CV display for Marcin Kamiński's personal website. This single-page application presents professional identity, work experience, education, skills, and contact information in a responsive, accessible, and performance-optimized format.

**Purpose:**
- Showcase complete professional background to recruiters and hiring managers
- Provide easy navigation through career history and qualifications
- Offer optimal viewing experience across all devices (mobile, tablet, desktop)
- Support user preferences (light/dark theme) with accessibility standards (WCAG 2.1 AA)
- Enable quick access to contact information and social media profiles

**Key Characteristics:**
- Static HTML/CSS/JavaScript implementation with no build process
- Mobile-first responsive design (320px - 2560px+ viewports)
- Fixed sidebar on desktop, collapsible accordions on mobile
- Visual timeline for work experience
- Theme switching with LocalStorage persistence
- Performance-optimized (LCP < 2.5s, FCP < 1.5s)

## 2. View Routing

**Path:** `/` or `/index.html`

**Access:**
- Direct URL access (homepage)
- Default landing page for domain
- Accessible without authentication or permissions

## 3. Component Structure

The Index View follows a vertical scroll layout with the following component hierarchy:

```
Index View
├── Skip to Content Link (hidden, keyboard accessible)
├── Hero Section
│   ├── Navigation Bar (sticky)
│   │   ├── Logo/Name Link
│   │   ├── Social Media Links (inline)
│   │   ├── Section Dropdown Menu
│   │   │   ├── Experience Link
│   │   │   ├── Education Link
│   │   │   └── Interests Link
│   │   └── Theme Toggle Button (to be added)
│   └── Hero Header
│       ├── h1: Name
│       └── h2: Professional Title/Tagline
├── Main Content Area
│   ├── About Me Section
│   │   ├── Professional Summary (text)
│   │   ├── Contact Information Block
│   │   └── Profile Image
│   ├── Experience Section
│   │   ├── Timeline Decoration (CSS-based)
│   │   └── Job Experience Cards[]
│   │       ├── Company Name
│   │       ├── Job Title
│   │       ├── Employment Dates
│   │       ├── Responsibilities List (ul/li)
│   │       └── Technologies/Tools
│   ├── Education Section
│   │   └── Education Cards[]
│   │       ├── Institution Name
│   │       ├── Degree Type
│   │       ├── Date Range
│   │       └── Specializations/Details
│   └── Interests Section
│       └── Interests Paragraph
├── Sidebar (Desktop ≥992px, Tablet 768-991px)
│   ├── Skills Section
│   ├── Technical Skills Section
│   ├── Trainings & Certifications Section
│   └── Languages Section
├── Accordion Container (Mobile <768px)
│   ├── Skills Accordion
│   ├── Technical Skills Accordion
│   ├── Trainings Accordion
│   └── Languages Accordion
├── Footer
│   ├── Social Media Icon Links
│   └── Copyright Notice
└── Back to Top Button (floating, appears on scroll)
```

**Layout Behavior:**
- **Desktop (≥992px):** Two-column layout with main content (left) and fixed sidebar (right, 550px)
- **Tablet (768-991px):** Two-column layout with reduced sidebar (200px)
- **Mobile (<768px):** Single column, sidebar content transforms to collapsible accordions below main content

## 4. Component Details

### Skip to Content Link

**Component Description:**
Accessibility feature allowing keyboard users to bypass navigation and jump directly to main content.

**Main Elements:**
- `<a>` element with `href="#main-content"`
- Visually hidden by default (CSS)
- Visible on keyboard focus
- Positioned at top of document (first focusable element)

**Handled Interactions:**
- Keyboard focus (Tab key from address bar)
- Click/Enter activation

**Handled Validation:**
None

**Types:**
None (static HTML element)

**Props:**
None (standalone element)

---

### Hero Section

**Component Description:**
Full-width section creating strong first impression with background image, professional identity, and primary navigation. Uses dark theme overlay for text contrast.

**Main Elements:**
- `<div class="hero" data-theme="dark">` - Container with background image
- Navigation bar (see Navigation Bar component)
- `<header class="container">` with `<hgroup>`
  - `<h1>` - Full name: "Personal CV page"
  - `<h2>` - Professional title: "Technical Product Owner with business and IT skills"

**Handled Interactions:**
None (static display, interactions handled by child components)

**Handled Validation:**
- Text contrast validation: Minimum 4.5:1 ratio against background
- Responsive image loading based on viewport width

**Types:**
None

**Props:**
None (top-level component)

---

### Navigation Bar

**Component Description:**
Sticky navigation providing access to sections, social media, and theme preferences. Remains visible during scroll for constant navigation access.

**Main Elements:**
- `<nav class="container-fluid">` with sticky/fixed positioning
- Logo/name link: `<a href="./">Marcin Kamiński</a>`
- Social media links (inline):
  - Facebook icon link
  - Twitter/X icon link
  - LinkedIn icon link
  - GitHub icon link
- Section dropdown: `<details role="list" dir="rtl">`
  - Summary: "Sections"
  - Listbox with section links (Experience, Education, Interests)
- Theme toggle button (to be added)

**Handled Interactions:**
- Click on logo → Scroll to top (smooth)
- Click on section link → Smooth scroll to target section with offset
- Click on social media link → Open external profile
- Click on theme toggle → Switch theme (light ↔ dark)
- Dropdown automatically closes after section selection
- Keyboard navigation (Tab, Enter, Escape)

**Handled Validation:**
- Verify section IDs exist before scrolling
- Ensure sticky position doesn't obscure content (scroll offset)
- Active section highlighting based on scroll position

**Types:**
```javascript
// Theme state
currentTheme: "light" | "dark"

// Navigation state
activeSection: "experience" | "education" | "interests" | null
```

**Props:**
None (component manages own state)

---

### Hero Header

**Component Description:**
Central header within hero section displaying name and professional title with proper heading hierarchy.

**Main Elements:**
- `<hgroup>` container
- `<h1>` - Primary heading: "Personal CV page"
- `<h2>` - Subheading: "Technical Product Owner with business and IT skills"

**Handled Interactions:**
None

**Handled Validation:**
- Heading hierarchy (single h1 on page)
- Text contrast against background
- Responsive font sizing (reduced on mobile)

**Types:**
None

**Props:**
None

---

### About Me Section

**Component Description:**
Two-column layout (desktop) introducing professional background with summary, contact information, and profile photo. Stacks vertically on mobile.

**Main Elements:**
- `<section class="about-me-section">`
- `<div class="flex-container">` - Flexbox wrapper
  - `<hgroup>` - Left column (text content)
    - `<h2>About Me</h2>`
    - `<p>` - Professional summary
    - Contact information block:
      - `<h3>Contact Information</h3>`
      - Email link: `<a href="mailto:emkaminsk@gmail.com">emkaminsk@gmail.com</a>`
  - `<figure>` - Right column (image)
    - `<img src="./img/MK03.jpg" alt="Marcin Kamiński">`
    - `<figcaption>Marcin Kamiński</figcaption>`

**Handled Interactions:**
- Click on email link → Open email client with pre-filled subject

**Handled Validation:**
- Email format validation (handled by browser)
- Image alt text present
- Responsive layout (flex-wrap on mobile)

**Types:**
```javascript
// Contact info
email: string
emailSubject: string // Pre-filled: "Inquiry from CV Website"
```

**Props:**
None

---

### Experience Section

**Component Description:**
Chronological display of work history with visual timeline, presenting jobs in reverse chronological order (newest first). Timeline simplified on mobile.

**Main Elements:**
- `<h3 id="experience">Experience</h3>` - Section heading
- Multiple `.job-experience` divs (one per job):
  - `<strong>` - Company name (bold, prominent)
  - `<span class="job-title">` - Job title
  - `<p>` - Employment dates (e.g., "August 2023 - now")
  - `<ul>` - Responsibilities list
    - `<li>` - Individual responsibilities
  - `<p>` - Tools (e.g., "Tools: VSCode, Azure DevOps, Miro")
  - `<p>` - Project technologies (e.g., "Project technologies: Java, React, Kubernetes")
- Timeline decoration (CSS ::before/::after on job-experience elements)

**Handled Interactions:**
- Scroll-based animations (optional enhancement)
- Intersection observer for fade-in effects

**Handled Validation:**
- Chronological order verification
- Visual timeline markers present (CSS)
- Responsibilities formatted as lists

**Types:**
```javascript
// Job experience structure
JobExperience {
  company: string
  title: string
  startDate: string
  endDate: string | "now"
  responsibilities: string[]
  tools: string
  technologies: string
}
```

**Props:**
None (content embedded in HTML)

---

### Education Section

**Component Description:**
Display of academic credentials and qualifications in chronological order with consistent card formatting.

**Main Elements:**
- `<h3 id="education">Education</h3>` - Section heading
- Multiple `.education-experience` divs (one per degree):
  - `<strong>` - Institution name (bold)
  - `<span class="education-title">` - Degree type (Master, eMBA, Postgraduate)
  - `<br>` - Line break
  - `<p>` - Date range
  - `<ul>` - Details/specializations
    - `<li>` - Individual details

**Handled Interactions:**
None

**Handled Validation:**
- Chronological order
- Consistent formatting with experience section

**Types:**
```javascript
// Education structure
Education {
  institution: string
  degree: string
  startDate: string
  endDate: string
  details: string[]
}
```

**Props:**
None

---

### Interests Section

**Component Description:**
Brief section humanizing the CV with personal interests and hobbies, maintaining professional tone.

**Main Elements:**
- `<h3 id="interests">Interests</h3>` - Section heading
- `<p>` - Interests paragraph (e.g., "Classical music, chess, go, podcasts, sci-fi, Vipassana.")

**Handled Interactions:**
None

**Handled Validation:**
- Keep content brief and professional
- Easy to scan

**Types:**
None

**Props:**
None

---

### Sidebar (Desktop/Tablet)

**Component Description:**
Fixed right sidebar displaying supplementary skills and qualifications. Independently scrollable on desktop. Hidden on mobile (<768px).

**Main Elements:**
- `<aside id="sidebar">` with fixed positioning
- Multiple `.sidebar-section` divs:
  1. Skills section
     - `<h4>Skills</h4>`
     - `<ul>` - Soft skills list
  2. Technical Skills section
     - `<h4>Technical Skills</h4>`
     - `<ul>` - Technical skills list
  3. Trainings section
     - `<h4>Trainings</h4>`
     - `<ul>` - Certifications list
  4. Languages section
     - `<h4>Languages</h4>`
     - `<ul>` - Languages with proficiency levels

**Handled Interactions:**
- Independent scrolling (overflow-y: auto)
- Scroll behavior independent of main content

**Handled Validation:**
- Display only on screens ≥768px
- Desktop: 550px width
- Tablet (768-991px): 200px width
- Position fixed at top: 250px, right: 0

**Types:**
```javascript
// Skill category
SkillCategory {
  title: string
  skills: string[]
}
```

**Props:**
None

---

### Accordion Container (Mobile)

**Component Description:**
Collapsible accordion panels displaying sidebar content on mobile devices. Provides same content as sidebar in mobile-friendly format. Displayed only on screens <768px.

**Main Elements:**
Four accordion items, each with:
- `<button aria-expanded="false" aria-controls="panel-id">` - Accordion header/trigger
  - Header text (e.g., "Skills")
  - Chevron/arrow icon (CSS or SVG)
- `<div id="panel-id" role="region" aria-labelledby="header-id">` - Accordion panel
  - `<ul>` - Content list (same as sidebar sections)

**Handled Interactions:**
- Click/tap on accordion header → Toggle expand/collapse
- Keyboard activation (Enter, Space)
- Multiple panels can be open simultaneously
- Smooth expand/collapse animation

**Handled Validation:**
- Display only on screens <768px
- Collapsed by default
- Proper ARIA attributes:
  - `aria-expanded`: "true" or "false"
  - `aria-controls`: Points to panel ID
  - `role="region"` on panel
  - `aria-labelledby`: Points to header ID

**Types:**
```javascript
// Accordion state
AccordionState {
  panelId: string
  isExpanded: boolean
}
```

**Props:**
None (component manages own state)

**Note:** Currently not implemented. Needs to be added.

---

### Footer

**Component Description:**
Site footer with social media links and copyright information, maintaining consistent branding.

**Main Elements:**
- `<footer class="container">`
- Social media icon links (currently in header, should be duplicated or moved to footer):
  - Facebook link with icon
  - Twitter/X link with icon
  - LinkedIn link with icon
  - GitHub link with icon
- `<small>© 2023 Marcin Kamiński</small>` - Copyright notice

**Handled Interactions:**
- Click on social media link → Open external profile in new tab

**Handled Validation:**
- All external links include `rel="noopener noreferrer"` for security
- Icon links have `aria-label` for accessibility
- Touch targets minimum 44x44px on mobile
- Keyboard accessible

**Types:**
```javascript
// Social media link
SocialMediaLink {
  platform: "Facebook" | "Twitter" | "LinkedIn" | "GitHub"
  url: string
  iconSrc: string
  ariaLabel: string
}
```

**Props:**
None

---

### Theme Toggle Button

**Component Description:**
Button in navigation bar allowing users to switch between light and dark themes. Displays icon representing current theme (sun for light, moon for dark).

**Main Elements:**
- `<button aria-label="Toggle dark mode" aria-pressed="false">` - Button element
- Icon (SVG):
  - Sun icon (☀) when in light mode
  - Moon icon (☾) when in dark mode

**Handled Interactions:**
- Click → Toggle theme (light ↔ dark)
- Keyboard activation (Enter, Space)
- Update icon based on current theme
- Update aria-pressed state

**Handled Validation:**
- ARIA attributes:
  - `aria-label`: Descriptive label
  - `aria-pressed`: "true" or "false"
- Keyboard accessible
- Focus indicator visible (2px outline)
- Smooth theme transition (0.3s)

**Types:**
```javascript
// Theme state
theme: "light" | "dark"
```

**Props:**
None (component manages theme via themeSwitcher module)

**Note:** Currently not implemented in navigation. Needs to be added.

---

### Back to Top Button

**Component Description:**
Floating button in bottom-right corner allowing quick return to top of page. Appears after scrolling past 500px, hidden when at top.

**Main Elements:**
- `<button aria-label="Back to top" class="back-to-top">` - Button element with fixed positioning
- Up arrow icon (SVG or Unicode ↑)

**Handled Interactions:**
- Scroll position >500px → Fade in
- Scroll position ≤500px → Fade out
- Click → Smooth scroll to top
- Keyboard activation (Enter, Space)

**Handled Validation:**
- Visibility based on scroll position
- ARIA label present
- Keyboard accessible
- Focus indicator visible
- Touch target minimum 44x44px on mobile
- z-index appropriate (99, below modals)
- Not in tab order when hidden (display: none)

**Types:**
```javascript
// Button state
isVisible: boolean
scrollPosition: number
```

**Props:**
None (component manages own state)

**Note:** Currently not implemented. Needs to be added.

## 5. Types

Since this is a static HTML/CSS/JavaScript project (not TypeScript or a framework), types are not explicitly defined in code. However, the following conceptual type definitions represent the data structures used in the view:

### PersonalInfo
```javascript
{
  name: "Marcin Kamiński",
  title: "Technical Product Owner",
  tagline: "Technical Product Owner with business and IT skills",
  summary: "Product Owner for IT projects with 5 years of Agile experience...",
  email: "emkaminsk@gmail.com",
  profileImage: {
    src: "./img/MK03.jpg",
    alt: "Marcin Kamiński",
    caption: "Marcin Kamiński"
  }
}
```

### JobExperience
```javascript
{
  company: string,          // e.g., "Sii Polska"
  title: string,            // e.g., "Technical Product Owner"
  startDate: string,        // e.g., "August 2023"
  endDate: string | "now",  // e.g., "now" or "July 2023"
  responsibilities: string[], // Array of responsibility descriptions
  tools: string,            // e.g., "VSCode, Azure DevOps, Miro"
  technologies: string      // e.g., "Java, React, Kubernetes"
}
```

### Education
```javascript
{
  institution: string,      // e.g., "Aalto University & WSB"
  degree: string,           // e.g., "eMBA", "Master", "Postgraduate"
  startDate: string,        // e.g., "November 2011"
  endDate: string,          // e.g., "June 2013"
  details: string[]         // Array of additional details/achievements
}
```

### SkillCategory
```javascript
{
  title: string,           // e.g., "Skills", "Technical Skills", "Trainings", "Languages"
  skills: string[]         // Array of skill descriptions
}
```

### SocialMediaLink
```javascript
{
  platform: "Facebook" | "Twitter" | "LinkedIn" | "GitHub",
  url: string,             // Full URL to profile
  iconSrc: string,         // Path to SVG icon
  ariaLabel: string        // e.g., "LinkedIn profile"
}
```

### ThemeState
```javascript
{
  current: "light" | "dark",
  preference: "light" | "dark" | "auto",
  systemPreference: "light" | "dark"
}
```

### NavigationState
```javascript
{
  activeSection: "experience" | "education" | "interests" | null,
  scrollPosition: number,
  isMenuOpen: boolean
}
```

### AccordionState
```javascript
{
  panels: {
    skills: boolean,         // true = expanded, false = collapsed
    technicalSkills: boolean,
    trainings: boolean,
    languages: boolean
  }
}
```

### ViewportState
```javascript
{
  width: number,
  breakpoint: "mobile" | "tablet" | "desktop",
  showSidebar: boolean,      // true for tablet/desktop
  showAccordions: boolean    // true for mobile
}
```

## 6. State Management

State management for this view is handled through vanilla JavaScript with browser APIs, without using a state management library or framework.

### Theme State

**Management Method:** JavaScript module (`themeSwitcher`) with LocalStorage persistence

**State Variables:**
- `_scheme`: Current theme ("light" | "dark")
- LocalStorage key: `"picoPreferredColorScheme"`

**State Initialization:**
1. Check LocalStorage for saved preference
2. If exists, use saved theme
3. If not, detect system preference (`prefers-color-scheme` media query)
4. Apply theme to `<html data-theme="light|dark">`

**State Updates:**
- User clicks theme toggle → Update `_scheme` → Save to LocalStorage → Apply to DOM
- Theme changes trigger CSS variable updates via `data-theme` attribute

**Persistence:**
- LocalStorage stores user preference
- Persists across browser sessions
- Cleared if user clears browser data

**Implementation:**
```javascript
// Existing implementation in minimal-theme-switcher.js
const themeSwitcher = {
  _scheme: "auto",
  localStorageKey: "picoPreferredColorScheme",

  init() {
    this.scheme = this.schemeFromLocalStorage;
    this.applyScheme();
  },

  set scheme(scheme) {
    // Update internal state
    // Save to LocalStorage
    // Apply to DOM
  },

  applyScheme() {
    document.querySelector("html").setAttribute("data-theme", this.scheme);
  }
}
```

### Navigation State

**Management Method:** Event listeners with DOM manipulation

**State Variables:**
- `activeSection`: Currently visible section (tracked via scroll position)
- `scrollPosition`: Current scroll offset (tracked via window.scrollY)
- `isMenuOpen`: Dropdown menu state (managed by browser via `<details>` element)

**State Updates:**
- Scroll event → Calculate active section → Update navigation highlighting
- Click on section link → Smooth scroll to section → Update active state
- Click outside dropdown or on link → Close menu

**Implementation:**
```javascript
// To be implemented
const navigationHandler = {
  activeSection: null,

  init() {
    this.observeSections();
    this.attachSectionLinks();
  },

  observeSections() {
    // Use IntersectionObserver to track visible sections
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.activeSection = entry.target.id;
          this.updateNavigation();
        }
      });
    }, { threshold: 0.5 });

    document.querySelectorAll('section[id]').forEach(section => {
      observer.observe(section);
    });
  },

  updateNavigation() {
    // Update active state on nav links
  },

  smoothScrollTo(targetId) {
    const target = document.getElementById(targetId);
    const navHeight = 80; // Height of sticky nav
    const targetPosition = target.offsetTop - navHeight;

    window.scrollTo({
      top: targetPosition,
      behavior: 'smooth'
    });
  }
}
```

### Back to Top Button State

**Management Method:** Scroll event listener with visibility toggle

**State Variables:**
- `isVisible`: Boolean indicating button visibility
- `scrollThreshold`: 500px (show button after this scroll position)

**State Updates:**
- Scroll event → Check position → Show/hide button
- Click on button → Scroll to top → Hide button

**Implementation:**
```javascript
// To be implemented
const backToTopHandler = {
  button: null,
  threshold: 500,

  init() {
    this.button = document.querySelector('.back-to-top');
    window.addEventListener('scroll', () => this.toggleVisibility());
    this.button.addEventListener('click', () => this.scrollToTop());
  },

  toggleVisibility() {
    if (window.scrollY > this.threshold) {
      this.button.classList.add('visible');
    } else {
      this.button.classList.remove('visible');
    }
  },

  scrollToTop() {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  }
}
```

### Accordion State (Mobile)

**Management Method:** Click event listeners with ARIA attribute manipulation

**State Variables:**
- Panel expansion state tracked via `aria-expanded` attribute on each button
- No centralized state object needed

**State Updates:**
- Click on accordion header → Toggle `aria-expanded` → Show/hide panel
- Update icon rotation (CSS transform based on aria-expanded)

**Implementation:**
```javascript
// To be implemented
const accordionHandler = {
  init() {
    document.querySelectorAll('[data-accordion-trigger]').forEach(button => {
      button.addEventListener('click', (e) => this.toggle(e.target));
    });
  },

  toggle(button) {
    const isExpanded = button.getAttribute('aria-expanded') === 'true';
    const panelId = button.getAttribute('aria-controls');
    const panel = document.getElementById(panelId);

    button.setAttribute('aria-expanded', !isExpanded);
    panel.style.display = isExpanded ? 'none' : 'block';
  }
}
```

### Responsive Layout State

**Management Method:** CSS media queries (no JavaScript state needed)

**Breakpoints:**
- Mobile: 0-767px → Single column, show accordions, hide sidebar
- Tablet: 768-991px → Two columns, show reduced sidebar (200px), hide accordions
- Desktop: 992px+ → Two columns, show full sidebar (550px), hide accordions

**CSS Implementation:**
```css
/* Sidebar visible on tablet/desktop */
#sidebar {
  display: block;
}

@media screen and (max-width: 768px) {
  #sidebar {
    display: none;
  }
}

/* Accordions visible on mobile */
.accordion-container {
  display: none;
}

@media screen and (max-width: 768px) {
  .accordion-container {
    display: block;
  }
}
```

### Custom Hook Equivalent (Initialization)

While this is not React, a custom "hook" pattern can be implemented as an initialization function:

```javascript
// Main initialization
document.addEventListener('DOMContentLoaded', () => {
  // Initialize theme
  themeSwitcher.init();

  // Initialize navigation
  navigationHandler.init();

  // Initialize back to top
  backToTopHandler.init();

  // Initialize accordions (mobile only)
  if (window.innerWidth < 768) {
    accordionHandler.init();
  }

  // Re-initialize on resize if crossing mobile breakpoint
  let wasMobile = window.innerWidth < 768;
  window.addEventListener('resize', () => {
    const isMobile = window.innerWidth < 768;
    if (isMobile !== wasMobile) {
      if (isMobile) {
        accordionHandler.init();
      }
      wasMobile = isMobile;
    }
  });
});
```

### State Summary

| State | Storage | Updates | Persistence |
|-------|---------|---------|-------------|
| Theme | LocalStorage + DOM attribute | Theme toggle click | Yes (LocalStorage) |
| Active Section | IntersectionObserver | Scroll, section visibility | No |
| Scroll Position | window.scrollY | Scroll event | No |
| Menu Open | `<details>` element | Click on summary/outside | No |
| Accordion Panels | aria-expanded attributes | Click on accordion header | No |
| Button Visibility | CSS class | Scroll event | No |
| Responsive Layout | CSS media queries | Window resize (automatic) | No |

## 7. API Integration

**API Integration:** None

This is a static HTML website with no backend API integration. All content is hard-coded in the HTML file and updated manually through direct HTML editing.

**Data Source:**
- Static HTML content embedded in `index.html`
- Images stored in `/img/` directory
- Icons stored in `/icons/` directory
- Styles in `custom.css`
- JavaScript utilities in `/js/minimal-theme-switcher.js`

**Content Updates:**
Content is updated by:
1. Directly editing `index.html` file
2. Modifying relevant sections (experience, education, skills, etc.)
3. Committing changes to Git repository
4. Deploying via GitHub Actions to production server (Mikr.us)

**External Resources:**
- Pico CSS Framework: `https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css` (CDN)

**Future Considerations:**
While out of scope for MVP, future versions could integrate:
- Headless CMS for easier content management
- Contact form API (Formspree, Netlify Forms)
- Analytics API (privacy-respecting analytics)

## 8. User Interactions

### 1. Section Navigation

**Interaction:** User clicks section link in navigation dropdown

**Flow:**
1. User opens section dropdown (click on "Sections")
2. User sees options: Experience, Education, Interests
3. User clicks desired section link (e.g., "Experience")
4. Page smoothly scrolls to target section
5. Scroll offset accounts for sticky navigation height (80px)
6. Dropdown menu closes automatically
7. Active section indicator updates in navigation

**Implementation Details:**
```javascript
// Attach click handlers to section links
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', (e) => {
    e.preventDefault();
    const targetId = link.getAttribute('href').substring(1);
    navigationHandler.smoothScrollTo(targetId);

    // Close dropdown (if using details/summary)
    const dropdown = link.closest('details');
    if (dropdown) dropdown.removeAttribute('open');
  });
});
```

**Expected Outcome:**
- Smooth scroll animation to target section
- Content visible below navigation (not hidden)
- Navigation dropdown closes
- User can immediately read target section

---

### 2. Theme Toggle

**Interaction:** User clicks theme toggle button to switch between light and dark modes

**Flow:**
1. User locates theme toggle button in navigation (sun/moon icon)
2. User clicks button
3. Theme switches:
   - Light → Dark: Background darkens, text lightens, icon changes to sun
   - Dark → Light: Background lightens, text darkens, icon changes to moon
4. Smooth transition animation (0.3s)
5. Preference saved to LocalStorage
6. ARIA pressed state updates

**Implementation Details:**
```javascript
// Theme toggle button handler
const themeToggleBtn = document.querySelector('[data-theme-toggle]');
themeToggleBtn.addEventListener('click', () => {
  const currentTheme = themeSwitcher.scheme;
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';

  themeSwitcher.scheme = newTheme;

  // Update button icon and aria-pressed
  updateThemeIcon(newTheme);
  themeToggleBtn.setAttribute('aria-pressed', newTheme === 'dark');
});
```

**Expected Outcome:**
- Instant theme change with smooth transition
- Icon updates to reflect new state
- Preference persists across sessions
- All content remains readable with proper contrast

---

### 3. Back to Top

**Interaction:** User clicks back-to-top button to return to page top

**Flow:**
1. User scrolls down page (>500px)
2. Back-to-top button fades in (bottom-right corner)
3. User clicks button or presses Enter/Space (if focused via keyboard)
4. Page smoothly scrolls to top
5. Button fades out when reaching top

**Implementation Details:**
```javascript
// Show/hide on scroll
window.addEventListener('scroll', () => {
  const btn = document.querySelector('.back-to-top');
  if (window.scrollY > 500) {
    btn.classList.add('visible');
  } else {
    btn.classList.remove('visible');
  }
});

// Scroll to top on click
document.querySelector('.back-to-top').addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
```

**Expected Outcome:**
- Smooth scroll to top of page
- Button becomes hidden when at top
- No content is skipped or hidden
- Keyboard accessible

---

### 4. Accordion Expand/Collapse (Mobile)

**Interaction:** User taps accordion header to expand/collapse skill sections

**Flow:**
1. User on mobile device (<768px) scrolls to accordion sections
2. All accordions collapsed by default (only headers visible)
3. User taps accordion header (e.g., "Skills")
4. Panel smoothly expands, revealing content list
5. Arrow icon rotates to indicate expanded state
6. User can expand multiple panels simultaneously
7. User taps header again to collapse panel

**Implementation Details:**
```javascript
// Accordion toggle
document.querySelectorAll('.accordion-header').forEach(header => {
  header.addEventListener('click', () => {
    const panel = header.nextElementSibling;
    const isExpanded = header.getAttribute('aria-expanded') === 'true';

    header.setAttribute('aria-expanded', !isExpanded);
    panel.style.maxHeight = isExpanded ? '0' : panel.scrollHeight + 'px';
    header.classList.toggle('expanded');
  });
});
```

**Expected Outcome:**
- Panel expands/collapses smoothly
- Content becomes visible/hidden
- Icon indicates state
- ARIA state announced to screen readers
- Multiple panels can be open

---

### 5. Social Media Link Click

**Interaction:** User clicks social media icon to visit external profile

**Flow:**
1. User locates social media icons (navigation or footer)
2. User hovers over icon → Visual feedback (color change, scale)
3. User clicks icon
4. External profile opens in new tab (if target="_blank")
5. Security attributes prevent window.opener attacks

**Implementation Details:**
```html
<a href="https://www.linkedin.com/in/marcinkaminski/"
   class="social-link"
   aria-label="LinkedIn profile"
   target="_blank"
   rel="noopener noreferrer">
  <img src="./icons/linkedin.svg" alt="LinkedIn" />
</a>
```

**Expected Outcome:**
- External profile opens in new tab
- Original CV tab remains open
- No security vulnerabilities
- Clear indication of external link

---

### 6. Email Contact Click

**Interaction:** User clicks email link to initiate contact

**Flow:**
1. User locates email in About Me section
2. User clicks email link
3. Default email client opens
4. Email address pre-populated: emkaminsk@gmail.com
5. Subject line pre-filled: "Inquiry from CV Website"
6. User can compose and send message

**Implementation Details:**
```html
<a href="mailto:emkaminsk@gmail.com?subject=Inquiry%20from%20CV%20Website">
  emkaminsk@gmail.com
</a>
```

**Expected Outcome:**
- Email client opens with pre-filled information
- User can immediately compose message
- Reduces friction for contacting

---

### 7. Logo/Name Click

**Interaction:** User clicks logo/name in navigation to return to top

**Flow:**
1. User clicks "Marcin Kamiński" link in navigation
2. Event prevented (no page reload)
3. Page smoothly scrolls to top
4. User sees hero section

**Implementation Details:**
```javascript
document.querySelector('nav a[href="./"]').addEventListener('click', (e) => {
  e.preventDefault();
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
```

**Expected Outcome:**
- Smooth scroll to top
- No page reload
- Fast navigation to beginning

---

### 8. Keyboard Navigation

**Interaction:** Keyboard user navigates site without mouse

**Flow:**
1. User presses Tab from address bar
2. Focus moves to "Skip to content" link (visible on focus)
3. User can activate (Enter) to skip to main content
4. Or continue tabbing through navigation elements
5. All interactive elements receive visible focus indicator
6. Enter/Space activates links and buttons
7. Escape closes dropdowns/menus
8. Tab order follows logical reading order

**Expected Outcome:**
- All functionality accessible via keyboard
- Focus indicators clearly visible (2px outline)
- Logical tab order
- No keyboard traps

---

### 9. Scroll-Based Active Section Highlighting

**Interaction:** Active section updates as user scrolls

**Flow:**
1. User scrolls through page
2. IntersectionObserver detects when section enters viewport
3. When section is 50% visible, it becomes "active"
4. Corresponding navigation link highlights (bold, underline, or color change)
5. Previous active link unhighlights
6. User knows current location on page

**Implementation Details:**
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // Update active navigation link
      document.querySelectorAll('nav a').forEach(link => {
        link.classList.remove('active');
      });

      const activeLink = document.querySelector(`nav a[href="#${entry.target.id}"]`);
      if (activeLink) activeLink.classList.add('active');
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('section[id]').forEach(section => {
  observer.observe(section);
});
```

**Expected Outcome:**
- Navigation reflects current position
- User orientation maintained
- Smooth visual feedback

## 9. Conditions and Validation

### Display Conditions

#### 1. Sidebar vs. Accordions Display

**Condition:** Viewport width determines which component displays

**Components Affected:**
- Sidebar (`#sidebar`)
- Accordion Container (`.accordion-container`)

**Validation Logic:**
```css
/* Desktop/Tablet: Show sidebar, hide accordions */
@media screen and (min-width: 768px) {
  #sidebar {
    display: block;
    width: 550px; /* Desktop */
  }
  .accordion-container {
    display: none;
  }
}

/* Tablet: Reduce sidebar width */
@media screen and (min-width: 768px) and (max-width: 991px) {
  #sidebar {
    width: 200px;
  }
}

/* Mobile: Hide sidebar, show accordions */
@media screen and (max-width: 767px) {
  #sidebar {
    display: none;
  }
  .accordion-container {
    display: block;
  }
}
```

**Interface Impact:**
- Desktop/Tablet: Skills always visible in sidebar
- Mobile: Skills in collapsible sections, collapsed by default

---

#### 2. Back-to-Top Button Visibility

**Condition:** Scroll position > 500px

**Component Affected:** Back-to-Top Button (`.back-to-top`)

**Validation Logic:**
```javascript
window.addEventListener('scroll', () => {
  const btn = document.querySelector('.back-to-top');
  const scrollPosition = window.scrollY;

  if (scrollPosition > 500) {
    btn.classList.add('visible'); // Fade in
    btn.style.display = 'block';
  } else {
    btn.classList.remove('visible'); // Fade out
    btn.style.display = 'none'; // Remove from tab order
  }
});
```

**Interface Impact:**
- Scroll position ≤500px: Button hidden, not in tab order
- Scroll position >500px: Button visible, focusable

---

#### 3. Theme Application

**Condition:** User preference (LocalStorage) OR system preference

**Components Affected:** All components (via CSS custom properties)

**Validation Logic:**
```javascript
// On page load
const savedTheme = localStorage.getItem('picoPreferredColorScheme');

if (savedTheme) {
  // Use saved preference
  applyTheme(savedTheme);
} else {
  // Detect system preference
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const theme = systemPrefersDark ? 'dark' : 'light';
  applyTheme(theme);
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
}
```

**Interface Impact:**
- Light theme: Light background, dark text, specific color palette
- Dark theme: Dark background, light text, adjusted colors
- Transition: 0.3s smooth animation between themes

---

#### 4. Navigation Dropdown State

**Condition:** Click on summary or outside dropdown

**Component Affected:** Section Navigation Dropdown (`<details>`)

**Validation Logic:**
```javascript
// Close dropdown after link click
document.querySelectorAll('details[role="list"] a').forEach(link => {
  link.addEventListener('click', () => {
    const details = link.closest('details');
    details.removeAttribute('open');
  });
});

// Close on outside click (optional enhancement)
document.addEventListener('click', (e) => {
  const dropdown = document.querySelector('details[role="list"]');
  if (dropdown && !dropdown.contains(e.target)) {
    dropdown.removeAttribute('open');
  }
});
```

**Interface Impact:**
- Open: Dropdown shows section links
- Closed: Dropdown hides links, shows only "Sections" label

---

#### 5. Accordion Panel Expansion

**Condition:** User clicks accordion header

**Components Affected:** Accordion panels (mobile)

**Validation Logic:**
```javascript
accordionHeader.addEventListener('click', () => {
  const isExpanded = accordionHeader.getAttribute('aria-expanded') === 'true';
  const panel = accordionHeader.nextElementSibling;

  // Toggle state
  accordionHeader.setAttribute('aria-expanded', !isExpanded);

  // Update display
  if (isExpanded) {
    panel.style.maxHeight = '0';
    panel.classList.remove('expanded');
  } else {
    panel.style.maxHeight = panel.scrollHeight + 'px';
    panel.classList.add('expanded');
  }
});
```

**Interface Impact:**
- aria-expanded="false": Panel collapsed, content hidden
- aria-expanded="true": Panel expanded, content visible

---

#### 6. Active Section Highlighting

**Condition:** Section is 50% visible in viewport

**Components Affected:** Navigation links

**Validation Logic:**
```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    const link = document.querySelector(`a[href="#${entry.target.id}"]`);

    if (entry.isIntersecting && entry.intersectionRatio >= 0.5) {
      // Section is active
      document.querySelectorAll('nav a').forEach(l => l.classList.remove('active'));
      link.classList.add('active');
    }
  });
}, { threshold: 0.5 });
```

**Interface Impact:**
- Active link: Bold, underlined, or distinct color
- Inactive links: Normal styling

---

### Content Validation

#### 7. Email Link Format

**Condition:** Valid email format

**Component Affected:** Contact email link

**Validation:**
```html
<a href="mailto:emkaminsk@gmail.com?subject=Inquiry%20from%20CV%20Website">
  emkaminsk@gmail.com
</a>
```

**Checks:**
- Email format: valid (handled by browser)
- Subject properly URL-encoded
- Link functional

---

#### 8. External Link Security

**Condition:** All external links must have security attributes

**Components Affected:** Social media links

**Validation:**
```html
<!-- Required attributes -->
<a href="https://linkedin.com/..."
   target="_blank"
   rel="noopener noreferrer"
   aria-label="LinkedIn profile">
```

**Checks:**
- `rel="noopener"`: Prevents window.opener access
- `rel="noreferrer"`: Prevents referrer leakage
- `aria-label`: Provides descriptive label for screen readers

---

#### 9. Image Accessibility

**Condition:** All images must have alt text

**Components Affected:** Profile image, social media icons

**Validation:**
```html
<!-- Profile image -->
<img src="./img/MK03.jpg" alt="Marcin Kamiński" />

<!-- Social icons (decorative, label on parent) -->
<a href="..." aria-label="LinkedIn profile">
  <img src="./icons/linkedin.svg" alt="" aria-hidden="true" />
</a>
```

**Checks:**
- Content images: Descriptive alt text
- Decorative images: Empty alt (`alt=""`) with `aria-hidden="true"`
- Icons: Parent element has `aria-label`

---

#### 10. Heading Hierarchy

**Condition:** Proper semantic heading structure

**Components Affected:** All sections

**Validation:**
- Single `<h1>` on page (in hero section)
- `<h2>` for main sections (About Me, Experience, Education, Interests)
- `<h3>` for subsections (section headings)
- `<h4>` for sidebar/accordion sections
- No skipped levels

**Interface Impact:**
- Screen readers can navigate by headings
- Proper document outline
- Better SEO

---

#### 11. Color Contrast

**Condition:** WCAG 2.1 AA compliance

**Components Affected:** All text content

**Validation:**
- Normal text: Minimum 4.5:1 contrast ratio
- Large text (18pt+): Minimum 3:1 contrast ratio
- Both themes (light and dark) must meet requirements
- Verify with tools: Chrome DevTools, axe DevTools

**Interface Impact:**
- Readable text for low vision users
- Professional appearance
- Accessibility compliance

---

#### 12. Touch Target Size (Mobile)

**Condition:** Minimum 44x44px for touch targets

**Components Affected:**
- Navigation links
- Theme toggle button
- Back-to-top button
- Accordion headers
- Social media icons

**Validation:**
```css
/* Ensure minimum touch target */
@media screen and (max-width: 768px) {
  button, a {
    min-width: 44px;
    min-height: 44px;
    padding: 12px;
  }
}
```

**Interface Impact:**
- Easier tapping on mobile devices
- Reduced mis-taps
- Better mobile UX

---

### Responsive Layout Validation

#### 13. No Horizontal Scroll

**Condition:** Content must fit within viewport width

**Validation:**
- Test at 320px, 375px, 768px, 992px, 1920px
- No elements exceed viewport width
- Images responsive (max-width: 100%)
- Long text wraps properly

**Interface Impact:**
- No horizontal scrolling required
- Content fully visible
- Professional appearance

---

#### 14. Smooth Scroll Offset

**Condition:** Section content not hidden behind sticky navigation

**Validation:**
```css
section {
  scroll-margin-top: 80px; /* Height of sticky nav */
}
```

```javascript
// Or in JavaScript
const navHeight = document.querySelector('nav').offsetHeight;
const targetPosition = targetElement.offsetTop - navHeight;
window.scrollTo({ top: targetPosition, behavior: 'smooth' });
```

**Interface Impact:**
- Section headings visible after smooth scroll
- Content not obscured by navigation
- Better user experience

## 10. Error Handling

### 1. Image Load Failures

**Scenario:** Profile image or hero background image fails to load

**Potential Causes:**
- Network issues
- Incorrect file path
- File deleted or moved
- Server error

**Handling Strategy:**

**For Profile Image:**
```html
<img src="./img/MK03.jpg"
     alt="Marcin Kamiński"
     onerror="this.style.display='none';" />
```

**For Hero Background:**
```css
.hero {
  background-color: #394046; /* Fallback color */
  background-image: url("img/sascha-eremin-DNQ-M93tHmA-unsplash-3000x1000.jpg");
}
```

**Expected Behavior:**
- Profile image: Hidden if fails to load, alt text remains in DOM for screen readers
- Hero background: Fallback to solid color (#394046), text remains readable
- No broken image icons displayed
- Layout remains intact

---

### 2. LocalStorage Unavailable

**Scenario:** LocalStorage disabled (private browsing) or unavailable

**Potential Causes:**
- Private/incognito browsing mode
- Browser settings disabled storage
- Browser doesn't support LocalStorage (very old browsers)
- Storage quota exceeded (unlikely for theme preference)

**Handling Strategy:**

```javascript
const themeSwitcher = {
  get schemeFromLocalStorage() {
    try {
      if (typeof window.localStorage !== "undefined") {
        const saved = window.localStorage.getItem(this.localStorageKey);
        if (saved !== null) {
          return saved;
        }
      }
    } catch (e) {
      console.warn('LocalStorage unavailable:', e);
    }
    return this._scheme; // Default to auto
  },

  schemeToLocalStorage() {
    try {
      if (typeof window.localStorage !== "undefined") {
        window.localStorage.setItem(this.localStorageKey, this.scheme);
      }
    } catch (e) {
      console.warn('Cannot save to LocalStorage:', e);
      // Theme still works, just doesn't persist
    }
  }
}
```

**Expected Behavior:**
- Theme switcher still functions
- Theme preference not persisted across sessions
- Falls back to system preference on each visit
- No errors thrown to user
- Console warning for developers (optional)

---

### 3. JavaScript Disabled

**Scenario:** User has JavaScript disabled or blocked

**Potential Causes:**
- Browser settings
- Privacy extensions (NoScript)
- Corporate security policies
- Very old browsers

**Handling Strategy:**

**Graceful Degradation:**
- All content remains accessible (static HTML)
- Navigation links work (anchor links: `<a href="#experience">`)
- Theme defaults to system preference (CSS `prefers-color-scheme`)
- Accordions remain expanded (content visible)
- Back-to-top button hidden (CSS: `display: none` by default)
- Theme toggle button visible but non-functional

**CSS-Only Alternatives:**
```css
/* Default theme based on system preference */
@media (prefers-color-scheme: dark) {
  :root {
    --bg-color: #1a1a1a;
    --text-color: #e0e0e0;
  }
}

/* Accordions expanded by default without JS */
.accordion-panel {
  display: block; /* Always visible if JS disabled */
}
```

**Expected Behavior:**
- Full content access maintained
- Reduced interactivity (no smooth scroll, no theme toggle)
- Layout remains intact
- No broken functionality
- Professional appearance maintained

---

### 4. Section ID Mismatch

**Scenario:** Navigation link references non-existent section ID

**Potential Causes:**
- Typo in href or ID
- Section removed but link remains
- Manual HTML editing error

**Handling Strategy:**

```javascript
function smoothScrollTo(targetId) {
  const target = document.getElementById(targetId);

  if (!target) {
    console.warn(`Section not found: ${targetId}`);
    return; // Do nothing, no error thrown
  }

  const navHeight = 80;
  const targetPosition = target.offsetTop - navHeight;

  window.scrollTo({
    top: targetPosition,
    behavior: 'smooth'
  });
}
```

**Expected Behavior:**
- Link click does nothing (no scroll)
- No error displayed to user
- Console warning for developers
- Page remains functional

**Prevention:**
- Verify all section IDs match navigation hrefs during testing
- Checklist: `#experience`, `#education`, `#interests`

---

### 5. Very Slow Network / Large Images

**Scenario:** Images load slowly on poor network connection

**Potential Causes:**
- 2G/3G mobile network
- Congested network
- Large unoptimized images
- Server issues

**Handling Strategy:**

**Image Optimization:**
```html
<!-- Specify dimensions to prevent layout shift -->
<img src="./img/MK03.jpg"
     alt="Marcin Kamiński"
     width="200"
     height="200"
     loading="lazy" />

<!-- Responsive background image -->
<style>
  .hero {
    background-image: url("img/hero-800.jpg");
  }

  @media (min-width: 768px) {
    .hero {
      background-image: url("img/hero-1200.jpg");
    }
  }

  @media (min-width: 1200px) {
    .hero {
      background-image: url("img/hero-2000.jpg");
    }
  }
</style>
```

**Expected Behavior:**
- Layout doesn't shift as images load (dimensions specified)
- Below-fold images lazy load (don't block critical content)
- Appropriate image sizes for viewport (smaller on mobile)
- Text content loads first (readable immediately)
- Progressive enhancement (content first, images enhance)

**Performance Targets:**
- First Contentful Paint: <1.5s (text visible)
- Largest Contentful Paint: <2.5s (hero image loaded)
- Cumulative Layout Shift: <0.1 (no jumps)

---

### 6. Browser Incompatibility

**Scenario:** User on unsupported browser (IE11, very old browsers)

**Potential Causes:**
- Corporate environment locked to IE11
- Very old browser version
- Niche browser without modern features

**Handling Strategy:**

**Progressive Enhancement:**
```javascript
// Check for IntersectionObserver support
if ('IntersectionObserver' in window) {
  // Use IntersectionObserver for active section
  initIntersectionObserver();
} else {
  // Fallback to scroll event listener
  window.addEventListener('scroll', calculateActiveSection);
}

// Check for smooth scroll support
if ('scrollBehavior' in document.documentElement.style) {
  // Use native smooth scroll
  window.scrollTo({ top: 0, behavior: 'smooth' });
} else {
  // Fallback to instant scroll or polyfill
  window.scrollTo(0, 0);
}
```

**CSS Fallbacks:**
```css
/* CSS Grid with flexbox fallback */
@supports (display: grid) {
  .grid {
    display: grid;
  }
}

@supports not (display: grid) {
  .grid {
    display: flex;
  }
}

/* CSS custom properties with fallback */
.element {
  color: #333333; /* Fallback */
  color: var(--text-color); /* Modern browsers */
}
```

**Expected Behavior:**
- Core functionality works on all browsers
- Enhanced features for modern browsers
- Graceful degradation for old browsers
- No broken layouts
- Content always accessible

---

### 7. External Link Failures

**Scenario:** Social media link returns 404 or profile deleted

**Potential Causes:**
- Profile deleted or suspended
- URL changed
- Platform shutdown (unlikely)

**Handling Strategy:**

**Prevention:**
- Regular link testing (manual)
- Keep social media profiles active
- Update URLs if changed

**Expected Behavior:**
- Link opens in new tab
- User sees 404 on external site (not our control)
- No impact on CV site functionality
- User can use other contact methods (email)

**Mitigation:**
- Provide multiple contact methods (email + multiple social platforms)
- Primary contact (email) is most reliable

---

### 8. Email Client Not Configured

**Scenario:** User clicks email link but has no email client configured

**Potential Causes:**
- No default email client set
- Using webmail only (Gmail, Outlook.com)
- Mobile device without email app

**Handling Strategy:**

**Current Implementation:**
```html
<a href="mailto:emkaminsk@gmail.com?subject=Inquiry%20from%20CV%20Website">
  emkaminsk@gmail.com
</a>
```

**Expected Behavior:**
- Browser attempts to open default email client
- If none configured: Browser shows error or does nothing
- Email address visible as text (user can copy manually)
- User can manually compose email in webmail

**Alternative Enhancement (Future):**
- Add contact form as alternative method
- Display email address clearly for manual copying
- Consider adding "Copy Email" button with JavaScript

---

### 9. Accordion Animation Issues

**Scenario:** Accordion animation glitches or doesn't animate smoothly

**Potential Causes:**
- CSS transition on max-height with dynamic content
- Browser rendering performance
- JavaScript timing issues

**Handling Strategy:**

**Robust Animation:**
```css
.accordion-panel {
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.3s ease-out;
}

.accordion-panel.expanded {
  max-height: 1000px; /* Large enough for content */
  /* Or calculate dynamically: panel.scrollHeight */
}
```

```javascript
// Calculate exact height for smooth animation
const panel = header.nextElementSibling;
panel.style.maxHeight = panel.scrollHeight + 'px';
```

**Fallback for Reduced Motion:**
```css
@media (prefers-reduced-motion: reduce) {
  .accordion-panel {
    transition: none; /* Instant toggle */
  }
}
```

**Expected Behavior:**
- Smooth animation on modern browsers
- Instant toggle if animations disabled
- No content cut-off
- Functional regardless of animation

---

### 10. Theme Flash (FOUC - Flash of Unstyled Content)

**Scenario:** Wrong theme flashes briefly before correct theme loads

**Potential Causes:**
- Theme applied by JavaScript after page render
- LocalStorage read after initial paint
- Slow JavaScript execution

**Handling Strategy:**

**Inline Critical Theme Script:**
```html
<head>
  <!-- Inline theme script BEFORE any stylesheets -->
  <script>
    (function() {
      const saved = localStorage.getItem('picoPreferredColorScheme');
      const theme = saved ||
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
      document.documentElement.setAttribute('data-theme', theme);
    })();
  </script>

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css" />
  <link rel="stylesheet" href="custom.css" />
</head>
```

**Expected Behavior:**
- Correct theme applied before first paint
- No flash of wrong theme
- Smooth user experience
- Theme consistent from page load

---

### 11. Viewport Extremes (320px or 2560px+)

**Scenario:** Layout breaks at very small or very large screen sizes

**Handling Strategy:**

**Minimum Width (320px):**
```css
@media (max-width: 320px) {
  .container {
    padding: 0.5rem;
  }

  h1 {
    font-size: 1.25rem;
  }

  .social-link {
    width: 40px;
    height: 40px;
  }
}
```

**Maximum Width (2560px+):**
```css
.container {
  max-width: 1400px; /* Prevent excessive line length */
  margin: 0 auto;
}
```

**Expected Behavior:**
- 320px: Content readable, no horizontal scroll, touch targets adequate
- 2560px: Content centered, proper line length, no stretching

**Testing:**
- Use browser DevTools responsive mode
- Test at 320px, 375px, 768px, 992px, 1920px, 2560px
- Verify layout, readability, interactions

## 11. Implementation Steps

### Phase 1: Setup and Foundation

#### Step 1: Review Current Implementation
- **Action:** Read through existing `index.html`, `custom.css`, and `minimal-theme-switcher.js`
- **Verify:**
  - Current structure matches component tree
  - CSS classes align with component needs
  - Identify gaps and missing features
- **Output:** List of features to add, modify, or maintain

#### Step 2: Add Missing HTML Structure
- **Action:** Update `index.html` with missing elements
- **Add:**
  - Skip to content link
  - Theme toggle button in navigation
  - Back-to-top button
  - Accordion container for mobile (duplicate sidebar content)
  - Missing ARIA attributes
  - Semantic landmarks
- **Example:**
  ```html
  <!-- Skip link -->
  <a href="#main-content" class="skip-link">Skip to content</a>

  <!-- Theme toggle in nav -->
  <button aria-label="Toggle dark mode"
          aria-pressed="false"
          data-theme-toggle>
    <svg aria-hidden="true"><!-- icon --></svg>
  </button>

  <!-- Main content landmark -->
  <main id="main-content">
    <!-- existing content -->
  </main>

  <!-- Accordions for mobile -->
  <div class="accordion-container">
    <div class="accordion-item">
      <button aria-expanded="false"
              aria-controls="skills-panel"
              class="accordion-header">
        Skills
      </button>
      <div id="skills-panel" role="region" class="accordion-panel">
        <ul><!-- skills list --></ul>
      </div>
    </div>
    <!-- repeat for other sections -->
  </div>

  <!-- Back to top -->
  <button aria-label="Back to top" class="back-to-top">
    <svg aria-hidden="true"><!-- up arrow --></svg>
  </button>
  ```

#### Step 3: Update CSS for New Components
- **Action:** Add styles to `custom.css`
- **Add styles for:**
  - Skip link (hidden by default, visible on focus)
  - Theme toggle button
  - Back-to-top button (hidden by default, positioned bottom-right)
  - Accordion container (hidden on desktop, visible on mobile)
  - Accordion headers and panels
  - Active navigation state
  - Focus indicators
  - Smooth transitions
- **Example:**
  ```css
  /* Skip link */
  .skip-link {
    position: absolute;
    top: -40px;
    left: 0;
    padding: 8px;
    z-index: 100;
  }

  .skip-link:focus {
    top: 0;
  }

  /* Theme toggle */
  [data-theme-toggle] {
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
  }

  /* Back to top */
  .back-to-top {
    position: fixed;
    bottom: 20px;
    right: 20px;
    display: none;
    z-index: 99;
    border: none;
    background: var(--primary);
    color: white;
    padding: 12px 16px;
    border-radius: 50%;
    cursor: pointer;
    transition: opacity 0.3s;
  }

  .back-to-top.visible {
    display: block;
  }

  /* Accordions */
  .accordion-container {
    display: none;
  }

  @media (max-width: 767px) {
    .accordion-container {
      display: block;
    }
  }

  .accordion-header {
    width: 100%;
    text-align: left;
    padding: 1rem;
    background: #f0f0f0;
    border: none;
    cursor: pointer;
  }

  .accordion-panel {
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease-out;
  }

  .accordion-panel.expanded {
    max-height: 1000px;
  }
  ```

---

### Phase 2: JavaScript Interactivity

#### Step 4: Integrate Theme Toggle
- **Action:** Add theme toggle button handler
- **Implementation:**
  ```javascript
  // In new file: js/main.js or inline in index.html

  document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.querySelector('[data-theme-toggle]');
    const icon = themeToggle.querySelector('svg');

    // Update icon based on current theme
    function updateThemeIcon(theme) {
      icon.innerHTML = theme === 'dark'
        ? '<!-- moon icon SVG -->'
        : '<!-- sun icon SVG -->';
    }

    // Initialize icon
    updateThemeIcon(themeSwitcher.scheme);

    // Toggle on click
    themeToggle.addEventListener('click', () => {
      const newTheme = themeSwitcher.scheme === 'light' ? 'dark' : 'light';
      themeSwitcher.scheme = newTheme;
      updateThemeIcon(newTheme);
      themeToggle.setAttribute('aria-pressed', newTheme === 'dark');
    });
  });
  ```

#### Step 5: Implement Smooth Scroll Navigation
- **Action:** Add smooth scroll with offset for section links
- **Implementation:**
  ```javascript
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      e.preventDefault();

      const targetId = link.getAttribute('href').substring(1);
      const target = document.getElementById(targetId);

      if (!target) return;

      const navHeight = document.querySelector('nav').offsetHeight;
      const targetPosition = target.offsetTop - navHeight;

      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });

      // Close dropdown if open
      const dropdown = link.closest('details');
      if (dropdown) dropdown.removeAttribute('open');
    });
  });
  ```

#### Step 6: Implement Active Section Highlighting
- **Action:** Use IntersectionObserver to track active section
- **Implementation:**
  ```javascript
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('nav a[href^="#"]');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && entry.intersectionRatio >= 0.5) {
        // Remove active from all links
        navLinks.forEach(link => link.classList.remove('active'));

        // Add active to current section's link
        const activeLink = document.querySelector(`nav a[href="#${entry.target.id}"]`);
        if (activeLink) activeLink.classList.add('active');
      }
    });
  }, { threshold: 0.5 });

  sections.forEach(section => observer.observe(section));
  ```

#### Step 7: Implement Back-to-Top Button
- **Action:** Show/hide button based on scroll, handle click
- **Implementation:**
  ```javascript
  const backToTopBtn = document.querySelector('.back-to-top');

  // Show/hide on scroll
  window.addEventListener('scroll', () => {
    if (window.scrollY > 500) {
      backToTopBtn.classList.add('visible');
    } else {
      backToTopBtn.classList.remove('visible');
    }
  });

  // Scroll to top on click
  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
  ```

#### Step 8: Implement Accordion Functionality (Mobile)
- **Action:** Add expand/collapse logic for accordions
- **Implementation:**
  ```javascript
  document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', () => {
      const panel = header.nextElementSibling;
      const isExpanded = header.getAttribute('aria-expanded') === 'true';

      // Toggle state
      header.setAttribute('aria-expanded', !isExpanded);
      panel.classList.toggle('expanded');

      // Animate
      if (!isExpanded) {
        panel.style.maxHeight = panel.scrollHeight + 'px';
      } else {
        panel.style.maxHeight = '0';
      }
    });
  });
  ```

---

### Phase 3: Accessibility Enhancements

#### Step 9: Add ARIA Labels and Attributes
- **Action:** Update HTML with proper ARIA attributes
- **Add to:**
  - Navigation: `<nav aria-label="Main navigation">`
  - Main content: `<main id="main-content">`
  - Sidebar: `<aside aria-label="Skills and qualifications">`
  - Footer: `<footer>`
  - Buttons: `aria-label`, `aria-pressed`
  - Accordions: `aria-expanded`, `aria-controls`, `role="region"`
  - Social links: `aria-label="LinkedIn profile"`

#### Step 10: Verify Keyboard Navigation
- **Action:** Test all interactions with keyboard only
- **Test:**
  - Tab through all focusable elements
  - Skip to content link works
  - Section links work with Enter
  - Theme toggle works with Space/Enter
  - Back-to-top works with Enter
  - Accordions work with Enter/Space
  - Escape closes dropdowns
  - No keyboard traps
- **Fix:** Any elements not keyboard accessible

#### Step 11: Add Focus Indicators
- **Action:** Ensure all interactive elements have visible focus
- **CSS:**
  ```css
  a:focus, button:focus, summary:focus {
    outline: 2px solid var(--primary);
    outline-offset: 2px;
  }

  /* Don't remove focus outline! */
  ```

---

### Phase 4: Performance Optimization

#### Step 12: Optimize Images
- **Action:** Compress and convert images
- **Tasks:**
  - Convert hero background to WebP (with JPEG fallback)
  - Create responsive sizes: 800px, 1200px, 2000px
  - Compress to 80% quality
  - Convert profile image to WebP
  - Add `width` and `height` attributes to prevent layout shift
  - Add `loading="lazy"` to profile image
- **Example:**
  ```html
  <img src="./img/MK03.webp"
       alt="Marcin Kamiński"
       width="200"
       height="200"
       loading="lazy">
  ```

#### Step 13: Minify CSS and JavaScript
- **Action:** Minify production files (optional for static site)
- **Tools:**
  - CSS: cssnano, clean-css
  - JS: uglify-js, terser
- **OR:** Keep readable for manual editing (acceptable for this project)

#### Step 14: Inline Critical Theme Script
- **Action:** Move theme initialization to inline `<script>` in `<head>`
- **Prevents:** Flash of wrong theme
- **Implementation:**
  ```html
  <head>
    <script>
      (function() {
        const saved = localStorage.getItem('picoPreferredColorScheme');
        const theme = saved ||
          (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
        document.documentElement.setAttribute('data-theme', theme);
      })();
    </script>
  </head>
  ```

---

### Phase 5: SEO and Metadata

#### Step 15: Add Meta Tags
- **Action:** Update `<head>` with complete metadata
- **Add:**
  ```html
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Marcin Kamiński - Technical Product Owner CV</title>
    <meta name="description" content="CV page for Marcin Kamiński, Technical Product Owner with both business and IT skills">
    <meta name="author" content="Marcin Kamiński">
    <link rel="canonical" href="https://yourdomain.com/">

    <!-- Open Graph -->
    <meta property="og:type" content="profile">
    <meta property="og:title" content="Marcin Kamiński - Technical Product Owner">
    <meta property="og:description" content="Product Owner with 5 years of Agile experience, programming skills, and e-MBA">
    <meta property="og:url" content="https://yourdomain.com">
    <meta property="og:image" content="https://yourdomain.com/img/MK03.jpg">
    <meta property="profile:first_name" content="Marcin">
    <meta property="profile:last_name" content="Kamiński">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary">
    <meta name="twitter:site" content="@emkaminsk">
    <meta name="twitter:title" content="Marcin Kamiński - Technical Product Owner">
    <meta name="twitter:description" content="Product Owner with 5 years of Agile experience, programming skills, and e-MBA">
    <meta name="twitter:image" content="https://yourdomain.com/img/MK03.jpg">
  </head>
  ```

#### Step 16: Add JSON-LD Structured Data
- **Action:** Add Schema.org Person markup
- **Implementation:**
  ```html
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Marcin Kamiński",
    "jobTitle": "Technical Product Owner",
    "description": "Product Owner for IT projects with 5 years of Agile experience...",
    "url": "https://yourdomain.com",
    "email": "emkaminsk@gmail.com",
    "image": "https://yourdomain.com/img/MK03.jpg",
    "alumniOf": [
      {
        "@type": "EducationalOrganization",
        "name": "University of Economics"
      },
      {
        "@type": "EducationalOrganization",
        "name": "Aalto University"
      },
      {
        "@type": "EducationalOrganization",
        "name": "Warsaw University of Technology"
      }
    ],
    "worksFor": {
      "@type": "Organization",
      "name": "Sii Polska"
    },
    "sameAs": [
      "https://www.linkedin.com/in/marcinkaminski/",
      "https://github.com/emkaminsk",
      "https://twitter.com/emkaminsk",
      "https://www.facebook.com/marcin.kaminski.01/"
    ],
    "knowsAbout": [
      "Product Management",
      "Agile",
      "Scrum",
      "Python",
      "Data Science"
    ],
    "knowsLanguage": [
      {
        "@type": "Language",
        "name": "English",
        "description": "Very fluent"
      },
      {
        "@type": "Language",
        "name": "Spanish",
        "description": "Basic communication"
      },
      {
        "@type": "Language",
        "name": "German",
        "description": "Basic reading skills"
      }
    ]
  }
  </script>
  ```

#### Step 17: Add Security Attributes to External Links
- **Action:** Add `rel="noopener noreferrer"` to all external links
- **Update:**
  ```html
  <a href="https://www.linkedin.com/in/marcinkaminski/"
     aria-label="LinkedIn profile"
     target="_blank"
     rel="noopener noreferrer">
    <img src="./icons/linkedin.svg" alt="LinkedIn" />
  </a>
  ```

---

### Phase 6: Testing and Validation

#### Step 18: Test Responsive Design
- **Action:** Test layout at all breakpoints
- **Test at:**
  - 320px (minimum)
  - 375px (mobile)
  - 768px (tablet)
  - 992px (desktop)
  - 1920px (large desktop)
  - 2560px (very large)
- **Verify:**
  - No horizontal scroll
  - Content readable
  - Touch targets adequate (44x44px minimum on mobile)
  - Images responsive
  - Sidebar/accordion swap at 768px

#### Step 19: Test Accessibility
- **Action:** Run accessibility audits
- **Tools:**
  - axe DevTools (Chrome extension)
  - Lighthouse Accessibility audit
  - WAVE (WebAIM)
  - Keyboard navigation (manual)
  - Screen reader (NVDA, VoiceOver)
- **Target:** 0 critical issues, WCAG 2.1 AA compliance
- **Verify:**
  - All interactive elements keyboard accessible
  - Focus indicators visible
  - ARIA attributes correct
  - Heading hierarchy logical
  - Color contrast sufficient
  - Alt text present

#### Step 20: Test Performance
- **Action:** Run performance audits
- **Tools:**
  - Lighthouse Performance audit
  - WebPageTest
  - Chrome DevTools Performance panel
- **Targets:**
  - LCP < 2.5s
  - FCP < 1.5s
  - CLS < 0.1
  - FID < 100ms
  - Lighthouse score ≥ 90
- **Optimize:** Any failing metrics

#### Step 21: Validate HTML and CSS
- **Action:** Run W3C validators
- **Tools:**
  - W3C HTML Validator: https://validator.w3.org/
  - W3C CSS Validator: https://jigsaw.w3.org/css-validator/
- **Fix:** Any validation errors

#### Step 22: Test Cross-Browser Compatibility
- **Action:** Test in multiple browsers
- **Browsers:**
  - Chrome (latest)
  - Firefox (latest)
  - Safari (latest)
  - Edge (latest)
  - Mobile Safari (iOS)
  - Chrome Mobile (Android)
- **Verify:**
  - Layout consistent
  - Interactions work
  - Theme switching works
  - Smooth scroll works (or fallback)

#### Step 23: Test User Stories
- **Action:** Manually verify each user story acceptance criteria
- **User Stories to Test:**
  - US-001: View Professional Identity
  - US-002: Navigate to Specific Sections
  - US-003: Return to Top of Page
  - US-004: View Work Experience Timeline
  - US-005: Review Educational Background
  - US-006: View Skills and Qualifications
  - US-007: View Personal Interests
  - US-008: Access Contact Information
- **Document:** Any failing criteria

---

### Phase 7: Deployment Preparation

#### Step 24: Create 404 Error Page
- **Action:** Update or verify `error404.html`
- **Include:**
  - Friendly error message
  - Link to homepage
  - Consistent branding
  - Theme support
  - Proper heading hierarchy
  - Accessible design

#### Step 25: Final Content Review
- **Action:** Proofread all content
- **Check:**
  - Spelling and grammar
  - Dates accurate and consistent format
  - Company names correct
  - Technologies spelled correctly
  - Contact information functional
  - Social media URLs correct

#### Step 26: Documentation
- **Action:** Update README.md (if needed)
- **Include:**
  - Project description
  - Tech stack
  - Local development instructions
  - Deployment process
  - Browser compatibility
  - Accessibility compliance
  - Performance metrics

---

### Phase 8: Deployment and Monitoring

#### Step 27: Commit and Push to Git
- **Action:** Commit all changes to feature branch
- **Commands:**
  ```bash
  git add .
  git commit -m "Implement index view with accessibility and performance optimizations"
  git push -u origin claude/view-implementation-plan-01ECCH9ETbZeSXVgkoSPjQXh
  ```

#### Step 28: Deploy to Production
- **Action:** Merge to main branch and deploy
- **Process:**
  - GitHub Actions automatically deploys to Mikr.us server
  - Verify deployment successful
  - Test live site

#### Step 29: Post-Deployment Testing
- **Action:** Test live production site
- **Verify:**
  - HTTPS certificate valid
  - All images load
  - Theme switching works
  - Navigation works
  - Accordions work (mobile)
  - Contact links functional
  - Social links functional
  - SEO metadata present
  - Performance targets met

#### Step 30: Ongoing Maintenance
- **Action:** Plan regular updates
- **Schedule:**
  - Update job experience when changed
  - Update skills as needed
  - Test quarterly for broken links
  - Review analytics (if added)
  - Keep dependencies updated (Pico CSS)
  - Monitor performance metrics

---

## Summary Checklist

**HTML Structure:**
- [ ] Skip to content link added
- [ ] Theme toggle button in navigation
- [ ] Back-to-top button added
- [ ] Accordion container for mobile created
- [ ] ARIA attributes on all interactive elements
- [ ] Semantic HTML5 landmarks (nav, main, aside, footer)
- [ ] Proper heading hierarchy (single h1)
- [ ] Alt text on all images
- [ ] Security attributes on external links

**CSS Styling:**
- [ ] Skip link styles (hidden/visible on focus)
- [ ] Theme toggle button styles
- [ ] Back-to-top button styles
- [ ] Accordion styles (mobile only)
- [ ] Active navigation state styles
- [ ] Focus indicators (2px outline)
- [ ] Responsive breakpoints (320px, 768px, 992px)
- [ ] Sidebar/accordion media queries
- [ ] Color contrast verified (WCAG 2.1 AA)

**JavaScript Functionality:**
- [ ] Theme toggle integration
- [ ] Smooth scroll with offset
- [ ] Active section highlighting (IntersectionObserver)
- [ ] Back-to-top show/hide and scroll
- [ ] Accordion expand/collapse
- [ ] Dropdown close after link click
- [ ] Inline theme initialization (prevent flash)

**Accessibility:**
- [ ] Keyboard navigation fully functional
- [ ] Screen reader tested
- [ ] ARIA labels on all icon buttons
- [ ] ARIA expanded on accordions
- [ ] Focus indicators visible
- [ ] Color contrast ≥ 4.5:1
- [ ] Alt text descriptive
- [ ] axe DevTools: 0 critical issues

**Performance:**
- [ ] Images optimized (WebP + JPEG fallback)
- [ ] Responsive image sizes (800px, 1200px, 2000px)
- [ ] Lazy loading on below-fold images
- [ ] Image dimensions specified
- [ ] CSS minified (optional)
- [ ] JS minified (optional)
- [ ] Lighthouse Performance score ≥ 90
- [ ] LCP < 2.5s
- [ ] FCP < 1.5s
- [ ] CLS < 0.1

**SEO:**
- [ ] Title tag optimized
- [ ] Meta description added
- [ ] Canonical URL specified
- [ ] Open Graph tags complete
- [ ] Twitter Card tags complete
- [ ] JSON-LD structured data added
- [ ] Structured data validated

**Testing:**
- [ ] Responsive design tested (320px - 2560px)
- [ ] Cross-browser tested (Chrome, Firefox, Safari, Edge)
- [ ] Mobile tested (iOS, Android)
- [ ] User stories verified
- [ ] HTML validated (W3C)
- [ ] CSS validated (W3C)
- [ ] Links tested (no 404s)

**Deployment:**
- [ ] Changes committed to Git
- [ ] Pushed to feature branch
- [ ] Deployed to production
- [ ] Live site tested
- [ ] HTTPS verified
- [ ] Documentation updated

---

**End of Implementation Plan**
