#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import json
from datetime import datetime

def create_database():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            english TEXT NOT NULL,
            phonetic TEXT,
            chinese TEXT NOT NULL,
            example TEXT,
            category TEXT NOT NULL,
            subcategory TEXT,
            difficulty INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS word_status (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word_id INTEGER NOT NULL,
            status TEXT DEFAULT 'gray',
            review_count INTEGER DEFAULT 0,
            last_reviewed TIMESTAMP,
            FOREIGN KEY (word_id) REFERENCES words (id)
        )
    ''')
    
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_category ON words(category)
    ''')
    
    cursor.execute('''
        CREATE INDEX IF NOT EXISTS idx_status ON word_status(status)
    ''')
    
    conn.commit()
    conn.close()
    print("数据库创建成功！")

def load_words_from_json():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    try:
        with open('../data/words.json', 'r', encoding='utf-8') as f:
            words = json.load(f)
            
        for word in words:
            cursor.execute('''
                INSERT OR IGNORE INTO words (english, phonetic, chinese, example, category, subcategory)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (word['english'], word['phonetic'], word['chinese'], word['example'], word['category'], ''))
        
        conn.commit()
        print(f"成功导入 {len(words)} 个单词到数据库")
    except FileNotFoundError:
        print("data/words.json 文件不存在，请先运行 convert.py")
    finally:
        conn.close()

def get_statistics():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT 
            COUNT(*) as total,
            SUM(CASE WHEN status = 'green' THEN 1 ELSE 0 END) as mastered,
            SUM(CASE WHEN status = 'red' THEN 1 ELSE 0 END) as difficult,
            SUM(CASE WHEN status = 'gray' OR status IS NULL THEN 1 ELSE 0 END) as learning
        FROM word_status
    ''')
    
    stats = cursor.fetchone()
    conn.close()
    
    return {
        'total': stats[0] or 0,
        'mastered': stats[1] or 0,
        'difficult': stats[2] or 0,
        'learning': stats[3] or 0
    }

def get_categories():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT DISTINCT category FROM words ORDER BY category')
    categories = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    return categories

if __name__ == '__main__':
    print("=== 英语单词学习系统 - 数据库初始化 ===")
    print("1. 创建数据库...")
    create_database()
    
    print("\n2. 导入单词数据...")
    load_words_from_json()
    
    print("\n3. 查看统计...")
    stats = get_statistics()
    print(f"   总单词: {stats['total']}")
    print(f"   已掌握: {stats['mastered']}")
    print(f"   难记: {stats['difficult']}")
    print(f"   学习中: {stats['learning']}")
    
    print("\n4. 查看分类...")
    categories = get_categories()
    print(f"   共 {len(categories)} 个分类:")
    for cat in categories:
        print(f"   - {cat}")
    
    print("\n✅ 初始化完成！")