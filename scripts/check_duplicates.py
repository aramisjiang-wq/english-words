import sqlite3

def check_duplicates():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    print("正在检查数据库中的重复单词...")
    
    cursor.execute('''
        SELECT english, COUNT(*) as count 
        FROM words 
        GROUP BY english 
        HAVING count > 1 
        ORDER BY count DESC
    ''')
    
    duplicates = cursor.fetchall()
    
    if duplicates:
        print(f"\n发现 {len(duplicates)} 个重复单词:")
        print("-" * 50)
        for word, count in duplicates:
            print(f"{word}: {count} 次")
    else:
        print("未发现重复单词")
    
    cursor.execute('SELECT COUNT(*) FROM words')
    total_words = cursor.fetchone()[0]
    print(f"\n数据库总单词数: {total_words}")
    
    conn.close()

if __name__ == "__main__":
    check_duplicates()
