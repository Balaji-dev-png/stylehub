import os, re, glob
base_dir = r"c:\Users\shaty\Downloads\E-commerce\stylehub\static"

def read_file(name):
    with open(os.path.join(base_dir, name), 'r', encoding='utf-8') as f:
        return f.read()

def write_file(name, content):
    with open(os.path.join(base_dir, name), 'w', encoding='utf-8') as f:
        f.write(content)

style1 = read_file('style1.css')

# Extract footer block from style1 perfectly
match = re.search(r'(/\* =========================================\n\s*THEME AWARE FOOTER.*?)(?=@media)', style1, re.DOTALL)
if not match:
    print("Could not find footer in style1.css")
    exit()

footer_css = match.group(1)

# Write to theme.css
theme_css = read_file('theme.css')
if "THEME AWARE FOOTER" not in theme_css:
    theme_css += "\n\n" + footer_css
    write_file('theme.css', theme_css)
    print("Added footer to theme.css")

# Clean all other style files
cleaned = 0
for file_path in glob.glob(os.path.join(base_dir, 'style*.css')):
    filename = os.path.basename(file_path)
    if 'style1.css' == filename or 'style10' in filename or 'style11' in filename: 
        pass
        # style10 and style11 have footer at the end, let's just strip everything after `.site-footer` 
        # Actually I can apply the same logic to all.
    
    content = read_file(filename)
    
    # Match type 1: /* Footer */ down to /* ===========================
    content = re.sub(r'/\*\s*Footer\s*\*/.*?(?=\n/\* ===========================)', '', content, flags=re.DOTALL)
    
    # Match type 2: /* ===========================\n   FOOTER ... down to @media or EOF
    content = re.sub(r'/\* ===========================\n\s*FOOTER.*?(?=\n@media|\Z)', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Match type 3: Just `.site-footer {` down to `.footer-contact a { ... }` inclusive
    content = re.sub(r'\.site-footer\s*\{.*?\.footer-contact\s*a\s*\{[^}]*\}', '', content, flags=re.DOTALL)
    
    # Handle style3.css specifically which had `/* --- CORRECTED FOOTER CSS --- */`
    content = re.sub(r'/\* --- CORRECTED FOOTER CSS --- \*/.*?(?=\n/\* ===========================)', '', content, flags=re.DOTALL)
    
    write_file(filename, content)
    cleaned += 1

print(f"Cleaned {cleaned} files")
