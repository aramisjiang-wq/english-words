import sqlite3
import json

def export_database_to_json():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT english, phonetic, chinese, example, category, subcategory FROM words')
    rows = cursor.fetchall()
    
    words = []
    for row in rows:
        words.append({
            'english': row[0],
            'phonetic': row[1],
            'chinese': row[2],
            'example': row[3],
            'category': row[4],
            'subcategory': row[5]
        })
    
    with open('../words.json', 'w', encoding='utf-8') as f:
        json.dump(words, f, ensure_ascii=False, indent=2)
    
    print(f'成功导出 {len(words)} 个单词到 words.json')
    
    conn.close()

if __name__ == "__main__":
    export_database_to_json()
