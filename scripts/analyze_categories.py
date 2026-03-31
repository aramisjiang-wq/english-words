import json

with open('../data/words_merged.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

categories = sorted(list(set(word['category'] for word in data)))
print(f'Total categories: {len(categories)}')
for i, cat in enumerate(categories):
    count = sum(1 for word in data if word['category'] == cat)
    print(f'{i+1}. {cat} ({count} words)')
