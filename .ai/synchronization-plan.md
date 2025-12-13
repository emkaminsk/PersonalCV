# CV Synchronization Plan

## Executive Summary

This document outlines the implementation plan for a Python script that synchronizes CV content between two formats:
- **Source of Truth**: LaTeX files in `awesome-CV/myCV/` directory
- **Target**: HTML webpage (`index.html`)

The synchronization ensures the web presence stays up-to-date with the authoritative LaTeX CV while preserving the unique formatting and structural characteristics of each format.

---

## 1. Project Scope

### 1.1 In Scope
- Automated parsing of LaTeX CV files (`.tex` format)
- Extraction of structured content from LaTeX macros
- Update of HTML content sections while preserving structure
- Handling of content discrepancies and data transformation
- Generation of sync report with changes made
- CLI interface for manual execution
- Optional: Git integration for automatic commits

### 1.2 Out of Scope
- Real-time synchronization (scheduled/triggered execution only)
- Reverse synchronization (HTML → LaTeX)
- Modification of CSS styling or page layout
- PDF generation from LaTeX sources
- Validation of LaTeX compilation

### 1.3 Key Constraints
- Must preserve HTML semantic structure and accessibility attributes
- Must maintain responsive design (desktop sidebar vs. mobile accordion)
- Must keep JSON-LD structured data in sync
- Should handle content that exists in one format but not the other
- Must be idempotent (running multiple times produces same result)

---

## 2. Content Mapping Analysis

### 2.1 Discovered Content Discrepancies

#### Critical Discrepancies (Data Errors)
1. **Education dates mismatch**: HTML shows "November 2016 - June 2017" for University of Economics Master's degree, but LaTeX shows correct dates "Oct. 1996 - Feb. 2001"
2. **Missing recent updates**: LaTeX experience section has more recent accomplishments and quantifiable metrics
3. **Certificate differences**: LaTeX has newer certificates (10xDevs Nov 2025, AiDevs3 Dec 2024) not present in HTML

#### Structural Differences
1. **Personal information**:
   - LaTeX includes: mobile phone, different homepage (mkhome.byst.re vs marcinkaminski.com)
   - LaTeX has professional tagline/quote
2. **Skills organization**:
   - LaTeX: 7 structured categories (Product Management, Business Analysis, Modeling, Technical Skills, Tools & Platforms, Domain Knowledge, Languages)
   - HTML: 4 simpler categories (Skills, Technical Skills, Trainings, Languages)
3. **Interests/Extracurricular**:
   - LaTeX includes specific hobby projects
   - HTML has generic list

### 2.2 Content Mapping Table

| LaTeX Source | HTML Target | Transformation Required |
|--------------|-------------|-------------------------|
| `cv.tex` (header: `\name`, `\position`, `\email`, etc.) | `index.html` (line 54-61, 252-255) | Extract personal info, update meta tags, header, JSON-LD |
| `cv/experience.tex` (`\cventry` blocks) | `index.html` (lines 294-409, `.job-experience` divs) | Parse LaTeX entries → HTML job divs with proper structure |
| `cv/education.tex` (`\cventry` blocks) | `index.html` (lines 410-441, `.education-experience` divs) | Parse LaTeX entries → HTML education divs |
| `cv/skills.tex` (`\cvskill` blocks) | `index.html` (lines 584-633 sidebar, 448-581 accordion) | Map skill categories to both sidebar and mobile accordion |
| `cv/certificates.tex` (`\cvhonor` blocks) | `index.html` (lines 539-548, Trainings section) | Transform honors to training list items |
| `cv/extracurricular.tex` (`\cvitems`) | `index.html` (line 443, Interests section) | Extract interest items, format as text/list |
| Not in LaTeX (social links) | `index.html` (lines 166-203) | Preserve existing HTML social media links |

---

## 3. Technical Architecture

### 3.1 Technology Stack
- **Language**: Python 3.8+
- **Core Libraries**:
  - `argparse` - CLI interface
  - `re` (regex) - LaTeX parsing
  - `pathlib` - File system operations
  - `typing` - Type hints for code clarity
  - `dataclasses` - Structured data models
  - `beautifulsoup4` - HTML parsing and manipulation
  - `jinja2` - Optional: Template-based HTML generation
  - `pytest` - Unit testing

### 3.2 Project Structure
```
PersonalCV/
├── sync_cv.py                    # Main CLI entry point
├── cv_sync/                      # Python package
│   ├── __init__.py
│   ├── parsers/
│   │   ├── __init__.py
│   │   ├── latex_parser.py       # LaTeX content extraction
│   │   └── html_parser.py        # HTML structure analysis
│   ├── models/
│   │   ├── __init__.py
│   │   ├── cv_data.py            # Data models (Experience, Education, etc.)
│   │   └── mapping.py            # Content mapping configuration
│   ├── updaters/
│   │   ├── __init__.py
│   │   ├── html_updater.py       # HTML modification logic
│   │   └── metadata_updater.py   # JSON-LD and meta tag updates
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py             # Logging configuration
│   │   └── validators.py         # Content validation
│   └── config.py                 # Configuration constants
├── tests/
│   ├── __init__.py
│   ├── test_latex_parser.py
│   ├── test_html_updater.py
│   └── fixtures/                 # Test data samples
├── requirements.txt              # Python dependencies
└── .ai/
    └── synchronization-plan.md   # This document
```

### 3.3 Data Models

```python
@dataclass
class PersonalInfo:
    first_name: str
    last_name: str
    position: str
    address: str
    mobile: Optional[str]
    email: str
    homepage: Optional[str]
    github: Optional[str]
    linkedin: Optional[str]
    quote: Optional[str]

@dataclass
class Experience:
    job_title: str
    organization: str
    location: str
    date_range: str
    responsibilities: List[str]
    tools: Optional[str]
    technologies: Optional[str]

@dataclass
class Education:
    degree: str
    institution: str
    location: str
    date_range: str
    details: List[str]

@dataclass
class Skill:
    category: str
    items: List[str]

@dataclass
class Certificate:
    name: str
    issuer: str
    credential_id: Optional[str]
    date: Optional[str]

@dataclass
class CVData:
    personal_info: PersonalInfo
    experiences: List[Experience]
    education: List[Education]
    skills: List[Skill]
    certificates: List[Certificate]
    interests: List[str]
```

---

## 4. Implementation Plan

### Phase 1: LaTeX Parser Development (Priority: HIGH)

#### 4.1 Personal Information Extraction
**File**: `cv_sync/parsers/latex_parser.py`

**Regex Patterns**:
```python
PATTERNS = {
    'name': r'\\name\{([^}]+)\}\{([^}]+)\}',
    'position': r'\\position\{([^}]+)\}',
    'address': r'\\address\{([^}]+)\}',
    'mobile': r'\\mobile\{([^}]+)\}',
    'email': r'\\email\{([^}]+)\}',
    'homepage': r'\\homepage\{([^}]+)\}',
    'github': r'\\github\{([^}]+)\}',
    'linkedin': r'\\linkedin\{([^}]+)\}',
    'quote': r'\\quote\{``([^"]+)"\}',
}
```

**Implementation Steps**:
1. Read `awesome-CV/myCV/cv.tex` file
2. Apply regex patterns to extract personal information
3. Clean LaTeX special characters (e.g., `\&`, `\\`, `\enskip`, `\cdotp`)
4. Construct `PersonalInfo` dataclass instance
5. Validate extracted data (email format, required fields)

#### 4.2 Experience Section Parsing
**Target File**: `awesome-CV/myCV/cv/experience.tex`

**Parsing Strategy**:
```python
def parse_experience_section(content: str) -> List[Experience]:
    # 1. Split by \cventry macro
    # 2. Extract 5 parameters: {job_title}{org}{location}{dates}{details}
    # 3. Parse \cvitems environment within details
    # 4. Extract individual \item entries
    # 5. Identify tool/technology lines via patterns
    # 6. Return structured Experience objects
```

**Regex Pattern for cventry**:
```regex
\\cventry\s*\{([^}]+)\}\s*%[^\n]*\n\s*\{([^}]+)\}\s*%[^\n]*\n\s*\{([^}]+)\}\s*%[^\n]*\n\s*\{([^}]+)\}\s*%[^\n]*\n\s*\{((?:[^{}]|\{[^}]*\})*)\}
```

**Special Handling**:
- Parse nested `\begin{cvitems}...\end{cvitems}` blocks
- Extract `\item` entries with complete text including LaTeX formatting
- Identify lines starting with "Tools:" or "Project technologies:"
- Clean LaTeX symbols: `\&`, `\/`, `\\`, `\%`

#### 4.3 Education Section Parsing
**Target File**: `awesome-CV/myCV/cv/education.tex`

Similar structure to experience, parse `\cventry` blocks with parameters:
1. Degree
2. Institution
3. Location
4. Date range
5. Details (cvitems)

#### 4.4 Skills Section Parsing
**Target File**: `awesome-CV/myCV/cv/skills.tex`

**Parsing Strategy**:
```python
def parse_skills_section(content: str) -> List[Skill]:
    # 1. Find all \cvskill blocks
    # 2. Extract {category}{comma-separated skills}
    # 3. Split skills by comma, clean whitespace
    # 4. Return Skill objects
```

**Regex Pattern**:
```regex
\\cvskill\s*\{([^}]+)\}\s*%[^\n]*\n\s*\{([^}]+)\}
```

#### 4.5 Certificates Section Parsing
**Target File**: `awesome-CV/myCV/cv/certificates.tex`

Parse `\cvhonor` blocks:
```regex
\\cvhonor\s*\{([^}]+)\}\s*%[^\n]*\n\s*\{([^}]+)\}\s*%[^\n]*\n\s*\{([^}]*)\}\s*%[^\n]*\n\s*\{([^}]*)\}
```
Extract: {name}{issuer}{credential_id}{date}

#### 4.6 Extracurricular/Interests Parsing
**Target File**: `awesome-CV/myCV/cv/extracurricular.tex`

Extract items from `\cvitems` environment, combine into interest list.

---

### Phase 2: HTML Updater Development (Priority: HIGH)

#### 2.1 HTML Structure Analysis
**File**: `cv_sync/parsers/html_parser.py`

Use BeautifulSoup4 to:
1. Load `index.html` with parser
2. Identify key sections by ID/class
3. Extract current content for comparison
4. Preserve structural elements (divs, classes, attributes)

#### 2.2 Personal Information Update
**Target Locations in HTML**:
1. `<title>` tag (line 6)
2. Meta tags (lines 7-30): description, og:title, og:description, twitter:description
3. JSON-LD structured data (lines 50-150): name, givenName, familyName, jobTitle, email, worksFor
4. Hero section `<h1>` and `<h2>` (lines 253-255)
5. Contact information (lines 275-278)

**Update Strategy**:
```python
def update_personal_info(soup: BeautifulSoup, info: PersonalInfo):
    # Update title
    soup.title.string = f"{info.first_name} {info.last_name} - {info.position} CV"

    # Update meta tags
    soup.find('meta', {'name': 'description'})['content'] = info.quote

    # Update JSON-LD
    json_ld = json.loads(soup.find('script', {'type': 'application/ld+json'}).string)
    json_ld['name'] = f"{info.first_name} {info.last_name}"
    json_ld['givenName'] = info.first_name
    json_ld['familyName'] = info.last_name
    json_ld['jobTitle'] = info.position
    # ... update other fields

    # Update hero section
    soup.find('h1').string = "Personal CV page"
    soup.find('h2').string = info.position
```

#### 2.3 Experience Section Update
**Target**: `<div class="job-experience">` blocks (lines 296-409)

**Update Strategy**:
1. Find parent section containing experience
2. Remove all existing `.job-experience` divs
3. Generate new divs from `experiences` list using template
4. Insert in chronological order (newest first)

**HTML Template** (preserve existing structure):
```html
<div class="job-experience">
    <strong>{organization},</strong>
    <span class="job-title">{job_title}</span>
    <p>{date_range}</p>
    <ul>
        {for item in responsibilities}
        <li>{item}</li>
        {endfor}
    </ul>
    {if tools}
    <p>Tools: {tools}</p>
    {endif}
    {if technologies}
    <p>Project technologies: {technologies}</p>
    {endif}
</div>
```

#### 2.4 Education Section Update
**Target**: `<div class="education-experience">` blocks (lines 412-441)

Similar approach to experience:
1. Clear existing education divs
2. Generate from `education` list
3. Preserve structure with `<strong>`, `<span class="education-title">`, `<p>`, `<ul>`

#### 2.5 Skills Section Update (Dual Update)
**Targets**:
1. **Desktop Sidebar** (lines 584-633): `<aside id="sidebar">` with `<section class="sidebar-section">`
2. **Mobile Accordion** (lines 448-581): `<div class="accordion-container">` with `<div class="accordion-item">`

**Mapping Strategy**:
- Map LaTeX skill categories to HTML categories
- Some consolidation may be needed (7 LaTeX categories → 4 HTML categories)

**Category Mapping**:
| LaTeX Category | HTML Sidebar Section | HTML Accordion |
|----------------|---------------------|----------------|
| Product Management | Skills | Skills |
| Business Analysis | Skills | Skills |
| Modeling | Skills | Skills |
| Technical Skills | Technical Skills | Technical Skills |
| Tools & Platforms | Technical Skills | Technical Skills |
| Domain Knowledge | Skills | Skills |
| Languages | Languages | Languages |

**Implementation**:
```python
def update_skills_section(soup: BeautifulSoup, skills: List[Skill]):
    # Update sidebar
    sidebar = soup.find('aside', id='sidebar')
    for section in sidebar.find_all('section', class_='sidebar-section'):
        section.decompose()

    # Regenerate sections based on mapping
    # Similar for accordion
```

#### 2.6 Certificates/Trainings Update
**Target**: Trainings accordion section (lines 539-548)

Transform Certificate objects → list items in trainings section.

**Format**: `{name}` or `{name} - {issuer}` (if issuer notable)

#### 2.7 Interests Update
**Target**: Interests paragraph (line 443)

Replace with comma-separated interests from LaTeX extracurricular section.

---

### Phase 3: CLI and Orchestration (Priority: MEDIUM)

#### 3.1 Main Script (`sync_cv.py`)

**CLI Interface**:
```bash
# Basic usage
python sync_cv.py

# With options
python sync_cv.py --dry-run            # Show changes without applying
python sync_cv.py --verbose            # Detailed logging
python sync_cv.py --output report.txt  # Save sync report
python sync_cv.py --backup             # Create index.html.bak before update
python sync_cv.py --commit             # Auto-commit changes to git
```

**Argument Parsing**:
```python
parser = argparse.ArgumentParser(description='Sync CV from LaTeX to HTML')
parser.add_argument('--dry-run', action='store_true', help='Preview changes without applying')
parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
parser.add_argument('--output', '-o', type=str, help='Output report file')
parser.add_argument('--backup', '-b', action='store_true', help='Backup HTML before update')
parser.add_argument('--commit', '-c', action='store_true', help='Commit changes to git')
parser.add_argument('--latex-dir', default='awesome-CV/myCV', help='LaTeX source directory')
parser.add_argument('--html-file', default='index.html', help='HTML target file')
```

#### 3.2 Orchestration Flow

```python
def main():
    args = parse_args()

    # 1. Setup logging
    setup_logger(args.verbose)

    # 2. Parse LaTeX sources
    logger.info("Parsing LaTeX CV files...")
    cv_data = parse_latex_cv(args.latex_dir)

    # 3. Load HTML
    logger.info("Loading HTML file...")
    with open(args.html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # 4. Backup if requested
    if args.backup:
        backup_html(args.html_file)

    # 5. Apply updates
    logger.info("Applying updates...")
    updater = HTMLUpdater(soup, cv_data)
    changes = updater.apply_all_updates()

    # 6. Dry-run check
    if args.dry_run:
        print_changes(changes)
        return

    # 7. Write updated HTML
    logger.info("Writing updated HTML...")
    with open(args.html_file, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

    # 8. Generate report
    report = generate_sync_report(changes, cv_data)
    if args.output:
        save_report(report, args.output)
    print(report)

    # 9. Git commit
    if args.commit:
        commit_changes(args.html_file, cv_data)
```

#### 3.3 Change Detection and Reporting

Track what changed:
```python
@dataclass
class ChangeReport:
    section: str
    change_type: str  # 'added', 'updated', 'removed'
    old_value: Optional[str]
    new_value: str

def generate_sync_report(changes: List[ChangeReport], cv_data: CVData) -> str:
    report = [
        "CV Synchronization Report",
        "=" * 50,
        f"Timestamp: {datetime.now().isoformat()}",
        f"Source: awesome-CV/myCV/",
        f"Target: index.html",
        "",
        "Changes Applied:",
        "-" * 50,
    ]

    for change in changes:
        report.append(f"[{change.section}] {change.change_type}: {change.new_value}")

    return "\n".join(report)
```

---

### Phase 4: Testing and Validation (Priority: MEDIUM)

#### 4.1 Unit Tests

**Test Coverage**:
1. `test_latex_parser.py`:
   - Test personal info extraction with various formats
   - Test experience parsing with edge cases (special characters, multiple jobs)
   - Test education parsing
   - Test skills parsing with different category counts
   - Test certificate parsing with missing fields

2. `test_html_updater.py`:
   - Test personal info update preserves structure
   - Test experience section regeneration
   - Test sidebar and accordion sync
   - Test JSON-LD update
   - Test meta tag updates

3. `test_integration.py`:
   - End-to-end test with sample CV
   - Verify idempotency (running twice produces same result)
   - Test dry-run mode
   - Test backup functionality

**Test Fixtures**:
```
tests/fixtures/
├── sample_cv.tex          # Minimal LaTeX CV for testing
├── sample_experience.tex
├── sample_education.tex
├── sample_skills.tex
├── sample_index.html      # Minimal HTML for testing
└── expected_output.html   # Expected result after sync
```

#### 4.2 Validation Rules

Implement validators in `cv_sync/utils/validators.py`:

```python
def validate_cv_data(cv_data: CVData) -> List[str]:
    errors = []

    # Personal info validation
    if not cv_data.personal_info.email:
        errors.append("Email is required")
    if not re.match(r'^[^@]+@[^@]+\.[^@]+$', cv_data.personal_info.email):
        errors.append("Invalid email format")

    # Experience validation
    if not cv_data.experiences:
        errors.append("At least one experience entry required")

    for exp in cv_data.experiences:
        if not exp.job_title or not exp.organization:
            errors.append(f"Incomplete experience entry: {exp}")

    # Education validation
    if not cv_data.education:
        errors.append("At least one education entry required")

    return errors

def validate_html_output(html: str) -> List[str]:
    errors = []

    # Check critical sections exist
    if '<aside id="sidebar"' not in html:
        errors.append("Missing sidebar section")

    if 'class="job-experience"' not in html:
        errors.append("Missing experience section")

    # Check accessibility
    if 'aria-label' not in html:
        errors.append("Missing accessibility attributes")

    return errors
```

#### 4.3 Manual Testing Checklist

After synchronization, manually verify:
- [ ] Desktop view displays correctly
- [ ] Mobile accordion works (expand/collapse)
- [ ] Theme switcher still functions
- [ ] Social media links preserved
- [ ] All internal navigation links work
- [ ] JSON-LD validates (use Google Rich Results Test)
- [ ] Meta tags populated correctly
- [ ] Responsive breakpoints work (768px, 1024px)
- [ ] No broken HTML structure
- [ ] Character encoding correct (special characters, quotes)

---

### Phase 5: Documentation and Deployment (Priority: LOW)

#### 5.1 User Documentation

Create `README-sync.md`:
```markdown
# CV Synchronization Tool

## Overview
Automatically synchronizes CV content from LaTeX source files to HTML webpage.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
# Basic sync
python sync_cv.py

# Preview changes
python sync_cv.py --dry-run

# Create backup and commit
python sync_cv.py --backup --commit
```

## Configuration
Edit `cv_sync/config.py` to customize:
- Source/target file paths
- Category mappings
- Validation rules

## Troubleshooting
...
```

#### 5.2 Configuration File

**File**: `cv_sync/config.py`

```python
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent
LATEX_DIR = BASE_DIR / 'awesome-CV' / 'myCV'
HTML_FILE = BASE_DIR / 'index.html'

# LaTeX files
LATEX_MAIN = LATEX_DIR / 'cv.tex'
LATEX_EXPERIENCE = LATEX_DIR / 'cv' / 'experience.tex'
LATEX_EDUCATION = LATEX_DIR / 'cv' / 'education.tex'
LATEX_SKILLS = LATEX_DIR / 'cv' / 'skills.tex'
LATEX_CERTIFICATES = LATEX_DIR / 'cv' / 'certificates.tex'
LATEX_EXTRACURRICULAR = LATEX_DIR / 'cv' / 'extracurricular.tex'

# Category mappings
SKILL_CATEGORY_MAPPING = {
    'Product Management': 'Skills',
    'Business Analysis': 'Skills',
    'Modeling': 'Skills',
    'Technical Skills': 'Technical Skills',
    'Tools & Platforms': 'Technical Skills',
    'Domain Knowledge': 'Skills',
    'Languages': 'Languages',
}

# Validation
REQUIRED_SECTIONS = ['experience', 'education', 'skills']
MIN_EXPERIENCE_ENTRIES = 1
MIN_EDUCATION_ENTRIES = 1
```

#### 5.3 GitHub Actions Integration (Optional)

Create `.github/workflows/sync-cv.yml`:
```yaml
name: Sync CV

on:
  push:
    paths:
      - 'awesome-CV/myCV/**/*.tex'
  workflow_dispatch:

jobs:
  sync:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run CV sync
        run: python sync_cv.py --commit

      - name: Push changes
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git push
```

---

## 5. Error Handling and Edge Cases

### 5.1 LaTeX Parsing Errors

**Scenario**: Malformed LaTeX syntax
**Handling**:
- Catch regex matching failures
- Log warning with line number
- Skip malformed entry or use partial data
- Continue processing other sections

```python
try:
    experiences = parse_experience_section(content)
except ParseError as e:
    logger.warning(f"Failed to parse experience section: {e}")
    experiences = []  # Use empty list as fallback
```

### 5.2 Missing Content

**Scenario**: LaTeX file missing or empty section
**Handling**:
- Check file existence before parsing
- Return empty list for missing sections
- Include in validation report
- Don't modify corresponding HTML section if source missing

### 5.3 Character Encoding Issues

**Scenario**: Special characters in LaTeX (e.g., `\&`, `\"o`)
**Handling**:
- Maintain mapping of LaTeX special chars → Unicode
- Apply character replacement during parsing
- Validate output encoding is UTF-8

```python
LATEX_CHAR_MAP = {
    r'\&': '&',
    r'\"a': 'ä',
    r'\"o': 'ö',
    r'\"u': 'ü',
    r'\enskip': ' ',
    r'\cdotp': '·',
    # ... more mappings
}
```

### 5.4 HTML Structure Changes

**Scenario**: HTML template updated with different class names
**Handling**:
- Use flexible CSS selectors (fallback to multiple options)
- Log warning if expected structure not found
- Provide configuration override for selectors

### 5.5 Data Conflicts

**Scenario**: Content exists in HTML but not in LaTeX (e.g., social media links)
**Handling**:
- Define "preserve" sections in config
- Don't touch sections not managed by sync tool
- Document which sections are sync-managed vs. manual

---

## 6. Performance Considerations

### 6.1 Execution Time

**Expected Runtime**: < 2 seconds for typical CV
**Optimization**:
- Use compiled regex patterns (cache with `re.compile`)
- Parse HTML once, modify in memory
- Batch file I/O operations
- Avoid unnecessary deep copies

### 6.2 Memory Usage

**Expected Memory**: < 50MB for typical CV
**Optimization**:
- Stream large files if needed (unlikely for CVs)
- Release parsed objects after use
- Use generators for large lists

---

## 7. Future Enhancements

### 7.1 Phase 2 Features (Post-MVP)
1. **Bidirectional sync**: Update LaTeX from HTML changes
2. **Conflict resolution**: Interactive merge for discrepancies
3. **Version tracking**: Store sync history, rollback capability
4. **Web UI**: Simple Flask/FastAPI interface for non-technical users
5. **CI/CD integration**: Automatic sync on LaTeX commits
6. **Multi-format support**: Export to Markdown, JSON resume format
7. **Content validation**: Check for outdated dates, missing info
8. **Localization**: Support multiple languages (EN/PL)

### 7.2 Technical Debt
- Replace regex parsing with proper LaTeX parser library (e.g., `TexSoup`)
- Add type checking with `mypy`
- Implement comprehensive error recovery
- Add performance benchmarks

---

## 8. Dependencies

### 8.1 Python Packages

Create `requirements.txt`:
```
beautifulsoup4>=4.12.0
lxml>=4.9.0
argparse>=1.4.0
pytest>=7.4.0
pytest-cov>=4.1.0
```

### 8.2 Development Dependencies

Create `requirements-dev.txt`:
```
black>=23.0.0
flake8>=6.0.0
mypy>=1.4.0
pytest-watch>=4.2.0
```

---

## 9. Security Considerations

### 9.1 Input Validation
- Sanitize LaTeX input to prevent code injection
- Validate file paths to prevent directory traversal
- Limit file sizes to prevent DoS

### 9.2 Output Sanitization
- Escape HTML special characters in generated content
- Validate URLs in social media links
- Ensure email addresses are properly formatted

### 9.3 File Operations
- Check write permissions before modifying files
- Create atomic writes (write to temp, then rename)
- Validate backup creation success

---

## 10. Success Metrics

### 10.1 Functional Metrics
- ✅ All LaTeX sections successfully parsed (100% coverage)
- ✅ HTML structure preserved (no broken tags)
- ✅ JSON-LD validates against schema.org
- ✅ Mobile and desktop views render correctly
- ✅ Idempotent execution (same result on repeated runs)

### 10.2 Quality Metrics
- ✅ Unit test coverage > 80%
- ✅ No critical bugs in production use
- ✅ Sync completes in < 5 seconds
- ✅ Zero data loss (all LaTeX content transferred)

### 10.3 Usability Metrics
- ✅ CLI is intuitive (no manual needed for basic use)
- ✅ Error messages are actionable
- ✅ Dry-run preview is accurate

---

## 11. Implementation Timeline

### Week 1: Core Parsing
- **Days 1-2**: LaTeX parser development (personal info, experience, education)
- **Days 3-4**: LaTeX parser completion (skills, certificates, interests)
- **Day 5**: Unit tests for parsers

### Week 2: HTML Update Logic
- **Days 1-2**: HTML updater for main sections (personal, experience, education)
- **Days 3-4**: Skills section update (sidebar + accordion)
- **Day 5**: Metadata and JSON-LD updates

### Week 3: Integration and Testing
- **Days 1-2**: CLI implementation and orchestration
- **Days 3-4**: Integration testing, manual QA
- **Day 5**: Documentation, bug fixes

### Week 4: Polish and Deployment
- **Days 1-2**: Error handling, edge cases
- **Days 3-4**: Final testing, validation
- **Day 5**: Deployment, documentation finalization

**Total Estimated Effort**: 15-20 development days

---

## 12. Risks and Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| LaTeX syntax too complex for regex | High | Medium | Use TexSoup library as fallback |
| HTML structure changes frequently | Medium | Low | Flexible selectors, configuration |
| Data loss during sync | High | Low | Mandatory backup, dry-run mode |
| Character encoding issues | Medium | Medium | Comprehensive char mapping, testing |
| Performance degradation | Low | Low | Benchmark, optimize bottlenecks |
| User error (wrong flags) | Medium | Medium | Validation, confirmations, dry-run default |

---

## 13. Appendix

### A. LaTeX Macro Reference

**Awesome CV Macros Used**:
- `\name{First}{Last}` - Personal name
- `\position{Title}` - Job position/title
- `\address{Location}` - Physical address
- `\mobile{Phone}` - Mobile phone number
- `\email{Email}` - Email address
- `\homepage{URL}` - Personal website
- `\github{Username}` - GitHub profile
- `\linkedin{Username}` - LinkedIn profile
- `\quote{Text}` - Professional tagline
- `\cventry{Title}{Org}{Location}{Dates}{Details}` - Experience/Education entry
- `\cvskill{Category}{Skills}` - Skill category and items
- `\cvhonor{Name}{Issuer}{ID}{Date}` - Certificate/Honor

### B. HTML Section Reference

**Key HTML Sections**:
- `<title>` - Page title (line 6)
- `<meta name="description">` - Page description (line 8)
- `<script type="application/ld+json">` - Structured data (lines 50-150)
- `<nav>` - Navigation bar (lines 157-250)
- `<header class="container">` - Hero section (lines 251-257)
- `<section>` - Main content area (lines 261-444)
- `<aside id="sidebar">` - Desktop sidebar (lines 584-633)
- `<div class="accordion-container">` - Mobile accordion (lines 448-581)

### C. Regular Expression Patterns

**Key Regex Patterns**:
```python
# Personal info
NAME_PATTERN = r'\\name\{([^}]+)\}\{([^}]+)\}'
POSITION_PATTERN = r'\\position\{([^}]+)\}'

# Experience entry (multi-line)
CVENTRY_PATTERN = r'''
    \\cventry\s*
    \{([^}]+)\}\s*%[^\n]*\n\s*  # Job title
    \{([^}]+)\}\s*%[^\n]*\n\s*  # Organization
    \{([^}]+)\}\s*%[^\n]*\n\s*  # Location
    \{([^}]+)\}\s*%[^\n]*\n\s*  # Date range
    \{((?:[^{}]|\{[^}]*\})*)\}  # Details (nested braces allowed)
'''

# Skills
CVSKILL_PATTERN = r'\\cvskill\s*\{([^}]+)\}\s*%[^\n]*\n\s*\{([^}]+)\}'

# Items within cvitems environment
ITEM_PATTERN = r'\\item\s*\{([^}]+)\}'
```

---

## 14. Conclusion

This synchronization script will streamline CV maintenance by establishing the LaTeX files as the single source of truth and automatically propagating changes to the web presence. The implementation prioritizes:

1. **Accuracy**: Complete data transfer without loss
2. **Safety**: Backup and dry-run capabilities
3. **Maintainability**: Modular architecture, comprehensive tests
4. **Usability**: Simple CLI, clear error messages

Upon completion, updating the CV will require only:
1. Edit LaTeX files in `awesome-CV/myCV/`
2. Run `python sync_cv.py`
3. Review changes and commit

This reduces manual effort, eliminates synchronization errors, and ensures consistency across all CV formats.

---

**Document Version**: 1.0
**Author**: Claude (AI Assistant)
**Date**: 2025-12-13
**Status**: Ready for Implementation
