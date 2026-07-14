import re

# Simulate the exact TypeScript regex on the exact API response
text_source = open(r'C:\Users\frota\Documents\Projetos\AI TUTOR\data\knowledge_bases\sadiku\raw\ch01_12-systems-of-units.md', encoding='utf-8').read()

re_ts = r'<garbled\s+page="?(\d+)"?\s+label="([^"]*)"?\s*/>'
matches = list(re.finditer(re_ts, text_source))
print(f'Matches: {len(matches)}')
for m in matches[:2]:
    print(f'  page={m.group(1)} label="{m.group(2)}"')
    print(f'  full match: {m.group(0)[:80]}')
