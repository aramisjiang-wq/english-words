import sqlite3

def expand_to_5000_batch7():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    new_words = [
        {
            "english": "masterpiece", "phonetic": "/ˈmæstərpiːs/", "chinese": "n. 杰作", 
            "example": "The painting is a masterpiece.", "category": "艺术文化"
        },
        {
            "english": "masterpiece", "phonetic": "/ˈmæstərpiːs/", "chinese": "n. 杰作", 
            "example": "The painting is a masterpiece.", "category": "艺术文化"
        },
        {
            "english": "masterwork", "phonetic": "/ˈmæstərwɜːrk/", "chinese": "n. 杰作", 
            "example": "The sculpture is a masterwork.", "category": "艺术文化"
        },
        {
            "english": "creation", "phonetic": "/kriˈeɪʃn/", "chinese": "n. 创作", 
            "example": "The artist's creation is beautiful.", "category": "艺术文化"
        },
        {
            "english": "composition", "phonetic": "/ˌkɑːmpəˈzɪʃn/", "chinese": "n. 构图", 
            "example": "The composition is balanced.", "category": "艺术文化"
        },
        {
            "english": "perspective", "phonetic": "/pərˈspektɪv/", "chinese": "n. 透视", 
            "example": "The perspective is realistic.", "category": "艺术文化"
        },
        {
            "english": "proportion", "phonetic": "/prəˈpɔːrʃn/", "chinese": "n. 比例", 
            "example": "The proportion is correct.", "category": "艺术文化"
        },
        {
            "english": "balance", "phonetic": "/ˈbæləns/", "chinese": "n. 平衡", 
            "example": "The design has good balance.", "category": "艺术文化"
        },
        {
            "english": "harmony", "phonetic": "/ˈhɑːrməni/", "chinese": "n. 和谐", 
            "example": "The colors are in harmony.", "category": "艺术文化"
        },
        {
            "english": "contrast", "phonetic": "/ˈkɑːntræst/", "chinese": "n. 对比", 
            "example": "The contrast is striking.", "category": "艺术文化"
        },
        {
            "english": "texture", "phonetic": "/ˈtekstʃər/", "chinese": "n. 质感", 
            "example": "The texture is smooth.", "category": "艺术文化"
        },
        {
            "english": "pattern", "phonetic": "/ˈpætərn/", "chinese": "n. 图案", 
            "example": "The pattern is intricate.", "category": "艺术文化"
        },
        {
            "english": "color", "phonetic": "/ˈkʌlər/", "chinese": "n. 颜色", 
            "example": "The color is vibrant.", "category": "艺术文化"
        },
        {
            "english": "shade", "phonetic": "/ʃeɪd/", "chinese": "n. 色调", 
            "example": "The shade is dark.", "category": "艺术文化"
        },
        {
            "english": "tone", "phonetic": "/toʊn/", "chinese": "n. 色调", 
            "example": "The tone is warm.", "category": "艺术文化"
        },
        {
            "english": "hue", "phonetic": "/hjuː/", "chinese": "n. 色相", 
            "example": "The hue is blue.", "category": "艺术文化"
        },
        {
            "english": "saturation", "phonetic": "/ˌsætʃəˈreɪʃn/", "chinese": "n. 饱和度", 
            "example": "The saturation is high.", "category": "艺术文化"
        },
        {
            "english": "brightness", "phonetic": "/ˈbraɪtnəs/", "chinese": "n. 亮度", 
            "example": "The brightness is good.", "category": "艺术文化"
        },
        {
            "english": "lighting", "phonetic": "/ˈlaɪtɪŋ/", "chinese": "n. 光线", 
            "example": "The lighting is dramatic.", "category": "艺术文化"
        },
        {
            "english": "shadow", "phonetic": "/ˈʃædoʊ/", "chinese": "n. 阴影", 
            "example": "The shadow is deep.", "category": "艺术文化"
        }
    ]
    
    added_count = 0
    for word in new_words:
        cursor.execute('''
            INSERT OR IGNORE INTO words (english, phonetic, chinese, example, category, subcategory)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (word['english'], word['phonetic'], word['chinese'], word['example'], word['category'], ''))
        
        if cursor.rowcount > 0:
            added_count += 1
    
    conn.commit()
    
    cursor.execute('SELECT COUNT(*) FROM words')
    total = cursor.fetchone()[0]
    
    print(f"成功添加 {added_count} 个新单词到数据库")
    print(f"数据库总单词数: {total}")
    
    conn.close()

if __name__ == "__main__":
    expand_to_5000_batch7()
