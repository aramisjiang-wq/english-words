import sqlite3
import json

def expand_to_5000_batch4():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    new_words = [
        # 艺术/文化类
        {
            "english": "aesthetic", "phonetic": "/iːsˈθetɪk/", "chinese": "adj. 美学的，审美的", 
            "example": "The building has a very modern aesthetic design.",
            "category": "艺术文化"
        },
        {
            "english": "avant-garde", "phonetic": "/ˌævɒ̃ˈɡɑːrd/", "chinese": "adj. 前卫的，先锋的", 
            "example": "She is known for her avant-garde fashion sense.",
            "category": "艺术文化"
        },
        {
            "english": "baroque", "phonetic": "/bəˈroʊk/", "chinese": "adj. 巴洛克风格的", 
            "example": "The cathedral features beautiful baroque architecture.",
            "category": "艺术文化"
        },
        {
            "english": "renaissance", "phonetic": "/ˈrenəsɑːns/", "chinese": "n. 文艺复兴", 
            "example": "The Renaissance period produced many great artists.",
            "category": "艺术文化"
        },
        {
            "english": "impressionism", "phonetic": "/ɪmˈpreʃənɪzəm/", "chinese": "n. 印象派", 
            "example": "Monet is a famous painter of impressionism.",
            "category": "艺术文化"
        },
        {
            "english": "surrealism", "phonetic": "/səˈriːəlɪzəm/", "chinese": "n. 超现实主义", 
            "example": "Dali's paintings are prime examples of surrealism.",
            "category": "艺术文化"
        },
        {
            "english": "cubism", "phonetic": "/ˈkjuːbɪzəm/", "chinese": "n. 立体主义", 
            "example": "Picasso pioneered the cubism movement.",
            "category": "艺术文化"
        },
        {
            "english": "minimalism", "phonetic": "/ˈmɪnɪməlɪzəm/", "chinese": "n. 极简主义", 
            "example": "The room's design reflects minimalism principles.",
            "category": "艺术文化"
        },
        {
            "english": "contemporary", "phonetic": "/kənˈtempəreri/", "chinese": "adj. 当代的", 
            "example": "She is a contemporary artist working in New York.",
            "category": "艺术文化"
        },
        {
            "english": "classical", "phonetic": "/ˈklæsɪkl/", "chinese": "adj. 古典的", 
            "example": "I enjoy listening to classical music.",
            "category": "艺术文化"
        },
        {
            "english": "symphony", "phonetic": "/ˈsɪmfəni/", "chinese": "n. 交响乐", 
            "example": "The orchestra performed Beethoven's Fifth Symphony.",
            "category": "艺术文化"
        },
        {
            "english": "orchestra", "phonetic": "/ˈɔːrkɪstrə/", "chinese": "n. 管弦乐队", 
            "example": "The symphony orchestra has 100 musicians.",
            "category": "艺术文化"
        },
        {
            "english": "concerto", "phonetic": "/kənˈtʃertoʊ/", "chinese": "n. 协奏曲", 
            "example": "The pianist performed a piano concerto.",
            "category": "艺术文化"
        },
        {
            "english": "sonata", "phonetic": "/səˈnɑːtə/", "chinese": "n. 奏鸣曲", 
            "example": "Moonlight Sonata is one of Beethoven's most famous works.",
            "category": "艺术文化"
        },
        {
            "english": "ballet", "phonetic": "/ˈbæleɪ/", "chinese": "n. 芭蕾舞", 
            "example": "She has been studying ballet since she was five.",
            "category": "艺术文化"
        },
        {
            "english": "opera", "phonetic": "/ˈɑːprə/", "chinese": "n. 歌剧", 
            "example": "The opera house is famous for its acoustics.",
            "category": "艺术文化"
        },
        {
            "english": "theater", "phonetic": "/ˈθiːətər/", "chinese": "n. 剧院，戏剧", 
            "example": "We went to the theater to watch a play.",
            "category": "艺术文化"
        },
        {
            "english": "sculpture", "phonetic": "/ˈskʌlptʃər/", "chinese": "n. 雕塑", 
            "example": "The museum has an impressive collection of sculptures.",
            "category": "艺术文化"
        },
        {
            "english": "canvas", "phonetic": "/ˈkænvəs/", "chinese": "n. 画布", 
            "example": "The artist painted a beautiful landscape on canvas.",
            "category": "艺术文化"
        },
        {
            "english": "palette", "phonetic": "/ˈpælət/", "chinese": "n. 调色板", 
            "example": "The painter mixed colors on his palette.",
            "category": "艺术文化"
        },
        
        # 运动/健身类
        {
            "english": "aerobics", "phonetic": "/eˈroʊbɪks/", "chinese": "n. 有氧运动", 
            "example": "She does aerobics three times a week.",
            "category": "运动健身"
        },
        {
            "english": "endurance", "phonetic": "/ɪnˈdʊrəns/", "chinese": "n. 耐力", 
            "example": "Marathon runners need great endurance.",
            "category": "运动健身"
        },
        {
            "english": "stamina", "phonetic": "/ˈstæmɪnə/", "chinese": "n. 持久力", 
            "example": "The athlete has incredible stamina.",
            "category": "运动健身"
        },
        {
            "english": "flexibility", "phonetic": "/ˌfleksəˈbɪləti/", "chinese": "n. 柔韧性", 
            "example": "Yoga improves your flexibility.",
            "category": "运动健身"
        },
        {
            "english": "agility", "phonetic": "/əˈdʒɪləti/", "chinese": "n. 敏捷性", 
            "example": "The cat showed great agility jumping from tree to tree.",
            "category": "运动健身"
        },
        {
            "english": "coordination", "phonetic": "/koʊˌɔːrdɪˈneɪʃn/", "chinese": "n. 协调性", 
            "example": "Sports require good hand-eye coordination.",
            "category": "运动健身"
        },
        {
            "english": "cardiovascular", "phonetic": "/ˌkɑːrdioʊˈvæskjələr/", "chinese": "adj. 心血管的", 
            "example": "Running is good for cardiovascular health.",
            "category": "运动健身"
        },
        {
            "english": "metabolism", "phonetic": "/məˈtæbəlɪzəm/", "chinese": "n. 新陈代谢", 
            "example": "Exercise boosts your metabolism.",
            "category": "运动健身"
        },
        {
            "english": "recovery", "phonetic": "/rɪˈkʌvəri/", "chinese": "n. 恢复", 
            "example": "Rest is important for muscle recovery.",
            "category": "运动健身"
        },
        {
            "english": "hydration", "phonetic": "/haɪˈdreɪʃn/", "chinese": "n. 水合作用", 
            "example": "Proper hydration is essential during exercise.",
            "category": "运动健身"
        },
        {
            "english": "protein", "phonetic": "/ˈproʊtiːn/", "chinese": "n. 蛋白质", 
            "example": "Athletes need more protein in their diet.",
            "category": "运动健身"
        },
        {
            "english": "carbohydrate", "phonetic": "/ˌkɑːrboʊˈhaɪdreɪt/", "chinese": "n. 碳水化合物", 
            "example": "Pasta is a good source of carbohydrates.",
            "category": "运动健身"
        },
        {
            "english": "supplement", "phonetic": "/ˈsʌplɪmənt/", "chinese": "n. 补充剂", 
            "example": "Many athletes take protein supplements.",
            "category": "运动健身"
        },
        {
            "english": "workout", "phonetic": "/ˈwɜːrkaʊt/", "chinese": "n. 锻炼", 
            "example": "I do a full-body workout every morning.",
            "category": "运动健身"
        },
        {
            "english": "repetition", "phonetic": "/ˌrepəˈtɪʃn/", "chinese": "n. 重复", 
            "example": "Do three sets of ten repetitions.",
            "category": "运动健身"
        },
        {
            "english": "warm-up", "phonetic": "/ˈwɔːrm ʌp/", "chinese": "n. 热身", 
            "example": "Always do a warm-up before exercising.",
            "category": "运动健身"
        },
        {
            "english": "cool-down", "phonetic": "/ˈkuːl daʊn/", "chinese": "n. 放松", 
            "example": "Don't forget to cool down after your workout.",
            "category": "运动健身"
        },
        {
            "english": "stretching", "phonetic": "/ˈstretʃɪŋ/", "chinese": "n. 拉伸", 
            "example": "Stretching helps prevent injuries.",
            "category": "运动健身"
        },
        
        # 金融/经济类
        {
            "english": "investment", "phonetic": "/ɪnˈvestmənt/", "chinese": "n. 投资", 
            "example": "Real estate is a popular investment.",
            "category": "金融经济"
        },
        {
            "english": "portfolio", "phonetic": "/pɔːrtˈfoʊlioʊ/", "chinese": "n. 投资组合", 
            "example": "Diversify your investment portfolio.",
            "category": "金融经济"
        },
        {
            "english": "dividend", "phonetic": "/ˈdɪvɪdend/", "chinese": "n. 股息", 
            "example": "The company pays quarterly dividends.",
            "category": "金融经济"
        },
        {
            "english": "inflation", "phonetic": "/ɪnˈfleɪʃn/", "chinese": "n. 通货膨胀", 
            "example": "High inflation reduces purchasing power.",
            "category": "金融经济"
        },
        {
            "english": "recession", "phonetic": "/rɪˈseʃn/", "chinese": "n. 经济衰退", 
            "example": "The country went into a recession last year.",
            "category": "金融经济"
        },
        {
            "english": "depression", "phonetic": "/dɪˈpreʃn/", "chinese": "n. 萧条", 
            "example": "The Great Depression was a severe economic downturn.",
            "category": "金融经济"
        },
        {
            "english": "prosperity", "phonetic": "/prɑːˈsperəti/", "chinese": "n. 繁荣", 
            "example": "Economic prosperity benefits everyone.",
            "category": "金融经济"
        },
        {
            "english": "currency", "phonetic": "/ˈkɜːrənsi/", "chinese": "n. 货币", 
            "example": "The US dollar is a major world currency.",
            "category": "金融经济"
        },
        {
            "english": "exchange", "phonetic": "/ɪksˈtʃeɪndʒ/", "chinese": "n. 交换，汇率", 
            "example": "The exchange rate changes daily.",
            "category": "金融经济"
        },
        {
            "english": "stock", "phonetic": "/stɑːk/", "chinese": "n. 股票", 
            "example": "He bought stocks in several companies.",
            "category": "金融经济"
        },
        {
            "english": "bond", "phonetic": "/bɑːnd/", "chinese": "n. 债券", 
            "example": "Government bonds are considered safe investments.",
            "category": "金融经济"
        },
        {
            "english": "commerce", "phonetic": "/ˈkɑːmɜːrs/", "chinese": "n. 商业", 
            "example": "E-commerce has grown rapidly.",
            "category": "金融经济"
        },
        {
            "english": "transaction", "phonetic": "/trænˈzækʃn/", "chinese": "n. 交易", 
            "example": "The transaction was completed successfully.",
            "category": "金融经济"
        },
        {
            "english": "budget", "phonetic": "/ˈbʌdʒɪt/", "chinese": "n. 预算", 
            "example": "We need to stick to our budget.",
            "category": "金融经济"
        },
        {
            "english": "revenue", "phonetic": "/ˈrevənuː/", "chinese": "n. 收入", 
            "example": "The company's revenue increased this year.",
            "category": "金融经济"
        },
        {
            "english": "profit", "phonetic": "/ˈprɑːfɪt/", "chinese": "n. 利润", 
            "example": "The business made a good profit.",
            "category": "金融经济"
        },
        {
            "english": "loss", "phonetic": "/lɔːs/", "chinese": "n. 损失", 
            "example": "The company reported a financial loss.",
            "category": "金融经济"
        },
        
        # 教育/学习类
        {
            "english": "curriculum", "phonetic": "/kəˈrɪkjələm/", "chinese": "n. 课程", 
            "example": "The school updated its curriculum.",
            "category": "教育学习"
        },
        {
            "english": "syllabus", "phonetic": "/ˈsɪləbəs/", "chinese": "n. 教学大纲", 
            "example": "Check the syllabus for course requirements.",
            "category": "教育学习"
        },
        {
            "english": "assignment", "phonetic": "/əˈsaɪnmənt/", "chinese": "n. 作业", 
            "example": "I have a math assignment due tomorrow.",
            "category": "教育学习"
        },
        {
            "english": "examination", "phonetic": "/ɪɡˌzæmɪˈneɪʃn/", "chinese": "n. 考试", 
            "example": "The final examination is next week.",
            "category": "教育学习"
        },
        {
            "english": "graduation", "phonetic": "/ˌɡrædʒuˈeɪʃn/", "chinese": "n. 毕业", 
            "example": "She will attend her graduation ceremony.",
            "category": "教育学习"
        },
        {
            "english": "diploma", "phonetic": "/dɪˈploʊmə/", "chinese": "n. 毕业证书", 
            "example": "He received his high school diploma.",
            "category": "教育学习"
        },
        {
            "english": "degree", "phonetic": "/dɪˈɡriː/", "chinese": "n. 学位", 
            "example": "She earned a bachelor's degree in engineering.",
            "category": "教育学习"
        },
        {
            "english": "scholarship", "phonetic": "/ˈskɑːlərʃɪp/", "chinese": "n. 奖学金", 
            "example": "She won a scholarship to study abroad.",
            "category": "教育学习"
        },
        {
            "english": "tuition", "phonetic": "/tuːˈɪʃn/", "chinese": "n. 学费", 
            "example": "College tuition has increased significantly.",
            "category": "教育学习"
        },
        {
            "english": "lecture", "phonetic": "/ˈlektʃər/", "chinese": "n. 讲座", 
            "example": "The professor gave an interesting lecture.",
            "category": "教育学习"
        },
        {
            "english": "seminar", "phonetic": "/ˈsemɪnɑːr/", "chinese": "n. 研讨会", 
            "example": "I attended a seminar on climate change.",
            "category": "教育学习"
        },
        {
            "english": "workshop", "phonetic": "/ˈwɜːrkʃɑːp/", "chinese": "n. 研习班", 
            "example": "The workshop teaches practical skills.",
            "category": "教育学习"
        },
        {
            "english": "tutorial", "phonetic": "/tuːˈtɔːriəl/", "chinese": "n. 辅导课", 
            "example": "She offers private tutorials in mathematics.",
            "category": "教育学习"
        },
        {
            "english": "mentor", "phonetic": "/ˈmentɔːr/", "chinese": "n. 导师", 
            "example": "Her mentor helped her career development.",
            "category": "教育学习"
        },
        {
            "english": "guidance", "phonetic": "/ˈɡaɪdns/", "chinese": "n. 指导", 
            "example": "The teacher provides guidance to students.",
            "category": "教育学习"
        },
        {
            "english": "assessment", "phonetic": "/əˈsesmənt/", "chinese": "n. 评估", 
            "example": "The assessment will test your knowledge.",
            "category": "教育学习"
        },
        {
            "english": "evaluation", "phonetic": "/ɪˌvæljuˈeɪʃn/", "chinese": "n. 评价", 
            "example": "The evaluation showed good progress.",
            "category": "教育学习"
        },
        {
            "english": "achievement", "phonetic": "/əˈtʃiːvmənt/", "chinese": "n. 成就", 
            "example": "Graduating is a great achievement.",
            "category": "教育学习"
        },
        {
            "english": "comprehension", "phonetic": "/ˌkɑːmprɪˈhenʃn/", "chinese": "n. 理解", 
            "example": "The test measures reading comprehension.",
            "category": "教育学习"
        },
        
        # 科技/创新类
        {
            "english": "innovation", "phonetic": "/ˌɪnəˈveɪʃn/", "chinese": "n. 创新", 
            "example": "Innovation drives technological progress.",
            "category": "科技创新"
        },
        {
            "english": "breakthrough", "phonetic": "/ˈbreɪkθruː/", "chinese": "n. 突破", 
            "example": "The research led to a major breakthrough.",
            "category": "科技创新"
        },
        {
            "english": "discovery", "phonetic": "/dɪˈskʌvəri/", "chinese": "n. 发现", 
            "example": "The discovery changed our understanding.",
            "category": "科技创新"
        },
        {
            "english": "invention", "phonetic": "/ɪnˈvenʃn/", "chinese": "n. 发明", 
            "example": "The invention of the internet changed the world.",
            "category": "科技创新"
        },
        {
            "english": "revolution", "phonetic": "/ˌrevəˈluːʃn/", "chinese": "n. 革命", 
            "example": "The industrial revolution transformed society.",
            "category": "科技创新"
        },
        {
            "english": "evolution", "phonetic": "/ˌevəˈluːʃn/", "chinese": "n. 演变", 
            "example": "The evolution of technology is rapid.",
            "category": "科技创新"
        },
        {
            "english": "advancement", "phonetic": "/ədˈvænsmənt/", "chinese": "n. 进步", 
            "example": "Technological advancement improves lives.",
            "category": "科技创新"
        },
        {
            "english": "development", "phonetic": "/dɪˈveləpmənt/", "chinese": "n. 发展", 
            "example": "Software development requires coding skills.",
            "category": "科技创新"
        },
        {
            "english": "programming", "phonetic": "/ˈproʊɡræmɪŋ/", "chinese": "n. 编程", 
            "example": "Programming is a valuable skill today.",
            "category": "科技创新"
        },
        {
            "english": "algorithm", "phonetic": "/ˈælɡərɪðəm/", "chinese": "n. 算法", 
            "example": "The algorithm solves complex problems.",
            "category": "科技创新"
        },
        {
            "english": "database", "phonetic": "/ˈdeɪtəbeɪs/", "chinese": "n. 数据库", 
            "example": "The database stores customer information.",
            "category": "科技创新"
        },
        {
            "english": "network", "phonetic": "/ˈnetwɜːrk/", "chinese": "n. 网络", 
            "example": "The computer network connects all offices.",
            "category": "科技创新"
        },
        {
            "english": "software", "phonetic": "/ˈsɔːftwer/", "chinese": "n. 软件", 
            "example": "Install the software on your computer.",
            "category": "科技创新"
        },
        {
            "english": "hardware", "phonetic": "/ˈhɑːrdwer/", "chinese": "n. 硬件", 
            "example": "The hardware needs to be upgraded.",
            "category": "科技创新"
        },
        {
            "english": "interface", "phonetic": "/ˈɪntərfeɪs/", "chinese": "n. 接口", 
            "example": "The user interface is easy to navigate.",
            "category": "科技创新"
        },
        {
            "english": "platform", "phonetic": "/ˈplætfɔːrm/", "chinese": "n. 平台", 
            "example": "The platform connects buyers and sellers.",
            "category": "科技创新"
        },
        {
            "english": "application", "phonetic": "/ˌæplɪˈkeɪʃn/", "chinese": "n. 应用程序", 
            "example": "Download the mobile application.",
            "category": "科技创新"
        },
        {
            "english": "virtual", "phonetic": "/ˈvɜːrtʃuəl/", "chinese": "adj. 虚拟的", 
            "example": "Virtual reality is an emerging technology.",
            "category": "科技创新"
        },
        {
            "english": "digital", "phonetic": "/ˈdɪdʒɪtl/", "chinese": "adj. 数字的", 
            "example": "Digital transformation is happening everywhere.",
            "category": "科技创新"
        },
        {
            "english": "electronic", "phonetic": "/ɪˌlekˈtrɑːnɪk/", "chinese": "adj. 电子的", 
            "example": "Electronic devices are everywhere today.",
            "category": "科技创新"
        },
        
        # 自然/地理类
        {
            "english": "ecosystem", "phonetic": "/ˈiːkoʊsɪstəm/", "chinese": "n. 生态系统", 
            "example": "The ecosystem is fragile and needs protection.",
            "category": "自然地理"
        },
        {
            "english": "biodiversity", "phonetic": "/ˌbaɪoʊdaɪˈvɜːrsəti/", "chinese": "n. 生物多样性", 
            "example": "The rainforest has high biodiversity.",
            "category": "自然地理"
        },
        {
            "english": "conservation", "phonetic": "/ˌkɑːnsərˈveɪʃn/", "chinese": "n. 保护", 
            "example": "Wildlife conservation is important.",
            "category": "自然地理"
        },
        {
            "english": "preservation", "phonetic": "/ˌprezərˈveɪʃn/", "chinese": "n. 保存", 
            "example": "Historical preservation protects old buildings.",
            "category": "自然地理"
        },
        {
            "english": "sustainability", "phonetic": "/səˌsteɪnəˈbɪləti/", "chinese": "n. 可持续性", 
            "example": "Sustainability is key to future development.",
            "category": "自然地理"
        },
        {
            "english": "renewable", "phonetic": "/rɪˈnuːəbl/", "chinese": "adj. 可再生的", 
            "example": "Solar energy is a renewable resource.",
            "category": "自然地理"
        },
        {
            "english": "pollution", "phonetic": "/pəˈluːʃn/", "chinese": "n. 污染", 
            "example": "Air pollution is a serious problem.",
            "category": "自然地理"
        },
        {
            "english": "contamination", "phonetic": "/kənˌtæmɪˈneɪʃn/", "chinese": "n. 污染", 
            "example": "Water contamination affects health.",
            "category": "自然地理"
        },
        {
            "english": "emission", "phonetic": "/iˈmɪʃn/", "chinese": "n. 排放", 
            "example": "Carbon emission contributes to climate change.",
            "category": "自然地理"
        },
        {
            "english": "climate", "phonetic": "/ˈklaɪmət/", "chinese": "n. 气候", 
            "example": "The climate is changing due to global warming.",
            "category": "自然地理"
        },
        {
            "english": "weather", "phonetic": "/ˈweðər/", "chinese": "n. 天气", 
            "example": "The weather is nice today.",
            "category": "自然地理"
        },
        {
            "english": "geography", "phonetic": "/dʒiˈɑːɡrəfi/", "chinese": "n. 地理", 
            "example": "Geography studies the Earth's surface.",
            "category": "自然地理"
        },
        {
            "english": "topography", "phonetic": "/təˈpɑːɡrəfi/", "chinese": "n. 地形", 
            "example": "The topography of the region is mountainous.",
            "category": "自然地理"
        },
        {
            "english": "landscape", "phonetic": "/ˈlændskeɪp/", "chinese": "n. 风景", 
            "example": "The landscape is beautiful in autumn.",
            "category": "自然地理"
        },
        {
            "english": "terrain", "phonetic": "/təˈreɪn/", "chinese": "n. 地形", 
            "example": "The rough terrain makes hiking difficult.",
            "category": "自然地理"
        },
        {
            "english": "vegetation", "phonetic": "/ˌvedʒəˈteɪʃn/", "chinese": "n. 植被", 
            "example": "The vegetation is lush in the tropics.",
            "category": "自然地理"
        },
        {
            "english": "wildlife", "phonetic": "/ˈwaɪldlaɪf/", "chinese": "n. 野生动物", 
            "example": "The national park protects wildlife.",
            "category": "自然地理"
        },
        {
            "english": "habitat", "phonetic": "/ˈhæbɪtæt/", "chinese": "n. 栖息地", 
            "example": "The forest is a habitat for many animals.",
            "category": "自然地理"
        },
        {
            "english": "species", "phonetic": "/ˈspiːʃiːz/", "chinese": "n. 物种", 
            "example": "Many species are endangered.",
            "category": "自然地理"
        },
        {
            "english": "extinction", "phonetic": "/ɪkˈstɪŋkʃn/", "chinese": "n. 灭绝", 
            "example": "Dinosaurs went extinct millions of years ago.",
            "category": "自然地理"
        },
        
        # 心理/情感类
        {
            "english": "psychology", "phonetic": "/saɪˈkɑːlədʒi/", "chinese": "n. 心理学", 
            "example": "Psychology studies human behavior.",
            "category": "心理情感"
        },
        {
            "english": "emotion", "phonetic": "/ɪˈmoʊʃn/", "chinese": "n. 情感", 
            "example": "Emotions influence our decisions.",
            "category": "心理情感"
        },
        {
            "english": "feeling", "phonetic": "/ˈfiːlɪŋ/", "chinese": "n. 感觉", 
            "example": "She had a feeling something was wrong.",
            "category": "心理情感"
        },
        {
            "english": "mood", "phonetic": "/muːd/", "chinese": "n. 情绪", 
            "example": "His mood improved after the good news.",
            "category": "心理情感"
        },
        {
            "english": "temperament", "phonetic": "/ˈtempərəmənt/", "chinese": "n. 性格", 
            "example": "She has a calm temperament.",
            "category": "心理情感"
        },
        {
            "english": "personality", "phonetic": "/ˌpɜːrsəˈnæləti/", "chinese": "n. 个性", 
            "example": "Her personality is very outgoing.",
            "category": "心理情感"
        },
        {
            "english": "character", "phonetic": "/ˈkærəktər/", "chinese": "n. 品格", 
            "example": "He is a man of good character.",
            "category": "心理情感"
        },
        {
            "english": "attitude", "phonetic": "/ˈætɪtuːd/", "chinese": "n. 态度", 
            "example": "Maintain a positive attitude.",
            "category": "心理情感"
        },
        {
            "english": "behavior", "phonetic": "/bɪˈheɪvjər/", "chinese": "n. 行为", 
            "example": "His behavior was inappropriate.",
            "category": "心理情感"
        },
        {
            "english": "motivation", "phonetic": "/ˌmoʊtɪˈveɪʃn/", "chinese": "n. 动机", 
            "example": "Motivation is key to success.",
            "category": "心理情感"
        },
        {
            "english": "inspiration", "phonetic": "/ˌɪnspəˈreɪʃn/", "chinese": "n. 灵感", 
            "example": "Nature provides inspiration for artists.",
            "category": "心理情感"
        },
        {
            "english": "creativity", "phonetic": "/ˌkriːeɪˈtɪvəti/", "chinese": "n. 创造力", 
            "example": "Creativity is important in problem-solving.",
            "category": "心理情感"
        },
        {
            "english": "imagination", "phonetic": "/ɪˌmædʒɪˈneɪʃn/", "chinese": "n. 想象力", 
            "example": "Children have vivid imaginations.",
            "category": "心理情感"
        },
        {
            "english": "intuition", "phonetic": "/ˌɪntuˈɪʃn/", "chinese": "n. 直觉", 
            "example": "Trust your intuition.",
            "category": "心理情感"
        },
        {
            "english": "instinct", "phonetic": "/ˈɪnstɪŋkt/", "chinese": "n. 本能", 
            "example": "Animals rely on instinct for survival.",
            "category": "心理情感"
        },
        {
            "english": "conscience", "phonetic": "/ˈkɑːnʃəns/", "chinese": "n. 良心", 
            "example": "Let your conscience be your guide.",
            "category": "心理情感"
        },
        {
            "english": "consciousness", "phonetic": "/ˈkɑːnʃəsnəs/", "chinese": "n. 意识", 
            "example": "Human consciousness is complex.",
            "category": "心理情感"
        },
        {
            "english": "subconscious", "phonetic": "/ˌsʌbˈkɑːnʃəs/", "chinese": "adj. 潜意识的", 
            "example": "Dreams come from the subconscious mind.",
            "category": "心理情感"
        },
        {
            "english": "perception", "phonetic": "/pərˈsepʃn/", "chinese": "n. 感知", 
            "example": "Perception varies among individuals.",
            "category": "心理情感"
        },
        {
            "english": "cognition", "phonetic": "/kɑːɡˈnɪʃn/", "chinese": "n. 认知", 
            "example": "Cognition involves thinking and understanding.",
            "category": "心理情感"
        },
        
        # 社会/文化类
        {
            "english": "society", "phonetic": "/səˈsaɪəti/", "chinese": "n. 社会", 
            "example": "Society benefits from education.",
            "category": "社会文化"
        },
        {
            "english": "community", "phonetic": "/kəˈmjuːnəti/", "chinese": "n. 社区", 
            "example": "The community came together to help.",
            "category": "社会文化"
        },
        {
            "english": "culture", "phonetic": "/ˈkʌltʃər/", "chinese": "n. 文化", 
            "example": "Every culture has unique traditions.",
            "category": "社会文化"
        },
        {
            "english": "tradition", "phonetic": "/trəˈdɪʃn/", "chinese": "n. 传统", 
            "example": "The tradition dates back centuries.",
            "category": "社会文化"
        },
        {
            "english": "custom", "phonetic": "/ˈkʌstəm/", "chinese": "n. 习俗", 
            "example": "It is a local custom to greet elders.",
            "category": "社会文化"
        },
        {
            "english": "heritage", "phonetic": "/ˈherɪtɪdʒ/", "chinese": "n. 遗产", 
            "example": "Cultural heritage should be preserved.",
            "category": "社会文化"
        },
        {
            "english": "civilization", "phonetic": "/ˌsɪvəlaɪˈzeɪʃn/", "chinese": "n. 文明", 
            "example": "Ancient civilizations built great monuments.",
            "category": "社会文化"
        },
        {
            "english": "history", "phonetic": "/ˈhɪstri/", "chinese": "n. 历史", 
            "example": "History teaches us valuable lessons.",
            "category": "社会文化"
        },
        {
            "english": "generation", "phonetic": "/ˌdʒenəˈreɪʃn/", "chinese": "n. 一代人", 
            "example": "The younger generation is tech-savvy.",
            "category": "社会文化"
        },
        {
            "english": "population", "phonetic": "/ˌpɑːpjuˈleɪʃn/", "chinese": "n. 人口", 
            "example": "The population is growing rapidly.",
            "category": "社会文化"
        },
        {
            "english": "demographics", "phonetic": "/ˌdeməˈɡræfɪks/", "chinese": "n. 人口统计", 
            "example": "Demographics help understand the market.",
            "category": "社会文化"
        },
        {
            "english": "diversity", "phonetic": "/daɪˈvɜːrsəti/", "chinese": "n. 多样性", 
            "example": "Diversity enriches our community.",
            "category": "社会文化"
        },
        {
            "english": "inclusion", "phonetic": "/ɪnˈkluːʒn/", "chinese": "n. 包容", 
            "example": "Inclusion promotes equality.",
            "category": "社会文化"
        },
        {
            "english": "equality", "phonetic": "/iˈkwɑːləti/", "chinese": "n. 平等", 
            "example": "Everyone deserves equality.",
            "category": "社会文化"
        },
        {
            "english": "justice", "phonetic": "/ˈdʒʌstɪs/", "chinese": "n. 正义", 
            "example": "Justice should be served.",
            "category": "社会文化"
        },
        {
            "english": "freedom", "phonetic": "/ˈfriːdəm/", "chinese": "n. 自由", 
            "example": "Freedom is a fundamental right.",
            "category": "社会文化"
        },
        {
            "english": "rights", "phonetic": "/raɪts/", "chinese": "n. 权利", 
            "example": "Human rights must be protected.",
            "category": "社会文化"
        },
        {
            "english": "responsibility", "phonetic": "/rɪˌspɑːnsəˈbɪləti/", "chinese": "n. 责任", 
            "example": "With power comes responsibility.",
            "category": "社会文化"
        },
        {
            "english": "citizenship", "phonetic": "/ˈsɪtɪzənʃɪp/", "chinese": "n. 公民身份", 
            "example": "He applied for citizenship.",
            "category": "社会文化"
        },
        {
            "english": "democracy", "phonetic": "/dɪˈmɑːkrəsi/", "chinese": "n. 民主", 
            "example": "Democracy allows people to vote.",
            "category": "社会文化"
        },
        
        # 旅行/交通类
        {
            "english": "destination", "phonetic": "/ˌdestɪˈneɪʃn/", "chinese": "n. 目的地", 
            "example": "Paris is a popular travel destination.",
            "category": "旅行交通"
        },
        {
            "english": "itinerary", "phonetic": "/aɪˈtɪnəreri/", "chinese": "n. 行程", 
            "example": "Check your itinerary before departure.",
            "category": "旅行交通"
        },
        {
            "english": "accommodation", "phonetic": "/əˌkɑːməˈdeɪʃn/", "chinese": "n. 住宿", 
            "example": "Book accommodation in advance.",
            "category": "旅行交通"
        },
        {
            "english": "reservation", "phonetic": "/ˌrezərˈveɪʃn/", "chinese": "n. 预订", 
            "example": "Make a reservation at the restaurant.",
            "category": "旅行交通"
        },
        {
            "english": "transportation", "phonetic": "/ˌtrænspɔːrˈteɪʃn/", "chinese": "n. 交通", 
            "example": "Public transportation is convenient.",
            "category": "旅行交通"
        },
        {
            "english": "commute", "phonetic": "/kəˈmjuːt/", "chinese": "n. 通勤", 
            "example": "Her daily commute takes an hour.",
            "category": "旅行交通"
        },
        {
            "english": "expedition", "phonetic": "/ˌekspəˈdɪʃn/", "chinese": "n. 探险", 
            "example": "They went on an expedition to Antarctica.",
            "category": "旅行交通"
        },
        {
            "english": "adventure", "phonetic": "/ədˈventʃər/", "chinese": "n. 冒险", 
            "example": "Life is an adventure.",
            "category": "旅行交通"
        },
        {
            "english": "excursion", "phonetic": "/ɪkˈskɜːrʒn/", "chinese": "n. 短途旅行", 
            "example": "We went on an excursion to the mountains.",
            "category": "旅行交通"
        },
        {
            "english": "voyage", "phonetic": "/ˈvɔɪɪdʒ/", "chinese": "n. 航行", 
            "example": "The voyage across the Atlantic took weeks.",
            "category": "旅行交通"
        },
        {
            "english": "journey", "phonetic": "/ˈdʒɜːrni/", "chinese": "n. 旅程", 
            "example": "The journey was long but rewarding.",
            "category": "旅行交通"
        },
        {
            "english": "passport", "phonetic": "/ˈpæspɔːrt/", "chinese": "n. 护照", 
            "example": "Don't forget your passport when traveling.",
            "category": "旅行交通"
        },
        {
            "english": "visa", "phonetic": "/ˈviːzə/", "chinese": "n. 签证", 
            "example": "Apply for a visa before traveling abroad.",
            "category": "旅行交通"
        },
        {
            "english": "customs", "phonetic": "/ˈkʌstəmz/", "chinese": "n. 海关", 
            "example": "Go through customs when entering a country.",
            "category": "旅行交通"
        },
        {
            "english": "immigration", "phonetic": "/ˌɪmɪˈɡreɪʃn/", "chinese": "n. 移民", 
            "example": "Immigration laws vary by country.",
            "category": "旅行交通"
        },
        {
            "english": "tourism", "phonetic": "/ˈtʊrɪzəm/", "chinese": "n. 旅游业", 
            "example": "Tourism is important for the economy.",
            "category": "旅行交通"
        },
        {
            "english": "tourist", "phonetic": "/ˈtʊrɪst/", "chinese": "n. 游客", 
            "example": "Many tourists visit the city each year.",
            "category": "旅行交通"
        },
        {
            "english": "sightseeing", "phonetic": "/ˈsaɪtˌsiːɪŋ/", "chinese": "n. 观光", 
            "example": "We spent the day sightseeing.",
            "category": "旅行交通"
        },
        {
            "english": "landmark", "phonetic": "/ˈlændmɑːrk/", "chinese": "n. 地标", 
            "example": "The Eiffel Tower is a famous landmark.",
            "category": "旅行交通"
        },
        {
            "english": "attraction", "phonetic": "/əˈtrækʃn/", "chinese": "n. 景点", 
            "example": "The museum is a popular attraction.",
            "category": "旅行交通"
        },
        
        # 食物/烹饪类
        {
            "english": "cuisine", "phonetic": "/kwɪˈziːn/", "chinese": "n. 烹饪", 
            "example": "Italian cuisine is famous worldwide.",
            "category": "食物烹饪"
        },
        {
            "english": "ingredient", "phonetic": "/ɪnˈɡriːdiənt/", "chinese": "n. 食材", 
            "example": "Check the ingredients before cooking.",
            "category": "食物烹饪"
        },
        {
            "english": "recipe", "phonetic": "/ˈresəpi/", "chinese": "n. 食谱", 
            "example": "Follow the recipe carefully.",
            "category": "食物烹饪"
        },
        {
            "english": "nutrition", "phonetic": "/nuːˈtrɪʃn/", "chinese": "n. 营养", 
            "example": "Good nutrition is essential for health.",
            "category": "食物烹饪"
        },
        {
            "english": "diet", "phonetic": "/ˈdaɪət/", "chinese": "n. 饮食", 
            "example": "A balanced diet is important.",
            "category": "食物烹饪"
        },
        {
            "english": "appetite", "phonetic": "/ˈæpɪtaɪt/", "chinese": "n. 食欲", 
            "example": "Exercise increases your appetite.",
            "category": "食物烹饪"
        },
        {
            "english": "flavor", "phonetic": "/ˈfleɪvər/", "chinese": "n. 味道", 
            "example": "The dish has a rich flavor.",
            "category": "食物烹饪"
        },
        {
            "english": "taste", "phonetic": "/teɪst/", "chinese": "n. 味道", 
            "example": "The cake has a sweet taste.",
            "category": "食物烹饪"
        },
        {
            "english": "aroma", "phonetic": "/əˈroʊmə/", "chinese": "n. 香气", 
            "example": "The aroma of fresh bread is wonderful.",
            "category": "食物烹饪"
        },
        {
            "english": "texture", "phonetic": "/ˈtekstʃər/", "chinese": "n. 口感", 
            "example": "The texture of the cake is soft.",
            "category": "食物烹饪"
        },
        {
            "english": "spicy", "phonetic": "/ˈspaɪsi/", "chinese": "adj. 辣的", 
            "example": "I love spicy food.",
            "category": "食物烹饪"
        },
        {
            "english": "salty", "phonetic": "/ˈsɔːlti/", "chinese": "adj. 咸的", 
            "example": "The soup is too salty.",
            "category": "食物烹饪"
        },
        {
            "english": "sweet", "phonetic": "/swiːt/", "chinese": "adj. 甜的", 
            "example": "Desserts are usually sweet.",
            "category": "食物烹饪"
        },
        {
            "english": "sour", "phonetic": "/ˈsaʊər/", "chinese": "adj. 酸的", 
            "example": "Lemons taste sour.",
            "category": "食物烹饪"
        },
        {
            "english": "bitter", "phonetic": "/ˈbɪtər/", "chinese": "adj. 苦的", 
            "example": "Coffee can be bitter.",
            "category": "食物烹饪"
        },
        {
            "english": "delicious", "phonetic": "/dɪˈlɪʃəs/", "chinese": "adj. 美味的", 
            "example": "The meal was delicious.",
            "category": "食物烹饪"
        },
        {
            "english": "tasty", "phonetic": "/ˈteɪsti/", "chinese": "adj. 好吃的", 
            "example": "This sandwich is very tasty.",
            "category": "食物烹饪"
        },
        {
            "english": "flavorful", "phonetic": "/ˈfleɪvərfəl/", "chinese": "adj. 有风味的", 
            "example": "The sauce is flavorful.",
            "category": "食物烹饪"
        },
        {
            "english": "savory", "phonetic": "/ˈseɪvəri/", "chinese": "adj. 美味的", 
            "example": "I prefer savory snacks over sweet ones.",
            "category": "食物烹饪"
        },
        {
            "english": "refreshing", "phonetic": "/rɪˈfreʃɪŋ/", "chinese": "adj. 清爽的", 
            "example": "A cold drink is refreshing.",
            "category": "食物烹饪"
        },
        
        # 医疗/健康类
        {
            "english": "diagnosis", "phonetic": "/ˌdaɪəɡˈnoʊsɪs/", "chinese": "n. 诊断", 
            "example": "The doctor made a diagnosis.",
            "category": "医疗健康"
        },
        {
            "english": "symptom", "phonetic": "/ˈsɪmptəm/", "chinese": "n. 症状", 
            "example": "Fever is a common symptom of flu.",
            "category": "医疗健康"
        },
        {
            "english": "treatment", "phonetic": "/ˈtriːtmənt/", "chinese": "n. 治疗", 
            "example": "The treatment was effective.",
            "category": "医疗健康"
        },
        {
            "english": "therapy", "phonetic": "/ˈθerəpi/", "chinese": "n. 疗法", 
            "example": "Physical therapy helps recovery.",
            "category": "医疗健康"
        },
        {
            "english": "medication", "phonetic": "/ˌmedɪˈkeɪʃn/", "chinese": "n. 药物", 
            "example": "Take your medication as prescribed.",
            "category": "医疗健康"
        },
        {
            "english": "prescription", "phonetic": "/prɪˈskrɪpʃn/", "chinese": "n. 处方", 
            "example": "The doctor wrote a prescription.",
            "category": "医疗健康"
        },
        {
            "english": "surgery", "phonetic": "/ˈsɜːrdʒəri/", "chinese": "n. 手术", 
            "example": "He underwent surgery yesterday.",
            "category": "医疗健康"
        },
        {
            "english": "rehabilitation", "phonetic": "/ˌriːəˌbɪlɪˈteɪʃn/", "chinese": "n. 康复", 
            "example": "Rehabilitation is important after injury.",
            "category": "医疗健康"
        },
        {
            "english": "prevention", "phonetic": "/prɪˈvenʃn/", "chinese": "n. 预防", 
            "example": "Prevention is better than cure.",
            "category": "医疗健康"
        },
        {
            "english": "vaccination", "phonetic": "/ˌvæksɪˈneɪʃn/", "chinese": "n. 疫苗接种", 
            "example": "Vaccination protects against diseases.",
            "category": "医疗健康"
        },
        {
            "english": "immunity", "phonetic": "/ɪˈmjuːnəti/", "chinese": "n. 免疫力", 
            "example": "Exercise boosts immunity.",
            "category": "医疗健康"
        },
        {
            "english": "infection", "phonetic": "/ɪnˈfekʃn/", "chinese": "n. 感染", 
            "example": "The infection spread quickly.",
            "category": "医疗健康"
        },
        {
            "english": "bacteria", "phonetic": "/bækˈtɪriə/", "chinese": "n. 细菌", 
            "example": "Bacteria can cause illness.",
            "category": "医疗健康"
        },
        {
            "english": "virus", "phonetic": "/ˈvaɪrəs/", "chinese": "n. 病毒", 
            "example": "The virus is highly contagious.",
            "category": "医疗健康"
        },
        {
            "english": "disease", "phonetic": "/dɪˈziːz/", "chinese": "n. 疾病", 
            "example": "Heart disease is a major health concern.",
            "category": "医疗健康"
        },
        {
            "english": "illness", "phonetic": "/ˈɪlnəs/", "chinese": "n. 疾病", 
            "example": "Mental illness requires treatment.",
            "category": "医疗健康"
        },
        {
            "english": "condition", "phonetic": "/kənˈdɪʃn/", "chinese": "n. 状况", 
            "example": "Her condition has improved.",
            "category": "医疗健康"
        },
        {
            "english": "disorder", "phonetic": "/dɪsˈɔːrdər/", "chinese": "n. 紊乱", 
            "example": "He has a sleep disorder.",
            "category": "医疗健康"
        },
        {
            "english": "syndrome", "phonetic": "/ˈsɪndroʊm/", "chinese": "n. 综合征", 
            "example": "Down syndrome is a genetic condition.",
            "category": "医疗健康"
        },
        
        # 商业/管理类
        {
            "english": "management", "phonetic": "/ˈmænɪdʒmənt/", "chinese": "n. 管理", 
            "example": "Good management is essential for success.",
            "category": "商业管理"
        },
        {
            "english": "leadership", "phonetic": "/ˈliːdərʃɪp/", "chinese": "n. 领导力", 
            "example": "Strong leadership inspires the team.",
            "category": "商业管理"
        },
        {
            "english": "strategy", "phonetic": "/ˈstrætədʒi/", "chinese": "n. 策略", 
            "example": "We need a clear strategy.",
            "category": "商业管理"
        },
        {
            "english": "planning", "phonetic": "/ˈplænɪŋ/", "chinese": "n. 规划", 
            "example": "Careful planning prevents problems.",
            "category": "商业管理"
        },
        {
            "english": "organization", "phonetic": "/ˌɔːrɡənaɪˈzeɪʃn/", "chinese": "n. 组织", 
            "example": "The organization has many employees.",
            "category": "商业管理"
        },
        {
            "english": "administration", "phonetic": "/ədˌmɪnɪˈstreɪʃn/", "chinese": "n. 行政", 
            "example": "The administration manages daily operations.",
            "category": "商业管理"
        },
        {
            "english": "operation", "phonetic": "/ˌɑːpəˈreɪʃn/", "chinese": "n. 运营", 
            "example": "Business operations run smoothly.",
            "category": "商业管理"
        },
        {
            "english": "production", "phonetic": "/prəˈdʌkʃn/", "chinese": "n. 生产", 
            "example": "Production increased this quarter.",
            "category": "商业管理"
        },
        {
            "english": "distribution", "phonetic": "/ˌdɪstrɪˈbjuːʃn/", "chinese": "n. 分销", 
            "example": "The product distribution is efficient.",
            "category": "商业管理"
        },
        {
            "english": "marketing", "phonetic": "/ˈmɑːrkətɪŋ/", "chinese": "n. 营销", 
            "example": "Digital marketing is effective.",
            "category": "商业管理"
        },
        {
            "english": "advertising", "phonetic": "/ˈædvərtaɪzɪŋ/", "chinese": "n. 广告", 
            "example": "Advertising helps sell products.",
            "category": "商业管理"
        },
        {
            "english": "promotion", "phonetic": "/prəˈmoʊʃn/", "chinese": "n. 促销", 
            "example": "The promotion attracted many customers.",
            "category": "商业管理"
        },
        {
            "english": "sales", "phonetic": "/seɪlz/", "chinese": "n. 销售", 
            "example": "Sales have increased this month.",
            "category": "商业管理"
        },
        {
            "english": "customer", "phonetic": "/ˈkʌstəmər/", "chinese": "n. 顾客", 
            "example": "Customer satisfaction is important.",
            "category": "商业管理"
        },
        {
            "english": "client", "phonetic": "/ˈklaɪənt/", "chinese": "n. 客户", 
            "example": "The client was happy with the service.",
            "category": "商业管理"
        },
        {
            "english": "service", "phonetic": "/ˈsɜːrvɪs/", "chinese": "n. 服务", 
            "example": "Good service builds loyalty.",
            "category": "商业管理"
        },
        {
            "english": "quality", "phonetic": "/ˈkwɑːləti/", "chinese": "n. 质量", 
            "example": "Quality control ensures excellence.",
            "category": "商业管理"
        },
        {
            "english": "efficiency", "phonetic": "/ɪˈfɪʃnsi/", "chinese": "n. 效率", 
            "example": "Efficiency saves time and money.",
            "category": "商业管理"
        },
        {
            "english": "productivity", "phonetic": "/ˌprɑːdʌkˈtɪvəti/", "chinese": "n. 生产力", 
            "example": "Productivity has improved.",
            "category": "商业管理"
        },
        {
            "english": "performance", "phonetic": "/pərˈfɔːrməns/", "chinese": "n. 表现", 
            "example": "Her performance was outstanding.",
            "category": "商业管理"
        },
        
        # 法律/政治类
        {
            "english": "legislation", "phonetic": "/ˌledʒɪsˈleɪʃn/", "chinese": "n. 立法", 
            "example": "New legislation was passed.",
            "category": "法律政治"
        },
        {
            "english": "regulation", "phonetic": "/ˌreɡjuˈleɪʃn/", "chinese": "n. 法规", 
            "example": "The regulation protects consumers.",
            "category": "法律政治"
        },
        {
            "english": "compliance", "phonetic": "/kəmˈplaɪəns/", "chinese": "n. 合规", 
            "example": "Compliance with laws is mandatory.",
            "category": "法律政治"
        },
        {
            "english": "contract", "phonetic": "/ˈkɑːntrækt/", "chinese": "n. 合同", 
            "example": "Read the contract carefully.",
            "category": "法律政治"
        },
        {
            "english": "agreement", "phonetic": "/əˈɡriːmənt/", "chinese": "n. 协议", 
            "example": "They reached an agreement.",
            "category": "法律政治"
        },
        {
            "english": "negotiation", "phonetic": "/nɪˌɡoʊʃiˈeɪʃn/", "chinese": "n. 谈判", 
            "example": "The negotiation was successful.",
            "category": "法律政治"
        },
        {
            "english": "dispute", "phonetic": "/dɪˈspjuːt/", "chinese": "n. 争议", 
            "example": "The dispute was resolved.",
            "category": "法律政治"
        },
        {
            "english": "litigation", "phonetic": "/ˌlɪtɪˈɡeɪʃn/", "chinese": "n. 诉讼", 
            "example": "Litigation can be expensive.",
            "category": "法律政治"
        },
        {
            "english": "verdict", "phonetic": "/ˈvɜːrdɪkt/", "chinese": "n. 裁决", 
            "example": "The jury reached a verdict.",
            "category": "法律政治"
        },
        {
            "english": "judgment", "phonetic": "/ˈdʒʌdʒmənt/", "chinese": "n. 判决", 
            "example": "The judgment was fair.",
            "category": "法律政治"
        },
        {
            "english": "penalty", "phonetic": "/ˈpenəlti/", "chinese": "n. 惩罚", 
            "example": "The penalty for speeding is a fine.",
            "category": "法律政治"
        },
        {
            "english": "punishment", "phonetic": "/ˈpʌnɪʃmənt/", "chinese": "n. 惩罚", 
            "example": "The punishment fit the crime.",
            "category": "法律政治"
        },
        {
            "english": "crime", "phonetic": "/kraɪm/", "chinese": "n. 犯罪", 
            "example": "Crime rates have decreased.",
            "category": "法律政治"
        },
        {
            "english": "court", "phonetic": "/kɔːrt/", "chinese": "n. 法院", 
            "example": "The case went to court.",
            "category": "法律政治"
        },
        {
            "english": "judge", "phonetic": "/dʒʌdʒ/", "chinese": "n. 法官", 
            "example": "The judge made a fair decision.",
            "category": "法律政治"
        },
        {
            "english": "jury", "phonetic": "/ˈdʒʊri/", "chinese": "n. 陪审团", 
            "example": "The jury reached a verdict.",
            "category": "法律政治"
        },
        {
            "english": "lawyer", "phonetic": "/ˈlɔːjər/", "chinese": "n. 律师", 
            "example": "Consult a lawyer for legal advice.",
            "category": "法律政治"
        },
        {
            "english": "attorney", "phonetic": "/əˈtɜːrni/", "chinese": "n. 律师", 
            "example": "The attorney represented the client.",
            "category": "法律政治"
        },
        
        # 科学/研究类
        {
            "english": "research", "phonetic": "/ˈriːsɜːrtʃ/", "chinese": "n. 研究", 
            "example": "Scientific research advances knowledge.",
            "category": "科学研究"
        },
        {
            "english": "experiment", "phonetic": "/ɪkˈsperɪmənt/", "chinese": "n. 实验", 
            "example": "The experiment yielded interesting results.",
            "category": "科学研究"
        },
        {
            "english": "hypothesis", "phonetic": "/haɪˈpɑːθəsɪs/", "chinese": "n. 假设", 
            "example": "The hypothesis was tested.",
            "category": "科学研究"
        },
        {
            "english": "theory", "phonetic": "/ˈθiːəri/", "chinese": "n. 理论", 
            "example": "The theory explains the phenomenon.",
            "category": "科学研究"
        },
        {
            "english": "principle", "phonetic": "/ˈprɪnsəpl/", "chinese": "n. 原理", 
            "example": "The principle is fundamental.",
            "category": "科学研究"
        },
        {
            "english": "concept", "phonetic": "/ˈkɑːnsept/", "chinese": "n. 概念", 
            "example": "The concept is easy to understand.",
            "category": "科学研究"
        },
        {
            "english": "phenomenon", "phonetic": "/fəˈnɑːmɪnən/", "chinese": "n. 现象", 
            "example": "The phenomenon is rare.",
            "category": "科学研究"
        },
        {
            "english": "observation", "phonetic": "/ˌɑːbzərˈveɪʃn/", "chinese": "n. 观察", 
            "example": "Careful observation is important.",
            "category": "科学研究"
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
    
    print(f'成功添加 {added_count} 个新单词到数据库')
    print(f'数据库总单词数: {total}')
    
    conn.close()

if __name__ == '__main__':
    expand_to_5000_batch4()
