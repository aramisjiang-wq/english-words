import sqlite3

def check_words_table():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    print("表 'words' 的结构:")
    cursor.execute("PRAGMA table_info(words)")
    columns = cursor.fetchall()
    for col in columns:
        print(f"  {col[1]} ({col[2]})")
    
    print(f"\n表 'words' 的前5条数据:")
    cursor.execute("SELECT * FROM words LIMIT 5")
    rows = cursor.fetchall()
    for row in rows:
        print(f"  {row}")
    
    print(f"\n总单词数:")
    cursor.execute("SELECT COUNT(*) FROM words")
    total = cursor.fetchone()[0]
    print(f"  {total}")
    
    conn.close()

if __name__ == "__main__":
    check_words_table()
