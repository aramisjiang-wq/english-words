import sqlite3

def check_table_structure():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    print("数据库中的表:")
    for table in tables:
        print(f"  - {table[0]}")
    
    if tables:
        table_name = tables[0][0]
        print(f"\n表 '{table_name}' 的结构:")
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        for col in columns:
            print(f"  {col[1]} ({col[2]})")
        
        print(f"\n表 '{table_name}' 的前5条数据:")
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
        rows = cursor.fetchall()
        for row in rows:
            print(f"  {row}")
    
    conn.close()

if __name__ == "__main__":
    check_table_structure()
