import sqlite3

def check_word_count():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM words')
    count = cursor.fetchone()[0]
    
    print(f"当前数据库中的单词总数: {count}")
    
    cursor.execute('SELECT category, COUNT(*) FROM words GROUP BY category')
    categories = cursor.fetchall()
    
    print("\n按类别统计:")
    for category, count in categories:
        print(f"  {category}: {count}")
    
    conn.close()

if __name__ == "__main__":
    check_word_count()