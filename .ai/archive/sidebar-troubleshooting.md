# Sidebar Toggle Troubleshooting Guide

## Changes Made
1. **JavaScript**: Added comprehensive error handling and console logging
2. **Condition Fix**: Changed initialization requirement from ALL 3 elements to just sidebar + toggle button
3. **Debug Logging**: Added console.log statements to track initialization and click events

## How to Debug

### Step 1: Open Browser Console
1. Open http://localhost:8000 in Chrome
2. Press F12 to open DevTools
3. Go to Console tab

### Step 2: Check Initialization
You should see on page load:
```
SidebarToggle initialized: {sidebar: true, toggleBtn: true, restoreBtn: true}
```

If you see `sidebar: false`, the sidebar element isn't found (might be hidden by media query on small screens)
If you see `toggleBtn: false`, the button wasn't found in the DOM

### Step 3: Test Click
1. Click the panel icon button in the navigation (rightmost button)
2. You should see in console:
```
Toggle button clicked
Toggling sidebar: open -> closed
```

### Step 4: Visual Check
After clicking, the sidebar should:
- Slide out to the right (transform: translateX(100%))
- Fade out (opacity: 0)
- The restore button (chevron) should appear at bottom-right

## Common Issues

### Issue 1: Button Not Clickable
**Symptoms**: No console messages when clicking
**Possible causes**:
- Button covered by another element
- JavaScript not loaded
- Event listener not attached

**Solutions**:
- Check if script is loaded: Look in Network tab for `sidebar-toggle.js` (should be 200 status)
- Check Elements tab: Find the button, verify it has the `data-sidebar-toggle` attribute
- Try clicking directly on the SVG icon inside the button

### Issue 2: Sidebar Not Visible
**Symptoms**: Console shows initialization but sidebar not visible
**Possible causes**:
- Screen width < 768px (sidebar hidden on mobile)
- Sidebar already in closed state

**Solutions**:
- Check viewport width: Console → run `window.innerWidth`
- Clear localStorage: Console → run `localStorage.removeItem('sidebarState')`
- Reload page

### Issue 3: Sidebar Doesn't Animate
**Symptoms**: Sidebar disappears instantly without animation
**Possible causes**:
- CSS transitions not applied
- `prefers-reduced-motion` setting enabled

**Solutions**:
- Check Elements tab → Styles → #sidebar
- Verify `transition: transform 0.3s ease, opacity 0.3s ease` is present
- Check for CSS specificity issues

### Issue 4: Console Shows Warnings
**Symptom**: `Sidebar or toggle button not found` in console
**Cause**: Elements not in DOM when script runs

**Solution**:
- Check HTML structure - sidebar should have `id="sidebar"`
- Toggle button should have `data-sidebar-toggle=""` attribute
- Make sure viewport is wide enough (>768px)

## Manual Testing Commands

Open Console and run these:

### Check if elements exist:
```javascript
console.log('Sidebar:', document.getElementById('sidebar'));
console.log('Toggle:', document.querySelector('[data-sidebar-toggle]'));
console.log('Restore:', document.querySelector('[data-restore-sidebar]'));
```

### Manually toggle sidebar:
```javascript
const sidebar = document.getElementById('sidebar');
sidebar.setAttribute('data-sidebar-state', 'closed'); // Close
sidebar.setAttribute('data-sidebar-state', 'open');   // Open
```

### Check current state:
```javascript
console.log(document.getElementById('sidebar').getAttribute('data-sidebar-state'));
console.log(localStorage.getItem('sidebarState'));
```

### Force reset:
```javascript
localStorage.removeItem('sidebarState');
location.reload();
```

## Expected Console Output (Normal Flow)

### On Page Load:
```
SidebarToggle initialized: {sidebar: true, toggleBtn: true, restoreBtn: true}
```

### On Toggle Button Click:
```
Toggle button clicked
Toggling sidebar: open -> closed
```

### On Restore Button Click:
```
Restore button clicked
```

## CSS Verification

The sidebar should have these styles when open:
```css
#sidebar {
  transform: translateX(0);
  opacity: 1;
  pointer-events: auto;
}
```

When closed:
```css
#sidebar[data-sidebar-state="closed"] {
  transform: translateX(100%);
  opacity: 0;
  pointer-events: none;
}
```

## If Nothing Works

Try this minimal test:
1. Open Console
2. Run:
```javascript
document.querySelector('[data-sidebar-toggle]').addEventListener('click', function() {
  alert('Button clicked!');
});
```
3. Click the button
4. If alert shows: JavaScript is working, issue is in the SidebarToggle class
5. If no alert: Button element issue or event blocking

## Next Steps

If you're still experiencing issues, please provide:
1. Complete console output
2. Screenshot of Elements tab showing the button
3. Window width (from console: `window.innerWidth`)
4. Any error messages in Console
