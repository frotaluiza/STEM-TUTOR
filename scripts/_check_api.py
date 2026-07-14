import requests, re
r = requests.get('http://localhost:8001/api/v1/knowledge/sadiku/files/ch01_12-systems-of-units.md')
if r.status_code == 200:
    text = r.text
    n = len(re.findall(r'<garbled', text))
    print(f'API has {n} garbled tags')
    if n == 0:
        print('First 300 chars:', text[:300])
else:
    print('Error:', r.status_code)
