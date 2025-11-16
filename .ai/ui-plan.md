# UI Architecture for PersonalCV - MVP

## 1. UI Structure Overview

The PersonalCV website is a single-page application (SPA) with a vertical scroll layout and fixed sidebar. The architecture follows a progressive disclosure pattern where users navigate through sections either by scrolling or using section navigation. The design is fully responsive, accessible (WCAG 2.1 AA compliant), and performance-optimized.

### Core Design Principles

- **Mobile-first responsive design** - Ensuring optimal experience across all devices
- **Progressive enhancement** - Base functionality works without JavaScript
- **Semantic HTML structure** - Proper document outline and accessibility
- **Performance-first** - Optimized images, minimal CSS/JS, lazy loading
- **Accessibility-focused** - Keyboard navigation, screen reader support, ARIA labels
- **Theme-aware** - Light/dark mode with system preference detection

### Layout Strategy

- **Desktop (≥992px):** Two-column layout with fixed right sidebar
- **Tablet (768px-991px):** Reduced sidebar width, condensed spacing
- **Mobile (<768px):** Single column, sidebar content moved to collapsible accordions

## 2. View List

### 2.1 Main View (index.html)

**Path:** `/` or `/index.html`

**Main Purpose:** Display comprehensive CV information in a professional, accessible, and engaging format

**Key Information to Display:**
- Professional identity (name, title, tagline)
- Work experience with timeline visualization
- Educational background
- Skills and technical expertise
- Contact information and social media links
- Personal interests

**Key View Components:**

#### Hero Section
- **Purpose:** Create strong first impression, establish professional identity
- **Elements:**
  - Full-width hero container with background image
  - H1 heading (name)
  - H2 subheading (professional title/tagline)
  - Responsive, optimized background image
- **UX Considerations:**
  - Eye-catching but professional design
  - Clear visual hierarchy
  - Readable text over background (sufficient contrast)
  - Reduced padding and font sizes on mobile
- **Accessibility:**
  - Proper heading hierarchy (h1 for name)
  - Background image treated as decorative (CSS background)
  - Minimum 4.5:1 color contrast ratio for text
- **Security:** None specific

#### Navigation Bar
- **Purpose:** Provide consistent access to all sections and theme control
- **Elements:**
  - Fixed/sticky navigation bar
  - Logo/name (links to top)
  - Section navigation menu (Experience, Education, Interests)
  - Theme toggle button (sun/moon icon)
  - Active section indicator
- **UX Considerations:**
  - Always visible (sticky position)
  - Clear visual feedback on hover/active states
  - Smooth scroll to sections with proper offset
  - Mobile: Dropdown menu or condensed navigation
  - Active section highlighted in menu
- **Accessibility:**
  - `<nav aria-label="Main navigation">`
  - Skip to content link (visually hidden, keyboard accessible)
  - ARIA labels for icon buttons
  - Keyboard navigable (Tab, Enter, Space)
  - Focus indicators visible
- **Security:** None specific

#### About Me Section
- **Purpose:** Introduce professional background and provide contact information
- **Elements:**
  - Two-column layout (text + photo on desktop)
  - Professional summary text (elevator pitch)
  - Contact information block with enhanced mailto link
  - Profile image with caption
- **UX Considerations:**
  - Scannable text with clear hierarchy
  - Professional photo placement (right side on desktop)
  - Easy-to-find contact info
  - Mobile: Stacked layout (text, then photo)
- **Accessibility:**
  - Alt text for profile image: "Marcin Kamiński, Technical Product Owner"
  - Semantic HTML (address element for contact)
  - Readable font size (min 16px on mobile)
  - Proper color contrast
- **Security:**
  - Email link with pre-filled subject: `mailto:emkaminsk@gmail.com?subject=Inquiry%20from%20CV%20Website`

#### Experience Section (Timeline)
- **Purpose:** Showcase work history and achievements with visual timeline
- **Elements:**
  - Vertical timeline with visual markers (dots/lines)
  - Job experience cards
  - Company names (bold, prominent)
  - Job titles
  - Employment dates with visual indicators
  - Responsibilities as bullet points
  - Technologies used (italic, distinct styling)
- **UX Considerations:**
  - Clear chronological order (newest first)
  - Visual timeline for easy scanning
  - Distinct visual markers for each position
  - Contrasting colors for different time periods
  - Subtle scroll animations (fade-in, slide-up)
  - Mobile: Simplified timeline, left-aligned
- **Accessibility:**
  - Semantic HTML (article for each job)
  - Proper list markup (ul/li for responsibilities)
  - Clear heading hierarchy (h3 for section, h4 for companies)
  - Timeline decorations via CSS (not critical content)
- **Security:** None specific

#### Education Section
- **Purpose:** Display academic credentials and qualifications
- **Elements:**
  - Education cards/blocks
  - Institution names (bold)
  - Degree types (Master, eMBA, Postgraduate)
  - Date ranges
  - Specializations and achievements
- **UX Considerations:**
  - Consistent card styling with experience section
  - Clear visual hierarchy
  - Scannable format
  - Chronological order
- **Accessibility:**
  - Semantic HTML (article/section elements)
  - Proper heading levels (h3/h4)
  - List markup for details
- **Security:** None specific

#### Interests Section
- **Purpose:** Humanize the CV, show personality
- **Elements:**
  - Simple paragraph or list format
  - Personal interests and hobbies
  - Optional: icons for visual interest
- **UX Considerations:**
  - Brief and professional
  - Easy to scan
  - Lighter tone than other sections
- **Accessibility:**
  - Simple, readable text
  - Proper paragraph/list markup
- **Security:** None specific

#### Sidebar (Desktop) / Collapsible Panels (Mobile)
- **Purpose:** Display supplementary skills and qualifications without cluttering main content
- **Elements:**
  - **Desktop:** Fixed right sidebar (550px width, scrollable)
  - **Mobile:** Collapsible accordion panels below main content
  - Four sections:
    1. Skills (soft skills)
    2. Technical Skills
    3. Trainings & Certifications
    4. Languages
- **UX Considerations:**
  - Desktop: Always visible, independently scrollable
  - Tablet: Reduced width (200px)
  - Mobile: Collapsed by default, expand on tap/click
  - Clear section headings
  - Scannable lists
  - Light background color (#f9f9f9) for differentiation
- **Accessibility:**
  - `<aside aria-label="Skills and qualifications">`
  - Keyboard accessible accordion buttons
  - ARIA attributes: `aria-expanded`, `aria-controls`
  - Proper button semantics for accordion triggers
  - Focus indicators on accordion headers
- **Security:** None specific

#### Footer
- **Purpose:** Provide social media links and copyright information
- **Elements:**
  - Social media icon links (LinkedIn, GitHub, X/Twitter, Facebook)
  - Copyright notice
  - Optional: Email contact duplicate
- **UX Considerations:**
  - Clear, accessible icon links
  - Professional presentation
  - Consistent with overall design
  - Adequate spacing between icons
  - Mobile: Responsive icon sizing
- **Accessibility:**
  - ARIA labels for icon links: `aria-label="LinkedIn profile"`
  - Sufficient color contrast
  - Keyboard accessible
  - Focus indicators
- **Security:**
  - External links with `rel="noopener noreferrer"` to prevent window.opener attacks

#### Theme Toggle Component
- **Purpose:** Allow users to switch between light and dark modes
- **Elements:**
  - Toggle button in navigation bar
  - Icon representation (sun for light, moon for dark)
  - Visual state indicator
  - LocalStorage integration for persistence
- **UX Considerations:**
  - Easy to find and access
  - Clear icon representation
  - Smooth theme transitions (CSS transitions)
  - Respects system preference on first visit
  - State persists across sessions
- **Accessibility:**
  - `<button aria-label="Toggle dark mode" aria-pressed="false">`
  - Keyboard accessible (Tab, Space/Enter)
  - Focus indicator visible
  - State announced to screen readers
- **Security:**
  - Client-side only (LocalStorage is safe for preferences)

#### Back-to-Top Button
- **Purpose:** Provide quick navigation to top of page
- **Elements:**
  - Floating button (fixed position, bottom-right)
  - Up arrow icon
  - Show/hide based on scroll position
- **UX Considerations:**
  - Appears after scrolling past hero section (>500px)
  - Smooth scroll to top animation
  - Not intrusive (positioned in corner)
  - Appropriate z-index (above content, below modals)
  - Mobile: Smaller size, adjusted position
- **Accessibility:**
  - `<button aria-label="Back to top">`
  - Keyboard accessible
  - Focus indicator
  - Not in tab order when hidden (display: none)
- **Security:** None specific

### 2.2 Error View (error404.html)

**Path:** `/404` or any non-existent path

**Main Purpose:** Handle 404 errors gracefully and guide users back to main content

**Key Information to Display:**
- Friendly error message
- Explanation
- Link to homepage

**Key View Components:**
- Centered container
- Large "404" or "Page not found" heading
- Explanatory text
- Prominent "Go to Homepage" link
- Maintains consistent branding

**UX Considerations:**
- Simple, uncluttered design
- Clear call-to-action
- Maintains theme support
- Helpful, not frustrating

**Accessibility:**
- Proper heading hierarchy
- Descriptive link text
- Keyboard accessible

**Security:** None specific

## 3. User Journey Map

### 3.1 Primary Journey: First-Time Visitor

**Step 1: Landing (Hero Section)**
- User arrives at the page
- Sees name, professional title, and tagline
- Gets immediate understanding of identity and role
- First impression formed

**Decision Point:** Continue scrolling or navigate to specific section

**Step 2: Navigation Decision**
User can:
- **Option A:** Scroll naturally through all sections (exploratory)
- **Option B:** Use navigation menu to jump to specific section (goal-oriented)
- **Option C:** Adjust theme preference if needed

**Step 3: Content Exploration**

**3a. Scroll Path (Exploratory User):**
1. About Me → Quick professional overview, contact info visible
2. Experience → Detailed work history, scans timeline visually
3. Education → Academic credentials
4. Interests → Personal touch
5. Skills (Sidebar or Accordions) → Supplementary qualifications

**3b. Direct Navigation (Goal-Oriented User):**
1. Clicks "Experience" in navigation
2. Smooth scrolls to Experience section
3. Reviews specific information
4. May use back-to-top button to return
5. May navigate to another section

**Step 4: Engagement**
- User reads content relevant to their needs
- Scans timeline for specific positions
- Reviews technical skills in sidebar
- Checks certifications and education

**Step 5: Action**
User may:
- Click email link to initiate contact (opens email client with pre-filled subject)
- Click social media icons to view profiles
- Bookmark page for later reference
- Share link with others (recruiter, colleague)

**Step 6: Exit**
- User satisfied with information
- Closes tab or navigates away
- May return later for reference

### 3.2 Secondary Journey: Returning Visitor

**Step 1: Direct Access**
- User knows what they're looking for
- Uses browser bookmark or direct URL

**Step 2: Quick Navigation**
- Uses navigation menu to jump directly to target section
- Example: Recruiter wants to verify specific job dates

**Step 3: Targeted Review**
- Scans specific section
- May verify information
- May use Ctrl+F to find specific keywords

**Step 4: Quick Contact**
- Clicks email or social media link
- Takes action to reach out

### 3.3 Edge Case Journeys

**Journey A: 404 Error**
1. User lands on non-existent page (typo, old link)
2. Sees friendly 404 message
3. Clicks "Go to Homepage" link
4. Lands on main page, continues normal journey

**Journey B: Mobile User**
1. Lands on mobile device
2. Experiences different layout (no sidebar)
3. Scrolls through main content
4. Scrolls to bottom, sees collapsible skill sections
5. Taps to expand skills, technical skills, etc.
6. Uses back-to-top button to navigate quickly

**Journey C: Accessibility User (Screen Reader)**
1. Screen reader announces page title
2. User hears "Skip to content" link, activates it
3. Jumps directly to main content
4. Navigates by headings (H1, H2, H3)
5. Hears descriptive ARIA labels for buttons and links
6. Activates links via keyboard (Enter)

**Journey D: Theme-Conscious User**
1. Lands on page, default theme loads (based on system preference)
2. Prefers different theme
3. Locates theme toggle in navigation
4. Clicks to switch theme
5. Preference saved to LocalStorage
6. Returns later, preferred theme loads automatically

## 4. Layout and Navigation Structure

### 4.1 Desktop Layout (≥992px)

```
┌─────────────────────────────────────────────────────────────┐
│ Navigation Bar (Sticky, z-index: 100)                       │
│ [Skip to content] [Name/Logo] [Experience|Education|        │
│ Interests ▼] [Theme Toggle ☀/☾]                            │
├───────────────────────────────────┬─────────────────────────┤
│                                   │                         │
│ Hero Section (Full Width)         │                         │
│ [Background Image]                │                         │
│ Name & Professional Title         │                         │
│                                   │                         │
├───────────────────────────────────┤                         │
│                                   │                         │
│ About Me Section                  │   Fixed Sidebar         │
│ ┌─────────────┬──────────────┐   │   (550px width)         │
│ │ Summary &   │ Profile      │   │                         │
│ │ Contact     │ Photo        │   │   ┌─────────────────┐   │
│ └─────────────┴──────────────┘   │   │ Skills          │   │
│                                   │   │ • Relationship  │   │
├───────────────────────────────────┤   │ • Engagement    │   │
│                                   │   │ ...             │   │
│ Experience Section                │   ├─────────────────┤   │
│ ┌─────────────────────────────┐   │   │ Technical Skills│   │
│ │ Timeline | Job Card         │   │   │ • Linux         │   │
│ │    ●────┐ [Company]         │   │   │ • Docker        │   │
│ │         │ [Title]           │   │   │ ...             │   │
│ │         │ [Dates]           │   │   ├─────────────────┤   │
│ │    ●────┤ • Responsibilities│   │   │ Trainings       │   │
│ │         │ [Company]         │   │   │ • AiDevs2       │   │
│ │         │ ...               │   │   │ • Prince2       │   │
│ └─────────────────────────────┘   │   │ ...             │   │
│                                   │   ├─────────────────┤   │
├───────────────────────────────────┤   │ Languages       │   │
│                                   │   │ • English       │   │
│ Education Section                 │   │ • Spanish       │   │
│ [Institution] [Degree]            │   │ ...             │   │
│                                   │   └─────────────────┘   │
├───────────────────────────────────┤                         │
│                                   │                         │
│ Interests Section                 │                         │
│                                   │                         │
├───────────────────────────────────┴─────────────────────────┤
│ Footer                                                      │
│ [LinkedIn] [GitHub] [Twitter] [Facebook]    © 2023 MK      │
└─────────────────────────────────────────────────────────────┘
                                                   [↑ Back to Top]
```

### 4.2 Mobile Layout (<768px)

```
┌─────────────────────────┐
│ Navigation Bar (Sticky) │
│ [Name] [Menu ▼] [☾]     │
├─────────────────────────┤
│                         │
│ Hero Section            │
│ [Background Image]      │
│ Name                    │
│ Title                   │
│                         │
├─────────────────────────┤
│                         │
│ About Me Section        │
│                         │
│ [Summary Text]          │
│                         │
│ [Contact Info]          │
│                         │
│ [Profile Photo]         │
│                         │
├─────────────────────────┤
│                         │
│ Experience (Timeline)   │
│                         │
│ ● [Company]             │
│   [Title]               │
│   [Dates]               │
│   • Responsibilities    │
│                         │
│ ● [Company]             │
│   ...                   │
│                         │
├─────────────────────────┤
│                         │
│ Education               │
│ [Institution]           │
│ [Degree]                │
│ ...                     │
│                         │
├─────────────────────────┤
│                         │
│ Interests               │
│ [Text]                  │
│                         │
├─────────────────────────┤
│ ▼ Skills                │
│ (Tap to expand)         │
├─────────────────────────┤
│ ▼ Technical Skills      │
│ (Tap to expand)         │
├─────────────────────────┤
│ ▼ Trainings             │
│ (Tap to expand)         │
├─────────────────────────┤
│ ▼ Languages             │
│ (Tap to expand)         │
├─────────────────────────┤
│ Footer                  │
│ [Social Icons]          │
│ © 2023 MK               │
└─────────────────────────┘
      [↑]
```

### 4.3 Navigation Behavior

#### Sticky Navigation
- Remains at top during scroll (position: sticky or fixed)
- Provides constant access to section links and theme toggle
- Proper z-index (z-index: 100) to stay above content
- Responsive height adjustment

#### Section Navigation
- **Desktop:** Dropdown menu in navigation bar
  - Hover or click to reveal section links
  - Links: Experience, Education, Interests
- **Mobile:** Dropdown select or collapsible menu
  - Tap to reveal section links
  - Touch-friendly tap targets (min 44x44px)
- **Behavior:**
  - Smooth scroll to target section
  - Scroll offset accounts for sticky nav height
  - Updates active state in menu
  - Closes dropdown after selection (mobile)

#### Visual Feedback
- **Active Section Highlighting:**
  - Current section highlighted in navigation menu
  - Implemented via intersection observer or scroll position
  - Visual indicator (underline, bold, color change)
- **Scroll Position:**
  - Back-to-top button appears after scrolling past hero (>500px)
  - Fade-in/fade-out animation
- **Interactive States:**
  - Hover: Subtle background color change, underline
  - Focus: Visible outline (2px solid, high contrast)
  - Active: Distinct styling to show current selection

#### Scroll Behavior
- **Smooth Scrolling:**
  - CSS: `html { scroll-behavior: smooth; }`
  - JavaScript fallback for browsers without support
- **Scroll Margin:**
  - CSS: `section { scroll-margin-top: 80px; }` (height of sticky nav)
  - Ensures section headings aren't hidden behind nav
- **Back-to-Top Button:**
  - Appears when scroll position > 500px
  - Smooth scroll to top on click
  - Positioned bottom-right (fixed, z-index: 99)

### 4.4 Responsive Breakpoints

| Breakpoint | Range | Key Changes |
|------------|-------|-------------|
| Mobile | 0-767px | Single column, sidebar → accordions at bottom, reduced spacing, smaller typography, stacked layouts |
| Tablet | 768-991px | Reduced sidebar (200px), condensed navigation, medium spacing |
| Desktop | 992px+ | Full sidebar (550px), complete navigation, optimal spacing, multi-column layouts |

### 4.5 Navigation Accessibility

- **Skip Links:** `<a href="#main-content" class="skip-link">Skip to content</a>` (visually hidden, keyboard accessible)
- **ARIA Landmarks:** `<nav>`, `<main>`, `<aside>`, `<footer>`
- **Keyboard Navigation:**
  - Tab: Move between interactive elements
  - Enter/Space: Activate links and buttons
  - Escape: Close dropdowns/menus
- **Focus Management:**
  - Visible focus indicators (2px outline)
  - Logical tab order
  - Focus moves to target section on navigation

## 5. Key Components

### 5.1 Card Component

**Used for:** Job experience entries, Education entries

**Structure:**
```
Card
├─ Header
│  ├─ Title (Company or Institution)
│  └─ Subtitle (Job Title or Degree)
├─ Body
│  ├─ Date Range
│  ├─ Description/Responsibilities (list)
│  └─ Technologies/Tools (if applicable)
└─ Footer (optional)
   └─ Tags or additional metadata
```

**Variants:**
- **Timeline Card:** Includes visual timeline marker (dot/line)
- **Simple Card:** No timeline decoration (used for education)

**Styling:**
- Consistent padding and margins
- Subtle background or border
- Responsive typography
- Hover state (subtle shadow or highlight)

**Accessibility:**
- Semantic HTML (`<article>` or `<section>`)
- Proper heading hierarchy
- List markup for bullet points

### 5.2 Timeline Connector Component

**Used for:** Visual timeline in Experience section

**Structure:**
- Vertical line connecting experience cards
- Date markers (dots or circles)
- Responsive design (simplified on mobile)

**Styling:**
- Line: 2-3px solid, accent color
- Dots: 12-16px circles, filled
- Contrasting colors for different periods (optional)
- CSS-based (not critical content)

**Responsive:**
- Desktop: Full timeline on left side
- Mobile: Simplified, minimal decorations

**Accessibility:**
- Decorative only (CSS ::before/::after)
- Not announced by screen readers
- Content remains accessible without visual timeline

### 5.3 Button Component

**Used for:** Theme toggle, Back-to-top, Contact actions, Navigation links

**Variants:**
- **Icon Button:** Contains only icon (theme toggle, back-to-top)
- **Text Button:** Contains text label
- **Link Button:** Styled link that looks like button

**States:**
- Default: Base styling
- Hover: Background color change, slight scale
- Focus: Visible outline (2px, high contrast)
- Active: Depressed appearance
- Disabled: Reduced opacity, no pointer events (if applicable)

**Styling:**
- Consistent border-radius
- Adequate padding (min 8px)
- Sufficient color contrast
- Touch-friendly size (min 44x44px on mobile)

**Accessibility:**
- Semantic `<button>` or `<a>` element
- ARIA labels for icon buttons
- Keyboard accessible (Tab, Enter/Space)
- Focus indicators
- Disabled state communicated to screen readers

### 5.4 Icon Component

**Used for:** Social media links, Theme toggle, Back-to-top, Timeline markers

**Implementation:**
- SVG format (scalable, accessible)
- Inline SVG or SVG sprite
- Consistent sizing (24x24px, 32x32px, 48x48px)

**Styling:**
- Fill/stroke colors match theme
- Hover states (color change, slight scale)
- Proper alignment (vertical-align or flexbox)

**Accessibility:**
- ARIA labels on parent link/button
- SVG has `aria-hidden="true"` (decorative)
- Text alternative provided via ARIA label

**Example:**
```html
<a href="https://linkedin.com/..." aria-label="LinkedIn profile">
  <svg aria-hidden="true">...</svg>
</a>
```

### 5.5 Accordion Component (Mobile)

**Used for:** Sidebar content on mobile devices

**Structure:**
```
Accordion
├─ Accordion Item
│  ├─ Header/Trigger (button)
│  └─ Panel (collapsible content)
├─ Accordion Item
│  └─ ...
```

**Behavior:**
- Collapsed by default
- Expands on click/tap
- Multiple panels can be open simultaneously
- Smooth expand/collapse animation

**Styling:**
- Clear visual indicator (arrow, chevron)
- Distinct header (clickable area)
- Adequate padding
- Border or separation between items

**Accessibility:**
- `<button aria-expanded="false" aria-controls="panel-id">Header</button>`
- `<div id="panel-id" role="region" aria-labelledby="header-id">Content</div>`
- Keyboard accessible (Tab, Enter/Space, Arrow keys optional)
- Focus indicators
- State changes announced to screen readers

### 5.6 Navigation Menu Component

**Desktop:** Inline navigation with dropdown

**Structure:**
```
Nav Menu
├─ Logo/Name Link
├─ Section Links
│  └─ Dropdown (Experience, Education, Interests)
└─ Theme Toggle Button
```

**Mobile:** Condensed menu with dropdown or hamburger

**Structure:**
```
Nav Menu
├─ Logo/Name
├─ Menu Button (☰)
│  └─ Dropdown Panel
│     ├─ Experience Link
│     ├─ Education Link
│     └─ Interests Link
└─ Theme Toggle Button
```

**Behavior:**
- Sticky positioning
- Smooth scroll on link click
- Active section highlighted
- Dropdown closes after selection

**Accessibility:**
- `<nav aria-label="Main navigation">`
- Proper button/link semantics
- Keyboard navigable
- ARIA attributes for dropdown state

### 5.7 Section Container Component

**Used for:** All major content sections

**Structure:**
- Consistent max-width (container class)
- Responsive padding
- Proper spacing between sections

**Styling:**
- Max-width: 1200px (desktop)
- Padding: 3rem 1rem (desktop), 1rem (mobile)
- Margin-bottom: 3rem (spacing between sections)

**Accessibility:**
- Semantic HTML5 elements (`<section>`, `<article>`)
- Proper heading hierarchy
- ARIA labels if needed

### 5.8 Skill List Component

**Used for:** Sidebar/accordion skill lists

**Structure:**
```
Skill Section
├─ Heading (h4)
└─ List (ul)
   ├─ Skill Item (li)
   ├─ Skill Item (li)
   └─ ...
```

**Styling:**
- Unordered list with custom bullets (square)
- Compact line-height (1.2)
- Smaller font size (0.9em)
- Adequate spacing

**Accessibility:**
- Semantic list markup
- Proper heading levels
- Readable text size

## 6. Accessibility Implementation

### 6.1 WCAG 2.1 AA Compliance Checklist

#### Perceivable
- ✓ Text alternatives for all images (alt attributes)
- ✓ Color contrast ratio ≥ 4.5:1 for normal text, ≥ 3:1 for large text
- ✓ Text resizable up to 200% without loss of functionality
- ✓ Responsive design adapts to different viewport sizes
- ✓ Visual focus indicators for interactive elements

#### Operable
- ✓ All functionality available via keyboard
- ✓ Skip to content link for keyboard users
- ✓ No keyboard traps
- ✓ Sufficient time for reading and interaction
- ✓ Descriptive link text (no "click here")
- ✓ Focus order follows logical reading order
- ✓ Multiple ways to navigate (scroll, section links)

#### Understandable
- ✓ Lang attribute on HTML element (`<html lang="en">`)
- ✓ Consistent navigation across pages
- ✓ Clear error messages (404 page)
- ✓ Labels and instructions for interactive elements
- ✓ Predictable behavior (no unexpected changes)

#### Robust
- ✓ Valid HTML5 markup
- ✓ ARIA landmarks (nav, main, footer, aside)
- ✓ ARIA labels for icon buttons and links
- ✓ Compatible with assistive technologies
- ✓ Semantic HTML elements

### 6.2 Specific ARIA Implementation

```html
<!-- Skip Link -->
<a href="#main-content" class="skip-link">Skip to content</a>

<!-- Navigation -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="#experience">Experience</a></li>
    <li><a href="#education">Education</a></li>
    <li><a href="#interests">Interests</a></li>
  </ul>
  <button aria-label="Toggle dark mode" aria-pressed="false">
    <svg aria-hidden="true"><!-- sun/moon icon --></svg>
  </button>
</nav>

<!-- Main Content -->
<main id="main-content">
  <!-- Content sections -->
</main>

<!-- Sidebar -->
<aside aria-label="Skills and qualifications">
  <!-- Skill sections -->
</aside>

<!-- Accordion (Mobile) -->
<button aria-expanded="false" aria-controls="skills-panel" id="skills-button">
  Skills
</button>
<div id="skills-panel" role="region" aria-labelledby="skills-button">
  <!-- Skills content -->
</div>

<!-- Social Links -->
<a href="https://linkedin.com/..." aria-label="LinkedIn profile" rel="noopener noreferrer">
  <svg aria-hidden="true"><!-- LinkedIn icon --></svg>
</a>

<!-- Back to Top -->
<button aria-label="Back to top" class="back-to-top">
  <svg aria-hidden="true"><!-- up arrow icon --></svg>
</button>
```

### 6.3 Keyboard Navigation Flow

1. Skip to content link (visible on focus)
2. Navigation: Logo/Name
3. Navigation: Section links (Tab through)
4. Navigation: Theme toggle button
5. Main content: Headings navigable via screen reader shortcuts
6. Interactive elements: Links, buttons (in document order)
7. Sidebar (desktop) or Accordions (mobile): Keyboard accessible
8. Footer: Social media links
9. Back-to-top button

**Keyboard Shortcuts:**
- **Tab:** Next interactive element
- **Shift+Tab:** Previous interactive element
- **Enter/Space:** Activate link or button
- **Escape:** Close dropdown/menu (if open)
- **Arrow keys:** Navigate within accordion (optional enhancement)

## 7. Performance Optimizations

### 7.1 Image Optimization

**Hero Background Image:**
- **Format:** WebP with JPEG fallback
- **Responsive sizes:**
  - Mobile: 800px width
  - Tablet: 1200px width
  - Desktop: 2000px width
- **Implementation:** CSS media queries or `<picture>` element
- **Compression:** 80% quality, optimized file size
- **Lazy loading:** Not needed (above the fold), but use for profile image

**Profile Image:**
- **Format:** WebP with JPEG fallback
- **Size:** Max 400px width (display size 200px)
- **Lazy loading:** `<img loading="lazy">`
- **Alt text:** "Marcin Kamiński, Technical Product Owner"

**Social Media Icons:**
- **Format:** SVG (inline or sprite)
- **Benefits:** Scalable, small file size, theme-able

### 7.2 CSS Optimization

- **Pico CSS via CDN:** Cached by browsers, fast delivery
- **Custom CSS:** Minified in production
- **Critical CSS:** Inline above-the-fold styles (optional)
- **Reduced specificity:** Faster rendering
- **CSS variables:** Efficient theme switching

### 7.3 JavaScript Optimization

- **Minimal JS:** Only theme switcher and minimal interactivity
- **Deferred loading:** `<script defer src="..."></script>`
- **No external libraries:** Vanilla JS, lightweight
- **LocalStorage:** Efficient theme persistence

### 7.4 General Optimizations

- **HTTP/2:** Multiplexing for parallel downloads
- **Gzip/Brotli compression:** Server-side compression
- **Caching headers:** Proper cache-control for static assets
- **Minimal DOM complexity:** Fewer elements, faster rendering
- **No render-blocking resources:** Async/defer scripts, inline critical CSS

### 7.5 Performance Metrics Goals

- **First Contentful Paint (FCP):** < 1.5s
- **Largest Contentful Paint (LCP):** < 2.5s
- **Cumulative Layout Shift (CLS):** < 0.1
- **First Input Delay (FID):** < 100ms
- **Time to Interactive (TTI):** < 3s

## 8. Theme Implementation

### 8.1 Light Theme

**Color Palette:**
- Background: #ffffff or #f5f5f5
- Text: #333333 or #1a1a1a
- Headings: #000000
- Links: #007bff (Pico CSS primary)
- Borders: #e0e0e0
- Sidebar: #f9f9f9

**Visual Style:**
- Clean, professional
- Subtle shadows for depth
- High contrast for readability

### 8.2 Dark Theme

**Color Palette:**
- Background: #1a1a1a or #121212
- Text: #e0e0e0 or #ffffff
- Headings: #ffffff
- Links: #4da6ff (adjusted for dark mode)
- Borders: #333333
- Sidebar: #2a2a2a

**Visual Style:**
- Reduced eye strain in low light
- Adjusted shadows (lighter, not darker)
- Maintains contrast ratios

### 8.3 Theme Switching

**CSS Custom Properties:**
```css
:root {
  --bg-color: #ffffff;
  --text-color: #333333;
  --heading-color: #000000;
  --link-color: #007bff;
  --border-color: #e0e0e0;
}

[data-theme="dark"] {
  --bg-color: #1a1a1a;
  --text-color: #e0e0e0;
  --heading-color: #ffffff;
  --link-color: #4da6ff;
  --border-color: #333333;
}

body {
  background-color: var(--bg-color);
  color: var(--text-color);
}
```

**JavaScript Logic:**
1. Check LocalStorage for saved preference
2. If no preference, detect system preference (`prefers-color-scheme`)
3. Apply theme by setting `data-theme` attribute on `<html>`
4. Toggle function switches theme and saves to LocalStorage
5. Smooth transition via CSS: `transition: background-color 0.3s, color 0.3s`

### 8.4 Theme Persistence

- **Storage:** LocalStorage key: `picoPreferredColorScheme`
- **Values:** `"light"`, `"dark"`, or `"auto"`
- **Behavior:** Persists across sessions, cleared if browser storage cleared

## 9. Security Considerations

### 9.1 External Links

**Implementation:**
```html
<a href="https://linkedin.com/..." target="_blank" rel="noopener noreferrer">
  LinkedIn
</a>
```

**Purpose:**
- `rel="noopener"`: Prevents access to `window.opener` in target page
- `rel="noreferrer"`: Doesn't send referrer information
- Protects against window.opener attacks and privacy leaks

### 9.2 Content Security

- **Static Site:** No server-side vulnerabilities, no database
- **No User Input:** No forms (currently), no XSS risk
- **External CDN:** Pico CSS from jsDelivr (consider adding SRI hash)

**Optional SRI Implementation:**
```html
<link rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css"
      integrity="sha384-..."
      crossorigin="anonymous">
```

### 9.3 Email Protection

**Current Implementation:**
```html
<a href="mailto:emkaminsk@gmail.com?subject=Inquiry%20from%20CV%20Website">
  emkaminsk@gmail.com
</a>
```

**Benefits:**
- Pre-filled subject reduces spam
- Visible email is acceptable for CV (intended for contact)

**Optional Enhancement (if spam becomes issue):**
- JavaScript-based email obfuscation
- Contact form with CAPTCHA (future)

### 9.4 HTTPS

**Requirement:**
- Site must be served over HTTPS (SSL/TLS certificate)
- Free certificates available via Let's Encrypt
- GitHub Pages provides HTTPS by default

**Benefits:**
- Encrypted data transmission
- Required for modern browser features
- Better SEO ranking

## 10. SEO and Structured Data

### 10.1 JSON-LD Structured Data

**Implementation:**
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Marcin Kamiński",
  "jobTitle": "Technical Product Owner",
  "description": "Product Owner for IT projects with 5 years of Agile experience facilitating communication between business and IT, with programming and testing skills, e-MBA, and background in finance and data science.",
  "url": "https://[domain].com",
  "email": "emkaminsk@gmail.com",
  "image": "https://[domain].com/img/MK03.jpg",
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
    "Data Science",
    "Banking",
    "Risk Management"
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

### 10.2 Meta Tags

**Basic Meta Tags:**
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="CV page for Marcin Kamiński, Technical Product Owner with both business and IT skills">
<meta name="author" content="Marcin Kamiński">
<title>Marcin Kamiński - Technical Product Owner CV</title>
```

**Open Graph Tags (Social Sharing):**
```html
<meta property="og:type" content="profile">
<meta property="og:title" content="Marcin Kamiński - Technical Product Owner">
<meta property="og:description" content="Product Owner with 5 years of Agile experience, programming skills, and e-MBA">
<meta property="og:url" content="https://[domain].com">
<meta property="og:image" content="https://[domain].com/img/MK03.jpg">
<meta property="profile:first_name" content="Marcin">
<meta property="profile:last_name" content="Kamiński">
```

**Twitter Card Tags:**
```html
<meta name="twitter:card" content="summary">
<meta name="twitter:site" content="@emkaminsk">
<meta name="twitter:title" content="Marcin Kamiński - Technical Product Owner">
<meta name="twitter:description" content="Product Owner with 5 years of Agile experience, programming skills, and e-MBA">
<meta name="twitter:image" content="https://[domain].com/img/MK03.jpg">
```

**Canonical URL:**
```html
<link rel="canonical" href="https://[domain].com/">
```

## 11. User Pain Points & Solutions

| Pain Point | Solution |
|------------|----------|
| **Can't find specific information quickly** | Section navigation menu, clear headings, visual timeline, table of contents feel |
| **Lost in long scroll** | Back-to-top button, sticky navigation, active section highlighting, smooth scroll with offset |
| **Difficult to read on mobile** | Responsive design, optimized typography (min 16px), collapsible sidebar content, adequate spacing |
| **Too bright/dark for current environment** | Theme toggle with light/dark modes, system preference detection, LocalStorage persistence |
| **Can't access sidebar on mobile** | Sidebar content moved to collapsible accordions at bottom of page, fully accessible |
| **Want to contact but don't have email client** | Visible email address, social media alternatives in footer, multiple contact options |
| **Difficult to understand chronology** | Visual timeline with clear date markers, newest-first ordering, visual flow |
| **Too much text, hard to scan** | Bullet points, clear headings, visual hierarchy, white space, cards for grouping |
| **Unclear which section is active** | Active state in navigation menu, scroll-based highlighting, visual feedback |
| **Accessibility barriers for keyboard users** | Skip to content link, keyboard accessible navigation, focus indicators, ARIA labels |
| **Accessibility barriers for screen reader users** | Semantic HTML, ARIA landmarks, descriptive labels, proper heading hierarchy |
| **Slow loading on mobile network** | Optimized images (WebP, responsive sizes), lazy loading, minimal CSS/JS, compressed assets |
| **Want to save or print CV** | Print-friendly CSS (future), semantic HTML for better copy/paste, clean structure |
| **Need to verify specific dates or details** | Clear formatting, consistent date formats, organized structure, Ctrl+F friendly |

## 12. Content Strategy

### 12.1 Information Hierarchy

1. **Primary (Hero, About Me):** Name, title, professional identity, contact
2. **Secondary (Experience, Education):** Detailed credentials and work history
3. **Tertiary (Skills, Interests):** Supplementary qualifications and personality
4. **Meta (Footer):** Social links, copyright, secondary navigation

### 12.2 Writing Tone

- Professional but approachable
- Achievement-oriented (specific results and responsibilities)
- Specific (technologies, companies, dates)
- Concise but comprehensive
- Action verbs (Led, Developed, Implemented, Managed)

### 12.3 Content Structure

**Experience Entries:**
- Company name (bold, prominent)
- Job title (distinct but secondary)
- Date range (clear format: "Month Year - Month Year")
- 3-5 bullet points (achievements and responsibilities)
- Technologies/tools (italicized, at end)

**Education Entries:**
- Institution name (bold)
- Degree type (Master, eMBA, etc.)
- Date range
- Notable achievements or specializations

**Skills:**
- Categorized clearly (Skills, Technical Skills, Trainings, Languages)
- Scannable lists
- Specific rather than vague

## 13. Future Enhancements (Out of Scope for MVP)

- Print-friendly CSS stylesheet for PDF generation
- Multi-language support (Polish/English toggle)
- Contact form with serverless backend (Formspree, Netlify Forms)
- Blog or portfolio section
- Analytics integration (privacy-respecting)
- Progressive Web App (PWA) capabilities
- Downloadable PDF version of CV
- Testimonials or recommendations section
- Project portfolio showcase
- Dark mode auto-switch based on time of day

---

**Document Version:** 1.0
**Last Updated:** 2025-11-16
**Author:** UI Architecture Planning Team
**Status:** Ready for Implementation
