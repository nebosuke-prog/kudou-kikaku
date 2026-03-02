with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

if 'DELIVER BEYOND' in text:
    print('HTML is modern Version')
else:
    print('HTML is Old Version!')
