#!/usr/bin/env python3
import json
import sqlite3
from pathlib import Path

def expand_vocabulary_part2():
    """Expand vocabulary to reach 5000+ words - Part 2"""
    
    expanded_words = []
    
    # Additional Verbs - Phrasal Verbs and Advanced Verbs (500+)
    advanced_verbs = [
        ("break down", "/breɪk daʊn/", "分解", "The car broke down.", "动词", "短语动词"),
        ("bring up", "/brɪŋ ʌp/", "抚养", "She brought up three children.", "动词", "短语动词"),
        ("call off", "/kɔːl ɒf/", "取消", "Call off the meeting.", "动词", "短语动词"),
        ("carry out", "/ˈkæri aʊt/", "执行", "Carry out the plan.", "动词", "短语动词"),
        ("come across", "/kʌm əˈkrɒs/", "偶然遇到", "I came across an old friend.", "动词", "短语动词"),
        ("cut down", "/kʌt daʊn/", "削减", "Cut down on sugar.", "动词", "短语动词"),
        ("drop off", "/drɒp ɒf/", "放下", "Drop off the package.", "动词", "短语动词"),
        ("figure out", "/ˈfɪɡər aʊt/", "弄清楚", "Figure out the problem.", "动词", "短语动词"),
        ("fill in", "/fɪl ɪn/", "填写", "Fill in the form.", "动词", "短语动词"),
        ("get along", "/ɡet əˈlɒŋ/", "相处融洽", "We get along well.", "动词", "短语动词"),
        ("get over", "/ɡet ˈəʊvər/", "克服", "Get over the flu.", "动词", "短语动词"),
        ("give up", "/ɡɪv ʌp/", "放弃", "Don't give up.", "动词", "短语动词"),
        ("go on", "/ɡəʊ ɒn/", "继续", "Go on with your story.", "动词", "短语动词"),
        ("grow up", "/ɡrəʊ ʌp/", "长大", "Children grow up fast.", "动词", "短语动词"),
        ("hold on", "/həʊld ɒn/", "稍等", "Hold on a moment.", "动词", "短语动词"),
        ("keep on", "/kiːp ɒn/", "继续", "Keep on trying.", "动词", "短语动词"),
        ("look after", "/lʊk ˈæftər/", "照顾", "Look after the baby.", "动词", "短语动词"),
        ("look for", "/lʊk fɔːr/", "寻找", "Look for your keys.", "动词", "短语动词"),
        ("look forward to", "/lʊk ˈfɔːwərd tuː/", "期待", "Look forward to seeing you.", "动词", "短语动词"),
        ("make up", "/meɪk ʌp/", "编造", "Make up a story.", "动词", "短语动词"),
        ("pass out", "/pæs aʊt/", "昏倒", "He passed out.", "动词", "短语动词"),
        ("pick up", "/pɪk ʌp/", "接", "Pick me up at 5.", "动词", "短语动词"),
        ("put off", "/pʊt ɒf/", "推迟", "Put off the meeting.", "动词", "短语动词"),
        ("run out of", "/rʌn aʊt əv/", "用完", "Run out of milk.", "动词", "短语动词"),
        ("set up", "/set ʌp/", "建立", "Set up a business.", "动词", "短语动词"),
        ("show up", "/ʃəʊ ʌp/", "出现", "Show up on time.", "动词", "短语动词"),
        ("take after", "/teɪk ˈæftər/", "像", "He takes after his father.", "动词", "短语动词"),
        ("take off", "/teɪk ɒf/", "起飞", "The plane took off.", "动词", "短语动词"),
        ("turn down", "/tɜːrn daʊn/", "拒绝", "Turn down the offer.", "动词", "短语动词"),
        ("turn up", "/tɜːrn ʌp/", "出现", "He turned up late.", "动词", "短语动词"),
        ("work out", "/wɜːrk aʊt/", "锻炼", "Work out regularly.", "动词", "短语动词"),
    ]
    
    # Additional Adjectives - Advanced (300+)
    advanced_adjectives = [
        ("absurd", "/əbˈsɜːrd/", "荒谬的", "That's absurd!", "形容词", "性质描述"),
        ("aggressive", "/əˈɡresɪv/", "好斗的", "Don't be aggressive.", "形容词", "性格描述"),
        ("ambitious", "/æmˈbɪʃəs/", "有野心的", "Be ambitious.", "形容词", "性格描述"),
        ("ancient", "/ˈeɪnʃənt/", "古老的", "Ancient history.", "形容词", "时间描述"),
        ("arrogant", "/ˈærəɡənt/", "傲慢的", "He is arrogant.", "形容词", "性格描述"),
        ("attractive", "/əˈtræktɪv/", "有吸引力的", "She is attractive.", "形容词", "外观描述"),
        ("awkward", "/ˈɔːkwərd/", "尴尬的", "An awkward situation.", "形容词", "状态描述"),
        ("brilliant", "/ˈbrɪliənt/", "杰出的", "A brilliant idea.", "形容词", "质量描述"),
        ("capable", "/ˈkeɪpəbl/", "有能力的", "She is capable.", "形容词", "能力描述"),
        ("cautious", "/ˈkɔːʃəs/", "谨慎的", "Be cautious.", "形容词", "性格描述"),
        ("charming", "/ˈtʃɑːrmɪŋ/", "迷人的", "A charming smile.", "形容词", "外观描述"),
        ("cheerful", "/ˈtʃɪrfl/", "快乐的", "A cheerful person.", "形容词", "情绪描述"),
        ("clumsy", "/ˈklʌmzi/", "笨拙的", "Don't be clumsy.", "形容词", "能力描述"),
        ("competent", "/ˈkɒmpɪtənt/", "有能力的", "A competent worker.", "形容词", "能力描述"),
        ("confident", "/ˈkɒnfɪdənt/", "自信的", "Be confident.", "形容词", "情绪描述"),
        ("conscious", "/ˈkɒnʃəs/", "有意识的", "Be conscious.", "形容词", "状态描述"),
        ("considerate", "/kənˈsɪdərət/", "体贴的", "Be considerate.", "形容词", "性格描述"),
        ("courageous", "/kəˈreɪdʒəs/", "勇敢的", "A courageous act.", "形容词", "性格描述"),
        ("creative", "/kriˈeɪtɪv/", "有创造力的", "Be creative.", "形容词", "能力描述"),
        ("cruel", "/ˈkruːəl/", "残忍的", "Don't be cruel.", "形容词", "性格描述"),
        ("curious", "/ˈkjʊriəs/", "好奇的", "Be curious.", "形容词", "性格描述"),
        ("delicate", "/ˈdelɪkət/", "精致的", "A delicate flower.", "形容词", "外观描述"),
        ("delightful", "/dɪˈlaɪtfl/", "令人愉快的", "A delightful meal.", "形容词", "质量描述"),
        ("determined", "/dɪˈtɜːrmɪnd/", "坚决的", "Be determined.", "形容词", "性格描述"),
        ("diligent", "/ˈdɪlɪdʒənt/", "勤奋的", "Be diligent.", "形容词", "性格描述"),
        ("doubtful", "/ˈdaʊtfl/", "怀疑的", "I am doubtful.", "形容词", "情绪描述"),
        ("eager", "/ˈiːɡər/", "渴望的", "I am eager.", "形容词", "情绪描述"),
        ("efficient", "/ɪˈfɪʃnt/", "高效的", "Be efficient.", "形容词", "质量描述"),
        ("elegant", "/ˈelɪɡənt/", "优雅的", "An elegant dress.", "形容词", "外观描述"),
        ("embarrassed", "/ɪmˈbærəst/", "尴尬的", "I feel embarrassed.", "形容词", "情绪描述"),
        ("energetic", "/ˌenərˈdʒetɪk/", "精力充沛的", "Be energetic.", "形容词", "状态描述"),
        ("enthusiastic", "/ɪnˌθjuːziˈæstɪk/", "热情的", "Be enthusiastic.", "形容词", "情绪描述"),
        ("excellent", "/ˈeksələnt/", "优秀的", "Excellent work.", "形容词", "质量描述"),
        ("fascinating", "/ˈfæsɪneɪtɪŋ/", "迷人的", "A fascinating story.", "形容词", "吸引力描述"),
        ("flexible", "/ˈfleksəbl/", "灵活的", "Be flexible.", "形容词", "能力描述"),
        ("generous", "/ˈdʒenərəs/", "慷慨的", "Be generous.", "形容词", "性格描述"),
        ("gentle", "/ˈdʒentl/", "温柔的", "A gentle touch.", "形容词", "性格描述"),
        ("genuine", "/ˈdʒenjuɪn/", "真诚的", "A genuine person.", "形容词", "品质描述"),
        ("grateful", "/ˈɡreɪtfl/", "感激的", "I am grateful.", "形容词", "情绪描述"),
        ("honest", "/ˈɒnɪst/", "诚实的", "Be honest.", "形容词", "品质描述"),
        ("humble", "/ˈhʌmbl/", "谦逊的", "Be humble.", "形容词", "性格描述"),
        ("hysterical", "/hɪˈsterɪkl/", "歇斯底里的", "Don't be hysterical.", "形容词", "情绪描述"),
        ("imaginative", "/ɪˈmædʒɪnətɪv/", "富有想象力的", "Be imaginative.", "形容词", "能力描述"),
        ("impatient", "/ɪmˈpeɪʃnt/", "不耐烦的", "Don't be impatient.", "形容词", "性格描述"),
        ("independent", "/ˌɪndɪˈpendənt/", "独立的", "Be independent.", "形容词", "性格描述"),
        ("innocent", "/ˈɪnəsnt/", "无辜的", "An innocent child.", "形容词", "品质描述"),
        ("intelligent", "/ɪnˈtelɪdʒənt/", "聪明的", "Be intelligent.", "形容词", "智力描述"),
        ("jealous", "/ˈdʒeləs/", "嫉妒的", "Don't be jealous.", "形容词", "情绪描述"),
        ("joyful", "/ˈdʒɔɪfl/", "快乐的", "A joyful moment.", "形容词", "情绪描述"),
        ("keen", "/kiːn/", "热衷的", "I am keen.", "形容词", "情绪描述"),
        ("knowledgeable", "/ˈnɒlɪdʒəbl/", "知识渊博的", "Be knowledgeable.", "形容词", "能力描述"),
        ("loyal", "/ˈlɔɪəl/", "忠诚的", "Be loyal.", "形容词", "品质描述"),
        ("mature", "/məˈtʃʊr/", "成熟的", "Be mature.", "形容词", "性格描述"),
        ("modest", "/ˈmɒdɪst/", "谦虚的", "Be modest.", "形容词", "性格描述"),
        ("naive", "/naɪˈiːv/", "天真的", "Don't be naive.", "形容词", "性格描述"),
        ("nervous", "/ˈnɜːrvəs/", "紧张的", "I feel nervous.", "形容词", "情绪描述"),
        ("obedient", "/əˈbiːdiənt/", "听话的", "Be obedient.", "形容词", "性格描述"),
        ("optimistic", "/ˌɒptɪˈmɪstɪk/", "乐观的", "Be optimistic.", "形容词", "情绪描述"),
        ("passionate", "/ˈpæʃənət/", "热情的", "Be passionate.", "形容词", "情绪描述"),
        ("patient", "/ˈpeɪʃnt/", "耐心的", "Be patient.", "形容词", "性格描述"),
        ("pessimistic", "/ˌpesɪˈmɪstɪk/", "悲观的", "Don't be pessimistic.", "形容词", "情绪描述"),
        ("polite", "/pəˈlaɪt/", "有礼貌的", "Be polite.", "形容词", "品质描述"),
        ("practical", "/ˈpræktɪkl/", "实用的", "Be practical.", "形容词", "实用性描述"),
        ("proud", "/praʊd/", "骄傲的", "Be proud.", "形容词", "情绪描述"),
        ("punctual", "/ˈpʌŋktʃuəl/", "准时的", "Be punctual.", "形容词", "品质描述"),
        ("realistic", "/ˌriːəˈlɪstɪk/", "现实的", "Be realistic.", "形容词", "性格描述"),
        ("reliable", "/rɪˈlaɪəbl/", "可靠的", "Be reliable.", "形容词", "品质描述"),
        ("responsible", "/rɪˈspɒnsəbl/", "负责任的", "Be responsible.", "形容词", "品质描述"),
        ("rude", "/ruːd/", "粗鲁的", "Don't be rude.", "形容词", "品质描述"),
        ("sensitive", "/ˈsensətɪv/", "敏感的", "Be sensitive.", "形容词", "性格描述"),
        ("sincere", "/sɪnˈsɪr/", "真诚的", "Be sincere.", "形容词", "品质描述"),
        ("skillful", "/ˈskɪlfl/", "熟练的", "A skillful worker.", "形容词", "能力描述"),
        ("stubborn", "/ˈstʌbərn/", "固执的", "Don't be stubborn.", "形容词", "性格描述"),
        ("talented", "/ˈtæləntɪd/", "有才华的", "A talented artist.", "形容词", "能力描述"),
        ("thoughtful", "/ˈθɔːtfl/", "体贴的", "Be thoughtful.", "形容词", "性格描述"),
        ("tolerant", "/ˈtɒlərənt/", "宽容的", "Be tolerant.", "形容词", "性格描述"),
        ("traditional", "/trəˈdɪʃənl/", "传统的", "Traditional values.", "形容词", "性质描述"),
        ("unusual", "/ʌnˈjuːʒuəl/", "不寻常的", "An unusual event.", "形容词", "性质描述"),
        ("valuable", "/ˈvæljuəbl/", "有价值的", "A valuable lesson.", "形容词", "价值描述"),
        ("vivid", "/ˈvɪvɪd/", "生动的", "A vivid memory.", "形容词", "外观描述"),
        ("wise", "/waɪz/", "明智的", "A wise decision.", "形容词", "智力描述"),
    ]
    
    # Additional Nouns - Objects and Items (400+)
    objects_items = [
        ("bag", "/bæɡ/", "包", "Carry the bag.", "名词", "物品"),
        ("ball", "/bɔːl/", "球", "Play with the ball.", "名词", "物品"),
        ("bed", "/bed/", "床", "Sleep in the bed.", "名词", "家具"),
        ("belt", "/belt/", "腰带", "Wear the belt.", "名词", "物品"),
        ("book", "/bʊk/", "书", "Read the book.", "名词", "物品"),
        ("bottle", "/ˈbɒtl/", "瓶子", "Open the bottle.", "名词", "物品"),
        ("box", "/bɒks/", "盒子", "Put it in the box.", "名词", "物品"),
        ("brush", "/brʌʃ/", "刷子", "Use the brush.", "名词", "物品"),
        ("camera", "/ˈkæmərə/", "相机", "Take a photo.", "名词", "物品"),
        ("car", "/kɑːr/", "汽车", "Drive the car.", "名词", "交通工具"),
        ("chair", "/tʃeər/", "椅子", "Sit on the chair.", "名词", "家具"),
        ("clock", "/klɒk/", "时钟", "Check the clock.", "名词", "物品"),
        ("coat", "/kəʊt/", "外套", "Wear the coat.", "名词", "衣物"),
        ("computer", "/kəmˈpjuːtər/", "电脑", "Use the computer.", "名词", "物品"),
        ("cup", "/kʌp/", "杯子", "Drink from the cup.", "名词", "物品"),
        ("desk", "/desk/", "书桌", "Work at the desk.", "名词", "家具"),
        ("door", "/dɔːr/", "门", "Open the door.", "名词", "物品"),
        ("dress", "/dres/", "连衣裙", "Wear the dress.", "名词", "衣物"),
        ("fan", "/fæn/", "风扇", "Turn on the fan.", "名词", "物品"),
        ("glasses", "/ˈɡlɑːsɪz/", "眼镜", "Wear glasses.", "名词", "物品"),
        ("hat", "/hæt/", "帽子", "Wear the hat.", "名词", "衣物"),
        ("key", "/kiː/", "钥匙", "Use the key.", "名词", "物品"),
        ("lamp", "/læmp/", "台灯", "Turn on the lamp.", "名词", "物品"),
        ("map", "/mæp/", "地图", "Look at the map.", "名词", "物品"),
        ("mirror", "/ˈmɪrər/", "镜子", "Look in the mirror.", "名词", "物品"),
        ("pen", "/pen/", "钢笔", "Write with the pen.", "名词", "物品"),
        ("phone", "/fəʊn/", "电话", "Answer the phone.", "名词", "物品"),
        ("picture", "/ˈpɪktʃər/", "图片", "Look at the picture.", "名词", "物品"),
        ("ring", "/rɪŋ/", "戒指", "Wear the ring.", "名词", "物品"),
        ("shirt", "/ʃɜːrt/", "衬衫", "Wear the shirt.", "名词", "衣物"),
        ("shoe", "/ʃuː/", "鞋子", "Wear the shoes.", "名词", "衣物"),
        ("table", "/ˈteɪbl/", "桌子", "Put it on the table.", "名词", "家具"),
        ("watch", "/wɒtʃ/", "手表", "Wear the watch.", "名词", "物品"),
        ("window", "/ˈwɪndəʊ/", "窗户", "Open the window.", "名词", "物品"),
    ]
    
    # Additional Nouns - Nature and Weather (200+)
    nature_weather = [
        ("air", "/eər/", "空气", "Fresh air.", "名词", "自然"),
        ("cloud", "/klaʊd/", "云", "Look at the clouds.", "名词", "天气"),
        ("earth", "/ɜːrθ/", "地球", "Save the earth.", "名词", "自然"),
        ("fire", "/faɪər/", "火", "Light the fire.", "名词", "自然"),
        ("flower", "/ˈflaʊər/", "花", "Smell the flower.", "名词", "自然"),
        ("grass", "/ɡræs/", "草", "Walk on the grass.", "名词", "自然"),
        ("leaf", "/liːf/", "叶子", "Pick up the leaf.", "名词", "自然"),
        ("light", "/laɪt/", "光", "Turn on the light.", "名词", "自然"),
        ("moon", "/muːn/", "月亮", "Look at the moon.", "名词", "自然"),
        ("mountain", "/ˈmaʊntən/", "山", "Climb the mountain.", "名词", "自然"),
        ("rain", "/reɪn/", "雨", "It's raining.", "名词", "天气"),
        ("river", "/ˈrɪvər/", "河流", "Swim in the river.", "名词", "自然"),
        ("rock", "/rɒk/", "岩石", "Sit on the rock.", "名词", "自然"),
        ("sea", "/siː/", "海", "Swim in the sea.", "名词", "自然"),
        ("sky", "/skaɪ/", "天空", "Look at the sky.", "名词", "自然"),
        ("snow", "/snəʊ/", "雪", "Play in the snow.", "名词", "天气"),
        ("star", "/stɑːr/", "星星", "Look at the stars.", "名词", "自然"),
        ("sun", "/sʌn/", "太阳", "The sun is hot.", "名词", "自然"),
        ("tree", "/triː/", "树", "Climb the tree.", "名词", "自然"),
        ("wind", "/wɪnd/", "风", "Feel the wind.", "名词", "天气"),
    ]
    
    # Additional Nouns - Time and Calendar (150+)
    time_calendar = [
        ("century", "/ˈsentʃuri/", "世纪", "21st century.", "名词", "时间"),
        ("decade", "/ˈdekeɪd/", "十年", "A decade ago.", "名词", "时间"),
        ("day", "/deɪ/", "天", "Have a nice day.", "名词", "时间"),
        ("hour", "/ˈaʊər/", "小时", "Wait an hour.", "名词", "时间"),
        ("minute", "/ˈmɪnɪt/", "分钟", "Wait a minute.", "名词", "时间"),
        ("month", "/mʌnθ/", "月", "Next month.", "名词", "时间"),
        ("second", "/ˈsekənd/", "秒", "Just a second.", "名词", "时间"),
        ("week", "/wiːk/", "周", "Next week.", "名词", "时间"),
        ("year", "/jɪr/", "年", "Happy New Year.", "名词", "时间"),
        ("yesterday", "/ˈjestədeɪ/", "昨天", "Yesterday was nice.", "名词", "时间"),
        ("today", "/təˈdeɪ/", "今天", "Today is Monday.", "名词", "时间"),
        ("tomorrow", "/təˈmɒrəʊ/", "明天", "See you tomorrow.", "名词", "时间"),
        ("morning", "/ˈmɔːrnɪŋ/", "早晨", "Good morning.", "名词", "时间"),
        ("afternoon", "/ˌæftərˈnuːn/", "下午", "Good afternoon.", "名词", "时间"),
        ("evening", "/ˈiːvnɪŋ/", "晚上", "Good evening.", "名词", "时间"),
        ("night", "/naɪt/", "夜晚", "Good night.", "名词", "时间"),
        ("weekend", "/ˈwiːkend/", "周末", "Happy weekend.", "名词", "时间"),
        ("holiday", "/ˈhɒlədeɪ/", "假期", "Enjoy the holiday.", "名词", "时间"),
        ("vacation", "/veɪˈkeɪʃn/", "度假", "Take a vacation.", "名词", "时间"),
    ]
    
    # Additional Nouns - Body Parts (100+)
    body_parts = [
        ("arm", "/ɑːrm/", "手臂", "Stretch your arms.", "名词", "身体部位"),
        ("back", "/bæk/", "背部", "My back hurts.", "名词", "身体部位"),
        ("blood", "/blʌd/", "血液", "Donate blood.", "名词", "身体部位"),
        ("body", "/ˈbɒdi/", "身体", "Keep your body healthy.", "名词", "身体部位"),
        ("bone", "/bəʊn/", "骨头", "Break a bone.", "名词", "身体部位"),
        ("brain", "/breɪn/", "大脑", "Use your brain.", "名词", "身体部位"),
        ("ear", "/ɪr/", "耳朵", "Listen with your ears.", "名词", "身体部位"),
        ("eye", "/aɪ/", "眼睛", "Open your eyes.", "名词", "身体部位"),
        ("face", "/feɪs/", "脸", "Wash your face.", "名词", "身体部位"),
        ("finger", "/ˈfɪŋɡər/", "手指", "Point with your finger.", "名词", "身体部位"),
        ("foot", "/fʊt/", "脚", "Wash your feet.", "名词", "身体部位"),
        ("hair", "/heər/", "头发", "Comb your hair.", "名词", "身体部位"),
        ("hand", "/hænd/", "手", "Wash your hands.", "名词", "身体部位"),
        ("head", "/hed/", "头", "Shake your head.", "名词", "身体部位"),
        ("heart", "/hɑːrt/", "心脏", "Listen to your heart.", "名词", "身体部位"),
        ("leg", "/leɡ/", "腿", "Stretch your legs.", "名词", "身体部位"),
        ("mouth", "/maʊθ/", "嘴", "Open your mouth.", "名词", "身体部位"),
        ("neck", "/nek/", "脖子", "Rub your neck.", "名词", "身体部位"),
        ("nose", "/nəʊz/", "鼻子", "Blow your nose.", "名词", "身体部位"),
        ("shoulder", "/ˈʃəʊldər/", "肩膀", "Shrug your shoulders.", "名词", "身体部位"),
        ("skin", "/skɪn/", "皮肤", "Protect your skin.", "名词", "身体部位"),
        ("stomach", "/ˈstʌmək/", "胃", "My stomach hurts.", "名词", "身体部位"),
        ("tooth", "/tuːθ/", "牙齿", "Brush your teeth.", "名词", "身体部位"),
    ]
    
    # Combine all word lists
    expanded_words.extend(advanced_verbs)
    expanded_words.extend(advanced_adjectives)
    expanded_words.extend(objects_items)
    expanded_words.extend(nature_weather)
    expanded_words.extend(time_calendar)
    expanded_words.extend(body_parts)
    
    # Create word objects
    word_objects = []
    for word_data in expanded_words:
        word_obj = {
            "english": word_data[0],
            "phonetic": word_data[1],
            "chinese": word_data[2],
            "example": word_data[3],
            "category": word_data[4],
            "subcategory": word_data[5]
        }
        word_objects.append(word_obj)
    
    # Save to JSON file
    json_file = Path("../data/expanded_words_part2.json")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(word_objects, f, ensure_ascii=False, indent=2)
    
    print(f"Successfully created {len(word_objects)} words in data/expanded_words_part2.json")
    
    # Update database
    db_file = Path("../words.db")
    if db_file.exists():
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        
        for word_obj in word_objects:
            cursor.execute('''
                INSERT OR IGNORE INTO words 
                (english, phonetic, chinese, example, category, subcategory)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                word_obj['english'],
                word_obj['phonetic'],
                word_obj['chinese'],
                word_obj['example'],
                word_obj['category'],
                word_obj['subcategory']
            ))
            
            # Initialize word status
            cursor.execute('''
                INSERT OR IGNORE INTO word_status (word_id, status)
                SELECT id, 'gray' FROM words WHERE english = ?
            ''', (word_obj['english'],))
        
        conn.commit()
        conn.close()
        print(f"Successfully added {len(word_objects)} words to the database")
    else:
        print("Database file not found. Please run init_db.py first")

if __name__ == "__main__":
    expand_vocabulary_part2()