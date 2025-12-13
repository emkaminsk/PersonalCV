# CV Synchronization Script

This directory contains a simple Python script that synchronizes CV content from LaTeX source files to the HTML website.

## Overview

The `sync_cv.py` script reads your CV content from LaTeX files in `awesome-CV/myCV/` and updates the corresponding sections in `index.html`.

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Run from the project root directory
python3 sync/sync_cv.py
```

The script will:
1. Create a timestamped backup of `index.html` (e.g., `index-20251213-214400.html.backup`)
2. Read all LaTeX CV files from `awesome-CV/myCV/`
3. Parse the content using regex patterns
4. Update the HTML sections in `index.html`
5. Save the updated HTML file

## What Gets Synchronized

### From LaTeX to HTML:

- **Personal Info** (`cv.tex`) → Meta tags, title, hero section, about section
- **Experience** (`cv/experience.tex`) → Experience section with all job entries
- **Education** (`cv/education.tex`) → Education section with all degrees
- **Skills** (`cv/skills.tex`) → Both sidebar and mobile accordion skills sections
- **Certificates** (`cv/certificates.tex`) → Trainings section in sidebar and accordion
- **Interests** (`cv/extracurricular.tex`) → Interests section

### What's Preserved in HTML:

- Name, email, phone number (not updated by script)
- Social media links
- CSS classes and styling
- Accessibility attributes (aria-labels, etc.)
- JavaScript functionality (theme switcher)

## LaTeX Content Mapping

The script understands these LaTeX macros:

- `\name{First}{Last}` - Person's name
- `\position{Title}` - Job position/title
- `\quote{"Description"}` - Professional summary
- `\cventry{title}{org}{location}{dates}{details}` - Experience/education entry
- `\cvskill{category}{skills}` - Skill category and items
- `\cvhonor{name}{issuer}{id}{date}` - Certificate/training
- `\item {text}` - Bullet point in lists

## Category Mapping

LaTeX skill categories are mapped to HTML sections:

| LaTeX Category | HTML Section |
|----------------|--------------|
| Product Management | Skills |
| Business Analysis | Skills |
| Modeling | Skills |
| Technical Skills | Technical Skills |
| Tools & Platforms | Technical Skills |
| Domain Knowledge | Skills |
| Languages | Languages |

## Backup Files

The script creates timestamped backups before making changes:
- Format: `index-YYYYMMDD-HHMMSS.html.backup`
- Location: Project root directory
- These are automatically ignored by git (see `.gitignore`)

## Troubleshooting

If the script reports 0 entries parsed:
1. Check that LaTeX files exist in `awesome-CV/myCV/cv/`
2. Verify the LaTeX syntax matches expected patterns
3. Run with Python 3.6 or higher

If HTML output looks incorrect:
1. Check one of the backup files to compare
2. Review the console output for warnings
3. Verify BeautifulSoup is installed correctly

## Technical Details

- **Language**: Python 3
- **Dependencies**: BeautifulSoup4, lxml
- **Size**: ~400 lines of code
- **Approach**: Simple regex parsing + DOM manipulation
- **No frameworks**: Just standard library + BS4

## Future Enhancements

Potential improvements (not currently implemented):
- Dry-run mode to preview changes
- Selective section updates
- HTML formatting/prettification
- Validation checks
- Detailed diff reports

---

**Last Updated**: 2025-12-13
**Implements**: `.ai/synchronization-plan.md`
