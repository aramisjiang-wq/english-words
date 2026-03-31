#!/usr/bin/env python3
import sqlite3

def expand_vocabulary_to_5000_part2():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    new_words = [
        # 医学/健康词汇 (50+)
        ("anatomy", "/əˈnætəmi/", "解剖学", "Study anatomy.", "名词"),
        ("antibiotic", "/ˌæntibaɪˈɒtɪk/", "抗生素", "Take antibiotic.", "名词"),
        ("bacteria", "/bækˈtɪəriə/", "细菌", "Harmful bacteria.", "名词"),
        ("biopsy", "/ˈbaɪɒpsi/", "活检", "Perform a biopsy.", "名词"),
        ("cardiology", "/ˌkɑːdiˈɒlədʒi/", "心脏病学", "Cardiology department.", "名词"),
        ("diagnosis", "/ˌdaɪəɡˈnəʊsɪs/", "诊断", "Make a diagnosis.", "名词"),
        ("epidemic", "/ˌepɪˈdemɪk/", "流行病", "Global epidemic.", "名词"),
        ("genetics", "/dʒəˈnetɪks/", "遗传学", "Study genetics.", "名词"),
        ("immunity", "/ɪˈmjuːnəti/", "免疫力", "Boost immunity.", "名词"),
        ("infection", "/ɪnˈfekʃn/", "感染", "Viral infection.", "名词"),
        ("medication", "/ˌmedɪˈkeɪʃn/", "药物", "Take medication.", "名词"),
        ("neurology", "/njʊəˈrɒlədʒi/", "神经学", "Neurology research.", "名词"),
        ("nutrition", "/njuˈtrɪʃn/", "营养", "Proper nutrition.", "名词"),
        ("oncology", "/ɒŋˈkɒlədʒi/", "肿瘤学", "Oncology treatment.", "名词"),
        ("pathology", "/pəˈθɒlədʒi/", "病理学", "Clinical pathology.", "名词"),
        ("pharmacy", "/ˈfɑːməsi/", "药房", "Go to pharmacy.", "名词"),
        ("physiology", "/ˌfɪziˈɒlədʒi/", "生理学", "Human physiology.", "名词"),
        ("psychiatry", "/saɪˈkaɪətri/", "精神病学", "Psychiatry clinic.", "名词"),
        ("recovery", "/rɪˈkʌvəri/", "康复", "Speed up recovery.", "名词"),
        ("rehabilitation", "/ˌriːəˌbɪlɪˈteɪʃn/", "康复", "Physical rehabilitation.", "名词"),
        ("symptom", "/ˈsɪmptəm/", "症状", "Common symptom.", "名词"),
        ("therapy", "/ˈθerəpi/", "治疗", "Physical therapy.", "名词"),
        ("transplant", "/trænsˈplɑːnt/", "移植", "Organ transplant.", "名词"),
        ("vaccine", "/ˈvæksiːn/", "疫苗", "Get a vaccine.", "名词"),
        ("virus", "/ˈvaɪrəs/", "病毒", "Computer virus.", "名词"),
        ("wellness", "/ˈwelness/", "健康", "Wellness program.", "名词"),
        ("x-ray", "/ˈeks reɪ/", "X光", "Take an x-ray.", "名词"),
        ("surgery", "/ˈsɜːdʒəri/", "手术", "Undergo surgery.", "名词"),
        ("hospital", "/ˈhɒspɪtl/", "医院", "Go to hospital.", "名词"),
        ("clinic", "/ˈklɪnɪk/", "诊所", "Visit the clinic.", "名词"),
        ("patient", "/ˈpeɪʃnt/", "病人", "Treat the patient.", "名词"),
        ("doctor", "/ˈdɒktə(r)/", "医生", "See the doctor.", "名词"),
        ("nurse", "/nɜːs/", "护士", "Call the nurse.", "名词"),
        ("surgeon", "/ˈsɜːdʒən/", "外科医生", "The surgeon operated.", "名词"),
        ("specialist", "/ˈspeʃəlɪst/", "专科医生", "See a specialist.", "名词"),
        ("physician", "/fɪˈzɪʃn/", "内科医生", "Consult the physician.", "名词"),
        ("pediatrician", "/ˌpiːdiəˈtrɪʃn/", "儿科医生", "Take child to pediatrician.", "名词"),
        ("dermatologist", "/ˌdɜːməˈtɒlədʒɪst/", "皮肤科医生", "Visit dermatologist.", "名词"),
        ("ophthalmologist", "/ˌɒfθælˈmɒlədʒɪst/", "眼科医生", "See ophthalmologist.", "名词"),
        ("dentist", "/ˈdentɪst/", "牙医", "Visit the dentist.", "名词"),
        ("orthodontist", "/ˌɔːθəˈdɒntɪst/", "正畸医生", "Consult orthodontist.", "名词"),
        ("chiropractor", "/ˈkaɪrəʊpræktə(r)/", "脊椎指压治疗师", "See chiropractor.", "名词"),
        ("pharmacist", "/ˈfɑːməsɪst/", "药剂师", "Ask the pharmacist.", "名词"),
        ("paramedic", "/ˌpærəˈmedɪk/", "急救人员", "Call paramedic.", "名词"),
        ("ambulance", "/ˈæmbjələns/", "救护车", "Call an ambulance.", "名词"),
        ("emergency", "/iˈmɜːdʒənsi/", "急诊", "Go to emergency.", "名词"),
        ("intensive", "/ɪnˈtensɪv/", "加强的", "Intensive care.", "形容词"),
        ("critical", "/ˈkrɪtɪkl/", "危急的", "Critical condition.", "形容词"),
        ("chronic", "/ˈkrɒnɪk/", "慢性的", "Chronic disease.", "形容词"),
        ("acute", "/əˈkjuːt/", "急性的", "Acute pain.", "形容词"),
        
        # 环境/自然词汇 (50+)
        ("atmosphere", "/ˈætməsfɪə(r)/", "大气层", "Earth's atmosphere.", "名词"),
        ("biodiversity", "/ˌbaɪəʊdaɪˈvɜːsəti/", "生物多样性", "Protect biodiversity.", "名词"),
        ("climate", "/ˈklaɪmət/", "气候", "Climate change.", "名词"),
        ("conservation", "/ˌkɒnsəˈveɪʃn/", "保护", "Wildlife conservation.", "名词"),
        ("deforestation", "/ˌdiːˌfɒrɪˈsteɪʃn/", "森林砍伐", "Stop deforestation.", "名词"),
        ("ecosystem", "/ˈiːkəʊsɪstəm/", "生态系统", "Marine ecosystem.", "名词"),
        ("emission", "/iˈmɪʃn/", "排放", "Carbon emission.", "名词"),
        ("environment", "/ɪnˈvaɪrənmənt/", "环境", "Protect the environment.", "名词"),
        ("extinction", "/ɪkˈstɪŋkʃn/", "灭绝", "Species extinction.", "名词"),
        ("fossil", "/ˈfɒsl/", "化石", "Fossil fuels.", "名词"),
        ("geology", "/dʒiˈɒlədʒi/", "地质学", "Study geology.", "名词"),
        ("habitat", "/ˈhæbɪtæt/", "栖息地", "Natural habitat.", "名词"),
        ("hurricane", "/ˈhʌrɪkən/", "飓风", "Hurricane warning.", "名词"),
        ("irrigation", "/ˌɪrɪˈɡeɪʃn/", "灌溉", "Agricultural irrigation.", "名词"),
        ("landslide", "/ˈlændslaɪd/", "山体滑坡", "Landslide risk.", "名词"),
        ("meteorology", "/ˌmiːtiəˈrɒlədʒi/", "气象学", "Meteorology study.", "名词"),
        ("ozone", "/ˈəʊzəʊn/", "臭氧", "Ozone layer.", "名词"),
        ("pollution", "/pəˈluːʃn/", "污染", "Air pollution.", "名词"),
        ("precipitation", "/prɪˌsɪpɪˈteɪʃn/", "降水", "Annual precipitation.", "名词"),
        ("radiation", "/ˌreɪdiˈeɪʃn/", "辐射", "Solar radiation.", "名词"),
        ("recycling", "/ˌriːˈsaɪklɪŋ/", "回收", "Plastic recycling.", "名词"),
        ("renewable", "/rɪˈnjuːəbl/", "可再生的", "Renewable energy.", "形容词"),
        ("solar", "/ˈsəʊlə(r)/", "太阳的", "Solar power.", "形容词"),
        ("sustainability", "/səˌsteɪnəˈbɪləti/", "可持续性", "Environmental sustainability.", "名词"),
        ("temperature", "/ˈtemprətʃə(r)/", "温度", "High temperature.", "名词"),
        ("tornado", "/tɔːˈneɪdəʊ/", "龙卷风", "Tornado alert.", "名词"),
        ("tsunami", "/tsuːˈnɑːmi/", "海啸", "Tsunami warning.", "名词"),
        ("volcano", "/vɒlˈkeɪnəʊ/", "火山", "Active volcano.", "名词"),
        ("wildlife", "/ˈwaɪldlaɪf/", "野生动物", "Protect wildlife.", "名词"),
        ("drought", "/draʊt/", "干旱", "Severe drought.", "名词"),
        ("flood", "/flʌd/", "洪水", "Flash flood.", "名词"),
        ("earthquake", "/ˈɜːθkweɪk/", "地震", "Earthquake damage.", "名词"),
        ("avalanche", "/ˈævəlɑːnʃ/", "雪崩", "Avalanche warning.", "名词"),
        ("blizzard", "/ˈblɪzəd/", "暴风雪", "Winter blizzard.", "名词"),
        ("cyclone", "/ˈsaɪkləʊn/", "气旋", "Tropical cyclone.", "名词"),
        ("monsoon", "/ˌmɒnˈsuːn/", "季风", "Monsoon season.", "名词"),
        ("glacier", "/ˈɡlæsiə(r)/", "冰川", "Melting glacier.", "名词"),
        ("wetland", "/ˈwetlænd/", "湿地", "Protect wetland.", "名词"),
        ("rainforest", "/ˈreɪnfɒrɪst/", "雨林", "Amazon rainforest.", "名词"),
        ("desert", "/ˈdezət/", "沙漠", "Sahara desert.", "名词"),
        ("tundra", "/ˈtʌndrə/", "苔原", "Arctic tundra.", "名词"),
        ("savanna", "/səˈvænə/", "稀树草原", "African savanna.", "名词"),
        ("canyon", "/ˈkænjən/", "峡谷", "Grand Canyon.", "名词"),
        ("waterfall", "/ˈwɔːtəfɔːl/", "瀑布", "Beautiful waterfall.", "名词"),
        ("lagoon", "/ləˈɡuːn/", "泻湖", "Coastal lagoon.", "名词"),
        ("estuary", "/ˈestʃuəri/", "河口", "River estuary.", "名词"),
        ("peninsula", "/pəˈnɪnsjələ/", "半岛", "Italian peninsula.", "名词"),
        ("archipelago", "/ˌɑːkɪˈpeləɡəʊ/", "群岛", "Philippine archipelago.", "名词"),
        ("continent", "/ˈkɒntɪnənt/", "大陆", "African continent.", "名词"),
        
        # 法律/政治词汇 (45+)
        ("amendment", "/əˈmendmənt/", "修正案", "Constitutional amendment.", "名词"),
        ("ballot", "/ˈbælət/", "选票", "Cast a ballot.", "名词"),
        ("cabinet", "/ˈkæbɪnət/", "内阁", "Cabinet meeting.", "名词"),
        ("campaign", "/kæmˈpeɪn/", "竞选活动", "Election campaign.", "名词"),
        ("candidate", "/ˈkændɪdət/", "候选人", "Presidential candidate.", "名词"),
        ("constitution", "/ˌkɒnstɪˈtjuːʃn/", "宪法", "US Constitution.", "名词"),
        ("democracy", "/dɪˈmɒkrəsi/", "民主", "Representative democracy.", "名词"),
        ("diplomacy", "/dɪˈpləʊməsi/", "外交", "International diplomacy.", "名词"),
        ("election", "/iˈlekʃn/", "选举", "General election.", "名词"),
        ("government", "/ˈɡʌvənmənt/", "政府", "Federal government.", "名词"),
        ("legislation", "/ˌledʒɪsˈleɪʃn/", "立法", "Pass legislation.", "名词"),
        ("legislator", "/ˈledʒɪsleɪtə(r)/", "立法者", "State legislator.", "名词"),
        ("ministry", "/ˈmɪnɪstri/", "部", "Foreign ministry.", "名词"),
        ("opposition", "/ˌɒpəˈzɪʃn/", "反对党", "Opposition party.", "名词"),
        ("parliament", "/ˈpɑːləmənt/", "议会", "European Parliament.", "名词"),
        ("policy", "/ˈpɒləsi/", "政策", "Foreign policy.", "名词"),
        ("politician", "/ˌpɒləˈtɪʃn/", "政治家", "Local politician.", "名词"),
        ("president", "/ˈprezɪdənt/", "总统", "The president spoke.", "名词"),
        ("republic", "/rɪˈpʌblɪk/", "共和国", "Federal republic.", "名词"),
        ("senate", "/ˈsenət/", "参议院", "US Senate.", "名词"),
        ("treaty", "/ˈtriːti/", "条约", "Peace treaty.", "名词"),
        ("voter", "/ˈvəʊtə(r)/", "选民", "Registered voter.", "名词"),
        ("accusation", "/ˌækjuˈzeɪʃn/", "指控", "Criminal accusation.", "名词"),
        ("arrest", "/əˈrest/", "逮捕", "Make an arrest.", "名词"),
        ("attorney", "/əˈtɜːni/", "律师", "Defense attorney.", "名词"),
        ("conviction", "/kənˈvɪkʃn/", "定罪", "Criminal conviction.", "名词"),
        ("court", "/kɔːt/", "法院", "Supreme Court.", "名词"),
        ("crime", "/kraɪm/", "犯罪", "Commit a crime.", "名词"),
        ("defendant", "/dɪˈfendənt/", "被告", "The defendant pleaded.", "名词"),
        ("evidence", "/ˈevɪdəns/", "证据", "Present evidence.", "名词"),
        ("guilty", "/ˈɡɪlti/", "有罪的", "Found guilty.", "形容词"),
        ("innocent", "/ˈɪnəsnt/", "无辜的", "Prove innocent.", "形容词"),
        ("judge", "/dʒʌdʒ/", "法官", "The judge ruled.", "名词"),
        ("jury", "/ˈdʒʊəri/", "陪审团", "Jury verdict.", "名词"),
        ("lawyer", "/ˈlɔːjə(r)/", "律师", "Hire a lawyer.", "名词"),
        ("penalty", "/ˈpenəlti/", "刑罚", "Death penalty.", "名词"),
        ("plaintiff", "/ˈpleɪntɪf/", "原告", "The plaintiff sued.", "名词"),
        ("prosecutor", "/ˈprɒsɪkjuːtə(r)/", "检察官", "Federal prosecutor.", "名词"),
        ("sentence", "/ˈsentəns/", "判决", "Serve sentence.", "名词"),
        ("testimony", "/ˈtestɪməni/", "证词", "Give testimony.", "名词"),
        ("verdict", "/ˈvɜːdɪkt/", "裁决", "Jury verdict.", "名词"),
        ("witness", "/ˈwɪtnəs/", "证人", "Call a witness.", "名词"),
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
    expand_vocabulary_to_5000_part2()
