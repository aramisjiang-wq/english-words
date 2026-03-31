import sqlite3

def check_database():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM words')
    total = cursor.fetchone()[0]
    print(f'当前单词总数: {total}')
    
    cursor.execute('SELECT english, COUNT(*) as count FROM words GROUP BY english HAVING count > 1')
    duplicates = cursor.fetchall()
    print(f'重复单词数量: {len(duplicates)}')
    
    if duplicates:
        print('重复的单词:')
        for dup in duplicates[:10]:
            print(f'  {dup[0]}: {dup[1]}次')
    
    conn.close()

if __name__ == "__main__":
    check_database()
