import json

with open('../data/words_merged.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

category_hierarchy = {
    '词性': {
        '名词': ['名词'],
        '动词': ['动词', '最常用动词', '常用动词'],
        '形容词': ['形容词', '最常用形容词'],
        '副词': ['副词'],
        '介词': ['介词'],
        '代词': ['代词'],
        '数词': ['数词'],
        '连词和冠词': ['连词和冠词'],
        '疑问词': ['疑问词'],
        '感叹词': ['感叹词'],
        '情态动词': ['情态动词']
    },
    '主题': {
        '商业': ['商业管理', '商业词汇', '金融经济', '货币词汇'],
        '法律': ['法律', '法律政治', '法律词汇'],
        '科学': ['科学研究', '科学词汇', '技术创新', '科技创新'],
        '医疗': ['医疗健康'],
        '教育': ['教育学习'],
        '自然': ['动物词汇', '地理词汇', '自然地理', '颜色和天气'],
        '日常生活': ['时间词汇', '日常生活词汇', '社交词汇', '食物烹饪', '旅行交通', '运动健身', '体育健身'],
        '文化': ['艺术文化', '社会文化', '历史词汇'],
        '心理学': ['心理学词汇', '心理情感'],
        '哲学': ['哲学词汇'],
        '通用': ['通用词汇', '综合词汇']
    }
}

reverse_mapping = {}
for parent, children in category_hierarchy.items():
    for child_name, subcategories in children.items():
        for subcategory in subcategories:
            reverse_mapping[subcategory] = {
                'parent': parent,
                'child': child_name
            }

updated_data = []
for word in data:
    original_category = word['category']
    
    hierarchy_info = reverse_mapping.get(original_category, {
        'parent': '其他',
        'child': '其他'
    })
    
    updated_word = {
        'english': word['english'],
        'phonetic': word['phonetic'],
        'chinese': word['chinese'],
        'example': word['example'],
        'category': original_category,
        'part_of_speech': word['part_of_speech'],
        'theme': word['theme'],
        'parent_category': hierarchy_info['parent'],
        'child_category': hierarchy_info['child']
    }
    updated_data.append(updated_word)

with open('../data/words_merged.json', 'w', encoding='utf-8') as f:
    json.dump(updated_data, f, ensure_ascii=False, indent=2)

print(f'Updated {len(updated_data)} words with hierarchy information')

print('\n分类层级结构:')
for parent, children in category_hierarchy.items():
    print(f'\n{parent}:')
    for child_name, subcategories in children.items():
        print(f'  {child_name}: {", ".join(subcategories)}')

parent_counts = {}
child_counts = {}
for word in updated_data:
    parent = word['parent_category']
    child = word['child_category']
    parent_counts[parent] = parent_counts.get(parent, 0) + 1
    child_counts[child] = child_counts.get(child, 0) + 1

print('\n父分类统计:')
for parent, count in sorted(parent_counts.items(), key=lambda x: -x[1]):
    print(f'  {parent}: {count} words')

print('\n子分类统计:')
for child, count in sorted(child_counts.items(), key=lambda x: -x[1]):
    print(f'  {child}: {count} words')
