import os
import glob

template_dir = r"c:\Users\shaty\Downloads\E-commerce\stylehub\templates"
for filepath in glob.glob(os.path.join(template_dir, "*.html")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    replacements = [
        ('<div class=\"logo\">Style<span>hub</span></div>', '<a href=\"{% url \'home\' %}\" style=\"text-decoration: none; color: inherit;\"><div class=\"logo\">Style<span>hub</span></div></a>'),
        ('<div class=\"logo\">Style<span>hub</span> Admin</div>', '<a href=\"{% url \'home\' %}\" style=\"text-decoration: none; color: inherit;\"><div class=\"logo\">Style<span>hub</span> Admin</div></a>'),
        ('<div class=\"card-logo\">Style<span>hub</span></div>', '<a href=\"{% url \'home\' %}\" style=\"text-decoration: none; color: inherit;\"><div class=\"card-logo\">Style<span>hub</span></div></a>'),
        ('<h2 class=\"footer-logo\">Stylehub™</h2>', '<a href=\"{% url \'home\' %}\" style=\"text-decoration: none; color: inherit;\"><h2 class=\"footer-logo\">Stylehub™</h2></a>')
    ]
    
    new_content = content
    for old, new in replacements:
        new_content = new_content.replace(old, new)
        
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")
print("Done!")
