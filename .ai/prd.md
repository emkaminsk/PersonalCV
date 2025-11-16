# Product Requirements Document (PRD) - Personal CV Website

## 1. Product Overview

### 1.1 Product Name
Personal CV - Marcin Kamiński

### 1.2 Product Summary
A modern, responsive personal CV webpage showcasing professional experience, education, skills, and technical expertise. Built with a simple tech stack (HTML5, CSS3, JavaScript) to enable easy content updates while providing a professional web presence for hiring and networking purposes.

### 1.3 Product Vision
To provide a professional, accessible, and performant online CV that effectively showcases career achievements, technical skills, and professional identity to recruiters, potential employers, and professional contacts.

### 1.4 Target Users
- Recruiters searching for Technical Product Owner candidates
- Hiring managers evaluating professional background
- Professional network contacts seeking career information
- Potential clients assessing expertise and experience
- Colleagues and collaborators verifying professional credentials

### 1.5 Key Features
- Responsive design (mobile, tablet, desktop)
- Light/dark theme switching with system preference detection
- Visual timeline for work experience
- Fixed sidebar (desktop) with collapsible accordions (mobile)
- Smooth section navigation
- Social media integration
- WCAG 2.1 AA accessibility compliance
- Performance-optimized with Core Web Vitals targets

### 1.6 Success Metrics
- Page load time: LCP less than 2.5s
- Accessibility: WCAG 2.1 AA compliance (axe DevTools score: 0 critical issues)
- Performance: Lighthouse score greater than or equal to 90
- Responsiveness: Functional on all screen sizes (320px to 1920px+)
- Usability: All interactive elements keyboard accessible
- SEO: Proper structured data implementation (JSON-LD)

## 2. User Problem

### 2.1 Problem Statement
Technical professionals, particularly those in Product Owner and IT leadership roles, need an effective online presence to showcase their comprehensive experience, skills, and professional background. Traditional paper CVs or basic LinkedIn profiles often fail to:

- Provide comprehensive detail about work experience and technical skills
- Offer an engaging, easy-to-navigate presentation of career history
- Adapt to different viewing contexts (mobile, desktop, light/dark environments)
- Remain accessible to all users, including those using assistive technologies
- Load quickly on various network conditions
- Present a professional brand that stands out in competitive job markets

### 2.2 Current Pain Points

For job seekers:
- LinkedIn profiles have limited customization and formatting options
- PDF CVs are not responsive or interactive
- Updating CVs across multiple platforms is time-consuming
- Difficult to showcase both business and technical skills effectively
- No control over viewing experience (theme, navigation)

For recruiters and hiring managers:
- Difficulty quickly scanning lengthy work histories
- Hard to find specific skills or qualifications in dense text
- Poor mobile experience on many CV websites
- Inaccessible content for users with disabilities
- Slow-loading pages waste time

### 2.3 Solution Approach
A custom, single-page CV website that:
- Provides complete control over content presentation and branding
- Offers intuitive navigation with visual timeline and section links
- Adapts seamlessly to any device or screen size
- Respects user preferences (theme, accessibility needs)
- Loads quickly with optimized assets
- Remains easy to update without requiring complex build processes

### 2.4 Value Proposition

For the CV owner:
- Professional online presence that stands out
- Easy content updates (simple HTML editing)
- Full control over branding and presentation
- Better discoverability through SEO and structured data
- Analytics capability (future enhancement)

For viewers (recruiters, employers):
- Quick access to comprehensive professional information
- Easy navigation to specific sections of interest
- Pleasant viewing experience in any environment
- Fast loading even on mobile networks
- Accessible to all users regardless of abilities

## 3. Functional Requirements

### 3.1 Core Functionality

#### 3.1.1 Responsive Layout
The website must adapt to three primary breakpoints:
- Mobile (0-767px): Single column layout, stacked content, collapsible sections
- Tablet (768-991px): Reduced sidebar (200px), condensed spacing
- Desktop (992px+): Full layout with fixed sidebar (550px), optimal spacing

All content must remain accessible and functional at any viewport size between 320px and 2560px width.

#### 3.1.2 Theme System
The website must support two visual themes:
- Light theme: Professional appearance with high contrast (#ffffff background, #333333 text)
- Dark theme: Reduced eye strain in low light (#1a1a1a background, #e0e0e0 text)

Theme requirements:
- Detect system preference on first visit (prefers-color-scheme media query)
- Provide manual toggle button in navigation
- Persist user preference in LocalStorage
- Apply smooth transitions during theme changes (0.3s duration)
- Maintain WCAG 2.1 AA color contrast in both themes

#### 3.1.3 Navigation System
Primary navigation must include:
- Sticky navigation bar (always visible during scroll)
- Logo/name link (returns to top)
- Section navigation dropdown (Experience, Education, Interests)
- Theme toggle button with icon indicator
- Active section highlighting

Navigation behavior:
- Smooth scrolling to target sections
- Scroll offset to account for sticky navigation height (80px)
- Visual feedback for hover, focus, and active states
- Dropdown closes after section selection (mobile)
- Back-to-top button appears after scrolling past 500px

#### 3.1.4 Content Sections
The website must display the following sections in order:

1. Hero Section
   - Full-width background image (responsive)
   - Name (h1)
   - Professional title/tagline (h2)
   - Professional visual presentation

2. About Me Section
   - Two-column layout on desktop (text + photo)
   - Professional summary
   - Contact information (email link)
   - Profile photo
   - Single column on mobile

3. Experience Section
   - Visual timeline (vertical, chronological)
   - Job cards containing:
     - Company name (bold)
     - Job title
     - Employment dates
     - Responsibilities (bullet list)
     - Technologies used (italic)
   - Newest position first
   - Simplified timeline on mobile

4. Education Section
   - Education cards containing:
     - Institution name (bold)
     - Degree type
     - Date range
     - Specializations/achievements
   - Chronological order

5. Interests Section
   - Brief personal interests
   - Paragraph or list format
   - Humanizing element

6. Sidebar (Desktop) / Accordions (Mobile)
   Four sub-sections:
   - Skills (soft skills)
   - Technical Skills
   - Trainings and Certifications
   - Languages

   Desktop: Fixed right sidebar (550px), independently scrollable
   Tablet: Reduced sidebar (200px)
   Mobile: Collapsible accordions below main content

7. Footer
   - Social media icon links (LinkedIn, GitHub, Twitter, Facebook)
   - Copyright notice
   - Consistent styling with overall design

#### 3.1.5 Interactive Elements

Theme Toggle:
- Button with sun/moon icon
- Located in navigation bar
- ARIA labels for accessibility
- Updates icon based on current theme

Back-to-Top Button:
- Floating button (bottom-right corner)
- Appears when scrolled past 500px
- Up arrow icon
- Smooth scroll to top on click
- Responsive sizing

Accordion System (Mobile):
- Four collapsible panels for sidebar content
- Collapsed by default
- Expand/collapse on tap
- Multiple panels can be open simultaneously
- Smooth animation
- Proper ARIA attributes

Social Media Links:
- Icon buttons in footer
- Links to external profiles
- Hover effects
- Security attributes (rel="noopener noreferrer")

Section Navigation:
- Dropdown menu in navigation
- Smooth scroll to sections
- Close dropdown after selection

#### 3.1.6 Accessibility Features

Required accessibility implementations:
- Skip to content link (keyboard accessible, visually hidden)
- Semantic HTML5 elements (nav, main, aside, footer, article, section)
- ARIA landmarks and labels
- Keyboard navigation support (Tab, Enter, Space, Escape)
- Visible focus indicators (2px outline, high contrast)
- Alt text for all images
- Color contrast ratios: 4.5:1 (normal text), 3:1 (large text)
- Proper heading hierarchy (single h1, logical h2-h4)
- Screen reader compatibility
- Accessible accordion implementation
- Descriptive link text
- Lang attribute on HTML element

#### 3.1.7 Performance Requirements

Image optimization:
- WebP format with JPEG fallback
- Responsive image sizes (srcset)
- Hero background: 800px (mobile), 1200px (tablet), 2000px (desktop)
- Profile photo: max 400px width, lazy loading
- SVG icons for social media
- 80% quality compression

Code optimization:
- Minified CSS and JavaScript in production
- Deferred script loading
- Minimal external dependencies (only Pico CSS via CDN)
- No render-blocking resources

Performance targets:
- First Contentful Paint (FCP): less than 1.5s
- Largest Contentful Paint (LCP): less than 2.5s
- Cumulative Layout Shift (CLS): less than 0.1
- First Input Delay (FID): less than 100ms
- Time to Interactive (TTI): less than 3s

#### 3.1.8 SEO and Metadata

Required meta tags:
- Charset and viewport
- Description meta tag
- Author meta tag
- Title tag (optimized)
- Canonical URL

Open Graph tags:
- og:type (profile)
- og:title
- og:description
- og:url
- og:image
- profile:first_name
- profile:last_name

Twitter Card tags:
- twitter:card (summary)
- twitter:site
- twitter:title
- twitter:description
- twitter:image

JSON-LD structured data:
- Schema.org Person markup
- Properties: name, jobTitle, description, email, image
- alumniOf (educational institutions)
- worksFor (current employer)
- sameAs (social media profiles)
- knowsAbout (skills and expertise)
- knowsLanguage (languages with proficiency)

#### 3.1.9 Error Handling

Custom 404 page (error404.html):
- Friendly error message
- Explanation
- Link to homepage
- Maintains consistent branding and theme support
- Accessible design

#### 3.1.10 Security Requirements

All external links must include:
- rel="noopener" (prevent window.opener access)
- rel="noreferrer" (privacy protection)

Email link:
- Pre-filled subject to reduce spam
- Visible email address (acceptable for CV context)

HTTPS:
- Site must be served over HTTPS
- Valid SSL/TLS certificate

Optional enhancements:
- SRI (Subresource Integrity) hashes for CDN resources

### 3.2 Browser Compatibility
The website must be compatible with:
- Chrome/Edge (latest versions)
- Firefox (latest versions)
- Safari (latest versions)
- Opera (latest versions)
- Limited support for Internet Explorer 11 (graceful degradation)

Required browser features:
- CSS Grid and Flexbox
- CSS Custom Properties (CSS variables)
- LocalStorage API
- ES6 JavaScript (arrow functions, const/let, template literals)

### 3.3 Non-Functional Requirements

#### 3.3.1 Maintainability
- Simple tech stack (no build process required)
- Clear code comments for complex sections
- Consistent naming conventions
- Modular CSS organization
- Documented theme system

#### 3.3.2 Scalability
- Content can be easily added or modified
- Structure supports additional sections
- Theme system extensible
- Performance maintained with content growth

#### 3.3.3 Usability
- Intuitive navigation
- Clear visual hierarchy
- Scannable content (headings, bullets, white space)
- Consistent interaction patterns
- Responsive to user preferences

## 4. Product Boundaries

### 4.1 In Scope for MVP

Included features:
- Responsive design across all device sizes
- Light/dark theme system with persistence
- Fixed sidebar (desktop) and collapsible accordions (mobile)
- Visual timeline for work experience
- Smooth section navigation
- Social media integration
- WCAG 2.1 AA accessibility compliance
- Performance optimization (images, code)
- SEO and structured data implementation
- Custom 404 error page
- Back-to-top button
- Theme toggle in navigation
- All content sections (Hero, About, Experience, Education, Interests, Sidebar)

### 4.2 Out of Scope for MVP

Deferred to future versions:
- Print-friendly CSS stylesheet for PDF generation
- Contact form with backend integration
- Multi-language support (Polish/English toggle)
- Downloadable PDF version of CV
- Blog or articles section
- Project portfolio showcase
- Testimonials or recommendations section
- Progressive Web App (PWA) capabilities
- Advanced analytics integration
- Content Management System (CMS) integration
- A/B testing for content optimization
- Dark mode auto-switch based on time of day
- User comments or feedback system
- Newsletter subscription
- Real-time chat integration
- Video introductions or presentations
- Interactive skills charts or visualizations

### 4.3 Technical Limitations

The MVP is limited to:
- Static HTML/CSS/JavaScript (no server-side processing)
- Manual content updates (editing HTML files)
- Client-side theme persistence only (LocalStorage)
- No user authentication or accounts
- No dynamic content or database
- No form submission handling (contact form deferred)

### 4.4 Content Boundaries

Content scope:
- Professional information only (work, education, skills)
- Single individual (Marcin Kamiński)
- Current and historical information (no future projections)
- Public information suitable for professional networking
- No sensitive or confidential information

### 4.5 User Interaction Boundaries

User capabilities:
- View content (read-only)
- Navigate between sections
- Toggle theme preference
- Click external links (social media, email)
- Scroll and navigate content

Users cannot:
- Edit or modify content
- Submit forms or data
- Create accounts or log in
- Comment or provide feedback (directly)
- Share or save content (beyond browser capabilities)
- Print with specialized formatting (deferred to future version)

## 5. User Stories

### 5.1 Content Viewing and Navigation

#### US-001: View Professional Identity
As a recruiter visiting the CV website
I want to immediately see the candidate's name and professional title
So that I can confirm I'm viewing the correct person's CV

Acceptance Criteria:
- Hero section displays full name as h1 heading
- Professional title displayed as h2 subheading
- Text is readable with minimum 4.5:1 contrast ratio against background
- Hero section is visible above the fold on all devices
- Background image loads with responsive sizing
- Text remains readable on mobile devices (minimum 16px font size)

#### US-002: Navigate to Specific Sections
As a hiring manager with limited time
I want to quickly jump to specific sections of the CV
So that I can find relevant information without scrolling through everything

Acceptance Criteria:
- Navigation bar contains section links (Experience, Education, Interests)
- Navigation bar remains visible during scroll (sticky position)
- Clicking section link scrolls smoothly to target section
- Scroll position accounts for navigation bar height (no content hidden)
- Active section is highlighted in navigation menu
- Dropdown menu closes after selection on mobile
- Navigation is accessible via keyboard (Tab, Enter)

#### US-003: Return to Top of Page
As a user who has scrolled through the CV
I want to quickly return to the top of the page
So that I can access navigation or review the hero section

Acceptance Criteria:
- Back-to-top button appears after scrolling past 500px
- Button is positioned in bottom-right corner (not obstructing content)
- Clicking button smoothly scrolls to top of page
- Button has clear visual indicator (up arrow icon)
- Button is accessible via keyboard
- Button has ARIA label for screen readers
- Button is appropriately sized for touch targets on mobile (minimum 44x44px)

#### US-004: View Work Experience Timeline
As a recruiter evaluating career progression
I want to see work experience presented in a visual timeline
So that I can quickly understand the chronological career history

Acceptance Criteria:
- Experience section displays jobs in reverse chronological order (newest first)
- Visual timeline markers (dots/lines) connect experience entries
- Each job entry displays: company name, job title, dates, responsibilities, technologies
- Company names are visually prominent (bold)
- Responsibilities are formatted as bullet lists
- Technologies are visually distinct (italic)
- Timeline is simplified on mobile (left-aligned, minimal decorations)
- Timeline decorations are CSS-based (not critical content)
- All text content is accessible without visual timeline

#### US-005: Review Educational Background
As a hiring manager assessing qualifications
I want to view the candidate's educational background
So that I can verify academic credentials and specialized training

Acceptance Criteria:
- Education section displays all degrees and certifications
- Each entry shows: institution name, degree type, dates, specializations
- Institution names are visually prominent (bold)
- Entries are in chronological order
- Formatting is consistent with experience section
- All text is readable with proper contrast
- Content is accessible on all device sizes

#### US-006: View Skills and Qualifications
As a recruiter searching for specific skills
I want to see a organized list of skills and qualifications
So that I can quickly determine if the candidate matches job requirements

Acceptance Criteria:
- Desktop: Skills displayed in fixed right sidebar (550px width)
- Tablet: Skills displayed in reduced sidebar (200px width)
- Mobile: Skills displayed in collapsible accordions below main content
- Four distinct sections: Skills, Technical Skills, Trainings, Languages
- Skills formatted as scannable lists
- Sidebar is independently scrollable on desktop
- Accordions are collapsed by default on mobile
- Accordion headers are clearly clickable/tappable
- Content is accessible in both sidebar and accordion formats

#### US-007: View Personal Interests
As a hiring manager wanting to understand culture fit
I want to see the candidate's personal interests
So that I can assess personality and culture alignment

Acceptance Criteria:
- Interests section displays personal hobbies and activities
- Content is brief and professionally presented
- Text is easy to read and scan
- Section is accessible on all devices
- Content adds humanizing element without excessive length

#### US-008: Access Contact Information
As a recruiter wanting to reach out
I want to easily find and use contact information
So that I can initiate communication with the candidate

Acceptance Criteria:
- Email address is visible in About Me section
- Email link opens default email client
- Email link includes pre-filled subject line
- Social media links are available in footer
- All contact links are clearly labeled
- Links are accessible via keyboard and screen readers
- External links include proper security attributes

### 5.2 Theme and Preferences

#### US-009: Switch Between Light and Dark Themes
As a user viewing the CV in different lighting conditions
I want to toggle between light and dark themes
So that I can choose the most comfortable viewing experience

Acceptance Criteria:
- Theme toggle button is visible in navigation bar
- Button displays appropriate icon (sun for light mode, moon for dark mode)
- Clicking button switches theme immediately
- Theme transition is smooth (0.3s animation)
- Both themes maintain WCAG 2.1 AA contrast ratios
- Button is accessible via keyboard
- Button has ARIA label and pressed state for screen readers
- No content is lost or obscured during theme change

#### US-010: Persist Theme Preference
As a returning user with a theme preference
I want my theme choice to be remembered
So that I don't have to change it on every visit

Acceptance Criteria:
- Selected theme is saved to LocalStorage
- Saved theme loads automatically on return visit
- Theme preference persists across browser sessions
- If no preference is saved, system preference is detected (prefers-color-scheme)
- Clearing browser data resets to system preference
- Theme loads before page render (no flash of wrong theme)

### 5.3 Responsive Design

#### US-011: View CV on Mobile Device
As a recruiter using a mobile phone
I want to view the CV with optimized mobile layout
So that I can easily read content on a small screen

Acceptance Criteria:
- Layout switches to single column on screens less than 768px
- Navigation is condensed (menu dropdown)
- Hero section has reduced padding and font sizes
- About Me section stacks vertically (text, then photo)
- Experience timeline is simplified (left-aligned)
- Sidebar content moves to collapsible accordions at bottom
- All text is readable (minimum 16px font size)
- Touch targets are minimum 44x44px
- No horizontal scrolling occurs
- Images are appropriately sized for mobile

#### US-012: View CV on Tablet Device
As a user on a tablet
I want to see an optimized layout for medium screens
So that I can comfortably view content without excessive white space or crowding

Acceptance Criteria:
- Layout adapts to tablet screens (768-991px)
- Sidebar is reduced to 200px width
- Spacing is condensed but readable
- Navigation remains accessible
- Images scale appropriately
- No horizontal scrolling
- Touch targets are adequate for tablet use

#### US-013: View CV on Desktop
As a user on a desktop computer
I want to see the full layout with optimal spacing
So that I can view maximum information at once

Acceptance Criteria:
- Two-column layout with main content and sidebar
- Fixed right sidebar (550px width)
- Full navigation bar with inline section links
- Optimal typography and spacing
- Background images display at high resolution
- Sidebar is independently scrollable
- Layout takes advantage of available screen width
- Content is centered with appropriate max-width

### 5.4 Accessibility

#### US-014: Navigate with Keyboard Only
As a user who cannot use a mouse
I want to access all functionality via keyboard
So that I can fully navigate and interact with the CV

Acceptance Criteria:
- All interactive elements are reachable via Tab key
- Tab order follows logical reading order
- Visible focus indicators on all focusable elements (minimum 2px outline)
- Enter/Space activates links and buttons
- Escape key closes dropdowns and menus
- Skip to content link is available as first focusable element
- No keyboard traps exist
- Back-to-top button is keyboard accessible
- Theme toggle is keyboard accessible
- Accordion panels are keyboard accessible

#### US-015: Access Content with Screen Reader
As a user who relies on a screen reader
I want all content to be properly announced
So that I can understand the CV structure and content

Acceptance Criteria:
- Semantic HTML elements used throughout (nav, main, aside, footer)
- ARIA landmarks properly labeled
- Heading hierarchy is logical (single h1, proper h2-h4 nesting)
- All images have descriptive alt text
- Icon buttons have ARIA labels
- Skip to content link is announced
- Accordion state is announced (expanded/collapsed)
- Active navigation state is announced
- External links are identified
- All content is accessible in linear order

#### US-016: View Content with Sufficient Contrast
As a user with low vision
I want all text to have sufficient contrast
So that I can read content comfortably

Acceptance Criteria:
- Normal text has minimum 4.5:1 contrast ratio
- Large text has minimum 3:1 contrast ratio
- Contrast requirements met in both light and dark themes
- Focus indicators have sufficient contrast
- Interactive elements are distinguishable from non-interactive
- Color is not the only means of conveying information
- All contrast ratios verified with accessibility tools

#### US-017: Expand Collapsible Sections Accessibly (Mobile)
As a mobile user with accessibility needs
I want to expand accordion sections using assistive technology
So that I can access sidebar content on mobile devices

Acceptance Criteria:
- Accordion triggers are semantic buttons
- Buttons have aria-expanded attribute (true/false)
- Buttons have aria-controls pointing to panel ID
- Panels have role="region" and aria-labelledby
- Keyboard can activate accordion (Enter/Space)
- Screen reader announces expanded/collapsed state
- Focus moves logically after activation
- Multiple panels can be open simultaneously
- Smooth animation respects prefers-reduced-motion

### 5.5 Performance

#### US-018: Load Page Quickly on Mobile Network
As a recruiter on a mobile network
I want the CV to load quickly
So that I don't waste time waiting or give up before viewing content

Acceptance Criteria:
- Largest Contentful Paint less than 2.5 seconds
- First Contentful Paint less than 1.5 seconds
- Time to Interactive less than 3 seconds
- Hero background image loads in appropriate size for viewport
- Profile image is lazy loaded
- Images are compressed (80% quality)
- WebP format used with JPEG fallback
- CSS and JavaScript are minified
- No render-blocking resources
- Lighthouse Performance score greater than or equal to 90

#### US-019: Experience Stable Layout During Load
As any user loading the page
I want the layout to remain stable as content loads
So that I don't lose my place or click wrong elements

Acceptance Criteria:
- Cumulative Layout Shift less than 0.1
- Image dimensions specified in HTML
- Font loading doesn't cause layout shift
- Navigation bar doesn't shift during render
- Content areas have reserved space
- No unexpected layout jumps during theme application

### 5.6 Social and Professional Integration

#### US-020: Connect via Social Media
As a recruiter wanting to learn more about the candidate
I want to access their social media profiles
So that I can view their professional network and online presence

Acceptance Criteria:
- Footer contains social media icon links
- Icons for: LinkedIn, GitHub, Twitter/X, Facebook
- Icons are clearly recognizable
- Hover state provides visual feedback
- Links open in new tab (if applicable)
- Links have rel="noopener noreferrer" for security
- Each link has descriptive ARIA label
- Icons are accessible via keyboard
- Touch targets are adequate on mobile (minimum 44x44px)

#### US-021: Email Candidate Directly
As a recruiter ready to contact the candidate
I want to send an email with minimal friction
So that I can quickly initiate communication

Acceptance Criteria:
- Email link is prominently displayed in About Me section
- Clicking email link opens default email client
- Subject line is pre-filled ("Inquiry from CV Website")
- Email address is visible as text (copy-paste friendly)
- Email link is keyboard accessible
- Email link has appropriate ARIA labeling
- Link works on mobile devices

### 5.7 SEO and Discoverability

#### US-022: Find CV via Search Engine
As a recruiter searching for Technical Product Owner candidates
I want the CV to appear in relevant search results
So that I can discover the candidate when searching for qualified professionals

Acceptance Criteria:
- Page has descriptive title tag optimized for search
- Meta description summarizes professional background
- JSON-LD structured data (Schema.org Person) is implemented
- Structured data includes: name, jobTitle, description, skills, education, employer
- Canonical URL is specified
- Heading hierarchy is semantic and logical
- Content is crawlable by search engines
- Structured data validates with Google Rich Results Test

#### US-023: Preview CV When Shared on Social Media
As a user sharing the CV on social media
I want an attractive preview to display
So that the link gets proper visibility and context

Acceptance Criteria:
- Open Graph meta tags are complete (type, title, description, url, image)
- Twitter Card meta tags are complete (card, site, title, description, image)
- Preview image is appropriate and professional
- Preview title accurately represents the CV
- Preview description summarizes professional background
- Preview validates with Facebook Debugger and Twitter Card Validator
- Image loads correctly in social media previews

### 5.8 Error Handling

#### US-024: Handle Non-Existent Pages Gracefully
As a user who navigates to an incorrect URL
I want to see a helpful error page
So that I can find the correct page without frustration

Acceptance Criteria:
- Custom 404 page (error404.html) is displayed for non-existent URLs
- Error page has friendly, professional messaging
- Clear explanation of the error
- Prominent link to homepage
- Error page maintains consistent branding
- Theme support is maintained on error page
- Error page is accessible (proper headings, keyboard navigation)
- Error page loads quickly

### 5.9 Visual Design and Branding

#### US-025: Experience Professional Visual Design
As any visitor to the CV website
I want to see a professional, polished design
So that I form a positive impression of the candidate

Acceptance Criteria:
- Consistent color palette throughout (light and dark themes)
- Professional typography with clear hierarchy
- Adequate white space and spacing
- Visual elements align and balance properly
- Hover states provide feedback on interactive elements
- Smooth transitions and animations (respecting prefers-reduced-motion)
- Hero section creates strong first impression
- Timeline provides visual interest in experience section
- Design is cohesive across all sections and devices

#### US-026: View Optimized Images
As a user on any device
I want images to load in appropriate sizes and formats
So that I get quality visuals without excessive load times

Acceptance Criteria:
- Hero background image has three sizes: 800px, 1200px, 2000px
- Correct image size loads based on viewport width
- WebP format used with JPEG fallback
- Profile photo is optimized (max 400px source, 200px display)
- Profile photo has lazy loading attribute
- All images have proper alt text
- Images have specified dimensions (prevent layout shift)
- Image compression maintains quality (80%)

### 5.10 Content Management

#### US-027: View Current Professional Information
As a visitor to the CV
I want to see up-to-date professional information
So that I can make decisions based on current qualifications

Acceptance Criteria:
- All work experience is current and accurate
- Education information is complete and accurate
- Skills and technical skills reflect current capabilities
- Contact information is functional and current
- Social media links point to active profiles
- Dates are formatted consistently (Month Year - Month Year)
- Most recent position appears first in experience section

#### US-028: Identify Technologies and Tools Used
As a technical recruiter looking for specific skills
I want to clearly see which technologies the candidate has used
So that I can match them to job requirements

Acceptance Criteria:
- Technologies are listed for each job in experience section
- Technologies are visually distinct (italic formatting)
- Technical Skills section provides comprehensive list
- Skills are categorized logically (Skills, Technical Skills, Trainings, Languages)
- Technology names are specific (not vague)
- Skills are easy to scan (list format)
- Skills section is accessible on all devices (sidebar or accordion)

### 5.11 Edge Cases and Alternative Scenarios

#### US-029: View CV with JavaScript Disabled
As a user with JavaScript disabled
I want to view CV content
So that I can access information regardless of browser settings

Acceptance Criteria:
- All content is accessible without JavaScript
- Navigation links work (anchor links)
- Layouts render correctly
- Images display properly
- Default theme is applied (based on CSS or server-side detection)
- Theme toggle gracefully degrades (not functional but doesn't break layout)
- No JavaScript errors visible to user

#### US-030: View CV with Reduced Motion Preference
As a user who experiences motion sensitivity
I want animations and transitions to be minimal
So that I can view content comfortably without disorientation

Acceptance Criteria:
- System preference for reduced motion is detected (prefers-reduced-motion)
- Smooth scrolling is disabled when reduced motion is preferred
- Theme transitions are instant (no animation)
- Accordion expand/collapse is instant
- Timeline animations are disabled
- All functionality remains intact without animations
- No content is hidden or inaccessible

#### US-031: View CV on Very Small Screen (320px)
As a user on a small mobile device
I want the CV to remain functional at minimum supported width
So that I can view content even on compact screens

Acceptance Criteria:
- Layout remains functional at 320px width
- No horizontal scrolling occurs
- Text remains readable (no cut-off)
- Navigation remains accessible
- Touch targets remain adequately sized
- Images scale appropriately
- All interactive elements remain usable

#### US-032: View CV on Very Large Screen (2560px+)
As a user on a large desktop monitor
I want the CV to use space effectively without excessive line lengths
So that content remains readable and visually balanced

Acceptance Criteria:
- Content has maximum width (prevents excessive line length)
- Layout is centered on screen
- White space is used effectively
- Images display at appropriate resolution
- No elements appear stretched or distorted
- Design remains visually balanced
- All functionality works at large viewport sizes

#### US-033: Load CV with Slow Internet Connection
As a user on a slow internet connection
I want to see content progressively load
So that I can start reading while other assets load

Acceptance Criteria:
- Critical content loads first (HTML, critical CSS)
- Hero section is visible quickly
- JavaScript is deferred (doesn't block rendering)
- Images load progressively
- Lazy loading is applied to below-fold images
- Page remains functional during load
- No long periods of blank screen
- Loading states don't cause layout shifts

#### US-034: Print CV from Browser
As a recruiter wanting a hard copy
I want to print the CV from my browser
So that I can have a physical reference or PDF

Acceptance Criteria:
- Page is printable via browser print function
- Content flows logically when printed
- Unnecessary elements are hidden (navigation, back-to-top button)
- Links are visible with URLs (optional enhancement)
- Page breaks occur at logical points
- Content is readable in black and white
- Note: Print-specific CSS optimization is deferred to future version

#### US-035: Copy Content for Reference
As a recruiter documenting candidate information
I want to copy text from the CV
So that I can paste it into my applicant tracking system

Acceptance Criteria:
- All text content is selectable
- Copy/paste preserves logical structure
- Lists copy as bullet points
- Headings are distinguishable from body text
- No elements prevent text selection
- Copied content is plain text (no hidden formatting)
- Timeline decorations don't interfere with text selection

#### US-036: Share CV URL
As a hiring manager recommending a candidate
I want to share the CV URL with colleagues
So that they can review the candidate's qualifications

Acceptance Criteria:
- URL is clean and memorable
- URL works when shared via email, chat, or social media
- Shared links display preview (Open Graph/Twitter Card)
- URL doesn't change or break over time (stable routing)
- Anchor links to specific sections work when shared
- Shared URL works across different devices and browsers

### 5.12 Maintenance and Updates

#### US-037: Update CV Content Easily
As the CV owner (Marcin Kamiński)
I want to update content by editing HTML
So that I can keep professional information current without complex tools

Acceptance Criteria:
- Content is clearly structured in semantic HTML
- Job entries are easily identifiable in code
- Adding new experience requires minimal HTML knowledge
- Code comments guide content updates
- Changes can be made with simple text editor
- Local testing is straightforward (open HTML file)
- Updates can be deployed via GitHub Actions to production server

#### US-038: Verify CV Quality After Updates
As the CV owner making content changes
I want to ensure accessibility and performance after updates
So that I maintain quality standards

Acceptance Criteria:
- Lighthouse audit can be run to verify performance
- axe DevTools can verify accessibility
- W3C validators can check HTML and CSS validity
- Structured data validator can verify JSON-LD
- Visual review possible at different screen sizes
- Browser DevTools available for testing
- Documentation exists for quality checks

---

## Appendix

### A. Glossary

- ARIA: Accessible Rich Internet Applications - specification for making web content accessible
- CLS: Cumulative Layout Shift - measure of visual stability
- CDN: Content Delivery Network - distributed server network for fast content delivery
- FCP: First Contentful Paint - time until first content is rendered
- FID: First Input Delay - time until page responds to user interaction
- JSON-LD: JavaScript Object Notation for Linked Data - structured data format
- LCP: Largest Contentful Paint - time until main content is visible
- LocalStorage: Browser API for client-side data persistence
- Open Graph: Protocol for social media preview metadata
- PWA: Progressive Web App - web application with app-like features
- Schema.org: Vocabulary for structured data markup
- SEO: Search Engine Optimization - techniques to improve search visibility
- SRI: Subresource Integrity - security feature for verifying resource integrity
- TTI: Time to Interactive - time until page is fully interactive
- WCAG: Web Content Accessibility Guidelines - accessibility standards
- WebP: Modern image format with superior compression

### B. References

- WCAG 2.1 Guidelines: https://www.w3.org/WAI/WCAG21/quickref/
- Schema.org Person: https://schema.org/Person
- Pico CSS Documentation: https://picocss.com/
- Core Web Vitals: https://web.dev/vitals/
- MDN Web Docs: https://developer.mozilla.org/

### C. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-16 | Product Manager | Initial PRD creation based on existing documentation |

### D. Approval

This PRD defines the complete scope for the Personal CV Website MVP. All user stories are testable and include clear acceptance criteria. The document is ready for development implementation.

Document Status: Ready for Implementation
