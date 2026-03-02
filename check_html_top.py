with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
if 'class="dual-track"' in text:
    print('Dual Track HTML found.')
else:
    print('Dual Track HTML NOT found.')

if 'class="track-container"' in text:
    print('Track Container found.')
