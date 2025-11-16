# Personal CV - Marcin Kamiński

[![CodeSandbox](https://img.shields.io/badge/CodeSandbox-000000?style=flat&logo=codesandbox&logoColor=white)](https://codesandbox.io/s/github/picocss/examples/tree/master/v1-company)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

A modern, responsive personal CV webpage showcasing professional experience, education, skills, and technical expertise. Built with clean HTML, CSS, and JavaScript using the Pico CSS framework for a professional and accessible presentation.

## Table of Contents

- [Project Description](#project-description)
- [Tech Stack](#tech-stack)
- [Getting Started Locally](#getting-started-locally)
- [Available Scripts](#available-scripts)
- [Project Scope](#project-scope)
- [Features](#features)
- [Project Structure](#project-structure)
- [Browser Compatibility](#browser-compatibility)
- [Project Status](#project-status)
- [License](#license)
- [Contact](#contact)

## Project Description

This is a simple HTML-based webpage containing a comprehensive CV for public review. The page features a clean, professional design with dynamic elements including:

- Responsive layout that adapts to different screen sizes
- Fixed sidebar displaying skills, technical abilities, trainings, and languages
- Integrated social media links (Facebook, LinkedIn, X/Twitter, GitHub)
- Sectioned navigation for easy access to Experience, Education, and Interests
- Dark/light theme support with local storage persistence
- Custom 404 error page

The project is designed for Technical Product Owners and IT professionals who need a modern web presence to showcase their career achievements and technical expertise.

## Getting Started Locally

Since this is a static HTML website, getting started is straightforward:

### Option 1: Direct File Opening

1. Clone the repository:
   ```bash
   git clone https://github.com/emkaminsk/PersonalCV.git
   cd PersonalCV
   ```

2. Open `index.html` in your web browser:
   - **Windows**: Double-click `index.html` or right-click → Open with → Your browser
   - **macOS**: Double-click `index.html` or `open index.html`
   - **Linux**: `xdg-open index.html`

### Option 2: Local Web Server (Recommended)

For a better development experience that handles relative paths and modern web features:

**Using Python 3:**
```bash
python3 -m http.server 8000
# Visit http://localhost:8000 in your browser
```

**Using Python 2:**
```bash
python -m SimpleHTTPServer 8000
# Visit http://localhost:8000 in your browser
```

**Using Node.js (with http-server):**
```bash
npx http-server -p 8000
# Visit http://localhost:8000 in your browser
```

**Using PHP:**
```bash
php -S localhost:8000
# Visit http://localhost:8000 in your browser
```

### Option 3: CodeSandbox

Open directly in CodeSandbox for online editing and preview:

[![Open in CodeSandbox](https://codesandbox.io/static/img/play-codesandbox.svg)](https://codesandbox.io/s/github/picocss/examples/tree/master/v1-company)

## Available Scripts

This is a static HTML project with no build process, so there are no npm scripts or package.json. However, you can use any of the local server options mentioned above for development.

### Recommended Development Tools

- **Live Server** (VS Code extension) - Auto-reload on file changes
- **Browser DevTools** - For debugging and responsive design testing
- **HTML/CSS validators** - For code quality checks

## Project Scope

This personal CV website showcases:

### Professional Information
- **Work Experience** - Detailed employment history with responsibilities and technologies
- **Education** - Academic background including eMBA and specialized training
- **Skills** - Soft skills including relationship-building, customer-centric approach, and cross-functional collaboration
- **Technical Skills** - Comprehensive list of tools, languages, and technologies
- **Certifications** - Professional trainings and certificates
- **Languages** - Proficiency levels in English, Spanish, and German
- **Interests** - Personal hobbies and activities

### Page Sections
1. **Hero Section** - Name, title, and navigation with background image
2. **About Me** - Professional summary and contact information
3. **Experience** - Chronological work history (2005 - Present)
4. **Education** - Academic qualifications and postgraduate studies
5. **Interests** - Personal interests and hobbies
6. **Sidebar** - Skills, technical abilities, trainings, and languages (desktop only)

## Features

### Responsive Design
- **Desktop** - Full layout with fixed sidebar (right-aligned)
- **Tablet** - Reduced sidebar width (200px)
- **Mobile** - Hidden sidebar, stacked content, optimized typography

### Theme Support
- Light and dark theme switching
- Automatic detection of system preferences
- Local storage persistence for user preference
- Seamless theme transitions

### Navigation
- Sticky navigation bar with contrast styling
- Section navigation dropdown (Experience, Education, Interests)
- Smooth scrolling to anchored sections

### Social Media Integration
- Direct links to Facebook, LinkedIn, X (Twitter), and GitHub
- Custom SVG icons for brand consistency
- Hover effects for better user interaction

## Project Structure

```
PersonalCV/
├── index.html                    # Main CV page
├── error404.html                 # Custom 404 error page
├── custom.css                    # Custom styles and responsive design
├── sandbox.config.json           # CodeSandbox configuration
├── .gitignore                    # Git ignore rules
├── README.md                     # Project documentation
├── js/
│   └── minimal-theme-switcher.js # Theme switching functionality
├── icons/
│   ├── facebook.svg              # Facebook icon
│   ├── github.svg                # GitHub icon
│   ├── linkedin.svg              # LinkedIn icon
│   └── x.svg                     # X (Twitter) icon
└── img/
    ├── MK03.jpg                  # Profile photo
    └── sascha-eremin-DNQ-M93tHmA-unsplash-3000x1000.jpg  # Hero background
```

## Browser Compatibility

This project uses modern HTML5, CSS3, and ES6+ JavaScript features. It is compatible with:

- ✅ Chrome/Edge (latest)
- ✅ Firefox (latest)
- ✅ Safari (latest)
- ✅ Opera (latest)
- ⚠️ Internet Explorer 11 (limited support - theme switcher may not work)

### Required Browser Features
- CSS Grid and Flexbox
- CSS Custom Properties (CSS Variables)
- LocalStorage API
- ES6 JavaScript (arrow functions, const/let, template literals)

## Project Status

**Status:** Active and Maintained

This project is actively maintained and updated with current professional information. The CV content is regularly reviewed and updated to reflect the latest work experience, skills, and achievements.

### Recent Updates
- ✅ README documentation
- ✅ Responsive design improvements
- ✅ Custom styling with Pico CSS framework
- ✅ Theme switcher implementation
- ✅ Social media integration

### Future Enhancements
- Consider adding a print-friendly CSS stylesheet
- Potential integration with a headless CMS for easier content updates
- Performance optimizations (image compression, lazy loading)
- Accessibility improvements (ARIA labels, keyboard navigation)
- Multi-language support (Polish/English)

## License

This project does not currently have a specified license. All rights reserved by Marcin Kamiński © 2023.

If you wish to use this template for your own CV, please:
1. Fork the repository
2. Replace all personal information with your own
3. Update images and icons as needed
4. Customize the styling to match your preferences

## Contact

**Marcin Kamiński**
Technical Product Owner

- **Email:** [emkaminsk@gmail.com](mailto:emkaminsk@gmail.com)
- **LinkedIn:** [linkedin.com/in/marcinkaminski](https://www.linkedin.com/in/marcinkaminski/)
- **GitHub:** [github.com/emkaminsk](https://github.com/emkaminsk)
- **Twitter/X:** [@emkaminsk](https://twitter.com/emkaminsk)
- **Facebook:** [facebook.com/marcin.kaminski.01](https://www.facebook.com/marcin.kaminski.01/)

---

**Built with ❤️ using [Pico CSS](https://picocss.com/)**
