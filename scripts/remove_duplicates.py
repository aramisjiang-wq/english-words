import sqlite3

def remove_duplicates():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT english, COUNT(*) as count FROM words GROUP BY english HAVING count > 1')
    duplicates = cursor.fetchall()
    
    print(f'发现 {len(duplicates)} 个重复单词')
    
    removed_count = 0
    for english_word, count in duplicates:
        cursor.execute('SELECT rowid FROM words WHERE english = ? ORDER BY rowid', (english_word,))
        rows = cursor.fetchall()
        
        for i in range(1, len(rows)):
            cursor.execute('DELETE FROM words WHERE rowid = ?', (rows[i][0],))
            removed_count += 1
    
    conn.commit()
    
    cursor.execute('SELECT COUNT(*) FROM words')
    total = cursor.fetchone()[0]
    
    print(f'删除了 {removed_count} 个重复记录')
    print(f'数据库总单词数: {total}')
    
    conn.close()

if __name__ == "__main__":
    remove_duplicates()
