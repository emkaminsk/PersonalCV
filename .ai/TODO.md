# PersonalCV MVP Development Plan

## Overview

This document outlines the comprehensive development plan for implementing the PersonalCV MVP based on the UI Architecture specification. The plan is organized into phases, with each phase containing specific tasks that build upon previous work.

**Project Goal:** Transform the current PersonalCV website into a fully accessible, performant, and user-friendly MVP that meets WCAG 2.1 AA standards.

**Timeline:** Estimated 3-4 weeks for full implementation
**Priority:** High-priority items marked with 🔴, Medium with 🟡, Low with 🟢

---

## Phase 1: Foundation & Project Setup

**Duration:** 2-3 days
**Goal:** Establish solid foundation with proper structure and tooling

### Tasks

- [ ] 🔴 **1.1** Review and audit current codebase structure
  - Assess existing HTML structure
  - Review CSS organization
  - Identify technical debt

- [ ] 🔴 **1.2** Set up development environment
  - Configure local server (Python SimpleHTTPServer or Node http-server)
  - Set up browser DevTools for testing
  - Install accessibility testing tools (axe DevTools, Lighthouse)

- [ ] 🟡 **1.3** Create project documentation structure
  - Ensure `.ai/` directory exists
  - Document development workflow
  - Create changelog template

- [ ] 🔴 **1.4** Optimize image assets
  - Convert hero background to WebP with JPEG fallback
  - Create responsive image sizes (800px, 1200px, 2000px)
  - Convert profile photo to WebP with JPEG fallback
  - Compress all images (80% quality)
  - Optimize social media SVG icons

- [ ] 🔴 **1.5** Set up semantic HTML structure
  - Review and update HTML5 semantic elements
  - Ensure proper document outline
  - Add lang attribute to `<html>` tag
  - Verify proper nesting and validation

**Deliverables:**
- ✅ Clean, validated HTML structure
- ✅ Optimized image assets
- ✅ Development environment configured
- ✅ Documentation structure in place

---

## Phase 2: Core Layout & Responsive Design

**Duration:** 4-5 days
**Goal:** Implement responsive layout with proper breakpoints

### Tasks

- [ ] 🔴 **2.1** Implement responsive grid system
  - Configure CSS Grid for main layout
  - Set up Flexbox for component layouts
  - Define breakpoints (Mobile <768px, Tablet 768-991px, Desktop ≥992px)
  - Test layout at all breakpoints

- [ ] 🔴 **2.2** Create fixed sidebar (desktop) layout
  - Implement fixed positioning for sidebar
  - Set sidebar width (550px desktop, 200px tablet)
  - Make sidebar independently scrollable
  - Style sidebar sections with light background (#f9f9f9)

- [ ] 🔴 **2.3** Implement mobile accordion system
  - Hide sidebar on mobile (<768px)
  - Create accordion HTML structure
  - Move sidebar content to bottom of page on mobile
  - Implement four accordion panels: Skills, Technical Skills, Trainings, Languages

- [ ] 🔴 **2.4** Responsive typography system
  - Define fluid typography scale
  - Set minimum font sizes (16px mobile)
  - Implement heading hierarchy (h1-h4)
  - Test text readability at all sizes

- [ ] 🟡 **2.5** Spacing and layout refinements
  - Implement consistent padding/margins
  - Define CSS custom properties for spacing
  - Create section containers with max-width
  - Ensure proper white space

**Deliverables:**
- ✅ Fully responsive layout (mobile, tablet, desktop)
- ✅ Fixed sidebar on desktop
- ✅ Mobile accordion system functional
- ✅ Responsive typography implemented

---

## Phase 3: Navigation & Interaction

**Duration:** 3-4 days
**Goal:** Implement navigation system with smooth scrolling and theme support

### Tasks

- [ ] 🔴 **3.1** Implement sticky navigation bar
  - Set navigation to sticky/fixed position
  - Configure proper z-index (100)
  - Style navigation for both themes
  - Ensure navigation stays above content

- [ ] 🔴 **3.2** Create section navigation dropdown
  - Build dropdown menu for sections (Experience, Education, Interests)
  - Desktop: Hover/click dropdown
  - Mobile: Touch-friendly dropdown
  - Close dropdown after selection

- [ ] 🔴 **3.3** Implement smooth scrolling
  - Add CSS: `scroll-behavior: smooth`
  - Implement JavaScript fallback for unsupported browsers
  - Configure scroll-margin-top for sections (80px offset)
  - Test smooth scroll on all links

- [ ] 🔴 **3.4** Active section highlighting
  - Implement Intersection Observer API
  - Highlight active section in navigation
  - Update on scroll
  - Visual indicator (underline, bold, or color change)

- [ ] 🔴 **3.5** Implement theme toggle functionality
  - Create theme toggle button in navigation
  - Add sun/moon icon (SVG)
  - Wire up JavaScript theme switcher (already exists, needs integration)
  - Add button to HTML navigation
  - Test theme switching
  - Verify LocalStorage persistence

- [ ] 🔴 **3.6** Create back-to-top button
  - Build floating button (bottom-right)
  - Add up arrow icon (SVG)
  - Show/hide based on scroll position (>500px)
  - Smooth scroll to top on click
  - Style for both themes
  - Responsive positioning

- [ ] 🟡 **3.7** Skip to content link
  - Add skip link as first element in HTML
  - Style to be visually hidden but keyboard accessible
  - Link to `#main-content`
  - Test keyboard navigation

**Deliverables:**
- ✅ Sticky navigation with section links
- ✅ Smooth scrolling with active section highlighting
- ✅ Theme toggle fully functional
- ✅ Back-to-top button working
- ✅ Skip to content link for accessibility

---

## Phase 4: Content Sections Implementation

**Duration:** 5-6 days
**Goal:** Build all content sections with proper styling and structure

### Tasks

- [ ] 🔴 **4.1** Hero section enhancement
  - Implement responsive background images
  - Use CSS media queries for different sizes
  - Ensure text contrast over background
  - Add proper heading structure (h1, h2)
  - Mobile: Reduce padding, smaller text

- [ ] 🔴 **4.2** About Me section
  - Create two-column layout (text + photo on desktop)
  - Style professional summary text
  - Implement contact information block
  - Enhance mailto link with pre-filled subject
  - Add profile image with proper caption
  - Mobile: Stack layout (text, then photo)

- [ ] 🔴 **4.3** Experience section with timeline
  - Design vertical timeline component
  - Create timeline markers (dots/lines)
  - Build job experience card component
  - Style company names (bold, prominent)
  - Format job titles, dates
  - Style responsibilities (bullet list)
  - Format technologies (italic)
  - Implement contrasting colors for periods
  - Mobile: Simplify timeline, left-align

- [ ] 🟡 **4.4** Add subtle scroll animations
  - Implement fade-in effects for timeline items
  - Use Intersection Observer for performance
  - Keep animations subtle (accessibility consideration)
  - Respect `prefers-reduced-motion` setting

- [ ] 🔴 **4.5** Education section
  - Create education card component
  - Style institution names (bold)
  - Format degree types, dates
  - List specializations and achievements
  - Match styling with experience section

- [ ] 🔴 **4.6** Interests section
  - Simple paragraph or list format
  - Style appropriately
  - Optional: Add icons for visual interest
  - Keep brief and professional

- [ ] 🔴 **4.7** Sidebar content sections
  - Style Skills section
  - Style Technical Skills section
  - Style Trainings section
  - Style Languages section
  - Ensure compact, scannable format
  - Custom bullet styles (square)

**Deliverables:**
- ✅ Hero section with responsive images
- ✅ About Me section with contact info
- ✅ Experience section with visual timeline
- ✅ Education section styled
- ✅ Interests section complete
- ✅ All sidebar sections styled

---

## Phase 5: Footer & Contact Elements

**Duration:** 1-2 days
**Goal:** Implement footer with social links

### Tasks

- [ ] 🔴 **5.1** Move social media links to footer
  - Remove social links from navigation (current placement)
  - Create footer component
  - Add social media icon links (LinkedIn, GitHub, Twitter, Facebook)
  - Ensure icons are accessible (ARIA labels)
  - Add `rel="noopener noreferrer"` to external links
  - Style for both themes

- [ ] 🔴 **5.2** Footer content
  - Add copyright notice
  - Optional: Add email contact
  - Ensure adequate spacing
  - Mobile-responsive layout

- [ ] 🟡 **5.3** Footer styling
  - Consistent with overall design
  - Proper padding and background
  - Icon hover effects
  - Adequate touch targets (44x44px mobile)

**Deliverables:**
- ✅ Social media links in footer
- ✅ Copyright and legal info
- ✅ Footer responsive design

---

## Phase 6: Accessibility Implementation

**Duration:** 3-4 days
**Goal:** Achieve WCAG 2.1 AA compliance

### Tasks

- [ ] 🔴 **6.1** ARIA landmarks and labels
  - Add `<nav aria-label="Main navigation">`
  - Add `<main id="main-content">`
  - Add `<aside aria-label="Skills and qualifications">`
  - Add `<footer>` element
  - Add ARIA labels to all icon buttons
  - Add ARIA labels to social media links

- [ ] 🔴 **6.2** Implement accordion accessibility
  - Add proper button semantics for accordion triggers
  - Add `aria-expanded` attribute (true/false)
  - Add `aria-controls` attribute
  - Add `role="region"` to accordion panels
  - Add `aria-labelledby` to panels
  - Implement keyboard navigation (Tab, Enter, Space)

- [ ] 🔴 **6.3** Keyboard navigation
  - Ensure all interactive elements are keyboard accessible
  - Implement visible focus indicators (2px outline)
  - Set logical tab order
  - Test with keyboard only (no mouse)
  - Ensure no keyboard traps

- [ ] 🔴 **6.4** Alt text for images
  - Add descriptive alt text to profile image
  - Background images treated as decorative (CSS)
  - SVG icons with `aria-hidden="true"` (labels on parent)
  - Test with screen reader

- [ ] 🔴 **6.5** Color contrast audit
  - Test all text for 4.5:1 contrast ratio (normal text)
  - Test large text for 3:1 contrast ratio
  - Test in both light and dark themes
  - Fix any contrast issues
  - Use tools: WebAIM Contrast Checker, axe DevTools

- [ ] 🔴 **6.6** Heading hierarchy
  - Ensure single h1 (name in hero)
  - Proper h2-h4 nesting
  - No skipped heading levels
  - Logical document outline

- [ ] 🟡 **6.7** Form accessibility (if contact form added in future)
  - Proper label association
  - Error messages
  - Required field indicators
  - (Not in current MVP, but plan ahead)

- [ ] 🔴 **6.8** Screen reader testing
  - Test with NVDA (Windows) or VoiceOver (Mac)
  - Verify all content is accessible
  - Check ARIA labels are announced correctly
  - Verify skip link works
  - Test accordion interaction

**Deliverables:**
- ✅ All ARIA landmarks and labels implemented
- ✅ Keyboard navigation fully functional
- ✅ Color contrast meets WCAG 2.1 AA
- ✅ Screen reader compatible
- ✅ WCAG 2.1 AA compliance achieved

---

## Phase 7: Theme System Implementation

**Duration:** 2-3 days
**Goal:** Complete light/dark theme system with persistence

### Tasks

- [ ] 🔴 **7.1** Define CSS custom properties
  - Create variables for colors (background, text, headings, links, borders)
  - Light theme palette
  - Dark theme palette
  - Ensure proper contrast in both themes

- [ ] 🔴 **7.2** Theme toggle JavaScript
  - Integrate existing minimal-theme-switcher.js
  - Add theme toggle button to navigation
  - Implement toggle function
  - Save preference to LocalStorage
  - Load preference on page load

- [ ] 🔴 **7.3** System preference detection
  - Detect `prefers-color-scheme` media query
  - Apply system preference on first visit
  - Allow user override with toggle
  - Persist user choice

- [ ] 🔴 **7.4** Theme transitions
  - Add smooth CSS transitions for theme changes
  - Transition properties: background-color, color (0.3s)
  - Test performance of transitions
  - Respect `prefers-reduced-motion`

- [ ] 🟡 **7.5** Test theme in all sections
  - Verify readability in both themes
  - Check all interactive elements (buttons, links)
  - Test sidebar and accordions
  - Verify timeline and cards

**Deliverables:**
- ✅ Complete theme system with light/dark modes
- ✅ LocalStorage persistence
- ✅ System preference detection
- ✅ Smooth theme transitions

---

## Phase 8: Performance Optimization

**Duration:** 3-4 days
**Goal:** Optimize for fast loading and smooth performance

### Tasks

- [ ] 🔴 **8.1** Image optimization implementation
  - Implement WebP with JPEG fallback using `<picture>` element
  - Create responsive image sizes (srcset)
  - Add `loading="lazy"` to profile image
  - Ensure proper image dimensions in HTML
  - Test image loading performance

- [ ] 🔴 **8.2** CSS optimization
  - Minify custom.css for production
  - Remove unused CSS rules
  - Optimize selectors for performance
  - Consider critical CSS inlining (optional)

- [ ] 🔴 **8.3** JavaScript optimization
  - Minify minimal-theme-switcher.js
  - Add `defer` attribute to script tags
  - Ensure no render-blocking scripts
  - Minimize DOM manipulation

- [ ] 🟡 **8.4** HTTP/2 and compression
  - Ensure server supports HTTP/2 (if applicable)
  - Enable Gzip/Brotli compression
  - Set proper caching headers
  - Test with PageSpeed Insights

- [ ] 🟡 **8.5** Lazy loading implementation
  - Implement lazy loading for below-fold images
  - Use native `loading="lazy"` attribute
  - Test lazy loading behavior
  - Ensure fallback for unsupported browsers

- [ ] 🔴 **8.6** Performance testing
  - Run Lighthouse audit
  - Target: LCP < 2.5s, FID < 100ms, CLS < 0.1
  - Test on mobile device/network throttling
  - Fix any performance issues
  - Document performance metrics

**Deliverables:**
- ✅ Optimized images (WebP, responsive, lazy loading)
- ✅ Minified CSS and JavaScript
- ✅ Performance metrics meet targets
- ✅ Fast loading on mobile networks

---

## Phase 9: SEO & Metadata

**Duration:** 2-3 days
**Goal:** Optimize for search engines and social sharing

### Tasks

- [ ] 🔴 **9.1** JSON-LD structured data
  - Add Schema.org Person markup
  - Include: name, jobTitle, description, email, image
  - Add alumniOf (educational organizations)
  - Add worksFor (current employer)
  - Add sameAs (social media profiles)
  - Add knowsAbout (skills and expertise)
  - Add knowsLanguage (languages)
  - Validate with Google Rich Results Test

- [ ] 🔴 **9.2** Meta tags
  - Add/update description meta tag
  - Add author meta tag
  - Optimize title tag
  - Add canonical URL
  - Verify charset and viewport tags

- [ ] 🔴 **9.3** Open Graph tags
  - Add og:type (profile)
  - Add og:title
  - Add og:description
  - Add og:url
  - Add og:image
  - Add profile-specific tags (first_name, last_name)
  - Test with Facebook Debugger

- [ ] 🔴 **9.4** Twitter Card tags
  - Add twitter:card (summary)
  - Add twitter:site (@emkaminsk)
  - Add twitter:title
  - Add twitter:description
  - Add twitter:image
  - Test with Twitter Card Validator

- [ ] 🟡 **9.5** Sitemap and robots.txt
  - Create sitemap.xml (if applicable)
  - Create robots.txt
  - Submit to search engines (Google Search Console)

**Deliverables:**
- ✅ JSON-LD structured data implemented
- ✅ Complete meta tags (OG, Twitter)
- ✅ SEO-optimized content
- ✅ Social sharing previews working

---

## Phase 10: Testing & Quality Assurance

**Duration:** 4-5 days
**Goal:** Comprehensive testing across browsers, devices, and accessibility tools

### Tasks

- [ ] 🔴 **10.1** Cross-browser testing
  - Chrome/Edge (latest)
  - Firefox (latest)
  - Safari (latest)
  - Opera (latest)
  - Test core functionality in each browser
  - Document any browser-specific issues
  - Fix critical compatibility issues

- [ ] 🔴 **10.2** Responsive testing
  - Test on actual mobile devices (iOS, Android)
  - Test on tablet devices
  - Test at various viewport sizes (320px, 375px, 768px, 1024px, 1920px)
  - Use Chrome DevTools device emulation
  - Test touch interactions on mobile
  - Verify accordion functionality on mobile

- [ ] 🔴 **10.3** Accessibility audit
  - Run axe DevTools accessibility scan
  - Run Lighthouse accessibility audit
  - Run WAVE accessibility checker
  - Test with keyboard only (no mouse)
  - Test with screen reader (NVDA or VoiceOver)
  - Fix all critical and serious issues
  - Document and plan for minor issues

- [ ] 🔴 **10.4** Performance audit
  - Run Lighthouse performance audit
  - Run PageSpeed Insights (mobile and desktop)
  - Run WebPageTest
  - Verify Core Web Vitals (LCP, FID, CLS)
  - Test on slow 3G network throttling
  - Fix any performance regressions

- [ ] 🟡 **10.5** Usability testing
  - Test with real users (if possible)
  - Gather feedback on navigation
  - Check comprehension of timeline
  - Verify contact flow works
  - Test theme toggle usability
  - Document user feedback

- [ ] 🔴 **10.6** Content review
  - Proofread all text content
  - Verify all dates and information are accurate
  - Check for typos and grammatical errors
  - Ensure consistent formatting
  - Verify all links work (no 404s)

- [ ] 🔴 **10.7** Security review
  - Verify all external links have `rel="noopener noreferrer"`
  - Ensure HTTPS is enforced
  - Check for any exposed sensitive data
  - Verify email link implementation
  - (Optional) Add SRI hashes for CDN resources

**Deliverables:**
- ✅ Cross-browser compatibility verified
- ✅ Responsive design tested on real devices
- ✅ Accessibility audit passed (WCAG 2.1 AA)
- ✅ Performance audit passed
- ✅ All content reviewed and accurate
- ✅ Security best practices implemented

---

## Phase 11: Documentation & Deployment

**Duration:** 2-3 days
**Goal:** Document the project and deploy to production

### Tasks

- [ ] 🟡 **11.1** Code documentation
  - Add comments to complex CSS
  - Document JavaScript functions
  - Create component documentation (if reusable)
  - Document theme system

- [ ] 🔴 **11.2** Update README.md
  - Ensure README reflects current state
  - Update feature list
  - Add screenshots (optional)
  - Document any new dependencies

- [ ] 🟡 **11.3** Create CHANGELOG.md
  - Document all changes from original version
  - List new features
  - List improvements
  - List bug fixes

- [x] 🔴 **11.4** Deployment preparation

- [x] 🔴 **11.5** Deploy to production
  - Deploy site to hosting platform
  - Verify all assets load correctly
  - Test all functionality in production
  - Verify SSL certificate is valid
  - Test from different networks/locations

- [] 🔴 **11.6** Deployment automation
  - build Github Action workflow
  - test the automation

- [ ] 🔴 **11.7** Post-deployment testing
  - Run final Lighthouse audit in production
  - Test all links and navigation
  - Verify theme toggle works
  - Test on mobile device via production URL
  - Check social sharing previews

- [ ] 🟡 **11.8** Set up monitoring (optional)  
  - Uptime monitoring
  - Error tracking
  - Performance monitoring

**Deliverables:**
- ✅ Complete code documentation
- ✅ Updated README and CHANGELOG
- ✅ Site deployed to production
- ✅ Post-deployment testing passed
- ✅ Monitoring set up (optional)

---

## Phase 12: Polish & Refinement

**Duration:** 2-3 days
**Goal:** Final polish and address any remaining issues

### Tasks

- [ ] 🟡 **12.1** Visual polish
  - Fine-tune spacing and alignment
  - Ensure consistent styling throughout
  - Verify hover and focus states
  - Polish transitions and animations
  - Test in both themes

- [ ] 🟡 **12.2** Micro-interactions
  - Ensure smooth hover effects
  - Verify button states
  - Check accordion expand/collapse smoothness
  - Test smooth scrolling
  - Verify theme transition smoothness

- [ ] 🟡 **12.3** Address feedback
  - Gather feedback from stakeholders
  - Create list of refinement tasks
  - Prioritize and implement changes
  - Re-test after changes

- [ ] 🔴 **12.4** Final validation
  - Run HTML validator (W3C)
  - Run CSS validator
  - Run accessibility validator
  - Fix any validation errors
  - Document any warnings

- [ ] 🟡 **12.5** Browser cache management
  - Add cache-busting for CSS/JS (versioning)
  - Set appropriate cache headers
  - Test cache invalidation

**Deliverables:**
- ✅ Visually polished design
- ✅ Smooth micro-interactions
- ✅ Validated HTML and CSS
- ✅ All feedback addressed

---

## Future Enhancements (Post-MVP)

These items are out of scope for the MVP but should be considered for future iterations:

### High Priority (Next Version)
- [ ] Print-friendly CSS stylesheet for PDF generation
- [ ] Contact form with serverless backend (Formspree or Netlify Forms)
- [ ] Multi-language support (Polish/English toggle)
- [ ] Downloadable PDF version of CV

### Medium Priority
- [ ] Blog or articles section
- [ ] Project portfolio showcase
- [ ] Testimonials or recommendations section
- [ ] Progressive Web App (PWA) capabilities

### Low Priority
- [ ] Dark mode auto-switch based on time of day
- [ ] Advanced analytics integration
- [ ] A/B testing for content optimization
- [ ] CMS integration for easier content updates

---

## Success Criteria

The MVP will be considered complete when:

✅ **Functionality**
- All navigation works smoothly (section links, back-to-top, theme toggle)
- Mobile accordion system functions correctly
- Theme switching persists across sessions
- All links are functional and point to correct destinations

✅ **Accessibility**
- WCAG 2.1 AA compliance achieved
- Passes axe DevTools audit (0 critical/serious issues)
- Fully keyboard navigable
- Screen reader compatible
- Sufficient color contrast in both themes

✅ **Performance**
- Lighthouse Performance score ≥ 90
- LCP < 2.5s
- FID < 100ms
- CLS < 0.1
- Fast loading on mobile networks

✅ **Responsiveness**
- Works on mobile, tablet, and desktop
- Tested on actual devices
- No horizontal scrolling
- Touch-friendly on mobile

✅ **SEO**
- Structured data implemented (JSON-LD)
- Meta tags complete (OG, Twitter)
- Proper semantic HTML
- Indexed by search engines

✅ **Quality**
- Cross-browser compatible (Chrome, Firefox, Safari, Edge)
- Valid HTML and CSS (W3C)
- No console errors
- Clean, maintainable code

---

## Risk Management

### Potential Risks & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Browser compatibility issues | Medium | Medium | Test early and often, use progressive enhancement |
| Accessibility barriers | High | Low | Regular testing with screen readers, axe DevTools |
| Performance regressions | Medium | Medium | Regular Lighthouse audits, image optimization |
| Timeline overruns | Low | Medium | Prioritize MVP features, defer enhancements |
| Theme toggle conflicts | Low | Low | Test thoroughly, use well-tested library |
| Mobile responsive issues | Medium | Low | Mobile-first approach, test on real devices |

---

## Resource Requirements

### Tools & Services
- Local web server (Python, Node, or PHP)
- Browser DevTools (Chrome, Firefox)
- Accessibility testing: axe DevTools, WAVE, Lighthouse
- Screen reader: NVDA (Windows) or VoiceOver (Mac)
- Image optimization: Squoosh, ImageOptim, or similar
- Code editor: VS Code (recommended)

### External Dependencies
- Pico CSS v1 (CDN)
- No additional libraries required for MVP

### Hosting
- GitHub Pages (recommended, free with HTTPS)
- Netlify or Vercel (alternatives)
- Custom hosting with SSL certificate

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-16 | UI Architecture Team | Initial development plan created |

---

**Document Status:** Ready for Implementation
**Last Updated:** 2025-11-16
**Next Review:** After Phase 3 completion
