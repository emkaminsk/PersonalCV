# CV Synchronization Plan (SIMPLIFIED)

## Executive Summary

A simple Python script (~200 lines) that:
1. Reads LaTeX files from `awesome-CV/myCV/`
2. Extracts text content using regex
3. Makes a backup of `index.html` to file `index-<timestamp>.html.backup`
4. Updates corresponding HTML sections in `index.html` and saves this file.


**Core Principle**: This is text replacement, not a complex ETL pipeline. Keep it simple.

---

## 1. What Actually Needs to Happen

### The Simple Reality
- LaTeX has structured content in predictable format (Awesome CV template)
- HTML has corresponding sections with clear divs/classes
- We need to: read LaTeX → extract text → replace HTML sections
- Single script, run manually when CV updates, ~30 seconds of work

### What We DON'T Need
- ❌ Complex data models with dataclasses
- ❌ Elaborate CLI with 10 flags
- ❌ Comprehensive testing framework (basic tests are fine)
- ❌ Git integration (just run git commit manually)
- ❌ 4-week development timeline (should be 1-2 days)
- ❌ Change tracking and detailed reports
- ❌ Validation frameworks

---

## 2. Simple Content Mapping

### What to Extract from LaTeX

**From `cv.tex`:**
- Position → Update HTML title, meta tags, hero section
- Quote → Update meta description

**From `cv/experience.tex`:**
- Each `\cventry{job}{org}{location}{dates}{items}` → One `.job-experience` div

**From `cv/education.tex`:**
- Each `\cventry{degree}{school}{location}{dates}{items}` → One `.education-experience` div

**From `cv/skills.tex`:**
- Each `\cvskill{category}{skills}` → Update sidebar + accordion (same content, two places)

**From `cv/certificates.tex`:**
- Each `\cvhonor{name}{issuer}{id}{date}` → List item in Trainings section

**From `cv/extracurricular.tex`:**
- Extract interest items → Comma-separated text in Interests section

### What to Preserve in HTML
- Name, phone, email address - not changing data
- Social media links
- CSS classes and structure
- Accessibility attributes (aria-label, etc.)
- Theme switcher and JavaScript

---

## 3. Simple Implementation

### Single Script: `sync_cv.py`

**That's it. One file. Keep it simple**

```
PersonalCV/
├── sync/
    ├── sync_cv.py           # The entire script
    └── requirements.txt     # Just: beautifulsoup4, lxml
└── (existing files and folders)    
```

### Core Functions Needed

```python
#!/usr/bin/env python3
"""Sync CV from LaTeX to HTML - Simple version"""

from bs4 import BeautifulSoup
import re
from pathlib import Path

# 1. Read LaTeX files
def read_latex_file(path):
    return Path(path).read_text(encoding='utf-8')

# 2. Extract content with simple regex
def extract_cventry(content):
    """Extract \cventry{}{}{}{}{} blocks"""
    pattern = r'\\cventry\s*{([^}]+)}{([^}]+)}{([^}]+)}{([^}]+)}{([^}]+)}'
    return re.findall(pattern, content, re.DOTALL)

def extract_personal_info(content):
    """Extract \name, \position, \email, etc."""
    name = re.search(r'\\name{([^}]+)}{([^}]+)}', content)
    position = re.search(r'\\position{([^}]+)}', content)
    email = re.search(r'\\email{([^}]+)}', content)
    # ... etc
    return {'name': name, 'position': position, 'email': email}

# 3. Update HTML sections
def update_experience_section(soup, experiences):
    """Replace all .job-experience divs with new content"""
    # Find parent, clear old divs, add new ones
    pass

def update_skills_section(soup, skills):
    """Update both sidebar and accordion with same content"""
    pass

# 4. Main
def main():
    # Read LaTeX
    cv_main = read_latex_file('awesome-CV/myCV/cv.tex')
    experience = read_latex_file('awesome-CV/myCV/cv/experience.tex')
    education = read_latex_file('awesome-CV/myCV/cv/education.tex')
    skills = read_latex_file('awesome-CV/myCV/cv/skills.tex')

    # Parse content
    experiences = extract_cventry(experience)
    # ... parse other sections

    # Load HTML
    html = Path('index.html').read_text(encoding='utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    # Update sections
    update_experience_section(soup, experiences)
    # ... update other sections

    # Write back
    Path('index.html').write_text(str(soup), encoding='utf-8')
    print("✓ Sync complete")

if __name__ == '__main__':
    main()
```

**That's the entire architecture. No packages, no models, no CLI framework.**

---

## 4. Implementation Steps

### Basic Parsing

**Write 5-6 simple regex patterns:**
- `\name{}{}`  → extract first, last name
- `\position{}` → extract job title
- `\cventry{}{}{}{}{}` → extract experience/education entries
- `\cvskill{}{}` → extract skill categories
- `\item {}` → extract bullet points
- Clean LaTeX symbols: `\&` → `&`, `\enskip` → ` `, etc.

### HTML Update

**Write 3-4 update functions:**
```python
def update_experience_html(soup, experiences):
    # 1. Find section with id="experience"
    # 2. Remove all <div class="job-experience">
    # 3. For each experience, create new div:
    div = soup.new_tag('div', attrs={'class': 'job-experience'})
    # Add <strong>, <span>, <ul> with content
    # 4. Append to section
```

Same pattern for education, skills, interests.

**Key insight**: Skills appear in TWO places (sidebar + accordion), but it's the same content copied. Just update both locations with same loop.

### Testing & Polish

- Run script, check HTML renders correctly
- Fix any regex issues or HTML formatting
- Add basic error handling (file not found, etc.)
- Done.

---

## 5. Key Regex Patterns (Copy-Paste Ready)

```python
import re

# Clean LaTeX special chars
def clean_latex(text):
    replacements = {
        r'\&': '&',
        r'\\': '',
        r'\enskip': ' ',
        r'\cdotp': '·',
        r'\/': '/',
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.strip()

# Extract personal info
def parse_personal_info(content):
    first = re.search(r'\\name\{([^}]+)\}\{([^}]+)\}', content)
    position = re.search(r'\\position\{([^}]+)\}', content)
    email = re.search(r'\\email\{([^}]+)\}', content)
    return {
        'first_name': first.group(1) if first else '',
        'last_name': first.group(2) if first else '',
        'position': clean_latex(position.group(1)) if position else '',
        'email': email.group(1) if email else '',
    }

# Extract experience/education entries
def parse_cventry(content):
    # Matches \cventry{title}{org}{location}{dates}{details}
    pattern = r'\\cventry\s*\{([^}]+)\}[^{]*\{([^}]+)\}[^{]*\{([^}]+)\}[^{]*\{([^}]+)\}[^{]*\{([^}]+)\}'
    matches = re.findall(pattern, content, re.DOTALL)

    entries = []
    for match in matches:
        # Extract \item bullets from details
        items = re.findall(r'\\item\s*\{([^}]+)\}', match[4])
        entries.append({
            'title': clean_latex(match[0]),
            'org': clean_latex(match[1]),
            'location': clean_latex(match[2]),
            'dates': clean_latex(match[3]),
            'items': [clean_latex(item) for item in items]
        })
    return entries

# Extract skills
def parse_cvskill(content):
    pattern = r'\\cvskill\s*\{([^}]+)\}[^{]*\{([^}]+)\}'
    matches = re.findall(pattern, content)
    return [{'category': clean_latex(m[0]), 'skills': clean_latex(m[1])}
            for m in matches]
```

**That's literally all the parsing needed.**

---

## 6. Real Challenges (and Simple Solutions)

### Challenge 1: Nested braces in LaTeX
**Problem**: `\cventry{}{}{}{}{content with {nested} braces}`
**Simple solution**: Use `re.DOTALL` and match `[^}]+` for simple cases. For nested braces, just read until next `\cventry` and extract manually.

### Challenge 2: Skills appear in sidebar AND accordion
**Problem**: Need to update two HTML locations
**Simple solution**: Extract skills once, then loop twice:
```python
skills = parse_skills(content)
update_sidebar(soup, skills)  # First location
update_accordion(soup, skills)  # Second location, same data
```

### Challenge 3: LaTeX has 7 skill categories, HTML has 4
**Problem**: Need to map/combine categories
**Simple solution**: Hardcode a mapping dict:
```python
CATEGORY_MAP = {
    'Product Management': 'Skills',
    'Business Analysis': 'Skills',
    'Modeling': 'Skills',
    'Technical Skills': 'Technical Skills',
    'Tools & Platforms': 'Technical Skills',
    'Domain Knowledge': 'Skills',
    'Languages': 'Languages',
}
```

Then group skills by target category before updating HTML.

---

## 7. What About Testing?

**Realistic approach:**
- Write the script
- Run it on actual CV
- Open index.html in browser
- Does it look right? Yes → Done. No → Fix regex.

**That's the test.** No need for pytest fixtures and 80% coverage for a personal CV script.

Optional: Keep backup of index.html before running, so you can diff the changes.

---

## 8. Appendix

### LaTeX Macros (Quick Reference)
- `\name{First}{Last}` → Name
- `\position{Title}` → Job title
- `\email{Email}` → Email
- `\cventry{A}{B}{C}{D}{E}` → Experience/Education (title, org, location, dates, details)
- `\cvskill{Category}{Skills}` → Skills
- `\cvhonor{Name}{Issuer}{ID}{Date}` → Certificate
- `\item {Text}` → Bullet point

### HTML Targets (Quick Reference)
- Title, meta tags → Update with personal info
- Section with class `job-experience` → Experience entries
- Section with class `education-experience` → Education entries
- `<aside id="sidebar">` → Skills (desktop)
- `<div class="accordion-container">` → Skills (mobile)
- Interests section → Extracurricular text

---

## 9. Conclusion (Simplified)

**What we're building:** A 200-line Python script that reads LaTeX, extracts content with regex, updates HTML with BeautifulSoup.

**Usage:**
```bash
python sync_cv.py  # That's it
```

**Maintenance:** When you update LaTeX CV, run the script. Done.

No overengineering. No frameworks. Just simple text processing.

---

**Document Version**: 2.0 (SIMPLIFIED)
**Author**: Claude (AI Assistant)
**Reviewed**: MK, with corrections
**Date**: 2025-12-13
**Status**: Ready for Implementation (Realistic Version)
