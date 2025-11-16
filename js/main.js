/**
 * Main JavaScript for Personal CV Page
 * Handles theme toggle, navigation, accordions, and back-to-top functionality
 */

document.addEventListener('DOMContentLoaded', () => {
  // ===== THEME TOGGLE =====
  const themeToggleBtn = document.querySelector('[data-theme-toggle]');
  const themeIcon = themeToggleBtn ? themeToggleBtn.querySelector('.theme-icon') : null;

  // Update icon based on current theme
  function updateThemeIcon(theme) {
    if (!themeIcon) return;

    if (theme === 'dark') {
      // Moon icon for dark mode
      themeIcon.innerHTML = `
        <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
      `;
    } else {
      // Sun icon for light mode
      themeIcon.innerHTML = `
        <circle cx="12" cy="12" r="5"></circle>
        <line x1="12" y1="1" x2="12" y2="3"></line>
        <line x1="12" y1="21" x2="12" y2="23"></line>
        <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
        <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
        <line x1="1" y1="12" x2="3" y2="12"></line>
        <line x1="21" y1="12" x2="23" y2="12"></line>
        <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
        <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
      `;
    }
  }

  // Initialize theme icon
  if (themeToggleBtn && typeof themeSwitcher !== 'undefined') {
    updateThemeIcon(themeSwitcher.scheme);

    // Toggle theme on button click
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = themeSwitcher.scheme;
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';
      themeSwitcher.scheme = newTheme;
      updateThemeIcon(newTheme);
      themeToggleBtn.setAttribute('aria-pressed', newTheme === 'dark');
    });
  }

  // ===== SMOOTH SCROLL NAVIGATION =====
  const sectionLinks = document.querySelectorAll('a[href^="#"]');

  sectionLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');

      // Skip if it's just "#"
      if (href === '#') {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }

      const targetId = href.substring(1);
      const target = document.getElementById(targetId);

      if (target) {
        e.preventDefault();

        // Calculate offset for sticky navigation
        const navHeight = document.querySelector('nav') ? document.querySelector('nav').offsetHeight : 0;
        const targetPosition = target.offsetTop - navHeight - 20;

        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });

        // Close dropdown if open
        const dropdown = link.closest('details');
        if (dropdown) {
          dropdown.removeAttribute('open');
        }
      }
    });
  });

  // ===== LOGO LINK SMOOTH SCROLL TO TOP =====
  const logoLink = document.getElementById('logo-link');
  if (logoLink) {
    logoLink.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // ===== BACK TO TOP BUTTON =====
  const backToTopBtn = document.querySelector('.back-to-top');
  const scrollThreshold = 500;

  if (backToTopBtn) {
    // Show/hide button based on scroll position
    function toggleBackToTopButton() {
      if (window.scrollY > scrollThreshold) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    }

    // Initial check
    toggleBackToTopButton();

    // Listen to scroll events
    window.addEventListener('scroll', toggleBackToTopButton);

    // Scroll to top on click
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // ===== ACCORDION FUNCTIONALITY (MOBILE) =====
  const accordionHeaders = document.querySelectorAll('[data-accordion-trigger]');

  accordionHeaders.forEach(header => {
    header.addEventListener('click', () => {
      const isExpanded = header.getAttribute('aria-expanded') === 'true';
      const panelId = header.getAttribute('aria-controls');
      const panel = document.getElementById(panelId);

      if (!panel) return;

      // Toggle aria-expanded
      header.setAttribute('aria-expanded', !isExpanded);

      // Toggle panel visibility
      if (isExpanded) {
        panel.classList.remove('expanded');
        panel.style.maxHeight = '0';
      } else {
        panel.classList.add('expanded');
        // Calculate exact height for smooth animation
        panel.style.maxHeight = panel.scrollHeight + 'px';
      }
    });
  });

  // ===== ACTIVE SECTION HIGHLIGHTING (Optional Enhancement) =====
  // Using IntersectionObserver to track which section is currently visible
  const sections = document.querySelectorAll('section[id], h3[id]');
  const navLinks = document.querySelectorAll('nav a[href^="#"]');

  if ('IntersectionObserver' in window && sections.length > 0) {
    const observerOptions = {
      root: null,
      rootMargin: '-100px 0px -66%',
      threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;

          // Remove active class from all nav links
          navLinks.forEach(link => {
            link.classList.remove('active');
          });

          // Add active class to current section's link
          const activeLink = document.querySelector(`nav a[href="#${id}"]`);
          if (activeLink) {
            activeLink.classList.add('active');
          }
        }
      });
    }, observerOptions);

    sections.forEach(section => {
      observer.observe(section);
    });
  }

  // ===== CLOSE DROPDOWN ON OUTSIDE CLICK (Enhancement) =====
  const dropdown = document.querySelector('details[role="list"]');

  if (dropdown) {
    document.addEventListener('click', (e) => {
      if (!dropdown.contains(e.target)) {
        dropdown.removeAttribute('open');
      }
    });
  }

  // ===== KEYBOARD NAVIGATION ENHANCEMENTS =====
  // Allow Escape key to close dropdowns
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      const openDropdown = document.querySelector('details[role="list"][open]');
      if (openDropdown) {
        openDropdown.removeAttribute('open');
      }
    }
  });

  // ===== FORM VALIDATION (if email subject is needed) =====
  // Already handled in HTML with mailto link

  console.log('Personal CV page initialized successfully');
});
