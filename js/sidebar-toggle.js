/**
 * Sidebar Toggle Functionality
 * Handles collapsible sidebar with localStorage persistence
 */

class SidebarToggle {
  constructor() {
    this.sidebar = document.getElementById('sidebar');
    this.toggleBtn = document.querySelector('[data-sidebar-toggle]');
    this.restoreBtn = document.querySelector('[data-restore-sidebar]');
    this.closeBtn = document.querySelector('[data-sidebar-close]');
    this.storageKey = 'sidebarState';

    // Debug logging
    console.log('SidebarToggle initialized:', {
      sidebar: !!this.sidebar,
      toggleBtn: !!this.toggleBtn,
      restoreBtn: !!this.restoreBtn,
      closeBtn: !!this.closeBtn
    });

    // Only initialize if sidebar and toggle button exist
    if (this.sidebar && this.toggleBtn) {
      this.init();
    } else {
      console.warn('Sidebar or toggle button not found');
    }
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
    if (this.toggleBtn) {
      this.toggleBtn.setAttribute('aria-pressed', state === 'open' ? 'true' : 'false');
    }

    if (this.restoreBtn) {
      if (state === 'closed') {
        this.restoreBtn.classList.add('visible');
      } else {
        this.restoreBtn.classList.remove('visible');
      }
    }
  }

  attachListeners() {
    if (this.toggleBtn) {
      this.toggleBtn.addEventListener('click', () => {
        console.log('Toggle button clicked');
        this.toggle();
      });
    }

    if (this.restoreBtn) {
      this.restoreBtn.addEventListener('click', () => {
        console.log('Restore button clicked');
        this.restore();
      });
    }

    if (this.closeBtn) {
      this.closeBtn.addEventListener('click', () => {
        console.log('Close button clicked');
        this.setState('closed');
      });
    }
  }

  toggle() {
    const current = this.sidebar.getAttribute('data-sidebar-state');
    const newState = current === 'open' ? 'closed' : 'open';
    console.log('Toggling sidebar:', current, '->', newState);
    this.setState(newState);
  }

  restore() {
    this.setState('open');
    // Move focus to sidebar for accessibility
    this.sidebar.setAttribute('tabindex', '-1');
    this.sidebar.focus();
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
