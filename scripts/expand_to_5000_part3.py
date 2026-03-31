#!/usr/bin/env python3
import sqlite3

def expand_vocabulary_to_5000_part3():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    new_words = [
        # 旅行/交通词汇 (30+)
        ("accommodation", "/əˌkɒməˈdeɪʃn/", "住宿", "Book accommodation.", "名词"),
        ("airline", "/ˈeəlaɪn/", "航空公司", "Major airline.", "名词"),
        ("airport", "/ˈeəpɔːt/", "机场", "Go to airport.", "名词"),
        ("baggage", "/ˈbæɡɪdʒ/", "行李", "Check baggage.", "名词"),
        ("cruise", "/kruːz/", "乘船游览", "Go on a cruise.", "名词"),
        ("destination", "/ˌdestɪˈneɪʃn/", "目的地", "Popular destination.", "名词"),
        ("excursion", "/ɪkˈskɜːʃn/", "短途旅行", "Book an excursion.", "名词"),
        ("itinerary", "/aɪˈtɪnərəri/", "行程", "Plan itinerary.", "名词"),
        ("luggage", "/ˈlʌɡɪdʒ/", "行李", "Pack luggage.", "名词"),
        ("passport", "/ˈpɑːspɔːt/", "护照", "Renew passport.", "名词"),
        ("reservation", "/ˌrezəˈveɪʃn/", "预订", "Make a reservation.", "名词"),
        ("sightseeing", "/ˈsaɪtˌsiːɪŋ/", "观光", "Go sightseeing.", "名词"),
        ("ticket", "/ˈtɪkɪt/", "票", "Buy a ticket.", "名词"),
        ("tourist", "/ˈtʊərɪst/", "游客", "Attract tourists.", "名词"),
        ("transportation", "/ˌtrænspɔːˈteɪʃn/", "交通", "Public transportation.", "名词"),
        ("vacation", "/veɪˈkeɪʃn/", "度假", "Summer vacation.", "名词"),
        ("visa", "/ˈviːzə/", "签证", "Apply for visa.", "名词"),
        ("voyage", "/ˈvɔɪɪdʒ/", "航行", "Long voyage.", "名词"),
        ("commute", "/kəˈmjuːt/", "通勤", "Daily commute.", "名词"),
        ("congestion", "/kənˈdʒestʃən/", "拥堵", "Traffic congestion.", "名词"),
        ("intersection", "/ˌɪntəˈsekʃn/", "十字路口", "Busy intersection.", "名词"),
        ("pedestrian", "/pəˈdestriən/", "行人", "Watch for pedestrians.", "名词"),
        ("railway", "/ˈreɪlweɪ/", "铁路", "Railway station.", "名词"),
        ("subway", "/ˈsʌbweɪ/", "地铁", "Take the subway.", "名词"),
        ("terminal", "/ˈtɜːmɪnl/", "航站楼", "Airport terminal.", "名词"),
        ("traffic", "/ˈtræfɪk/", "交通", "Heavy traffic.", "名词"),
        ("vehicle", "/ˈviːəkl/", "车辆", "Motor vehicle.", "名词"),
        ("highway", "/ˈhaɪweɪ/", "高速公路", "Drive on highway.", "名词"),
        ("freeway", "/ˈfriːweɪ/", "高速公路", "Take the freeway.", "名词"),
        ("bridge", "/brɪdʒ/", "桥梁", "Cross the bridge.", "名词"),
        ("tunnel", "/ˈtʌnl/", "隧道", "Go through tunnel.", "名词"),
        
        # 食物/烹饪词汇 (30+)
        ("appetite", "/ˈæpɪtaɪt/", "食欲", "Good appetite.", "名词"),
        ("beverage", "/ˈbevərɪdʒ/", "饮料", "Alcoholic beverage.", "名词"),
        ("cuisine", "/kwɪˈziːn/", "烹饪", "French cuisine.", "名词"),
        ("delicacy", "/ˈdelɪkəsi/", "美味", "Local delicacy.", "名词"),
        ("dessert", "/dɪˈzɜːt/", "甜点", "Order dessert.", "名词"),
        ("ingredient", "/ɪnˈɡriːdiənt/", "配料", "Fresh ingredients.", "名词"),
        ("nutrition", "/njuˈtrɪʃn/", "营养", "Balanced nutrition.", "名词"),
        ("recipe", "/ˈresəpi/", "食谱", "Follow the recipe.", "名词"),
        ("spice", "/spaɪs/", "香料", "Add spice.", "名词"),
        ("utensil", "/juːˈtensl/", "餐具", "Kitchen utensil.", "名词"),
        ("appetizer", "/ˈæpɪtaɪzə(r)/", "开胃菜", "Order appetizer.", "名词"),
        ("beverage", "/ˈbevərɪdʒ/", "饮料", "Order beverage.", "名词"),
        ("catering", "/ˈkeɪtərɪŋ/", "餐饮服务", "Wedding catering.", "名词"),
        ("delicious", "/dɪˈlɪʃəs/", "美味的", "Delicious meal.", "形容词"),
        ("flavor", "/ˈfleɪvə(r)/", "味道", "Rich flavor.", "名词"),
        ("gourmet", "/ˈɡʊəmeɪ/", "美食家", "Gourmet restaurant.", "名词"),
        ("homemade", "/ˌhəʊmˈmeɪd/", "自制的", "Homemade bread.", "形容词"),
        ("kitchen", "/ˈkɪtʃn/", "厨房", "Modern kitchen.", "名词"),
        ("menu", "/ˈmenjuː/", "菜单", "Read the menu.", "名词"),
        ("restaurant", "/ˈrestrɒnt/", "餐厅", "Fancy restaurant.", "名词"),
        ("snack", "/snæk/", "零食", "Healthy snack.", "名词"),
        ("tasty", "/ˈteɪsti/", "美味的", "Tasty dish.", "形容词"),
        ("vegetarian", "/ˌvedʒəˈteəriən/", "素食者", "Vegetarian option.", "名词"),
        ("breakfast", "/ˈbrekfəst/", "早餐", "Eat breakfast.", "名词"),
        ("lunch", "/lʌntʃ/", "午餐", "Have lunch.", "名词"),
        ("dinner", "/ˈdɪnə(r)/", "晚餐", "Cook dinner.", "名词"),
        ("supper", "/ˈsʌpə(r)/", "晚餐", "Family supper.", "名词"),
        ("banquet", "/ˈbæŋkwɪt/", "宴会", "Attend banquet.", "名词"),
        ("buffet", "/bəˈfeɪ/", "自助餐", "Buffet dinner.", "名词"),
        ("cafeteria", "/ˌkæfəˈtɪəriə/", "自助食堂", "School cafeteria.", "名词"),
        ("bakery", "/ˈbeɪkəri/", "面包店", "Visit bakery.", "名词"),
        
        # 情感/心理词汇 (20+)
        ("affection", "/əˈfekʃn/", "喜爱", "Show affection.", "名词"),
        ("anxiety", "/æŋˈzaɪəti/", "焦虑", "Feel anxiety.", "名词"),
        ("confidence", "/ˈkɒnfɪdəns/", "自信", "Build confidence.", "名词"),
        ("curiosity", "/ˌkjʊəriˈɒsəti/", "好奇心", "Satisfy curiosity.", "名词"),
        ("depression", "/dɪˈpreʃn/", "抑郁", "Treat depression.", "名词"),
        ("empathy", "/ˈempəθi/", "同理心", "Show empathy.", "名词"),
        ("frustration", "/frʌˈstreɪʃn/", "挫折", "Feel frustration.", "名词"),
        ("gratitude", "/ˈɡrætɪtjuːd/", "感激", "Express gratitude.", "名词"),
        ("happiness", "/ˈhæpinəs/", "幸福", "Pursue happiness.", "名词"),
        ("jealousy", "/ˈdʒeləsi/", "嫉妒", "Overcome jealousy.", "名词"),
        ("loneliness", "/ˈləʊnlinəs/", "孤独", "Feel loneliness.", "名词"),
        ("motivation", "/ˌməʊtɪˈveɪʃn/", "动力", "Lack motivation.", "名词"),
        ("optimism", "/ˈɒptɪmɪzəm/", "乐观", "Maintain optimism.", "名词"),
        ("passion", "/ˈpæʃn/", "激情", "Follow passion.", "名词"),
        ("resentment", "/rɪˈzentmənt/", "怨恨", "Hide resentment.", "名词"),
        ("satisfaction", "/ˌsætɪsˈfækʃn/", "满意", "Job satisfaction.", "名词"),
        ("sympathy", "/ˈsɪmpəθi/", "同情", "Show sympathy.", "名词"),
        ("trust", "/trʌst/", "信任", "Build trust.", "名词"),
        ("wisdom", "/ˈwɪzdəm/", "智慧", "Gain wisdom.", "名词"),
        ("enthusiasm", "/ɪnˈθjuːziæzəm/", "热情", "Show enthusiasm.", "名词"),
        ("patience", "/ˈpeɪʃns/", "耐心", "Have patience.", "名词"),
        ("courage", "/ˈkʌrɪdʒ/", "勇气", "Show courage.", "名词"),
        ("fear", "/fɪə(r)/", "恐惧", "Overcome fear.", "名词"),
        ("hope", "/həʊp/", "希望", "Hold onto hope.", "名词"),
        ("love", "/lʌv/", "爱", "Feel love.", "名词"),
    ]
    
    added_count = 0
    skipped_count = 0
    
    for word in new_words:
        cursor.execute('SELECT COUNT(*) FROM words WHERE english = ?', (word[0],))
        if cursor.fetchone()[0] == 0:
            cursor.execute('INSERT INTO words (english, phonetic, chinese, example, category) VALUES (?, ?, ?, ?, ?)', word)
            added_count += 1
        else:
            skipped_count += 1
    
    conn.commit()
    
    cursor.execute('SELECT COUNT(*) FROM words')
    total_count = cursor.fetchone()[0]
    
    print(f'添加了 {added_count} 个新单词')
    print(f'跳过了 {skipped_count} 个已存在的单词')
    print(f'数据库总单词数: {total_count}')
    
    conn.close()

if __name__ == '__main__':
    expand_vocabulary_to_5000_part3()
