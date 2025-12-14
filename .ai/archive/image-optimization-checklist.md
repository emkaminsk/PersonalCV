# Image Optimization Checklist

## Current Status
The site currently uses unoptimized JPEG images that need to be converted to modern formats and responsive sizes for better performance.

## Images to Optimize

### 1. Profile Image (MK03.jpg)
- **Current**: 243x243px JPEG
- **Status**: ✅ Already has width/height attributes (200x200)
- **Status**: ✅ Already has loading="lazy"

**Actions Needed**:
- [ ] Convert to WebP format with JPEG fallback
- [ ] Compress to ~80% quality
- [ ] Update HTML to use `<picture>` element:
```html
<picture>
  <source srcset="./img/MK03.webp" type="image/webp">
  <img src="./img/MK03.jpg" alt="Marcin Kamiński" width="200" height="200" loading="lazy">
</picture>
```

### 2. Hero Background Image (sascha-eremin-DNQ-M93tHmA-unsplash-3000x1000.jpg)
- **Current**: 3000x1000px JPEG
- **Status**: ⚠️ No responsive sizes
- **Status**: ⚠️ Not optimized for different viewports

**Actions Needed**:
- [ ] Create responsive sizes:
  - Mobile: 800x267px
  - Tablet: 1200x400px
  - Desktop: 2000x667px
  - Large: 3000x1000px (current)
- [ ] Convert each size to WebP with JPEG fallback
- [ ] Compress to ~80% quality
- [ ] Update CSS to use responsive images:

```css
/* Mobile first */
.hero {
  background-color: #394046; /* Fallback color */
  background-image: url("img/hero-800.jpg");
  background-position: center;
  background-size: cover;
}

/* Tablet */
@media (min-width: 768px) {
  .hero {
    background-image: url("img/hero-1200.jpg");
  }

  /* WebP support */
  .webp .hero {
    background-image: url("img/hero-1200.webp");
  }
}

/* Desktop */
@media (min-width: 1200px) {
  .hero {
    background-image: url("img/hero-2000.jpg");
  }

  /* WebP support */
  .webp .hero {
    background-image: url("img/hero-2000.webp");
  }
}

/* Large screens */
@media (min-width: 2000px) {
  .hero {
    background-image: url("img/hero-3000.jpg");
  }

  /* WebP support */
  .webp .hero {
    background-image: url("img/hero-3000.webp");
  }
}
```

## Image Optimization Tools

### Option 1: Using ImageMagick (Command Line)
```bash
# Install ImageMagick
sudo apt-get install imagemagick

# Resize hero image for different viewports
convert img/sascha-eremin-DNQ-M93tHmA-unsplash-3000x1000.jpg -resize 800x267 -quality 80 img/hero-800.jpg
convert img/sascha-eremin-DNQ-M93tHmA-unsplash-3000x1000.jpg -resize 1200x400 -quality 80 img/hero-1200.jpg
convert img/sascha-eremin-DNQ-M93tHmA-unsplash-3000x1000.jpg -resize 2000x667 -quality 80 img/hero-2000.jpg
convert img/sascha-eremin-DNQ-M93tHmA-unsplash-3000x1000.jpg -quality 80 img/hero-3000.jpg

# Compress profile image
convert img/MK03.jpg -quality 80 -resize 200x200 img/MK03-optimized.jpg
```

### Option 2: Using cwebp (WebP Conversion)
```bash
# Install webp tools
sudo apt-get install webp

# Convert to WebP
cwebp -q 80 img/hero-800.jpg -o img/hero-800.webp
cwebp -q 80 img/hero-1200.jpg -o img/hero-1200.webp
cwebp -q 80 img/hero-2000.jpg -o img/hero-2000.webp
cwebp -q 80 img/hero-3000.jpg -o img/hero-3000.webp
cwebp -q 80 img/MK03-optimized.jpg -o img/MK03.webp
```

### Option 3: Using Online Tools
- **Squoosh**: https://squoosh.app/ (Google's image compression tool)
- **TinyPNG**: https://tinypng.com/ (Online compression)
- **CloudConvert**: https://cloudconvert.com/ (Format conversion)

### Option 4: Using Node.js Sharp
```bash
# Install sharp
npm install sharp

# Create optimization script
node optimize-images.js
```

## WebP Detection Script

Add this to the beginning of `<head>` to detect WebP support:

```html
<script>
  (function() {
    const webpTest = new Image();
    webpTest.onload = webpTest.onerror = function() {
      if (webpTest.height === 2) {
        document.documentElement.classList.add('webp');
      }
    };
    webpTest.src = 'data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA';
  })();
</script>
```

## Performance Targets

After optimization, images should meet these targets:
- [ ] **Profile image**: < 20KB (currently ~15KB based on 243x243)
- [ ] **Hero background (mobile, 800px)**: < 50KB
- [ ] **Hero background (tablet, 1200px)**: < 100KB
- [ ] **Hero background (desktop, 2000px)**: < 150KB
- [ ] **Hero background (large, 3000px)**: < 200KB

## Verification

After implementing image optimization:
1. Test with Lighthouse Performance audit
2. Verify LCP (Largest Contentful Paint) < 2.5s
3. Verify no CLS (Cumulative Layout Shift) from images
4. Check network tab for correct image loading
5. Test on slow 3G connection

## Expected Performance Impact

- **Before**: Hero image ~300-500KB, LCP likely >3s on slow connections
- **After**: Hero image ~50-150KB (depending on viewport), LCP <2.5s

## Related Files to Update

- [ ] `index.html` - Update image elements with `<picture>` tags
- [ ] `custom.css` - Add responsive background images with WebP support
- [ ] `js/main.js` - Add WebP detection if not using CSS-only approach
