import re

text = open(r'C:\Users\frota\Documents\Projetos\AI TUTOR\data\modules\sadiku\sections\ch01_12-systems-of-units.md', encoding='utf-8').read()
matches = re.findall(r'<garbled[^>]*/>', text)
print(f'Total tags: {len(matches)}')
ids = set()
for m in matches:
    idm = re.search(r'id="?(\d+)"?', m)
    if idm:
        ids.add(idm.group(1))
print(f'Unique IDs: {len(ids)}')
for m in matches[:5]:
    print(f'  {m}')
