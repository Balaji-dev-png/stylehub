import os
import re

base_dir = r"c:\Users\shaty\Downloads\E-commerce\stylehub\static"

def read_file(name):
    with open(os.path.join(base_dir, name), 'r', encoding='utf-8') as f:
        return f.read()

def write_file(name, content):
    with open(os.path.join(base_dir, name), 'w', encoding='utf-8') as f:
        f.write(content)

style1 = read_file('style1.css')

# Extract footer block from style1
match = re.search(r'(/\* =========================================\s*THEME AWARE FOOTER\s*========================================= \*/.*?\n)(?:@media)', style1, re.DOTALL)

if match:
    footer_css = match.group(1)
    print("Found foot css!")
else:
    print("Could not extract from style1")
    footer_css = None

# Append to theme.css since theme.css goes everywhere and overwrite the rest.
if footer_css:
    theme_css = read_file('theme.css')
    if "THEME AWARE FOOTER" not in theme_css:
        theme_css += "\n\n" + footer_css
        write_file('theme.css', theme_css)
        print("Written to theme.css")

    # Now remove from style2-style11
    import glob
    for css_file in glob.glob(os.path.join(base_dir, 'style*.css')):
        if 'style1.css' in css_file: continue
        content = read_file(os.path.basename(css_file))
        # Use regex to strip .site-footer to the end or before media queries
        # Simply stripping specific blocks might be harder, but let's just wipe `.site-footer` related classes
        
        content = re.sub(r'\.site-footer\s*\{.*?\}', '', content, flags=re.DOTALL)
        content = re.sub(r'\.footer-content\s*\{.*?\}', '', content, flags=re.DOTALL)
        content = re.sub(r'\.footer-brand\s*\{.*?\}', '', content, flags=re.DOTALL)
        content = re.sub(r'\.footer-logo\s*\{.*?\}', '', content, flags=re.DOTALL)
        content = re.sub(r'\.social-icons\s*\{.*?\}', '', content, flags=re.DOTALL)
        content = re.sub(r'\.social-icons.*?', '', content) # Needs care
        write_file(os.path.basename(css_file), content)
        print(f"Cleaned {css_file}")
