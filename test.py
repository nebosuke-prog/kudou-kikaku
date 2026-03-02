with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
if 'DELIVER BEYOND' in text:
    print('DELIVER BEYOND string found')
else:
    print('DELIVER BEYOND string NOT found!')

if 'hero-en-title' in text:
    print('hero-en-title class found')
else:
    print('hero-en-title NOT found')

