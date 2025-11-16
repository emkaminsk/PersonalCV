#!/usr/bin/env node

/**
 * Image Optimization Script for Personal CV Website
 *
 * This script optimizes images for web performance by:
 * 1. Creating responsive sizes for hero background
 * 2. Converting images to WebP format with JPEG fallback
 * 3. Compressing images to ~80% quality
 *
 * Prerequisites:
 * - Node.js installed
 * - Run: npm install sharp
 *
 * Usage:
 * - node optimize-images.js
 */

const fs = require('fs');
const path = require('path');

// Check if sharp is installed
let sharp;
try {
  sharp = require('sharp');
} catch (error) {
  console.error('Error: Sharp is not installed.');
  console.error('Please run: npm install sharp');
  process.exit(1);
}

// Configuration
const config = {
  inputDir: './img',
  outputDir: './img',
  quality: 80,

  // Hero background responsive sizes
  heroSizes: [
    { width: 800, height: 267, suffix: '-800' },
    { width: 1200, height: 400, suffix: '-1200' },
    { width: 2000, height: 667, suffix: '-2000' },
    { width: 3000, height: 1000, suffix: '-3000' }
  ],

  // Profile image size
  profileSize: {
    width: 200,
    height: 200
  }
};

// Image processing tasks
const tasks = [
  {
    name: 'Hero Background',
    input: 'sascha-eremin-DNQ-M93tHmA-unsplash-3000x1000.jpg',
    sizes: config.heroSizes,
    prefix: 'hero'
  },
  {
    name: 'Profile Image',
    input: 'MK03.jpg',
    sizes: [{ width: config.profileSize.width, height: config.profileSize.height, suffix: '' }],
    prefix: 'MK03'
  }
];

/**
 * Process a single image: resize, compress, and convert to WebP
 */
async function processImage(inputPath, outputPath, width, height, quality) {
  try {
    const image = sharp(inputPath);

    // Resize and compress JPEG
    await image
      .resize(width, height, { fit: 'cover', position: 'center' })
      .jpeg({ quality, mozjpeg: true })
      .toFile(outputPath);

    console.log(`  ✓ Created JPEG: ${path.basename(outputPath)}`);

    // Convert to WebP
    const webpPath = outputPath.replace(/\.jpg$/, '.webp');
    await sharp(inputPath)
      .resize(width, height, { fit: 'cover', position: 'center' })
      .webp({ quality })
      .toFile(webpPath);

    console.log(`  ✓ Created WebP: ${path.basename(webpPath)}`);

    // Get file sizes
    const jpegSize = fs.statSync(outputPath).size;
    const webpSize = fs.statSync(webpPath).size;
    const savings = ((1 - webpSize / jpegSize) * 100).toFixed(1);

    console.log(`  📊 JPEG: ${formatBytes(jpegSize)}, WebP: ${formatBytes(webpSize)} (${savings}% smaller)`);

    return { jpegSize, webpSize };
  } catch (error) {
    console.error(`  ✗ Error processing image: ${error.message}`);
    return null;
  }
}

/**
 * Format bytes to human-readable size
 */
function formatBytes(bytes) {
  if (bytes === 0) return '0 Bytes';
  const k = 1024;
  const sizes = ['Bytes', 'KB', 'MB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
}

/**
 * Main optimization function
 */
async function optimizeImages() {
  console.log('🖼️  Personal CV - Image Optimization\n');
  console.log('Configuration:');
  console.log(`  Quality: ${config.quality}%`);
  console.log(`  Input Directory: ${config.inputDir}`);
  console.log(`  Output Directory: ${config.outputDir}\n`);

  let totalJpegSize = 0;
  let totalWebpSize = 0;
  let processedCount = 0;

  for (const task of tasks) {
    console.log(`Processing: ${task.name}`);
    console.log(`  Source: ${task.input}\n`);

    const inputPath = path.join(config.inputDir, task.input);

    // Check if input file exists
    if (!fs.existsSync(inputPath)) {
      console.error(`  ✗ Error: Input file not found: ${inputPath}\n`);
      continue;
    }

    // Process each size
    for (const size of task.sizes) {
      const suffix = size.suffix || '';
      const outputFilename = `${task.prefix}${suffix}.jpg`;
      const outputPath = path.join(config.outputDir, outputFilename);

      console.log(`  Creating ${size.width}x${size.height}...`);

      const result = await processImage(
        inputPath,
        outputPath,
        size.width,
        size.height,
        config.quality
      );

      if (result) {
        totalJpegSize += result.jpegSize;
        totalWebpSize += result.webpSize;
        processedCount++;
      }

      console.log('');
    }
  }

  // Summary
  console.log('─'.repeat(50));
  console.log('✅ Optimization Complete!\n');
  console.log('Summary:');
  console.log(`  Images processed: ${processedCount}`);
  console.log(`  Total JPEG size: ${formatBytes(totalJpegSize)}`);
  console.log(`  Total WebP size: ${formatBytes(totalWebpSize)}`);

  if (totalJpegSize > 0) {
    const totalSavings = ((1 - totalWebpSize / totalJpegSize) * 100).toFixed(1);
    console.log(`  Total savings: ${totalSavings}%\n`);
  }

  // Next steps
  console.log('Next Steps:');
  console.log('1. Update custom.css to use responsive background images');
  console.log('2. Update index.html to use <picture> element for profile image');
  console.log('3. Test image loading across different viewports');
  console.log('4. Run Lighthouse performance audit to verify improvements\n');

  console.log('See .ai/image-optimization-checklist.md for implementation details.');
}

// Run optimization
optimizeImages().catch(error => {
  console.error('Fatal error:', error);
  process.exit(1);
});
