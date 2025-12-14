#!/usr/bin/env python3
"""
CV Synchronization Script
Syncs content from LaTeX CV files to HTML index.html
Simple version - no overengineering
"""

import re
import sys
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup  # type: ignore[import-untyped]


# =============================================================================
# LaTeX Parsing Functions
# =============================================================================

def clean_latex(text):
    """Clean LaTeX special characters and commands"""
    if not text:
        return ""

    replacements = {
        r'\&': '&',
        r'\\': '',
        r'\enskip': ' ',
        r'\cdotp': '·',
        r'\/': '/',
        r'\item': '',
        r'\%': '%',
        r'\#': '#',
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove extra whitespace
    text = ' '.join(text.split())
    return text.strip()


def read_latex_file(path):
    """Read a LaTeX file and return its content"""
    return Path(path).read_text(encoding='utf-8')


def parse_personal_info(content):
    """Extract personal information from cv.tex"""
    first = re.search(r'\\name\{([^}]+)\}\{([^}]+)\}', content)

    # Extract position with nested braces support
    position_match = re.search(r'\\position\{((?:[^{}]|\\[{}]|{[^}]*})*)\}', content)
    position_text = ''
    if position_match:
        position_text = position_match.group(1)
        # Replace {\enskip\cdotp\enskip} with comma
        position_text = position_text.replace(r'{\enskip\cdotp\enskip}', ', ')

    quote = re.search(r'\\quote\{``([^"]+)"', content)

    return {
        'first_name': first.group(1) if first else '',
        'last_name': first.group(2) if first else '',
        'position': clean_latex(position_text),
        'quote': clean_latex(quote.group(1)) if quote else '',
    }


def parse_cventry(content):
    """Extract cventry{}{}{}{}{} blocks from LaTeX"""
    entries = []

    # Find all \cventry blocks - split by \cventry
    parts = re.split(r'\\cventry', content)

    for part in parts[1:]:  # Skip first empty part
        # Extract the 5 arguments manually with better brace handling
        args = []
        brace_count = 0
        current_arg = ""
        in_arg = False

        for char in part:
            if char == '{':
                if in_arg:
                    brace_count += 1
                    if brace_count > 1:  # Only add if nested
                        current_arg += char
                else:
                    in_arg = True
                    brace_count = 1
            elif char == '}':
                if in_arg:
                    brace_count -= 1
                    if brace_count == 0:
                        args.append(current_arg.strip())
                        current_arg = ""
                        in_arg = False
                        if len(args) == 5:  # Got all 5 arguments
                            break
                    else:
                        current_arg += char
            elif in_arg:
                current_arg += char

        if len(args) == 5:
            # Extract \item bullets from the 5th argument (details)
            items = re.findall(r'\\item\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', args[4], re.DOTALL)

            entries.append({
                'title': clean_latex(args[0]),
                'org': clean_latex(args[1]),
                'location': clean_latex(args[2]),
                'dates': clean_latex(args[3]),
                'items': [clean_latex(item) for item in items]
            })

    return entries


def parse_cvskill(content):
    """Extract cvskill{}{} blocks from LaTeX"""
    skills = []

    # Find all \cvskill blocks - split by \cvskill
    parts = re.split(r'\\cvskill', content)

    for part in parts[1:]:  # Skip first empty part
        # Extract the 2 arguments manually
        args = []
        brace_count = 0
        current_arg = ""
        in_arg = False

        for char in part:
            if char == '{':
                if in_arg:
                    brace_count += 1
                    if brace_count > 1:  # Only add if nested
                        current_arg += char
                else:
                    in_arg = True
                    brace_count = 1
            elif char == '}':
                if in_arg:
                    brace_count -= 1
                    if brace_count == 0:
                        args.append(current_arg.strip())
                        current_arg = ""
                        in_arg = False
                        if len(args) == 2:  # Got both arguments
                            break
                    else:
                        current_arg += char
            elif in_arg:
                current_arg += char

        if len(args) == 2:
            skills.append({
                'category': clean_latex(args[0]),
                'skills': clean_latex(args[1])
            })

    return skills


def parse_cvhonor(content):
    """Extract cvhonor{}{}{}{} blocks from LaTeX"""
    honors = []

    # Find all \cvhonor blocks - split by \cvhonor
    parts = re.split(r'\\cvhonor', content)

    for part in parts[1:]:  # Skip first empty part
        # Extract the 4 arguments manually
        args = []
        brace_count = 0
        current_arg = ""
        in_arg = False

        for char in part:
            if char == '{':
                if in_arg:
                    brace_count += 1
                    if brace_count > 1:  # Only add if nested
                        current_arg += char
                else:
                    in_arg = True
                    brace_count = 1
            elif char == '}':
                if in_arg:
                    brace_count -= 1
                    if brace_count == 0:
                        args.append(current_arg.strip())
                        current_arg = ""
                        in_arg = False
                        if len(args) == 4:  # Got all 4 arguments
                            break
                    else:
                        current_arg += char
            elif in_arg:
                current_arg += char

        if len(args) == 4:
            honors.append({
                'name': clean_latex(args[0]),
                'issuer': clean_latex(args[1]),
                'id': clean_latex(args[2]),
                'date': clean_latex(args[3])
            })

    return honors


def parse_interests(content):
    """Extract interest items from extracurricular.tex"""
    # Extract all \item content from the file
    items = re.findall(r'\\item\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}', content, re.DOTALL)
    return [clean_latex(item) for item in items]


# =============================================================================
# HTML Update Functions
# =============================================================================

def update_meta_tags(soup, personal_info):
    """Update meta tags and title with personal information"""
    # Create full name for use in multiple meta tags
    name = f"{personal_info['first_name']} {personal_info['last_name']}"

    # Update title
    title = soup.find('title')
    if title:
        title.string = f"{name} - {personal_info['position']} CV"

    # Update meta description
    meta_desc = soup.find('meta', {'name': 'description'})
    if meta_desc and personal_info['quote']:
        meta_desc['content'] = personal_info['quote']

    # Update Open Graph title
    og_title = soup.find('meta', {'property': 'og:title'})
    if og_title:
        og_title['content'] = f"{name} - {personal_info['position']}"

    # Update Open Graph description
    og_desc = soup.find('meta', {'property': 'og:description'})
    if og_desc and personal_info['quote']:
        og_desc['content'] = personal_info['quote']

    # Update Twitter title
    tw_title = soup.find('meta', {'name': 'twitter:title'})
    if tw_title:
        tw_title['content'] = f"{name} - {personal_info['position']}"

    # Update Twitter description
    tw_desc = soup.find('meta', {'name': 'twitter:description'})
    if tw_desc and personal_info['quote']:
        tw_desc['content'] = personal_info['quote']


def update_hero_section(soup, personal_info):
    """Update hero section with position"""
    header = soup.find('header', {'class': 'container'})
    if header:
        h2 = header.find('h2')
        if h2:
            h2.string = personal_info['position']


def update_about_section(soup, personal_info):
    """Update about me section with quote"""
    about_section = soup.find('div', {'class': 'about-me-section'})
    if about_section and personal_info['quote']:
        hgroup = about_section.find('hgroup')
        if hgroup:
            p = hgroup.find('p')
            if p:
                p.string = clean_latex(personal_info['quote'])


def update_experience_section(soup, experiences):
    """Replace all job experience divs with new content from LaTeX"""
    # Find the experience section
    experience_h3 = soup.find('h3', {'id': 'experience'})
    if not experience_h3:
        print("⚠ Warning: Experience section not found")
        return

    # Remove all existing job-experience divs
    for div in soup.find_all('div', {'class': 'job-experience'}):
        div.decompose()

    # Add new experiences
    for exp in experiences:
        div = soup.new_tag('div', attrs={'class': 'job-experience'})

        # Organization name
        strong = soup.new_tag('strong')
        strong.string = f"{exp['org']},"
        div.append(strong)
        div.append(' ')

        # Job title
        span = soup.new_tag('span', attrs={'class': 'job-title'})
        span.string = exp['title']
        div.append(span)

        # Dates
        p_dates = soup.new_tag('p')
        p_dates.string = exp['dates']
        div.append(p_dates)

        # Items list
        if exp['items']:
            ul = soup.new_tag('ul')
            for item in exp['items']:
                li = soup.new_tag('li')
                li.string = item
                ul.append(li)
            div.append(ul)

        # Insert after experience h3
        experience_h3.insert_after(div)

    # Fix order: collect all divs and re-insert in correct order
    # Since insert_after() reverses the initial order, we need to reverse back
    # Collect all divs
    divs = []
    current = experience_h3.find_next_sibling('div', {'class': 'job-experience'})
    while current:
        divs.append(current)
        next_div = current.find_next_sibling('div', {'class': 'job-experience'})
        current.extract()
        current = next_div

    # Re-insert in same order (divs already reversed from first insertion)
    for div in divs:
        experience_h3.insert_after(div)


def update_education_section(soup, education):
    """Replace all education experience divs with new content from LaTeX"""
    # Find the education section
    education_h3 = soup.find('h3', {'id': 'education'})
    if not education_h3:
        print("⚠ Warning: Education section not found")
        return

    # Remove all existing education-experience divs
    for div in soup.find_all('div', {'class': 'education-experience'}):
        div.decompose()

    # Add new education entries
    for edu in education:
        div = soup.new_tag('div', attrs={'class': 'education-experience'})

        # Degree
        strong = soup.new_tag('strong')
        strong.string = edu['title']
        div.append(strong)

        # Institution
        p_inst = soup.new_tag('p')
        p_inst.string = edu['org']
        div.append(p_inst)

        # Dates
        p_dates = soup.new_tag('p')
        p_dates.string = edu['dates']
        div.append(p_dates)

        # Items list
        if edu['items']:
            ul = soup.new_tag('ul')
            for item in edu['items']:
                li = soup.new_tag('li')
                li.string = item
                ul.append(li)
            div.append(ul)

        # Insert after education h3
        education_h3.insert_after(div)

    # Fix order: collect all divs and re-insert in correct order
    # Since insert_after() reverses the initial order, we need to reverse back
    divs = []
    current = education_h3.find_next_sibling('div', {'class': 'education-experience'})
    while current:
        divs.append(current)
        next_div = current.find_next_sibling('div', {'class': 'education-experience'})
        current.extract()
        current = next_div

    # Re-insert in same order (divs already reversed from first insertion)
    for div in divs:
        education_h3.insert_after(div)


def update_skills_sections(soup, skills):
    """Update both sidebar and accordion with skills"""
    # Category mapping (LaTeX -> HTML)
    CATEGORY_MAP = {
        'Product Management': 'Skills',
        'Business Analysis': 'Skills',
        'Modeling': 'Skills',
        'Technical Skills': 'Technical Skills',
        'Tools & Platforms': 'Technical Skills',
        'Domain Knowledge': 'Skills',
        'Languages': 'Languages',
    }

    # Group skills by target HTML category
    grouped = {}
    for skill in skills:
        latex_cat = skill['category']
        html_cat = CATEGORY_MAP.get(latex_cat, 'Skills')

        if html_cat not in grouped:
            grouped[html_cat] = []
        grouped[html_cat].append(skill['skills'])

    # Update sidebar
    sidebar = soup.find('aside', {'id': 'sidebar'})
    if sidebar:
        for html_cat, skill_list in grouped.items():
            # Find section with h4 matching category
            sections = sidebar.find_all('section', {'class': 'sidebar-section'})
            for section in sections:
                h4 = section.find('h4')
                if h4 and h4.string == html_cat:
                    # Clear existing ul
                    ul = section.find('ul')
                    if ul:
                        ul.clear()
                        # Add new skills
                        for skills_text in skill_list:
                            li = soup.new_tag('li')
                            li.string = skills_text
                            ul.append(li)

    # Update accordion (mobile view)
    accordion = soup.find('div', {'class': 'accordion-container'})
    if accordion:
        for html_cat, skill_list in grouped.items():
            # Find accordion item matching category
            items = accordion.find_all('div', {'class': 'accordion-item'})
            for item in items:
                button = item.find('button', {'class': 'accordion-header'})
                if button:
                    span = button.find('span')
                    if span and span.string == html_cat:
                        # Find the panel
                        panel = item.find('div', {'class': 'accordion-panel'})
                        if panel:
                            ul = panel.find('ul')
                            if ul:
                                ul.clear()
                                # Add new skills
                                for skills_text in skill_list:
                                    li = soup.new_tag('li')
                                    li.string = skills_text
                                    ul.append(li)


def update_trainings_section(soup, certificates):
    """Update trainings/certificates in sidebar and accordion"""
    # Update sidebar
    sidebar = soup.find('aside', {'id': 'sidebar'})
    if sidebar:
        sections = sidebar.find_all('section', {'class': 'sidebar-section'})
        for section in sections:
            h4 = section.find('h4')
            if h4 and h4.string == 'Trainings':
                ul = section.find('ul')
                if ul:
                    ul.clear()
                    for cert in certificates:
                        li = soup.new_tag('li')
                        if cert['date']:
                            li.string = f"{cert['name']} - {cert['date']}"
                        else:
                            li.string = cert['name']
                        ul.append(li)

    # Update accordion
    accordion = soup.find('div', {'class': 'accordion-container'})
    if accordion:
        items = accordion.find_all('div', {'class': 'accordion-item'})
        for item in items:
            button = item.find('button', {'class': 'accordion-header'})
            if button:
                span = button.find('span')
                if span and span.string == 'Trainings':
                    panel = item.find('div', {'class': 'accordion-panel'})
                    if panel:
                        ul = panel.find('ul')
                        if ul:
                            ul.clear()
                            for cert in certificates:
                                li = soup.new_tag('li')
                                if cert['date']:
                                    li.string = f"{cert['name']} - {cert['date']}"
                                else:
                                    li.string = cert['name']
                                ul.append(li)


def update_interests_section(soup, interests):
    """Update interests section"""
    interests_h3 = soup.find('h3', {'id': 'interests'})
    if interests_h3:
        # Remove all existing p tags after h3 until next h3 or major section
        current = interests_h3.find_next_sibling('p')
        while current:
            next_sibling = current.find_next_sibling()
            if next_sibling and next_sibling.name in ['h3', 'h2', 'aside']:
                break
            current.decompose()
            current = next_sibling if next_sibling and next_sibling.name == 'p' else None

        # Insert a paragraph for each interest
        for interest in interests:
            p = soup.new_tag('p')
            p.string = interest
            interests_h3.insert_after(p)
            interests_h3 = p  # Move anchor for next insertion


# =============================================================================
# Main Function
# =============================================================================

def create_backup(html_path):
    """Create a timestamped backup of index.html"""
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    backup_path = html_path.parent / f"index-{timestamp}.html.backup"
    backup_path.write_text(html_path.read_text(encoding='utf-8'), encoding='utf-8')
    print(f"✓ Backup created: {backup_path.name}")
    return backup_path


def find_latest_backup(base_path):
    """Find the most recent backup file in the base directory"""
    backup_files = sorted(base_path.glob('index-*.html.backup'))
    return backup_files[-1] if backup_files else None


def revert_to_backup(base_path):
    """Restore index.html from the latest backup file"""
    print("=" * 60)
    print("CV Revert: Restoring from Latest Backup")
    print("=" * 60)

    html_path = base_path / 'index.html'
    backup_file = find_latest_backup(base_path)

    if not backup_file:
        print("✗ No backup files found")
        sys.exit(1)

    print(f"\n✓ Found backup: {backup_file.name}")

    # Restore from backup
    html_path.write_text(backup_file.read_text(encoding='utf-8'), encoding='utf-8')
    print(f"✓ Restored index.html from {backup_file.name}")
    print("\n" + "=" * 60)
    print("✓ Revert complete!")
    print("=" * 60)


def sync():
    """Main synchronization function"""
    print("=" * 60)
    print("CV Synchronization: LaTeX → HTML")
    print("=" * 60)

    # Define paths
    base_path = Path(__file__).parent.parent
    latex_path = base_path / '.awesome-CV' / 'myCV'
    html_path = base_path / 'index.html'

    # 1. Create backup
    print("\n[1/5] Creating backup...")
    create_backup(html_path)

    # 2. Read LaTeX files
    print("\n[2/5] Reading LaTeX files...")
    cv_main = read_latex_file(latex_path / 'cv.tex')
    experience = read_latex_file(latex_path / 'cv' / 'experience.tex')
    education = read_latex_file(latex_path / 'cv' / 'education.tex')
    skills = read_latex_file(latex_path / 'cv' / 'skills.tex')
    certificates = read_latex_file(latex_path / 'cv' / 'certificates.tex')
    extracurricular = read_latex_file(latex_path / 'cv' / 'extracurricular.tex')
    print("✓ LaTeX files read successfully")

    # 3. Parse content
    print("\n[3/5] Parsing LaTeX content...")
    personal_info = parse_personal_info(cv_main)
    experiences = parse_cventry(experience)
    education_entries = parse_cventry(education)
    skill_entries = parse_cvskill(skills)
    cert_entries = parse_cvhonor(certificates)
    interests_list = parse_interests(extracurricular)

    print(f"  - Personal info: {personal_info['first_name']} {personal_info['last_name']}")
    print(f"  - Experience entries: {len(experiences)}")
    print(f"  - Education entries: {len(education_entries)}")
    print(f"  - Skill categories: {len(skill_entries)}")
    print(f"  - Certificates: {len(cert_entries)}")
    print(f"  - Interest items: {len(interests_list)}")

    # 4. Load and parse HTML
    print("\n[4/5] Loading HTML...")
    html_content = html_path.read_text(encoding='utf-8')
    soup = BeautifulSoup(html_content, 'html.parser')
    print("✓ HTML loaded successfully")

    # 5. Update HTML sections
    print("\n[5/5] Updating HTML sections...")
    update_meta_tags(soup, personal_info)
    print("  ✓ Meta tags updated")

    update_hero_section(soup, personal_info)
    print("  ✓ Hero section updated")

    update_about_section(soup, personal_info)
    print("  ✓ About section updated")

    update_experience_section(soup, experiences)
    print("  ✓ Experience section updated")

    update_education_section(soup, education_entries)
    print("  ✓ Education section updated")

    update_skills_sections(soup, skill_entries)
    print("  ✓ Skills sections updated")

    update_trainings_section(soup, cert_entries)
    print("  ✓ Trainings section updated")

    update_interests_section(soup, interests_list)
    print("  ✓ Interests section updated")

    # 6. Write updated HTML
    html_path.write_text(str(soup), encoding='utf-8')

    print("\n" + "=" * 60)
    print("✓ Synchronization complete!")
    print("=" * 60)


if __name__ == '__main__':
    base_path = Path(__file__).parent.parent

    if '--revert' in sys.argv:
        revert_to_backup(base_path)
    else:
        sync()
