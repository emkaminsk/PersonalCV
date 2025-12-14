# Index.html Sidebar Improvement Plan

## Overview
Transform the static right-side sidebar into a **vertically-full, collapsible panel** with a restore button. The sidebar will display at full viewport height and can be toggled closed/open without impacting the CV synchronization script.

## Current State Analysis

### HTML Structure (lines 294-311)
- **Element**: `<aside id="sidebar" aria-label="Skills and qualifications">`
- **Content**: 4 sections (Skills, Technical Skills, Trainings, Languages)
- **Desktop**: Fixed positioning at top: 250px, right: 0, width: 550px
- **Tablet**: 960px+ breakpoint reduces width to 200px
- **Mobile**: Hidden entirely at 768px and below

### CSS Styling (lines 541-598)
- **Position**: `fixed` (always visible on desktop)
- **Height**: `calc(300% - 250px)` (unclear calculation)
- **Overflow**: `auto` (scrollable content)
- **Display**: Hidden at 768px via `display: none`
- **Responsive**: Two breakpoints (960px, 768px)

### sync_cv.py Integration (lines 399-462)
- Updates sidebar via BeautifulSoup DOM manipulation
- Targets: `#sidebar` → `.sidebar-section` → `<ul>` elements
- **Safe zone**: Only modifies list items (`<li>`) within existing structure
- **No dependencies on**: Sidebar visibility state, positioning, or CSS classes

## Implementation Plan

### Phase 1: HTML Structure Enhancement

#### 1.1 Add Sidebar Toggle Button
**Location**: Top right of navigation bar (next to theme toggle)
**Element**: Semantic button with aria-label and aria-controls

```html
<button
  aria-label="Toggle sidebar"
  aria-controls="sidebar"
  aria-pressed="true"
  class="sidebar-toggle-btn"
  data-sidebar-toggle="">
  <svg><!-- Menu/X icon --></svg>
</button>
```

**Position in index.html**: Line 193 (after theme toggle button, before closing `</ul>`)

#### 1.2 Add Restore Button (Hidden by default)
**Location**: Fixed bottom-right corner (above "back-to-top" button)
**Element**: Appears only when sidebar is closed
**Styling**: Similar to back-to-top button

```html
<button
  aria-label="Restore sidebar"
  class="restore-sidebar-btn"
  data-restore-sidebar="">
  <svg><!-- Chevron left icon --></svg>
</button>
```

**Position in index.html**: Line 312 (before `.back-to-top` button)

#### 1.3 Sidebar Container Wrapper (Optional Enhancement)
- No structural change needed - existing `<aside>` serves as container
- Add `data-sidebar-state="open"` attribute for state tracking

### Phase 2: CSS Modifications

#### 2.1 Base Sidebar Styles (Unmodified safe zones)
- **Keep**:
  - `.sidebar-section` styling (content sections)
  - `.sidebar-section h4` styling (headings)
  - `.sidebar-section ul` styling (lists)
  - `.sidebar-section li` styling (list items)
  - ALL inner content styling remains untouched

#### 2.2 Sidebar Position & Visibility (Modified)
```css
/* Full-height sidebar (desktop only) */
#sidebar {
  position: fixed;
  top: 0;                    /* Changed: 250px → 0 */
  right: 0;
  width: 550px;
  height: 100vh;             /* Changed: calc(300% - 250px) → 100vh */
  background-color: #f9f9f9;
  overflow-y: auto;
  padding: 20px;
  padding-top: 80px;         /* Add spacing for header */
  box-shadow: -2px 0 5px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  transition: transform 0.3s ease, opacity 0.3s ease;
  transform: translateX(0);
  opacity: 1;
}

/* Sidebar closed state */
#sidebar[data-sidebar-state="closed"] {
  transform: translateX(100%);     /* Slide off right edge */
  opacity: 0;
  pointer-events: none;            /* Prevent interaction when hidden */
}
```

#### 2.3 Toggle Button Styling
```css
.sidebar-toggle-btn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-left: auto;
  transition: transform 0.2s ease;
  color: inherit;
}

.sidebar-toggle-btn:hover {
  transform: scale(1.1);
}

.sidebar-toggle-btn:focus {
  outline: 2px solid var(--contrast-hover);
  outline-offset: 2px;
  border-radius: 0.25rem;
}

/* Icon rotation when sidebar is closed */
#sidebar[data-sidebar-state="closed"] ~ nav .sidebar-toggle-btn svg {
  transform: scaleX(-1);
}
```

#### 2.4 Restore Button Styling
```css
.restore-sidebar-btn {
  position: fixed;
  bottom: 6rem;              /* Above back-to-top button */
  right: 2rem;
  display: none;
  z-index: 99;
  border: none;
  background: var(--primary);
  color: white;
  padding: 0.75rem;
  border-radius: 50%;
  cursor: pointer;
  width: 48px;
  height: 48px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  transition: opacity 0.3s ease, transform 0.2s ease;
  opacity: 0;
  align-items: center;
  justify-content: center;
}

.restore-sidebar-btn.visible {
  display: flex;
  opacity: 1;
}

.restore-sidebar-btn:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
}

.restore-sidebar-btn:focus {
  outline: 2px solid var(--primary-focus);
  outline-offset: 2px;
}
```

#### 2.5 Responsive Adjustments (Tablet/Mobile)
```css
@media screen and (max-width: 960px) {
  #sidebar {
    width: 200px;
    padding-top: 60px;       /* Adjust for smaller header on tablet */
  }
}

@media screen and (max-width: 768px) {
  #sidebar {
    display: none;           /* Keep existing mobile behavior */
  }

  .restore-sidebar-btn {
    display: none !important; /* Hide restore button on mobile */
  }
}
```

### Phase 3: JavaScript Implementation

#### 3.1 Sidebar Toggle Functionality
**Location**: Create `js/sidebar-toggle.js` (new file)

**Core Functionality**:
```javascript
class SidebarToggle {
  constructor() {
    this.sidebar = document.getElementById('sidebar');
    this.toggleBtn = document.querySelector('[data-sidebar-toggle]');
    this.restoreBtn = document.querySelector('[data-restore-sidebar]');
    this.storageKey = 'sidebarState';

    this.init();
  }

  init() {
    this.restoreState();
    this.attachListeners();
  }

  restoreState() {
    const saved = localStorage.getItem(this.storageKey);
    const state = saved || 'open';
    this.setState(state);
  }

  setState(state) {
    this.sidebar.setAttribute('data-sidebar-state', state);
    this.updateButtonStates(state);
    localStorage.setItem(this.storageKey, state);
  }

  updateButtonStates(state) {
    if (state === 'closed') {
      this.toggleBtn.setAttribute('aria-pressed', 'false');
      this.restoreBtn.classList.add('visible');
    } else {
      this.toggleBtn.setAttribute('aria-pressed', 'true');
      this.restoreBtn.classList.remove('visible');
    }
  }

  attachListeners() {
    this.toggleBtn?.addEventListener('click', () => this.toggle());
    this.restoreBtn?.addEventListener('click', () => this.restore());
  }

  toggle() {
    const current = this.sidebar.getAttribute('data-sidebar-state');
    const newState = current === 'open' ? 'closed' : 'open';
    this.setState(newState);
  }

  restore() {
    this.setState('open');
    this.sidebar.focus(); /* A11y: move focus to sidebar */
  }
}

// Initialize on DOM ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    new SidebarToggle();
  });
} else {
  new SidebarToggle();
}
```

#### 3.2 Script Integration
**Location**: Add to index.html after existing scripts (line 324)
```html
<script src="js/sidebar-toggle.js"></script>
```

### Phase 4: Accessibility & UX Considerations

#### 4.1 Keyboard Navigation
- Toggle button: Tab-accessible, Space/Enter to activate
- Restore button: Tab-accessible, Space/Enter to activate
- Sidebar content: Remains keyboard-navigable when open
- Focus management: ARIA attributes updated dynamically

#### 4.2 Screen Reader Support
- Toggle button: `aria-label="Toggle sidebar"`, `aria-controls="sidebar"`, `aria-pressed` state
- Restore button: `aria-label="Restore sidebar"`
- Sidebar: `aria-label="Skills and qualifications"` (existing)
- State changes announced via aria-pressed updates

#### 4.3 Visual Feedback
- Smooth transitions (0.3s ease)
- Icon rotation on toggle
- Button hover/focus states
- Restore button appears above back-to-top button

#### 4.4 Responsive Behavior
- Desktop (1024px+): Full sidebar toggle functionality
- Tablet (768px-1023px): Full sidebar toggle functionality
- Mobile (<768px): Sidebar hidden, no restore button (existing behavior preserved)

### Phase 5: sync_cv.py Compatibility

#### 5.1 Why No Changes Required
1. **Target selectors unchanged**: `#sidebar`, `.sidebar-section`, `ul`, `li` all remain
2. **No new classes in content**: New classes only on buttons (`sidebar-toggle-btn`, `restore-sidebar-btn`)
3. **Data attributes non-disruptive**: `data-sidebar-state` on `<aside>` doesn't interfere with list updates
4. **BeautifulSoup DOM operations**: All `ul.clear()` and `li` creation logic works identically
5. **Section structure preserved**: 4 sidebar sections with h4 headings remain exactly the same

#### 5.2 Testing Strategy
- Run `sync_cv.py` after implementation
- Verify all skills, trainings, languages sections update correctly
- Confirm sidebar state (open/closed) persists after sync

## Implementation Order

1. **HTML Structure** (index.html)
   - Add toggle button in nav (line 193)
   - Add restore button (line 312)
   - Add data-sidebar-state attribute to aside

2. **CSS Styles** (custom.css)
   - Update #sidebar positioning (full-height, 0 top offset)
   - Add transform/opacity transitions
   - Add .sidebar-toggle-btn styles
   - Add .restore-sidebar-btn styles
   - Update responsive breakpoints

3. **JavaScript** (create js/sidebar-toggle.js)
   - Implement SidebarToggle class
   - Add localStorage persistence
   - Add event listeners

4. **Script Reference** (index.html)
   - Link sidebar-toggle.js before closing body tag

5. **Testing**
   - Manual browser testing (desktop, tablet, mobile)
   - Verify theme switching integration
   - Run sync_cv.py validation
   - Accessibility testing (keyboard, screen reader)

## Files to Modify

| File | Changes | Impact | sync_cv.py Safe? |
|------|---------|--------|------------------|
| index.html | Add 2 buttons, add attribute | Structure only | ✅ Yes |
| custom.css | Update sidebar + add styles | Styling only | ✅ Yes |
| js/sidebar-toggle.js | Create new file | New functionality | ✅ Yes |

## Browser Support

- ✅ Chrome/Edge 88+
- ✅ Firefox 87+
- ✅ Safari 14+
- ✅ Mobile (iOS Safari, Chrome Mobile)
- ⚠️ IE11 (CSS transitions may be basic, functionality works)

## Fallback Behavior

If JavaScript fails to load:
- Sidebar displays as open by default
- Toggle button has no effect (but remains accessible)
- Restore button remains hidden
- Layout and content unaffected
- Graceful degradation with full content visibility

## Success Criteria

1. ✅ Sidebar displays full viewport height (desktop)
2. ✅ Toggle button closes/opens sidebar smoothly
3. ✅ Restore button appears when sidebar is closed
4. ✅ State persists across page refreshes (localStorage)
5. ✅ Keyboard and screen reader accessible
6. ✅ sync_cv.py runs without errors
7. ✅ Mobile behavior unchanged (sidebar hidden)
8. ✅ Tablet behavior enhanced with toggle
