import json

with open('../data/words_merged.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

part_of_speech_mapping = {
    '名词': '名词',
    '动词': '动词',
    '形容词': '形容词',
    '副词': '副词',
    '介词': '介词',
    '代词': '代词',
    '数词': '数词',
    '连词和冠词': '连词和冠词',
    '疑问词': '疑问词',
    '感叹词': '感叹词',
    '情态动词': '情态动词',
    '最常用动词': '动词',
    '最常用形容词': '形容词',
    '常用动词': '动词'
}

theme_mapping = {
    '商业管理': '商业',
    '商业词汇': '商业',
    '金融经济': '商业',
    '货币词汇': '商业',
    '法律': '法律',
    '法律政治': '法律',
    '法律词汇': '法律',
    '科学研究': '科学',
    '科学词汇': '科学',
    '技术创新': '科学',
    '科技创新': '科学',
    '医疗健康': '医疗',
    '教育学习': '教育',
    '动物词汇': '自然',
    '地理词汇': '自然',
    '自然地理': '自然',
    '颜色和天气': '自然',
    '时间词汇': '日常生活',
    '日常生活词汇': '日常生活',
    '社交词汇': '日常生活',
    '食物烹饪': '日常生活',
    '旅行交通': '日常生活',
    '运动健身': '日常生活',
    '体育健身': '日常生活',
    '艺术文化': '文化',
    '社会文化': '文化',
    '历史词汇': '文化',
    '心理学词汇': '心理学',
    '心理情感': '心理学',
    '哲学词汇': '哲学',
    '通用词汇': '通用'
}

updated_data = []
for word in data:
    original_category = word['category']
    part_of_speech = part_of_speech_mapping.get(original_category, '其他')
    theme = theme_mapping.get(original_category, '其他')
    
    updated_word = {
        'english': word['english'],
        'phonetic': word['phonetic'],
        'chinese': word['chinese'],
        'example': word['example'],
        'category': original_category,
        'part_of_speech': part_of_speech,
        'theme': theme
    }
    updated_data.append(updated_word)

with open('../data/words_merged.json', 'w', encoding='utf-8') as f:
    json.dump(updated_data, f, ensure_ascii=False, indent=2)

print(f'Updated {len(updated_data)} words with part_of_speech and theme fields')

part_of_speech_counts = {}
theme_counts = {}
for word in updated_data:
    pos = word['part_of_speech']
    theme = word['theme']
    part_of_speech_counts[pos] = part_of_speech_counts.get(pos, 0) + 1
    theme_counts[theme] = theme_counts.get(theme, 0) + 1

print('\n词性分类:')
for pos, count in sorted(part_of_speech_counts.items(), key=lambda x: -x[1]):
    print(f'  {pos}: {count} words')

print('\n主题分类:')
for theme, count in sorted(theme_counts.items(), key=lambda x: -x[1]):
    print(f'  {theme}: {count} words')
