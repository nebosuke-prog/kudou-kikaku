import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# メディアクエリ周りの括弧構造が壊れている部分を探して一発で直したいが
# 手動で置換した方が安全そうなので、問題箇所（余計なインデントがついている行450〜など）を特定。
print(f"Total length: {len(css_content)}")
