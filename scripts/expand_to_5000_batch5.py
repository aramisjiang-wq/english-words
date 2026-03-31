import sqlite3

def expand_to_5000_batch5():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    new_words = [
        # 科学研究类
        {
            "english": "astronomy", "phonetic": "/əˈstrɑːnəmi/", "chinese": "n. 天文学", 
            "example": "Astronomy studies stars and planets.", "category": "科学研究"
        },
        {
            "english": "geology", "phonetic": "/dʒiˈɑːlədʒi/", "chinese": "n. 地质学", 
            "example": "Geology studies the earth.", "category": "科学研究"
        },
        {
            "english": "ecology", "phonetic": "/iˈkɑːlədʒi/", "chinese": "n. 生态学", 
            "example": "Ecology studies ecosystems.", "category": "科学研究"
        },
        {
            "english": "neuroscience", "phonetic": "/ˌnʊroʊˈsaɪəns/", "chinese": "n. 神经科学", 
            "example": "Neuroscience studies the brain.", "category": "科学研究"
        },
        {
            "english": "genetics", "phonetic": "/dʒəˈnetɪks/", "chinese": "n. 遗传学", 
            "example": "Genetics studies heredity.", "category": "科学研究"
        },
        {
            "english": "biochemistry", "phonetic": "/ˌbaɪoʊˈkemɪstri/", "chinese": "n. 生物化学", 
            "example": "Biochemistry studies chemical processes.", "category": "科学研究"
        },
        {
            "english": "microbiology", "phonetic": "/ˌmaɪkroʊbaɪˈɑːlədʒi/", "chinese": "n. 微生物学", 
            "example": "Microbiology studies microorganisms.", "category": "科学研究"
        },
        {
            "english": "quantum", "phonetic": "/ˈkwɑːntəm/", "chinese": "n. 量子", 
            "example": "Quantum physics is complex.", "category": "科学研究"
        },
        {
            "english": "hypothesis", "phonetic": "/haɪˈpɑːθəsɪs/", "chinese": "n. 假设", 
            "example": "Test the hypothesis.", "category": "科学研究"
        },
        {
            "english": "experiment", "phonetic": "/ɪkˈsperɪmənt/", "chinese": "n. 实验", 
            "example": "Conduct an experiment.", "category": "科学研究"
        },
        {
            "english": "conclusion", "phonetic": "/kənˈkluːʒn/", "chinese": "n. 结论", 
            "example": "Draw a conclusion.", "category": "科学研究"
        },
        {
            "english": "methodology", "phonetic": "/ˌmeθəˈdɑːlədʒi/", "chinese": "n. 方法论", 
            "example": "Use proper methodology.", "category": "科学研究"
        },
        {
            "english": "analysis", "phonetic": "/əˈnæləsɪs/", "chinese": "n. 分析", 
            "example": "Perform data analysis.", "category": "科学研究"
        },
        {
            "english": "synthesis", "phonetic": "/ˈsɪnθəsɪs/", "chinese": "n. 合成", 
            "example": "Chemical synthesis.", "category": "科学研究"
        },
        {
            "english": "innovation", "phonetic": "/ˌɪnəˈveɪʃn/", "chinese": "n. 创新", 
            "example": "Drive innovation.", "category": "科学研究"
        },
        {
            "english": "discovery", "phonetic": "/dɪsˈkʌvəri/", "chinese": "n. 发现", 
            "example": "Make a discovery.", "category": "科学研究"
        },
        {
            "english": "invention", "phonetic": "/ɪnˈvenʃn/", "chinese": "n. 发明", 
            "example": "The invention changed lives.", "category": "科学研究"
        },
        {
            "english": "breakthrough", "phonetic": "/ˈbreɪkθruː/", "chinese": "n. 突破", 
            "example": "Achieve a breakthrough.", "category": "科学研究"
        },
        {
            "english": "researcher", "phonetic": "/rɪˈsɜːrtʃər/", "chinese": "n. 研究员", 
            "example": "The researcher published.", "category": "科学研究"
        },
        {
            "english": "scientist", "phonetic": "/ˈsaɪəntɪst/", "chinese": "n. 科学家", 
            "example": "The scientist discovered.", "category": "科学研究"
        },
        # 商业管理类
        {
            "english": "entrepreneur", "phonetic": "/ˌɑːntrəprəˈnɜːr/", "chinese": "n. 企业家", 
            "example": "The entrepreneur started.", "category": "商业管理"
        },
        {
            "english": "investment", "phonetic": "/ɪnˈvestmənt/", "chinese": "n. 投资", 
            "example": "Make an investment.", "category": "商业管理"
        },
        {
            "english": "dividend", "phonetic": "/ˈdɪvɪdend/", "chinese": "n. 股息", 
            "example": "Receive dividends.", "category": "商业管理"
        },
        {
            "english": "portfolio", "phonetic": "/pɔːrtˈfoʊlioʊ/", "chinese": "n. 投资组合", 
            "example": "Manage the portfolio.", "category": "商业管理"
        },
        {
            "english": "revenue", "phonetic": "/ˈrevənuː/", "chinese": "n. 收入", 
            "example": "Increase revenue.", "category": "商业管理"
        },
        {
            "english": "profitability", "phonetic": "/ˌprɑːfɪtəˈbɪləti/", "chinese": "n. 盈利能力", 
            "example": "Improve profitability.", "category": "商业管理"
        },
        {
            "english": "merger", "phonetic": "/ˈmɜːrdʒər/", "chinese": "n. 合并", 
            "example": "The merger was approved.", "category": "商业管理"
        },
        {
            "english": "acquisition", "phonetic": "/ˌækwɪˈzɪʃn/", "chinese": "n. 收购", 
            "example": "Complete the acquisition.", "category": "商业管理"
        },
        {
            "english": "stakeholder", "phonetic": "/ˈsteɪkhoʊldər/", "chinese": "n. 利益相关者", 
            "example": "Engage stakeholders.", "category": "商业管理"
        },
        {
            "english": "shareholder", "phonetic": "/ˈʃerhoʊldər/", "chinese": "n. 股东", 
            "example": "The shareholder voted.", "category": "商业管理"
        },
        {
            "english": "leadership", "phonetic": "/ˈliːdərʃɪp/", "chinese": "n. 领导力", 
            "example": "Show leadership.", "category": "商业管理"
        },
        {
            "english": "management", "phonetic": "/ˈmænɪdʒmənt/", "chinese": "n. 管理", 
            "example": "Effective management.", "category": "商业管理"
        },
        {
            "english": "strategy", "phonetic": "/ˈstrætədʒi/", "chinese": "n. 战略", 
            "example": "Develop a strategy.", "category": "商业管理"
        },
        {
            "english": "competitive", "phonetic": "/kəmˈpetətɪv/", "chinese": "adj. 竞争的", 
            "example": "Stay competitive.", "category": "商业管理"
        },
        {
            "english": "advantage", "phonetic": "/ədˈvæntɪdʒ/", "chinese": "n. 优势", 
            "example": "Gain an advantage.", "category": "商业管理"
        },
        {
            "english": "disadvantage", "phonetic": "/ˌdɪsədˈvæntɪdʒ/", "chinese": "n. 劣势", 
            "example": "Overcome disadvantages.", "category": "商业管理"
        },
        {
            "english": "negotiation", "phonetic": "/nɪˌɡoʊʃiˈeɪʃn/", "chinese": "n. 谈判", 
            "example": "Enter negotiation.", "category": "商业管理"
        },
        {
            "english": "contract", "phonetic": "/ˈkɑːntrækt/", "chinese": "n. 合同", 
            "example": "Sign the contract.", "category": "商业管理"
        },
        {
            "english": "agreement", "phonetic": "/əˈɡriːmənt/", "chinese": "n. 协议", 
            "example": "Reach an agreement.", "category": "商业管理"
        },
        # 法律政治类
        {
            "english": "legislation", "phonetic": "/ˌledʒɪsˈleɪʃn/", "chinese": "n. 立法", 
            "example": "Pass legislation.", "category": "法律政治"
        },
        {
            "english": "regulation", "phonetic": "/ˌreɡjəˈleɪʃn/", "chinese": "n. 法规", 
            "example": "Follow regulations.", "category": "法律政治"
        },
        {
            "english": "constitution", "phonetic": "/ˌkɑːnstɪˈtuːʃn/", "chinese": "n. 宪法", 
            "example": "The constitution protects.", "category": "法律政治"
        },
        {
            "english": "amendment", "phonetic": "/əˈmendmənt/", "chinese": "n. 修正案", 
            "example": "Propose an amendment.", "category": "法律政治"
        },
        {
            "english": "jurisdiction", "phonetic": "/ˌdʒʊrɪsˈdɪkʃn/", "chinese": "n. 管辖权", 
            "example": "Claim jurisdiction.", "category": "法律政治"
        },
        {
            "english": "litigation", "phonetic": "/ˌlɪtɪˈɡeɪʃn/", "chinese": "n. 诉讼", 
            "example": "Enter litigation.", "category": "法律政治"
        },
        {
            "english": "verdict", "phonetic": "/ˈvɜːrdɪkt/", "chinese": "n. 裁决", 
            "example": "The verdict was read.", "category": "法律政治"
        },
        {
            "english": "sentence", "phonetic": "/ˈsentəns/", "chinese": "n. 判决", 
            "example": "The sentence was given.", "category": "法律政治"
        },
        {
            "english": "prosecution", "phonetic": "/ˌprɑːsɪˈkjuːʃn/", "chinese": "n. 起诉", 
            "example": "The prosecution argued.", "category": "法律政治"
        },
        {
            "english": "defense", "phonetic": "/dɪˈfens/", "chinese": "n. 辩护", 
            "example": "The defense presented.", "category": "法律政治"
        },
        {
            "english": "attorney", "phonetic": "/əˈtɜːrni/", "chinese": "n. 律师", 
            "example": "Consult the attorney.", "category": "法律政治"
        },
        {
            "english": "counsel", "phonetic": "/ˈkaʊnsəl/", "chinese": "n. 法律顾问", 
            "example": "Seek counsel.", "category": "法律政治"
        },
        {
            "english": "democracy", "phonetic": "/dɪˈmɑːkrəsi/", "chinese": "n. 民主", 
            "example": "Support democracy.", "category": "法律政治"
        },
        {
            "english": "republic", "phonetic": "/rɪˈpʌblɪk/", "chinese": "n. 共和国", 
            "example": "The republic stands.", "category": "法律政治"
        },
        {
            "english": "election", "phonetic": "/ɪˈlekʃn/", "chinese": "n. 选举", 
            "example": "Win the election.", "category": "法律政治"
        },
        {
            "english": "campaign", "phonetic": "/kæmˈpeɪn/", "chinese": "n. 竞选活动", 
            "example": "Run a campaign.", "category": "法律政治"
        },
        {
            "english": "candidate", "phonetic": "/ˈkændɪdeɪt/", "chinese": "n. 候选人", 
            "example": "The candidate spoke.", "category": "法律政治"
        },
        {
            "english": "policy", "phonetic": "/ˈpɑːləsi/", "chinese": "n. 政策", 
            "example": "Implement policy.", "category": "法律政治"
        },
        {
            "english": "administration", "phonetic": "/ədˌmɪnɪˈstreɪʃn/", "chinese": "n. 行政", 
            "example": "The administration works.", "category": "法律政治"
        },
        # 医疗健康类
        {
            "english": "diagnosis", "phonetic": "/ˌdaɪəɡˈnoʊsɪs/", "chinese": "n. 诊断", 
            "example": "Make a diagnosis.", "category": "医疗健康"
        },
        {
            "english": "symptom", "phonetic": "/ˈsɪmptəm/", "chinese": "n. 症状", 
            "example": "Identify symptoms.", "category": "医疗健康"
        },
        {
            "english": "treatment", "phonetic": "/ˈtriːtmənt/", "chinese": "n. 治疗", 
            "example": "Provide treatment.", "category": "医疗健康"
        },
        {
            "english": "therapy", "phonetic": "/ˈθerəpi/", "chinese": "n. 疗法", 
            "example": "Start therapy.", "category": "医疗健康"
        },
        {
            "english": "medication", "phonetic": "/ˌmedɪˈkeɪʃn/", "chinese": "n. 药物", 
            "example": "Take medication.", "category": "医疗健康"
        },
        {
            "english": "prescription", "phonetic": "/prɪˈskrɪpʃn/", "chinese": "n. 处方", 
            "example": "Fill the prescription.", "category": "医疗健康"
        },
        {
            "english": "surgery", "phonetic": "/ˈsɜːrdʒəri/", "chinese": "n. 手术", 
            "example": "Perform surgery.", "category": "医疗健康"
        },
        {
            "english": "recovery", "phonetic": "/rɪˈkʌvəri/", "chinese": "n. 康复", 
            "example": "Speed recovery.", "category": "医疗健康"
        },
        {
            "english": "rehabilitation", "phonetic": "/ˌriːəˌbɪlɪˈteɪʃn/", "chinese": "n. 康复治疗", 
            "example": "Enter rehabilitation.", "category": "医疗健康"
        },
        {
            "english": "prevention", "phonetic": "/prɪˈvenʃn/", "chinese": "n. 预防", 
            "example": "Focus on prevention.", "category": "医疗健康"
        },
        {
            "english": "vaccination", "phonetic": "/ˌvæksɪˈneɪʃn/", "chinese": "n. 疫苗接种", 
            "example": "Get vaccination.", "category": "医疗健康"
        },
        {
            "english": "immunity", "phonetic": "/ɪˈmjuːnəti/", "chinese": "n. 免疫力", 
            "example": "Build immunity.", "category": "医疗健康"
        },
        {
            "english": "infection", "phonetic": "/ɪnˈfekʃn/", "chinese": "n. 感染", 
            "example": "Treat the infection.", "category": "医疗健康"
        },
        {
            "english": "disease", "phonetic": "/dɪˈziːz/", "chinese": "n. 疾病", 
            "example": "Prevent disease.", "category": "医疗健康"
        },
        {
            "english": "condition", "phonetic": "/kənˈdɪʃn/", "chinese": "n. 状况", 
            "example": "The condition improved.", "category": "医疗健康"
        },
        {
            "english": "specialist", "phonetic": "/ˈspeʃəlɪst/", "chinese": "n. 专家", 
            "example": "See a specialist.", "category": "医疗健康"
        },
        {
            "english": "physician", "phonetic": "/fɪˈzɪʃn/", "chinese": "n. 医师", 
            "example": "Consult the physician.", "category": "医疗健康"
        },
        {
            "english": "surgeon", "phonetic": "/ˈsɜːrdʒən/", "chinese": "n. 外科医生", 
            "example": "The surgeon operated.", "category": "医疗健康"
        },
        {
            "english": "nurse", "phonetic": "/nɜːrs/", "chinese": "n. 护士", 
            "example": "The nurse helped.", "category": "医疗健康"
        },
        {
            "english": "hospital", "phonetic": "/ˈhɑːspɪtl/", "chinese": "n. 医院", 
            "example": "Go to the hospital.", "category": "医疗健康"
        },
        {
            "english": "clinic", "phonetic": "/ˈklɪnɪk/", "chinese": "n. 诊所", 
            "example": "Visit the clinic.", "category": "医疗健康"
        },
        # 教育学习类
        {
            "english": "curriculum", "phonetic": "/kəˈrɪkjələm/", "chinese": "n. 课程", 
            "example": "Design the curriculum.", "category": "教育学习"
        },
        {
            "english": "syllabus", "phonetic": "/ˈsɪləbəs/", "chinese": "n. 教学大纲", 
            "example": "Follow the syllabus.", "category": "教育学习"
        },
        {
            "english": "assignment", "phonetic": "/əˈsaɪnmənt/", "chinese": "n. 作业", 
            "example": "Complete the assignment.", "category": "教育学习"
        },
        {
            "english": "examination", "phonetic": "/ɪɡˌzæmɪˈneɪʃn/", "chinese": "n. 考试", 
            "example": "Pass the examination.", "category": "教育学习"
        },
        {
            "english": "qualification", "phonetic": "/ˌkwɑːlɪfɪˈkeɪʃn/", "chinese": "n. 资格", 
            "example": "Gain qualification.", "category": "教育学习"
        },
        {
            "english": "certification", "phonetic": "/ˌsɜːrtɪfɪˈkeɪʃn/", "chinese": "n. 证书", 
            "example": "Obtain certification.", "category": "教育学习"
        },
        {
            "english": "degree", "phonetic": "/dɪˈɡriː/", "chinese": "n. 学位", 
            "example": "Earn a degree.", "category": "教育学习"
        },
        {
            "english": "diploma", "phonetic": "/dɪˈploʊmə/", "chinese": "n. 文凭", 
            "example": "Receive the diploma.", "category": "教育学习"
        },
        {
            "english": "scholarship", "phonetic": "/ˈskɑːlərʃɪp/", "chinese": "n. 奖学金", 
            "example": "Win a scholarship.", "category": "教育学习"
        },
        {
            "english": "tuition", "phonetic": "/tuːˈɪʃn/", "chinese": "n. 学费", 
            "example": "Pay tuition.", "category": "教育学习"
        },
        {
            "english": "enrollment", "phonetic": "/ɪnˈroʊlmənt/", "chinese": "n. 入学", 
            "example": "Complete enrollment.", "category": "教育学习"
        },
        {
            "english": "graduation", "phonetic": "/ˌɡrædʒuˈeɪʃn/", "chinese": "n. 毕业", 
            "example": "Attend graduation.", "category": "教育学习"
        },
        {
            "english": "institution", "phonetic": "/ˌɪnstɪˈtuːʃn/", "chinese": "n. 机构", 
            "example": "The institution educates.", "category": "教育学习"
        },
        {
            "english": "university", "phonetic": "/ˌjuːnɪˈvɜːrsəti/", "chinese": "n. 大学", 
            "example": "Attend university.", "category": "教育学习"
        },
        {
            "english": "college", "phonetic": "/ˈkɑːlɪdʒ/", "chinese": "n. 学院", 
            "example": "Go to college.", "category": "教育学习"
        },
        {
            "english": "professor", "phonetic": "/prəˈfesər/", "chinese": "n. 教授", 
            "example": "The professor taught.", "category": "教育学习"
        },
        {
            "english": "instructor", "phonetic": "/ɪnˈstrʌktər/", "chinese": "n. 讲师", 
            "example": "The instructor guided.", "category": "教育学习"
        },
        {
            "english": "student", "phonetic": "/ˈstuːdnt/", "chinese": "n. 学生", 
            "example": "The student studied.", "category": "教育学习"
        },
        {
            "english": "knowledge", "phonetic": "/ˈnɑːlɪdʒ/", "chinese": "n. 知识", 
            "example": "Gain knowledge.", "category": "教育学习"
        },
        {
            "english": "comprehension", "phonetic": "/ˌkɑːmprɪˈhenʃn/", "chinese": "n. 理解", 
            "example": "Test comprehension.", "category": "教育学习"
        },
        # 技术创新类
        {
            "english": "algorithm", "phonetic": "/ˈælɡərɪðəm/", "chinese": "n. 算法", 
            "example": "Design the algorithm.", "category": "技术创新"
        },
        {
            "english": "programming", "phonetic": "/ˈproʊɡræmɪŋ/", "chinese": "n. 编程", 
            "example": "Learn programming.", "category": "技术创新"
        },
        {
            "english": "database", "phonetic": "/ˈdeɪtəbeɪs/", "chinese": "n. 数据库", 
            "example": "Query the database.", "category": "技术创新"
        },
        {
            "english": "interface", "phonetic": "/ˈɪntərfeɪs/", "chinese": "n. 接口", 
            "example": "Design the interface.", "category": "技术创新"
        },
        {
            "english": "platform", "phonetic": "/ˈplætfɔːrm/", "chinese": "n. 平台", 
            "example": "Build the platform.", "category": "技术创新"
        },
        {
            "english": "application", "phonetic": "/ˌæplɪˈkeɪʃn/", "chinese": "n. 应用程序", 
            "example": "Develop the application.", "category": "技术创新"
        },
        {
            "english": "software", "phonetic": "/ˈsɔːftwer/", "chinese": "n. 软件", 
            "example": "Install the software.", "category": "技术创新"
        },
        {
            "english": "hardware", "phonetic": "/ˈhɑːrdwer/", "chinese": "n. 硬件", 
            "example": "Upgrade the hardware.", "category": "技术创新"
        },
        {
            "english": "network", "phonetic": "/ˈnetwɜːrk/", "chinese": "n. 网络", 
            "example": "Connect to the network.", "category": "技术创新"
        },
        {
            "english": "wireless", "phonetic": "/ˈwaɪərləs/", "chinese": "adj. 无线的", 
            "example": "Use wireless connection.", "category": "技术创新"
        },
        {
            "english": "encryption", "phonetic": "/ɪnˈkrɪpʃn/", "chinese": "n. 加密", 
            "example": "Apply encryption.", "category": "技术创新"
        },
        {
            "english": "security", "phonetic": "/sɪˈkjʊrəti/", "chinese": "n. 安全", 
            "example": "Ensure security.", "category": "技术创新"
        },
        {
            "english": "authentication", "phonetic": "/ɔːˌθentɪˈkeɪʃn/", "chinese": "n. 认证", 
            "example": "Complete authentication.", "category": "技术创新"
        },
        {
            "english": "authorization", "phonetic": "/ˌɔːθərəˈzeɪʃn/", "chinese": "n. 授权", 
            "example": "Grant authorization.", "category": "技术创新"
        },
        {
            "english": "virtual", "phonetic": "/ˈvɜːrtʃuəl/", "chinese": "adj. 虚拟的", 
            "example": "Virtual reality.", "category": "技术创新"
        },
        {
            "english": "digital", "phonetic": "/ˈdɪdʒɪtl/", "chinese": "adj. 数字的", 
            "example": "Digital transformation.", "category": "技术创新"
        },
        {
            "english": "electronic", "phonetic": "/ɪˌlekˈtrɑːnɪk/", "chinese": "adj. 电子的", 
            "example": "Electronic device.", "category": "技术创新"
        },
        {
            "english": "automated", "phonetic": "/ˈɔːtəmeɪtɪd/", "chinese": "adj. 自动化的", 
            "example": "Automated system.", "category": "技术创新"
        },
        {
            "english": "robotic", "phonetic": "/roʊˈbɑːtɪk/", "chinese": "adj. 机器人的", 
            "example": "Robotic automation.", "category": "技术创新"
        },
        {
            "english": "artificial", "phonetic": "/ˌɑːrtɪˈfɪʃl/", "chinese": "adj. 人工的", 
            "example": "Artificial intelligence.", "category": "技术创新"
        },
        # 自然地理类
        {
            "english": "mountain", "phonetic": "/ˈmaʊntən/", "chinese": "n. 山", 
            "example": "Climb the mountain.", "category": "自然地理"
        },
        {
            "english": "valley", "phonetic": "/ˈvæli/", "chinese": "n. 山谷", 
            "example": "The valley is green.", "category": "自然地理"
        },
        {
            "english": "canyon", "phonetic": "/ˈkænjən/", "chinese": "n. 峡谷", 
            "example": "Visit the canyon.", "category": "自然地理"
        },
        {
            "english": "plateau", "phonetic": "/plæˈtoʊ/", "chinese": "n. 高原", 
            "example": "The plateau is high.", "category": "自然地理"
        },
        {
            "english": "desert", "phonetic": "/ˈdezərt/", "chinese": "n. 沙漠", 
            "example": "Cross the desert.", "category": "自然地理"
        },
        {
            "english": "forest", "phonetic": "/ˈfɔːrɪst/", "chinese": "n. 森林", 
            "example": "Explore the forest.", "category": "自然地理"
        },
        {
            "english": "jungle", "phonetic": "/ˈdʒʌŋɡl/", "chinese": "n. 丛林", 
            "example": "The jungle is dense.", "category": "自然地理"
        },
        {
            "english": "grassland", "phonetic": "/ˈɡræslænd/", "chinese": "n. 草原", 
            "example": "The grassland is vast.", "category": "自然地理"
        },
        {
            "english": "wetland", "phonetic": "/ˈwetlænd/", "chinese": "n. 湿地", 
            "example": "Protect the wetland.", "category": "自然地理"
        },
        {
            "english": "coastline", "phonetic": "/ˈkoʊstlaɪn/", "chinese": "n. 海岸线", 
            "example": "Follow the coastline.", "category": "自然地理"
        },
        {
            "english": "peninsula", "phonetic": "/pəˈnɪnsələ/", "chinese": "n. 半岛", 
            "example": "The peninsula extends.", "category": "自然地理"
        },
        {
            "english": "island", "phonetic": "/ˈaɪlənd/", "chinese": "n. 岛屿", 
            "example": "Visit the island.", "category": "自然地理"
        },
        {
            "english": "archipelago", "phonetic": "/ˌɑːrkəˈpeləɡoʊ/", "chinese": "n. 群岛", 
            "example": "The archipelago is beautiful.", "category": "自然地理"
        },
        {
            "english": "volcano", "phonetic": "/vɑːlˈkeɪnoʊ/", "chinese": "n. 火山", 
            "example": "The volcano erupted.", "category": "自然地理"
        },
        {
            "english": "earthquake", "phonetic": "/ˈɜːrθkweɪk/", "chinese": "n. 地震", 
            "example": "The earthquake struck.", "category": "自然地理"
        },
        {
            "english": "tsunami", "phonetic": "/tsuːˈnɑːmi/", "chinese": "n. 海啸", 
            "example": "The tsunami hit.", "category": "自然地理"
        },
        {
            "english": "hurricane", "phonetic": "/ˈhʌrɪkeɪn/", "chinese": "n. 飓风", 
            "example": "The hurricane passed.", "category": "自然地理"
        },
        {
            "english": "tornado", "phonetic": "/tɔːrˈneɪdoʊ/", "chinese": "n. 龙卷风", 
            "example": "The tornado formed.", "category": "自然地理"
        },
        {
            "english": "blizzard", "phonetic": "/ˈblɪzərd/", "chinese": "n. 暴风雪", 
            "example": "The blizzard came.", "category": "自然地理"
        },
        {
            "english": "drought", "phonetic": "/draʊt/", "chinese": "n. 干旱", 
            "example": "The drought continued.", "category": "自然地理"
        },
        # 社会文化类
        {
            "english": "tradition", "phonetic": "/trəˈdɪʃn/", "chinese": "n. 传统", 
            "example": "Keep the tradition.", "category": "社会文化"
        },
        {
            "english": "custom", "phonetic": "/ˈkʌstəm/", "chinese": "n. 习俗", 
            "example": "Follow the custom.", "category": "社会文化"
        },
        {
            "english": "ritual", "phonetic": "/ˈrɪtʃuəl/", "chinese": "n. 仪式", 
            "example": "Perform the ritual.", "category": "社会文化"
        },
        {
            "english": "ceremony", "phonetic": "/ˈserəmoʊni/", "chinese": "n. 典礼", 
            "example": "Attend the ceremony.", "category": "社会文化"
        },
        {
            "english": "festival", "phonetic": "/ˈfestɪvl/", "chinese": "n. 节日", 
            "example": "Celebrate the festival.", "category": "社会文化"
        },
        {
            "english": "celebration", "phonetic": "/ˌselɪˈbreɪʃn/", "chinese": "n. 庆祝", 
            "example": "Join the celebration.", "category": "社会文化"
        },
        {
            "english": "community", "phonetic": "/kəˈmjuːnəti/", "chinese": "n. 社区", 
            "example": "Serve the community.", "category": "社会文化"
        },
        {
            "english": "society", "phonetic": "/səˈsaɪəti/", "chinese": "n. 社会", 
            "example": "Build society.", "category": "社会文化"
        },
        {
            "english": "culture", "phonetic": "/ˈkʌltʃər/", "chinese": "n. 文化", 
            "example": "Respect the culture.", "category": "社会文化"
        },
        {
            "english": "heritage", "phonetic": "/ˈherɪtɪdʒ/", "chinese": "n. 遗产", 
            "example": "Preserve heritage.", "category": "社会文化"
        },
        {
            "english": "monument", "phonetic": "/ˈmɑːnjumənt/", "chinese": "n. 纪念碑", 
            "example": "Visit the monument.", "category": "社会文化"
        },
        {
            "english": "landmark", "phonetic": "/ˈlændmɑːrk/", "chinese": "n. 地标", 
            "example": "The landmark is famous.", "category": "社会文化"
        },
        {
            "english": "architecture", "phonetic": "/ˌɑːrkɪˈtektʃər/", "chinese": "n. 建筑", 
            "example": "Admire the architecture.", "category": "社会文化"
        },
        {
            "english": "sculpture", "phonetic": "/ˈskʌlptʃər/", "chinese": "n. 雕塑", 
            "example": "Create sculpture.", "category": "社会文化"
        },
        {
            "english": "painting", "phonetic": "/ˈpeɪntɪŋ/", "chinese": "n. 绘画", 
            "example": "The painting is beautiful.", "category": "社会文化"
        },
        {
            "english": "literature", "phonetic": "/ˈlɪtrətʃər/", "chinese": "n. 文学", 
            "example": "Read literature.", "category": "社会文化"
        },
        {
            "english": "poetry", "phonetic": "/ˈpoʊətri/", "chinese": "n. 诗歌", 
            "example": "Write poetry.", "category": "社会文化"
        },
        {
            "english": "music", "phonetic": "/ˈmjuːzɪk/", "chinese": "n. 音乐", 
            "example": "Listen to music.", "category": "社会文化"
        },
        {
            "english": "dance", "phonetic": "/dæns/", "chinese": "n. 舞蹈", 
            "example": "Learn to dance.", "category": "社会文化"
        },
        {
            "english": "theater", "phonetic": "/ˈθiːətər/", "chinese": "n. 剧院", 
            "example": "Go to the theater.", "category": "社会文化"
        },
        # 旅行交通类
        {
            "english": "destination", "phonetic": "/ˌdestɪˈneɪʃn/", "chinese": "n. 目的地", 
            "example": "Reach the destination.", "category": "旅行交通"
        },
        {
            "english": "itinerary", "phonetic": "/aɪˈtɪnəreri/", "chinese": "n. 行程", 
            "example": "Plan the itinerary.", "category": "旅行交通"
        },
        {
            "english": "reservation", "phonetic": "/ˌrezərˈveɪʃn/", "chinese": "n. 预订", 
            "example": "Make a reservation.", "category": "旅行交通"
        },
        {
            "english": "accommodation", "phonetic": "/əˌkɑːməˈdeɪʃn/", "chinese": "n. 住宿", 
            "example": "Find accommodation.", "category": "旅行交通"
        },
        {
            "english": "transportation", "phonetic": "/ˌtrænspɔːrˈteɪʃn/", "chinese": "n. 交通", 
            "example": "Use transportation.", "category": "旅行交通"
        },
        {
            "english": "vehicle", "phonetic": "/ˈviːhɪkl/", "chinese": "n. 车辆", 
            "example": "Drive the vehicle.", "category": "旅行交通"
        },
        {
            "english": "airplane", "phonetic": "/ˈerpleɪn/", "chinese": "n. 飞机", 
            "example": "Board the airplane.", "category": "旅行交通"
        },
        {
            "english": "train", "phonetic": "/treɪn/", "chinese": "n. 火车", 
            "example": "Take the train.", "category": "旅行交通"
        },
        {
            "english": "bus", "phonetic": "/bʌs/", "chinese": "n. 公交车", 
            "example": "Ride the bus.", "category": "旅行交通"
        },
        {
            "english": "subway", "phonetic": "/ˈsʌbweɪ/", "chinese": "n. 地铁", 
            "example": "Take the subway.", "category": "旅行交通"
        },
        {
            "english": "taxi", "phonetic": "/ˈtæksi/", "chinese": "n. 出租车", 
            "example": "Call a taxi.", "category": "旅行交通"
        },
        {
            "english": "bicycle", "phonetic": "/ˈbaɪsɪkl/", "chinese": "n. 自行车", 
            "example": "Ride the bicycle.", "category": "旅行交通"
        },
        {
            "english": "motorcycle", "phonetic": "/ˈmoʊtərsaɪkl/", "chinese": "n. 摩托车", 
            "example": "Drive the motorcycle.", "category": "旅行交通"
        },
        {
            "english": "ship", "phonetic": "/ʃɪp/", "chinese": "n. 船", 
            "example": "Board the ship.", "category": "旅行交通"
        },
        {
            "english": "ferry", "phonetic": "/ˈferi/", "chinese": "n. 渡轮", 
            "example": "Take the ferry.", "category": "旅行交通"
        },
        {
            "english": "cruise", "phonetic": "/kruːz/", "chinese": "n. 巡航", 
            "example": "Go on a cruise.", "category": "旅行交通"
        },
        {
            "english": "passenger", "phonetic": "/ˈpæsɪndʒər/", "chinese": "n. 乘客", 
            "example": "The passenger waited.", "category": "旅行交通"
        },
        {
            "english": "driver", "phonetic": "/ˈdraɪvər/", "chinese": "n. 司机", 
            "example": "The driver drove.", "category": "旅行交通"
        },
        {
            "english": "pilot", "phonetic": "/ˈpaɪlət/", "chinese": "n. 飞行员", 
            "example": "The pilot flew.", "category": "旅行交通"
        },
        {
            "english": "captain", "phonetic": "/ˈkæptɪn/", "chinese": "n. 船长", 
            "example": "The captain commanded.", "category": "旅行交通"
        },
        # 食物烹饪类
        {
            "english": "ingredient", "phonetic": "/ɪnˈɡriːdiənt/", "chinese": "n. 原料", 
            "example": "Mix the ingredients.", "category": "食物烹饪"
        },
        {
            "english": "recipe", "phonetic": "/ˈresəpi/", "chinese": "n. 食谱", 
            "example": "Follow the recipe.", "category": "食物烹饪"
        },
        {
            "english": "cuisine", "phonetic": "/kwɪˈziːn/", "chinese": "n. 烹饪", 
            "example": "Enjoy the cuisine.", "category": "食物烹饪"
        },
        {
            "english": "delicious", "phonetic": "/dɪˈlɪʃəs/", "chinese": "adj. 美味的", 
            "example": "The food is delicious.", "category": "食物烹饪"
        },
        {
            "english": "flavor", "phonetic": "/ˈfleɪvər/", "chinese": "n. 味道", 
            "example": "Enjoy the flavor.", "category": "食物烹饪"
        },
        {
            "english": "taste", "phonetic": "/teɪst/", "chinese": "n. 味道", 
            "example": "Taste the food.", "category": "食物烹饪"
        },
        {
            "english": "spice", "phonetic": "/spaɪs/", "chinese": "n. 香料", 
            "example": "Add the spice.", "category": "食物烹饪"
        },
        {
            "english": "herb", "phonetic": "/hɜːrb/", "chinese": "n. 草药", 
            "example": "Use the herb.", "category": "食物烹饪"
        },
        {
            "english": "seasoning", "phonetic": "/ˈsiːzənɪŋ/", "chinese": "n. 调味品", 
            "example": "Add seasoning.", "category": "食物烹饪"
        },
        {
            "english": "sauce", "phonetic": "/sɔːs/", "chinese": "n. 酱汁", 
            "example": "Pour the sauce.", "category": "食物烹饪"
        },
        {
            "english": "soup", "phonetic": "/suːp/", "chinese": "n. 汤", 
            "example": "Eat the soup.", "category": "食物烹饪"
        },
        {
            "english": "salad", "phonetic": "/ˈsæləd/", "chinese": "n. 沙拉", 
            "example": "Make a salad.", "category": "食物烹饪"
        },
        {
            "english": "sandwich", "phonetic": "/ˈsænwɪtʃ/", "chinese": "n. 三明治", 
            "example": "Eat a sandwich.", "category": "食物烹饪"
        },
        {
            "english": "pizza", "phonetic": "/ˈpiːtsə/", "chinese": "n. 披萨", 
            "example": "Order pizza.", "category": "食物烹饪"
        },
        {
            "english": "pasta", "phonetic": "/ˈpæstə/", "chinese": "n. 意大利面", 
            "example": "Cook pasta.", "category": "食物烹饪"
        },
        {
            "english": "bread", "phonetic": "/bred/", "chinese": "n. 面包", 
            "example": "Bake bread.", "category": "食物烹饪"
        },
        {
            "english": "rice", "phonetic": "/raɪs/", "chinese": "n. 米饭", 
            "example": "Cook rice.", "category": "食物烹饪"
        },
        {
            "english": "noodle", "phonetic": "/ˈnuːdl/", "chinese": "n. 面条", 
            "example": "Eat noodles.", "category": "食物烹饪"
        },
        {
            "english": "vegetable", "phonetic": "/ˈvedʒtəbl/", "chinese": "n. 蔬菜", 
            "example": "Eat vegetables.", "category": "食物烹饪"
        },
        {
            "english": "fruit", "phonetic": "/fruːt/", "chinese": "n. 水果", 
            "example": "Eat fruit.", "category": "食物烹饪"
        },
        # 心理情感类
        {
            "english": "emotion", "phonetic": "/ɪˈmoʊʃn/", "chinese": "n. 情感", 
            "example": "Express emotion.", "category": "心理情感"
        },
        {
            "english": "feeling", "phonetic": "/ˈfiːlɪŋ/", "chinese": "n. 感觉", 
            "example": "Share your feeling.", "category": "心理情感"
        },
        {
            "english": "mood", "phonetic": "/muːd/", "chinese": "n. 心情", 
            "example": "Improve your mood.", "category": "心理情感"
        },
        {
            "english": "attitude", "phonetic": "/ˈætɪtuːd/", "chinese": "n. 态度", 
            "example": "Change your attitude.", "category": "心理情感"
        },
        {
            "english": "behavior", "phonetic": "/bɪˈheɪvjər/", "chinese": "n. 行为", 
            "example": "Observe behavior.", "category": "心理情感"
        },
        {
            "english": "personality", "phonetic": "/ˌpɜːrsəˈnæləti/", "chinese": "n. 个性", 
            "example": "Develop personality.", "category": "心理情感"
        },
        {
            "english": "character", "phonetic": "/ˈkærəktər/", "chinese": "n. 性格", 
            "example": "Build character.", "category": "心理情感"
        },
        {
            "english": "temperament", "phonetic": "/ˈtempərəmənt/", "chinese": "n. 气质", 
            "example": "Show temperament.", "category": "心理情感"
        },
        {
            "english": "motivation", "phonetic": "/ˌmoʊtɪˈveɪʃn/", "chinese": "n. 动机", 
            "example": "Find motivation.", "category": "心理情感"
        },
        {
            "english": "inspiration", "phonetic": "/ˌɪnspəˈreɪʃn/", "chinese": "n. 灵感", 
            "example": "Seek inspiration.", "category": "心理情感"
        },
        {
            "english": "ambition", "phonetic": "/æmˈbɪʃn/", "chinese": "n. 野心", 
            "example": "Pursue ambition.", "category": "心理情感"
        },
        {
            "english": "confidence", "phonetic": "/ˈkɑːnfɪdəns/", "chinese": "n. 自信", 
            "example": "Build confidence.", "category": "心理情感"
        },
        {
            "english": "courage", "phonetic": "/ˈkɜːrɪdʒ/", "chinese": "n. 勇气", 
            "example": "Show courage.", "category": "心理情感"
        },
        {
            "english": "patience", "phonetic": "/ˈpeɪʃns/", "chinese": "n. 耐心", 
            "example": "Have patience.", "category": "心理情感"
        },
        {
            "english": "perseverance", "phonetic": "/ˌpɜːrsəˈvɪrəns/", "chinese": "n. 毅力", 
            "example": "Show perseverance.", "category": "心理情感"
        },
        {
            "english": "determination", "phonetic": "/dɪˌtɜːrmɪˈneɪʃn/", "chinese": "n. 决心", 
            "example": "Show determination.", "category": "心理情感"
        },
        {
            "english": "enthusiasm", "phonetic": "/ɪnˈθuːziæzəm/", "chinese": "n. 热情", 
            "example": "Show enthusiasm.", "category": "心理情感"
        },
        {
            "english": "optimism", "phonetic": "/ˈɑːptɪmɪzəm/", "chinese": "n. 乐观", 
            "example": "Maintain optimism.", "category": "心理情感"
        },
        {
            "english": "pessimism", "phonetic": "/ˈpesɪmɪzəm/", "chinese": "n. 悲观", 
            "example": "Avoid pessimism.", "category": "心理情感"
        },
        {
            "english": "anxiety", "phonetic": "/æŋˈzaɪəti/", "chinese": "n. 焦虑", 
            "example": "Manage anxiety.", "category": "心理情感"
        },
        {
            "english": "depression", "phonetic": "/dɪˈpreʃn/", "chinese": "n. 抑郁", 
            "example": "Overcome depression.", "category": "心理情感"
        },
        # 体育健身类
        {
            "english": "exercise", "phonetic": "/ˈeksərsaɪz/", "chinese": "n. 运动", 
            "example": "Do exercise.", "category": "体育健身"
        },
        {
            "english": "fitness", "phonetic": "/ˈfɪtnəs/", "chinese": "n. 健身", 
            "example": "Improve fitness.", "category": "体育健身"
        },
        {
            "english": "workout", "phonetic": "/ˈwɜːrkaʊt/", "chinese": "n. 锻炼", 
            "example": "Complete the workout.", "category": "体育健身"
        },
        {
            "english": "training", "phonetic": "/ˈtreɪnɪŋ/", "chinese": "n. 训练", 
            "example": "Start training.", "category": "体育健身"
        },
        {
            "english": "coach", "phonetic": "/koʊtʃ/", "chinese": "n. 教练", 
            "example": "The coach trained.", "category": "体育健身"
        },
        {
            "english": "athlete", "phonetic": "/ˈæθliːt/", "chinese": "n. 运动员", 
            "example": "The athlete competed.", "category": "体育健身"
        },
        {
            "english": "competition", "phonetic": "/ˌkɑːmpəˈtɪʃn/", "chinese": "n. 比赛", 
            "example": "Enter the competition.", "category": "体育健身"
        },
        {
            "english": "tournament", "phonetic": "/ˈtʊrnəmənt/", "chinese": "n. 锦标赛", 
            "example": "Win the tournament.", "category": "体育健身"
        },
        {
            "english": "championship", "phonetic": "/ˈtʃæmpiənʃɪp/", "chinese": "n. 冠军赛", 
            "example": "Win the championship.", "category": "体育健身"
        },
        {
            "english": "medal", "phonetic": "/ˈmedl/", "chinese": "n. 奖牌", 
            "example": "Win a medal.", "category": "体育健身"
        },
        {
            "english": "trophy", "phonetic": "/ˈtroʊfi/", "chinese": "n. 奖杯", 
            "example": "Lift the trophy.", "category": "体育健身"
        },
        {
            "english": "record", "phonetic": "/ˈrekərd/", "chinese": "n. 记录", 
            "example": "Break the record.", "category": "体育健身"
        },
        {
            "english": "performance", "phonetic": "/pərˈfɔːrməns/", "chinese": "n. 表现", 
            "example": "Improve performance.", "category": "体育健身"
        },
        {
            "english": "strength", "phonetic": "/streŋθ/", "chinese": "n. 力量", 
            "example": "Build strength.", "category": "体育健身"
        },
        {
            "english": "endurance", "phonetic": "/ɪnˈdʊrəns/", "chinese": "n. 耐力", 
            "example": "Increase endurance.", "category": "体育健身"
        },
        {
            "english": "flexibility", "phonetic": "/ˌfleksəˈbɪləti/", "chinese": "n. 柔韧性", 
            "example": "Improve flexibility.", "category": "体育健身"
        },
        {
            "english": "balance", "phonetic": "/ˈbæləns/", "chinese": "n. 平衡", 
            "example": "Maintain balance.", "category": "体育健身"
        },
        {
            "english": "coordination", "phonetic": "/koʊˌɔːrdɪˈneɪʃn/", "chinese": "n. 协调性", 
            "example": "Develop coordination.", "category": "体育健身"
        },
        {
            "english": "agility", "phonetic": "/əˈdʒɪləti/", "chinese": "n. 敏捷性", 
            "example": "Show agility.", "category": "体育健身"
        },
        {
            "english": "speed", "phonetic": "/spiːd/", "chinese": "n. 速度", 
            "example": "Increase speed.", "category": "体育健身"
        },
        {
            "english": "power", "phonetic": "/ˈpaʊər/", "chinese": "n. 力量", 
            "example": "Generate power.", "category": "体育健身"
        },
        # 金融经济类
        {
            "english": "economy", "phonetic": "/ɪˈkɑːnəmi/", "chinese": "n. 经济", 
            "example": "The economy grows.", "category": "金融经济"
        },
        {
            "english": "finance", "phonetic": "/faɪˈnæns/", "chinese": "n. 金融", 
            "example": "Study finance.", "category": "金融经济"
        },
        {
            "english": "banking", "phonetic": "/ˈbæŋkɪŋ/", "chinese": "n. 银行业", 
            "example": "Work in banking.", "category": "金融经济"
        },
        {
            "english": "currency", "phonetic": "/ˈkɜːrənsi/", "chinese": "n. 货币", 
            "example": "Exchange currency.", "category": "金融经济"
        },
        {
            "english": "inflation", "phonetic": "/ɪnˈfleɪʃn/", "chinese": "n. 通货膨胀", 
            "example": "Control inflation.", "category": "金融经济"
        },
        {
            "english": "deflation", "phonetic": "/ˌdiːˈfleɪʃn/", "chinese": "n. 通货紧缩", 
            "example": "Prevent deflation.", "category": "金融经济"
        },
        {
            "english": "recession", "phonetic": "/rɪˈseʃn/", "chinese": "n. 衰退", 
            "example": "End the recession.", "category": "金融经济"
        },
        {
            "english": "depression", "phonetic": "/dɪˈpreʃn/", "chinese": "n. 萧条", 
            "example": "Overcome depression.", "category": "金融经济"
        },
        {
            "english": "prosperity", "phonetic": "/prɑːˈsperəti/", "chinese": "n. 繁荣", 
            "example": "Enjoy prosperity.", "category": "金融经济"
        },
        {
            "english": "growth", "phonetic": "/ɡroʊθ/", "chinese": "n. 增长", 
            "example": "Achieve growth.", "category": "金融经济"
        },
        {
            "english": "market", "phonetic": "/ˈmɑːrkɪt/", "chinese": "n. 市场", 
            "example": "Enter the market.", "category": "金融经济"
        },
        {
            "english": "trade", "phonetic": "/treɪd/", "chinese": "n. 贸易", 
            "example": "Engage in trade.", "category": "金融经济"
        },
        {
            "english": "commerce", "phonetic": "/ˈkɑːmɜːrs/", "chinese": "n. 商业", 
            "example": "Promote commerce.", "category": "金融经济"
        },
        {
            "english": "industry", "phonetic": "/ˈɪndəstri/", "chinese": "n. 工业", 
            "example": "Develop industry.", "category": "金融经济"
        },
        {
            "english": "manufacturing", "phonetic": "/ˌmænjuˈfæktʃərɪŋ/", "chinese": "n. 制造业", 
            "example": "Boost manufacturing.", "category": "金融经济"
        },
        {
            "english": "production", "phonetic": "/prəˈdʌkʃn/", "chinese": "n. 生产", 
            "example": "Increase production.", "category": "金融经济"
        },
        {
            "english": "consumption", "phonetic": "/kənˈsʌmpʃn/", "chinese": "n. 消费", 
            "example": "Reduce consumption.", "category": "金融经济"
        },
        {
            "english": "supply", "phonetic": "/səˈplaɪ/", "chinese": "n. 供应", 
            "example": "Meet the supply.", "category": "金融经济"
        },
        {
            "english": "demand", "phonetic": "/dɪˈmænd/", "chinese": "n. 需求", 
            "example": "Satisfy demand.", "category": "金融经济"
        },
        {
            "english": "price", "phonetic": "/praɪs/", "chinese": "n. 价格", 
            "example": "Set the price.", "category": "金融经济"
        },
        {
            "english": "value", "phonetic": "/ˈvæljuː/", "chinese": "n. 价值", 
            "example": "Create value.", "category": "金融经济"
        },
        # 艺术文化类
        {
            "english": "masterpiece", "phonetic": "/ˈmæstərpiːs/", "chinese": "n. 杰作", 
            "example": "The masterpiece is famous.", "category": "艺术文化"
        },
        {
            "english": "gallery", "phonetic": "/ˈɡæləri/", "chinese": "n. 画廊", 
            "example": "Visit the gallery.", "category": "艺术文化"
        },
        {
            "english": "museum", "phonetic": "/mjuːˈziːəm/", "chinese": "n. 博物馆", 
            "example": "Explore the museum.", "category": "艺术文化"
        },
        {
            "english": "exhibition", "phonetic": "/ˌeksɪˈbɪʃn/", "chinese": "n. 展览", 
            "example": "Attend the exhibition.", "category": "艺术文化"
        },
        {
            "english": "collection", "phonetic": "/kəˈlekʃn/", "chinese": "n. 收藏", 
            "example": "Build a collection.", "category": "艺术文化"
        },
        {
            "english": "artist", "phonetic": "/ˈɑːrtɪst/", "chinese": "n. 艺术家", 
            "example": "The artist created.", "category": "艺术文化"
        },
        {
            "english": "musician", "phonetic": "/mjuːˈzɪʃn/", "chinese": "n. 音乐家", 
            "example": "The musician played.", "category": "艺术文化"
        },
        {
            "english": "composer", "phonetic": "/kəmˈpoʊzər/", "chinese": "n. 作曲家", 
            "example": "The composer wrote.", "category": "艺术文化"
        },
        {
            "english": "conductor", "phonetic": "/kənˈdʌktər/", "chinese": "n. 指挥家", 
            "example": "The conductor led.", "category": "艺术文化"
        },
        {
            "english": "performer", "phonetic": "/pərˈfɔːrmər/", "chinese": "n. 表演者", 
            "example": "The performer entertained.", "category": "艺术文化"
        },
        {
            "english": "audience", "phonetic": "/ˈɔːdiəns/", "chinese": "n. 观众", 
            "example": "The audience applauded.", "category": "艺术文化"
        },
        {
            "english": "critic", "phonetic": "/ˈkrɪtɪk/", "chinese": "n. 评论家", 
            "example": "The critic reviewed.", "category": "艺术文化"
        },
        {
            "english": "review", "phonetic": "/rɪˈvjuː/", "chinese": "n. 评论", 
            "example": "Write a review.", "category": "艺术文化"
        },
        {
            "english": "appreciation", "phonetic": "/əˌpriːʃiˈeɪʃn/", "chinese": "n. 欣赏", 
            "example": "Show appreciation.", "category": "艺术文化"
        },
        {
            "english": "creativity", "phonetic": "/ˌkriːeɪˈtɪvəti/", "chinese": "n. 创造力", 
            "example": "Express creativity.", "category": "艺术文化"
        },
        {
            "english": "imagination", "phonetic": "/ɪˌmædʒɪˈneɪʃn/", "chinese": "n. 想象力", 
            "example": "Use imagination.", "category": "艺术文化"
        },
        {
            "english": "inspiration", "phonetic": "/ˌɪnspəˈreɪʃn/", "chinese": "n. 灵感", 
            "example": "Find inspiration.", "category": "艺术文化"
        },
        {
            "english": "expression", "phonetic": "/ɪkˈspreʃn/", "chinese": "n. 表达", 
            "example": "Express yourself.", "category": "艺术文化"
        },
        {
            "english": "style", "phonetic": "/staɪl/", "chinese": "n. 风格", 
            "example": "Develop your style.", "category": "艺术文化"
        },
        {
            "english": "technique", "phonetic": "/tekˈniːk/", "chinese": "n. 技巧", 
            "example": "Master the technique.", "category": "艺术文化"
        },
        {
            "english": "talent", "phonetic": "/ˈtælənt/", "chinese": "n. 天赋", 
            "example": "Show talent.", "category": "艺术文化"
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
    expand_to_5000_batch5()
