import os
import re

html_file = 'case-hazard.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_images = [
    '301dc123-06.png',
    '301dc123-07.png',
    '301dc123-08.png',
    '301dc123-11.png',
    '301dc123-17.png',
    '301dc123-18.png',
    '301dc123-19.png',
    '301dc123-22.png',
    '301dc123-24.png',
    '301dc123-27.png'
]

# We are replacing exactly 10 images that match 'case hazard \d+\.png'
def repl(match):
    repl.count += 1
    idx = repl.count - 1
    if idx < len(new_images):
        return new_images[idx]
    return match.group(0)
repl.count = 0

new_content = re.sub(r'case hazard \d+\.png', repl, content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Replaced {repl.count} images.")
