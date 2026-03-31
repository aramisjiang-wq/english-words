import sqlite3

def expand_to_5000_batch6():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    new_words = [
        # 科学研究类
        {
            "english": "laboratory", "phonetic": "/ˈlæbrətɔːri/", "chinese": "n. 实验室", 
            "example": "Work in the laboratory.", "category": "科学研究"
        },
        {
            "english": "microscope", "phonetic": "/ˈmaɪkrəskoʊp/", "chinese": "n. 显微镜", 
            "example": "Use the microscope.", "category": "科学研究"
        },
        {
            "english": "telescope", "phonetic": "/ˈtelɪskoʊp/", "chinese": "n. 望远镜", 
            "example": "Look through the telescope.", "category": "科学研究"
        },
        {
            "english": "specimen", "phonetic": "/ˈspesɪmən/", "chinese": "n. 样本", 
            "example": "Collect the specimen.", "category": "科学研究"
        },
        {
            "english": "sample", "phonetic": "/ˈsæmpl/", "chinese": "n. 样品", 
            "example": "Take a sample.", "category": "科学研究"
        },
        {
            "english": "data", "phonetic": "/ˈdeɪtə/", "chinese": "n. 数据", 
            "example": "Analyze the data.", "category": "科学研究"
        },
        {
            "english": "statistics", "phonetic": "/stəˈtɪstɪks/", "chinese": "n. 统计", 
            "example": "Use statistics.", "category": "科学研究"
        },
        {
            "english": "probability", "phonetic": "/ˌprɑːbəˈbɪləti/", "chinese": "n. 概率", 
            "example": "Calculate probability.", "category": "科学研究"
        },
        {
            "english": "calculation", "phonetic": "/ˌkælkjuˈleɪʃn/", "chinese": "n. 计算", 
            "example": "Perform calculation.", "category": "科学研究"
        },
        {
            "english": "measurement", "phonetic": "/ˈmeʒərmənt/", "chinese": "n. 测量", 
            "example": "Take measurement.", "category": "科学研究"
        },
        {
            "english": "observation", "phonetic": "/ˌɑːbzərˈveɪʃn/", "chinese": "n. 观察", 
            "example": "Make observation.", "category": "科学研究"
        },
        {
            "english": "investigation", "phonetic": "/ɪnˌvestɪˈɡeɪʃn/", "chinese": "n. 调查", 
            "example": "Conduct investigation.", "category": "科学研究"
        },
        {
            "english": "exploration", "phonetic": "/ˌekspləˈreɪʃn/", "chinese": "n. 探索", 
            "example": "Space exploration.", "category": "科学研究"
        },
        {
            "english": "discovery", "phonetic": "/dɪsˈkʌvəri/", "chinese": "n. 发现", 
            "example": "Make a discovery.", "category": "科学研究"
        },
        {
            "english": "invention", "phonetic": "/ɪnˈvenʃn/", "chinese": "n. 发明", 
            "example": "The invention changed.", "category": "科学研究"
        },
        {
            "english": "innovation", "phonetic": "/ˌɪnəˈveɪʃn/", "chinese": "n. 创新", 
            "example": "Encourage innovation.", "category": "科学研究"
        },
        {
            "english": "development", "phonetic": "/dɪˈveləpmənt/", "chinese": "n. 发展", 
            "example": "Promote development.", "category": "科学研究"
        },
        {
            "english": "progress", "phonetic": "/ˈprɑːɡres/", "chinese": "n. 进步", 
            "example": "Make progress.", "category": "科学研究"
        },
        {
            "english": "achievement", "phonetic": "/əˈtʃiːvmənt/", "chinese": "n. 成就", 
            "example": "Celebrate achievement.", "category": "科学研究"
        },
        {
            "english": "contribution", "phonetic": "/ˌkɑːntrɪˈbjuːʃn/", "chinese": "n. 贡献", 
            "example": "Make a contribution.", "category": "科学研究"
        },
        # 商业管理类
        {
            "english": "enterprise", "phonetic": "/ˈentərpraɪz/", "chinese": "n. 企业", 
            "example": "Build an enterprise.", "category": "商业管理"
        },
        {
            "english": "corporation", "phonetic": "/ˌkɔːrpəˈreɪʃn/", "chinese": "n. 公司", 
            "example": "The corporation operates.", "category": "商业管理"
        },
        {
            "english": "organization", "phonetic": "/ˌɔːrɡənəˈzeɪʃn/", "chinese": "n. 组织", 
            "example": "Join the organization.", "category": "商业管理"
        },
        {
            "english": "department", "phonetic": "/dɪˈpɑːrtmənt/", "chinese": "n. 部门", 
            "example": "Work in the department.", "category": "商业管理"
        },
        {
            "english": "division", "phonetic": "/dɪˈvɪʒn/", "chinese": "n. 分部", 
            "example": "Lead the division.", "category": "商业管理"
        },
        {
            "english": "branch", "phonetic": "/bræntʃ/", "chinese": "n. 分支", 
            "example": "Open a branch.", "category": "商业管理"
        },
        {
            "english": "franchise", "phonetic": "/ˈfræntʃaɪz/", "chinese": "n. 特许经营", 
            "example": "Buy a franchise.", "category": "商业管理"
        },
        {
            "english": "subsidiary", "phonetic": "/səbˈsɪdieri/", "chinese": "n. 子公司", 
            "example": "The subsidiary operates.", "category": "商业管理"
        },
        {
            "english": "headquarters", "phonetic": "/ˈhedkwɔːrtərz/", "chinese": "n. 总部", 
            "example": "Visit headquarters.", "category": "商业管理"
        },
        {
            "english": "office", "phonetic": "/ˈɔːfɪs/", "chinese": "n. 办公室", 
            "example": "Work in the office.", "category": "商业管理"
        },
        {
            "english": "workplace", "phonetic": "/ˈwɜːrkpleɪs/", "chinese": "n. 工作场所", 
            "example": "Improve the workplace.", "category": "商业管理"
        },
        {
            "english": "environment", "phonetic": "/ɪnˈvaɪrənmənt/", "chinese": "n. 环境", 
            "example": "Protect the environment.", "category": "商业管理"
        },
        {
            "english": "culture", "phonetic": "/ˈkʌltʃər/", "chinese": "n. 文化", 
            "example": "Build the culture.", "category": "商业管理"
        },
        {
            "english": "values", "phonetic": "/ˈvæljuːz/", "chinese": "n. 价值观", 
            "example": "Share the values.", "category": "商业管理"
        },
        {
            "english": "mission", "phonetic": "/ˈmɪʃn/", "chinese": "n. 使命", 
            "example": "Fulfill the mission.", "category": "商业管理"
        },
        {
            "english": "vision", "phonetic": "/ˈvɪʒn/", "chinese": "n. 愿景", 
            "example": "Share the vision.", "category": "商业管理"
        },
        {
            "english": "goal", "phonetic": "/ɡoʊl/", "chinese": "n. 目标", 
            "example": "Achieve the goal.", "category": "商业管理"
        },
        {
            "english": "objective", "phonetic": "/əbˈdʒektɪv/", "chinese": "n. 目的", 
            "example": "Meet the objective.", "category": "商业管理"
        },
        {
            "english": "target", "phonetic": "/ˈtɑːrɡɪt/", "chinese": "n. 目标", 
            "example": "Hit the target.", "category": "商业管理"
        },
        {
            "english": "deadline", "phonetic": "/ˈdedlaɪn/", "chinese": "n. 截止日期", 
            "example": "Meet the deadline.", "category": "商业管理"
        },
        # 法律政治类
        {
            "english": "court", "phonetic": "/kɔːrt/", "chinese": "n. 法庭", 
            "example": "Go to court.", "category": "法律政治"
        },
        {
            "english": "judge", "phonetic": "/dʒʌdʒ/", "chinese": "n. 法官", 
            "example": "The judge decided.", "category": "法律政治"
        },
        {
            "english": "jury", "phonetic": "/ˈdʒʊri/", "chinese": "n. 陪审团", 
            "example": "The jury deliberated.", "category": "法律政治"
        },
        {
            "english": "witness", "phonetic": "/ˈwɪtnəs/", "chinese": "n. 证人", 
            "example": "The witness testified.", "category": "法律政治"
        },
        {
            "english": "evidence", "phonetic": "/ˈevɪdəns/", "chinese": "n. 证据", 
            "example": "Present evidence.", "category": "法律政治"
        },
        {
            "english": "proof", "phonetic": "/pruːf/", "chinese": "n. 证明", 
            "example": "Provide proof.", "category": "法律政治"
        },
        {
            "english": "testimony", "phonetic": "/ˈtestɪmoʊni/", "chinese": "n. 证词", 
            "example": "Give testimony.", "category": "法律政治"
        },
        {
            "english": "allegation", "phonetic": "/ˌæləˈɡeɪʃn/", "chinese": "n. 指控", 
            "example": "Make an allegation.", "category": "法律政治"
        },
        {
            "english": "accusation", "phonetic": "/ˌækjuˈzeɪʃn/", "chinese": "n. 指控", 
            "example": "Face the accusation.", "category": "法律政治"
        },
        {
            "english": "indictment", "phonetic": "/ɪnˈdaɪtmənt/", "chinese": "n. 起诉", 
            "example": "The indictment was filed.", "category": "法律政治"
        },
        {
            "english": "conviction", "phonetic": "/kənˈvɪkʃn/", "chinese": "n. 定罪", 
            "example": "The conviction stood.", "category": "法律政治"
        },
        {
            "english": "acquittal", "phonetic": "/əˈkwɪtl/", "chinese": "n. 无罪释放", 
            "example": "The acquittal was granted.", "category": "法律政治"
        },
        {
            "english": "appeal", "phonetic": "/əˈpiːl/", "chinese": "n. 上诉", 
            "example": "File an appeal.", "category": "法律政治"
        },
        {
            "english": "parole", "phonetic": "/pəˈroʊl/", "chinese": "n. 假释", 
            "example": "Grant parole.", "category": "法律政治"
        },
        {
            "english": "probation", "phonetic": "/proʊˈbeɪʃn/", "chinese": "n. 缓刑", 
            "example": "Serve probation.", "category": "法律政治"
        },
        {
            "english": "sentence", "phonetic": "/ˈsentəns/", "chinese": "n. 判决", 
            "example": "The sentence was given.", "category": "法律政治"
        },
        {
            "english": "penalty", "phonetic": "/ˈpenəlti/", "chinese": "n. 惩罚", 
            "example": "Pay the penalty.", "category": "法律政治"
        },
        {
            "english": "fine", "phonetic": "/faɪn/", "chinese": "n. 罚款", 
            "example": "Pay the fine.", "category": "法律政治"
        },
        {
            "english": "imprisonment", "phonetic": "/ɪmˈprɪznmənt/", "chinese": "n. 监禁", 
            "example": "Serve imprisonment.", "category": "法律政治"
        },
        {
            "english": "detention", "phonetic": "/dɪˈtenʃn/", "chinese": "n. 拘留", 
            "example": "Place in detention.", "category": "法律政治"
        },
        # 医疗健康类
        {
            "english": "symptom", "phonetic": "/ˈsɪmptəm/", "chinese": "n. 症状", 
            "example": "Identify the symptom.", "category": "医疗健康"
        },
        {
            "english": "diagnosis", "phonetic": "/ˌdaɪəɡˈnoʊsɪs/", "chinese": "n. 诊断", 
            "example": "Make a diagnosis.", "category": "医疗健康"
        },
        {
            "english": "prognosis", "phonetic": "/prɑːɡˈnoʊsɪs/", "chinese": "n. 预后", 
            "example": "The prognosis is good.", "category": "医疗健康"
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
            "english": "dosage", "phonetic": "/ˈdoʊsɪdʒ/", "chinese": "n. 剂量", 
            "example": "Check the dosage.", "category": "医疗健康"
        },
        {
            "english": "side effect", "phonetic": "/saɪd ɪˈfekt/", "chinese": "n. 副作用", 
            "example": "Watch for side effects.", "category": "医疗健康"
        },
        {
            "english": "allergy", "phonetic": "/ˈælərdʒi/", "chinese": "n. 过敏", 
            "example": "Treat the allergy.", "category": "医疗健康"
        },
        {
            "english": "infection", "phonetic": "/ɪnˈfekʃn/", "chinese": "n. 感染", 
            "example": "Prevent infection.", "category": "医疗健康"
        },
        {
            "english": "virus", "phonetic": "/ˈvaɪrəs/", "chinese": "n. 病毒", 
            "example": "The virus spreads.", "category": "医疗健康"
        },
        {
            "english": "bacteria", "phonetic": "/bækˈtɪriə/", "chinese": "n. 细菌", 
            "example": "Kill the bacteria.", "category": "医疗健康"
        },
        {
            "english": "germ", "phonetic": "/dʒɜːrm/", "chinese": "n. 细菌", 
            "example": "Kill the germ.", "category": "医疗健康"
        },
        {
            "english": "disease", "phonetic": "/dɪˈziːz/", "chinese": "n. 疾病", 
            "example": "Cure the disease.", "category": "医疗健康"
        },
        {
            "english": "illness", "phonetic": "/ˈɪlnəs/", "chinese": "n. 疾病", 
            "example": "Treat the illness.", "category": "医疗健康"
        },
        {
            "english": "sickness", "phonetic": "/ˈsɪknəs/", "chinese": "n. 疾病", 
            "example": "Overcome sickness.", "category": "医疗健康"
        },
        {
            "english": "disorder", "phonetic": "/dɪsˈɔːrdər/", "chinese": "n. 紊乱", 
            "example": "Treat the disorder.", "category": "医疗健康"
        },
        {
            "english": "condition", "phonetic": "/kənˈdɪʃn/", "chinese": "n. 状况", 
            "example": "Monitor the condition.", "category": "医疗健康"
        },
        {
            "english": "syndrome", "phonetic": "/ˈsɪndroʊm/", "chinese": "n. 综合征", 
            "example": "Identify the syndrome.", "category": "医疗健康"
        },
        # 教育学习类
        {
            "english": "education", "phonetic": "/ˌedʒuˈkeɪʃn/", "chinese": "n. 教育", 
            "example": "Value education.", "category": "教育学习"
        },
        {
            "english": "learning", "phonetic": "/ˈlɜːrnɪŋ/", "chinese": "n. 学习", 
            "example": "Enjoy learning.", "category": "教育学习"
        },
        {
            "english": "teaching", "phonetic": "/ˈtiːtʃɪŋ/", "chinese": "n. 教学", 
            "example": "Improve teaching.", "category": "教育学习"
        },
        {
            "english": "instruction", "phonetic": "/ɪnˈstrʌkʃn/", "chinese": "n. 指导", 
            "example": "Provide instruction.", "category": "教育学习"
        },
        {
            "english": "training", "phonetic": "/ˈtreɪnɪŋ/", "chinese": "n. 培训", 
            "example": "Complete training.", "category": "教育学习"
        },
        {
            "english": "development", "phonetic": "/dɪˈveləpmənt/", "chinese": "n. 发展", 
            "example": "Support development.", "category": "教育学习"
        },
        {
            "english": "improvement", "phonetic": "/ɪmˈpruːvmənt/", "chinese": "n. 改进", 
            "example": "Show improvement.", "category": "教育学习"
        },
        {
            "english": "progress", "phonetic": "/ˈprɑːɡres/", "chinese": "n. 进步", 
            "example": "Track progress.", "category": "教育学习"
        },
        {
            "english": "achievement", "phonetic": "/əˈtʃiːvmənt/", "chinese": "n. 成就", 
            "example": "Celebrate achievement.", "category": "教育学习"
        },
        {
            "english": "success", "phonetic": "/səkˈses/", "chinese": "n. 成功", 
            "example": "Achieve success.", "category": "教育学习"
        },
        {
            "english": "failure", "phonetic": "/ˈfeɪljər/", "chinese": "n. 失败", 
            "example": "Learn from failure.", "category": "教育学习"
        },
        {
            "english": "challenge", "phonetic": "/ˈtʃælɪndʒ/", "chinese": "n. 挑战", 
            "example": "Accept the challenge.", "category": "教育学习"
        },
        {
            "english": "opportunity", "phonetic": "/ˌɑːpərˈtuːnəti/", "chinese": "n. 机会", 
            "example": "Seize the opportunity.", "category": "教育学习"
        },
        {
            "english": "possibility", "phonetic": "/ˌpɑːsəˈbɪləti/", "chinese": "n. 可能性", 
            "example": "Explore possibility.", "category": "教育学习"
        },
        {
            "english": "potential", "phonetic": "/pəˈtenʃl/", "chinese": "n. 潜力", 
            "example": "Realize potential.", "category": "教育学习"
        },
        {
            "english": "ability", "phonetic": "/əˈbɪləti/", "chinese": "n. 能力", 
            "example": "Develop ability.", "category": "教育学习"
        },
        {
            "english": "skill", "phonetic": "/skɪl/", "chinese": "n. 技能", 
            "example": "Master the skill.", "category": "教育学习"
        },
        {
            "english": "talent", "phonetic": "/ˈtælənt/", "chinese": "n. 天赋", 
            "example": "Show talent.", "category": "教育学习"
        },
        {
            "english": "gift", "phonetic": "/ɡɪft/", "chinese": "n. 天赋", 
            "example": "Use your gift.", "category": "教育学习"
        },
        {
            "english": "aptitude", "phonetic": "/ˈæptɪtuːd/", "chinese": "n. 资质", 
            "example": "Test aptitude.", "category": "教育学习"
        },
        # 技术创新类
        {
            "english": "technology", "phonetic": "/tekˈnɑːlədʒi/", "chinese": "n. 技术", 
            "example": "Use technology.", "category": "技术创新"
        },
        {
            "english": "innovation", "phonetic": "/ˌɪnəˈveɪʃn/", "chinese": "n. 创新", 
            "example": "Drive innovation.", "category": "技术创新"
        },
        {
            "english": "invention", "phonetic": "/ɪnˈvenʃn/", "chinese": "n. 发明", 
            "example": "Create invention.", "category": "技术创新"
        },
        {
            "english": "discovery", "phonetic": "/dɪsˈkʌvəri/", "chinese": "n. 发现", 
            "example": "Make a discovery.", "category": "技术创新"
        },
        {
            "english": "advancement", "phonetic": "/ədˈvænsmənt/", "chinese": "n. 进步", 
            "example": "Promote advancement.", "category": "技术创新"
        },
        {
            "english": "improvement", "phonetic": "/ɪmˈpruːvmənt/", "chinese": "n. 改进", 
            "example": "Make improvement.", "category": "技术创新"
        },
        {
            "english": "enhancement", "phonetic": "/ɪnˈhænsmənt/", "chinese": "n. 增强", 
            "example": "Provide enhancement.", "category": "技术创新"
        },
        {
            "english": "upgrade", "phonetic": "/ˈʌpɡreɪd/", "chinese": "n. 升级", 
            "example": "Perform upgrade.", "category": "技术创新"
        },
        {
            "english": "update", "phonetic": "/ˈʌpdeɪt/", "chinese": "n. 更新", 
            "example": "Install update.", "category": "技术创新"
        },
        {
            "english": "version", "phonetic": "/ˈvɜːrʒn/", "chinese": "n. 版本", 
            "example": "Check the version.", "category": "技术创新"
        },
        {
            "english": "release", "phonetic": "/rɪˈliːs/", "chinese": "n. 发布", 
            "example": "Wait for release.", "category": "技术创新"
        },
        {
            "english": "launch", "phonetic": "/lɔːntʃ/", "chinese": "n. 发布", 
            "example": "Plan the launch.", "category": "技术创新"
        },
        {
            "english": "deployment", "phonetic": "/dɪˈplɔɪmənt/", "chinese": "n. 部署", 
            "example": "Complete deployment.", "category": "技术创新"
        },
        {
            "english": "installation", "phonetic": "/ˌɪnstəˈleɪʃn/", "chinese": "n. 安装", 
            "example": "Perform installation.", "category": "技术创新"
        },
        {
            "english": "configuration", "phonetic": "/kənˌfɪɡjəˈreɪʃn/", "chinese": "n. 配置", 
            "example": "Change configuration.", "category": "技术创新"
        },
        {
            "english": "customization", "phonetic": "/ˌkʌstəmaɪˈzeɪʃn/", "chinese": "n. 定制", 
            "example": "Offer customization.", "category": "技术创新"
        },
        {
            "english": "personalization", "phonetic": "/ˌpɜːrsənəlaɪˈzeɪʃn/", "chinese": "n. 个性化", 
            "example": "Enable personalization.", "category": "技术创新"
        },
        {
            "english": "integration", "phonetic": "/ˌɪntɪˈɡreɪʃn/", "chinese": "n. 集成", 
            "example": "Complete integration.", "category": "技术创新"
        },
        {
            "english": "compatibility", "phonetic": "/kəmˌpætəˈbɪləti/", "chinese": "n. 兼容性", 
            "example": "Check compatibility.", "category": "技术创新"
        },
        {
            "english": "interoperability", "phonetic": "/ˌɪntərˌɑːpərəˈbɪləti/", "chinese": "n. 互操作性", 
            "example": "Ensure interoperability.", "category": "技术创新"
        },
        {
            "english": "scalability", "phonetic": "/ˌskeɪləˈbɪləti/", "chinese": "n. 可扩展性", 
            "example": "Test scalability.", "category": "技术创新"
        },
        # 自然地理类
        {
            "english": "climate", "phonetic": "/ˈklaɪmət/", "chinese": "n. 气候", 
            "example": "Study the climate.", "category": "自然地理"
        },
        {
            "english": "weather", "phonetic": "/ˈweðər/", "chinese": "n. 天气", 
            "example": "Check the weather.", "category": "自然地理"
        },
        {
            "english": "temperature", "phonetic": "/ˈtemprətʃər/", "chinese": "n. 温度", 
            "example": "Measure temperature.", "category": "自然地理"
        },
        {
            "english": "humidity", "phonetic": "/hjuːˈmɪdəti/", "chinese": "n. 湿度", 
            "example": "Control humidity.", "category": "自然地理"
        },
        {
            "english": "atmosphere", "phonetic": "/ˈætməsfɪr/", "chinese": "n. 大气", 
            "example": "Protect the atmosphere.", "category": "自然地理"
        },
        {
            "english": "environment", "phonetic": "/ɪnˈvaɪrənmənt/", "chinese": "n. 环境", 
            "example": "Preserve environment.", "category": "自然地理"
        },
        {
            "english": "ecosystem", "phonetic": "/ˈiːkoʊsɪstəm/", "chinese": "n. 生态系统", 
            "example": "Protect the ecosystem.", "category": "自然地理"
        },
        {
            "english": "habitat", "phonetic": "/ˈhæbɪtæt/", "chinese": "n. 栖息地", 
            "example": "Save the habitat.", "category": "自然地理"
        },
        {
            "english": "species", "phonetic": "/ˈspiːʃiːz/", "chinese": "n. 物种", 
            "example": "Protect the species.", "category": "自然地理"
        },
        {
            "english": "biodiversity", "phonetic": "/ˌbaɪoʊdaɪˈvɜːrsəti/", "chinese": "n. 生物多样性", 
            "example": "Maintain biodiversity.", "category": "自然地理"
        },
        {
            "english": "conservation", "phonetic": "/ˌkɑːnsərˈveɪʃn/", "chinese": "n. 保护", 
            "example": "Support conservation.", "category": "自然地理"
        },
        {
            "english": "preservation", "phonetic": "/ˌprezərˈveɪʃn/", "chinese": "n. 保护", 
            "example": "Ensure preservation.", "category": "自然地理"
        },
        {
            "english": "restoration", "phonetic": "/ˌrestəˈreɪʃn/", "chinese": "n. 恢复", 
            "example": "Complete restoration.", "category": "自然地理"
        },
        {
            "english": "regeneration", "phonetic": "/rɪˌdʒenəˈreɪʃn/", "chinese": "n. 再生", 
            "example": "Promote regeneration.", "category": "自然地理"
        },
        {
            "english": "sustainability", "phonetic": "/səˌsteɪnəˈbɪləti/", "chinese": "n. 可持续性", 
            "example": "Achieve sustainability.", "category": "自然地理"
        },
        {
            "english": "renewable", "phonetic": "/rɪˈnuːəbl/", "chinese": "adj. 可再生的", 
            "example": "Use renewable energy.", "category": "自然地理"
        },
        {
            "english": "pollution", "phonetic": "/pəˈluːʃn/", "chinese": "n. 污染", 
            "example": "Reduce pollution.", "category": "自然地理"
        },
        {
            "english": "contamination", "phonetic": "/kənˌtæmɪˈneɪʃn/", "chinese": "n. 污染", 
            "example": "Prevent contamination.", "category": "自然地理"
        },
        {
            "english": "waste", "phonetic": "/weɪst/", "chinese": "n. 废物", 
            "example": "Reduce waste.", "category": "自然地理"
        },
        {
            "english": "recycling", "phonetic": "/ˌriːˈsaɪklɪŋ/", "chinese": "n. 回收", 
            "example": "Promote recycling.", "category": "自然地理"
        },
        {
            "english": "disposal", "phonetic": "/dɪˈspoʊzl/", "chinese": "n. 处理", 
            "example": "Proper disposal.", "category": "自然地理"
        },
        # 社会文化类
        {
            "english": "community", "phonetic": "/kəˈmjuːnəti/", "chinese": "n. 社区", 
            "example": "Build community.", "category": "社会文化"
        },
        {
            "english": "society", "phonetic": "/səˈsaɪəti/", "chinese": "n. 社会", 
            "example": "Serve society.", "category": "社会文化"
        },
        {
            "english": "civilization", "phonetic": "/ˌsɪvəlaɪˈzeɪʃn/", "chinese": "n. 文明", 
            "example": "Study civilization.", "category": "社会文化"
        },
        {
            "english": "culture", "phonetic": "/ˈkʌltʃər/", "chinese": "n. 文化", 
            "example": "Respect culture.", "category": "社会文化"
        },
        {
            "english": "tradition", "phonetic": "/trəˈdɪʃn/", "chinese": "n. 传统", 
            "example": "Keep tradition.", "category": "社会文化"
        },
        {
            "english": "custom", "phonetic": "/ˈkʌstəm/", "chinese": "n. 习俗", 
            "example": "Follow custom.", "category": "社会文化"
        },
        {
            "english": "ritual", "phonetic": "/ˈrɪtʃuəl/", "chinese": "n. 仪式", 
            "example": "Perform ritual.", "category": "社会文化"
        },
        {
            "english": "ceremony", "phonetic": "/ˈserəmoʊni/", "chinese": "n. 典礼", 
            "example": "Attend ceremony.", "category": "社会文化"
        },
        {
            "english": "festival", "phonetic": "/ˈfestɪvl/", "chinese": "n. 节日", 
            "example": "Celebrate festival.", "category": "社会文化"
        },
        {
            "english": "celebration", "phonetic": "/ˌselɪˈbreɪʃn/", "chinese": "n. 庆祝", 
            "example": "Join celebration.", "category": "社会文化"
        },
        {
            "english": "heritage", "phonetic": "/ˈherɪtɪdʒ/", "chinese": "n. 遗产", 
            "example": "Preserve heritage.", "category": "社会文化"
        },
        {
            "english": "legacy", "phonetic": "/ˈleɡəsi/", "chinese": "n. 遗产", 
            "example": "Leave a legacy.", "category": "社会文化"
        },
        {
            "english": "monument", "phonetic": "/ˈmɑːnjumənt/", "chinese": "n. 纪念碑", 
            "example": "Visit monument.", "category": "社会文化"
        },
        {
            "english": "landmark", "phonetic": "/ˈlændmɑːrk/", "chinese": "n. 地标", 
            "example": "See the landmark.", "category": "社会文化"
        },
        {
            "english": "symbol", "phonetic": "/ˈsɪmbl/", "chinese": "n. 象征", 
            "example": "The symbol represents.", "category": "社会文化"
        },
        {
            "english": "emblem", "phonetic": "/ˈembləm/", "chinese": "n. 徽章", 
            "example": "Wear the emblem.", "category": "社会文化"
        },
        {
            "english": "badge", "phonetic": "/bædʒ/", "chinese": "n. 徽章", 
            "example": "Display the badge.", "category": "社会文化"
        },
        {
            "english": "flag", "phonetic": "/flæɡ/", "chinese": "n. 旗帜", 
            "example": "Raise the flag.", "category": "社会文化"
        },
        {
            "english": "anthem", "phonetic": "/ˈænθəm/", "chinese": "n. 国歌", 
            "example": "Sing the anthem.", "category": "社会文化"
        },
        {
            "english": "identity", "phonetic": "/aɪˈdentəti/", "chinese": "n. 身份", 
            "example": "Build identity.", "category": "社会文化"
        },
        {
            "english": "belonging", "phonetic": "/bɪˈlɔːŋɪŋ/", "chinese": "n. 归属感", 
            "example": "Feel belonging.", "category": "社会文化"
        },
        # 旅行交通类
        {
            "english": "journey", "phonetic": "/ˈdʒɜːrni/", "chinese": "n. 旅程", 
            "example": "Begin the journey.", "category": "旅行交通"
        },
        {
            "english": "voyage", "phonetic": "/ˈvɔɪɪdʒ/", "chinese": "n. 航行", 
            "example": "Complete the voyage.", "category": "旅行交通"
        },
        {
            "english": "expedition", "phonetic": "/ˌekspəˈdɪʃn/", "chinese": "n. 探险", 
            "example": "Join the expedition.", "category": "旅行交通"
        },
        {
            "english": "adventure", "phonetic": "/ədˈventʃər/", "chinese": "n. 冒险", 
            "example": "Seek adventure.", "category": "旅行交通"
        },
        {
            "english": "exploration", "phonetic": "/ˌekspləˈreɪʃn/", "chinese": "n. 探索", 
            "example": "Go on exploration.", "category": "旅行交通"
        },
        {
            "english": "discovery", "phonetic": "/dɪsˈkʌvəri/", "chinese": "n. 发现", 
            "example": "Make a discovery.", "category": "旅行交通"
        },
        {
            "english": "experience", "phonetic": "/ɪkˈspɪriəns/", "chinese": "n. 经历", 
            "example": "Gain experience.", "category": "旅行交通"
        },
        {
            "english": "memory", "phonetic": "/ˈmeməri/", "chinese": "n. 记忆", 
            "example": "Create memories.", "category": "旅行交通"
        },
        {
            "english": "souvenir", "phonetic": "/ˌsuːvəˈnɪr/", "chinese": "n. 纪念品", 
            "example": "Buy a souvenir.", "category": "旅行交通"
        },
        {
            "english": "photograph", "phonetic": "/ˈfoʊtəɡræf/", "chinese": "n. 照片", 
            "example": "Take a photograph.", "category": "旅行交通"
        },
        {
            "english": "album", "phonetic": "/ˈælbəm/", "chinese": "n. 相册", 
            "example": "Create an album.", "category": "旅行交通"
        },
        {
            "english": "diary", "phonetic": "/ˈdaɪəri/", "chinese": "n. 日记", 
            "example": "Keep a diary.", "category": "旅行交通"
        },
        {
            "english": "journal", "phonetic": "/ˈdʒɜːrnl/", "chinese": "n. 日志", 
            "example": "Write in the journal.", "category": "旅行交通"
        },
        {
            "english": "blog", "phonetic": "/blɑːɡ/", "chinese": "n. 博客", 
            "example": "Update the blog.", "category": "旅行交通"
        },
        {
            "english": "review", "phonetic": "/rɪˈvjuː/", "chinese": "n. 评论", 
            "example": "Write a review.", "category": "旅行交通"
        },
        {
            "english": "recommendation", "phonetic": "/ˌrekəmenˈdeɪʃn/", "chinese": "n. 推荐", 
            "example": "Make a recommendation.", "category": "旅行交通"
        },
        {
            "english": "suggestion", "phonetic": "/səˈdʒestʃən/", "chinese": "n. 建议", 
            "example": "Offer a suggestion.", "category": "旅行交通"
        },
        {
            "english": "advice", "phonetic": "/ədˈvaɪs/", "chinese": "n. 建议", 
            "example": "Give advice.", "category": "旅行交通"
        },
        {
            "english": "tip", "phonetic": "/tɪp/", "chinese": "n. 提示", 
            "example": "Share a tip.", "category": "旅行交通"
        },
        {
            "english": "guide", "phonetic": "/ɡaɪd/", "chinese": "n. 指南", 
            "example": "Follow the guide.", "category": "旅行交通"
        },
        # 食物烹饪类
        {
            "english": "ingredient", "phonetic": "/ɪnˈɡriːdiənt/", "chinese": "n. 原料", 
            "example": "Choose ingredients.", "category": "食物烹饪"
        },
        {
            "english": "recipe", "phonetic": "/ˈresəpi/", "chinese": "n. 食谱", 
            "example": "Follow the recipe.", "category": "食物烹饪"
        },
        {
            "english": "technique", "phonetic": "/tekˈniːk/", "chinese": "n. 技巧", 
            "example": "Master the technique.", "category": "食物烹饪"
        },
        {
            "english": "method", "phonetic": "/ˈmeθəd/", "chinese": "n. 方法", 
            "example": "Use the method.", "category": "食物烹饪"
        },
        {
            "english": "process", "phonetic": "/ˈprɑːses/", "chinese": "n. 过程", 
            "example": "Follow the process.", "category": "食物烹饪"
        },
        {
            "english": "preparation", "phonetic": "/ˌprepəˈreɪʃn/", "chinese": "n. 准备", 
            "example": "Complete preparation.", "category": "食物烹饪"
        },
        {
            "english": "cooking", "phonetic": "/ˈkʊkɪŋ/", "chinese": "n. 烹饪", 
            "example": "Enjoy cooking.", "category": "食物烹饪"
        },
        {
            "english": "baking", "phonetic": "/ˈbeɪkɪŋ/", "chinese": "n. 烘焙", 
            "example": "Try baking.", "category": "食物烹饪"
        },
        {
            "english": "grilling", "phonetic": "/ˈɡrɪlɪŋ/", "chinese": "n. 烧烤", 
            "example": "Start grilling.", "category": "食物烹饪"
        },
        {
            "english": "frying", "phonetic": "/ˈfraɪɪŋ/", "chinese": "n. 油炸", 
            "example": "Avoid frying.", "category": "食物烹饪"
        },
        {
            "english": "boiling", "phonetic": "/ˈbɔɪlɪŋ/", "chinese": "n. 煮沸", 
            "example": "Start boiling.", "category": "食物烹饪"
        },
        {
            "english": "steaming", "phonetic": "/ˈstiːmɪŋ/", "chinese": "n. 蒸", 
            "example": "Try steaming.", "category": "食物烹饪"
        },
        {
            "english": "roasting", "phonetic": "/ˈroʊstɪŋ/", "chinese": "n. 烤", 
            "example": "Begin roasting.", "category": "食物烹饪"
        },
        {
            "english": "sautéing", "phonetic": "/soʊˈteɪɪŋ/", "chinese": "n. 煎炒", 
            "example": "Practice sautéing.", "category": "食物烹饪"
        },
        {
            "english": "seasoning", "phonetic": "/ˈsiːzənɪŋ/", "chinese": "n. 调味", 
            "example": "Add seasoning.", "category": "食物烹饪"
        },
        {
            "english": "marinade", "phonetic": "/ˌmærɪˈneɪd/", "chinese": "n. 腌料", 
            "example": "Use marinade.", "category": "食物烹饪"
        },
        {
            "english": "sauce", "phonetic": "/sɔːs/", "chinese": "n. 酱汁", 
            "example": "Make sauce.", "category": "食物烹饪"
        },
        {
            "english": "dressing", "phonetic": "/ˈdresɪŋ/", "chinese": "n. 调味酱", 
            "example": "Add dressing.", "category": "食物烹饪"
        },
        {
            "english": "garnish", "phonetic": "/ˈɡɑːrnɪʃ/", "chinese": "n. 装饰", 
            "example": "Add garnish.", "category": "食物烹饪"
        },
        {
            "english": "presentation", "phonetic": "/ˌpriːzenˈteɪʃn/", "chinese": "n. 摆盘", 
            "example": "Improve presentation.", "category": "食物烹饪"
        },
        # 心理情感类
        {
            "english": "emotion", "phonetic": "/ɪˈmoʊʃn/", "chinese": "n. 情感", 
            "example": "Express emotion.", "category": "心理情感"
        },
        {
            "english": "feeling", "phonetic": "/ˈfiːlɪŋ/", "chinese": "n. 感觉", 
            "example": "Share feelings.", "category": "心理情感"
        },
        {
            "english": "sentiment", "phonetic": "/ˈsentɪmənt/", "chinese": "n. 情绪", 
            "example": "Express sentiment.", "category": "心理情感"
        },
        {
            "english": "mood", "phonetic": "/muːd/", "chinese": "n. 心情", 
            "example": "Improve mood.", "category": "心理情感"
        },
        {
            "english": "temper", "phonetic": "/ˈtempər/", "chinese": "n. 脾气", 
            "example": "Control temper.", "category": "心理情感"
        },
        {
            "english": "attitude", "phonetic": "/ˈætɪtuːd/", "chinese": "n. 态度", 
            "example": "Change attitude.", "category": "心理情感"
        },
        {
            "english": "mindset", "phonetic": "/ˈmaɪndset/", "chinese": "n. 思维模式", 
            "example": "Develop mindset.", "category": "心理情感"
        },
        {
            "english": "perspective", "phonetic": "/pərˈspektɪv/", "chinese": "n. 视角", 
            "example": "Change perspective.", "category": "心理情感"
        },
        {
            "english": "outlook", "phonetic": "/ˈaʊtlʊk/", "chinese": "n. 观点", 
            "example": "Positive outlook.", "category": "心理情感"
        },
        {
            "english": "viewpoint", "phonetic": "/ˈvjuːpɔɪnt/", "chinese": "n. 观点", 
            "example": "Share viewpoint.", "category": "心理情感"
        },
        {
            "english": "opinion", "phonetic": "/əˈpɪnjən/", "chinese": "n. 意见", 
            "example": "Express opinion.", "category": "心理情感"
        },
        {
            "english": "belief", "phonetic": "/bɪˈliːf/", "chinese": "n. 信念", 
            "example": "Hold belief.", "category": "心理情感"
        },
        {
            "english": "conviction", "phonetic": "/kənˈvɪkʃn/", "chinese": "n. 坚信", 
            "example": "Show conviction.", "category": "心理情感"
        },
        {
            "english": "faith", "phonetic": "/feɪθ/", "chinese": "n. 信仰", 
            "example": "Have faith.", "category": "心理情感"
        },
        {
            "english": "trust", "phonetic": "/trʌst/", "chinese": "n. 信任", 
            "example": "Build trust.", "category": "心理情感"
        },
        {
            "english": "confidence", "phonetic": "/ˈkɑːnfɪdəns/", "chinese": "n. 自信", 
            "example": "Show confidence.", "category": "心理情感"
        },
        {
            "english": "self-esteem", "phonetic": "/ˌself ɪˈstiːm/", "chinese": "n. 自尊", 
            "example": "Build self-esteem.", "category": "心理情感"
        },
        {
            "english": "dignity", "phonetic": "/ˈdɪɡnəti/", "chinese": "n. 尊严", 
            "example": "Maintain dignity.", "category": "心理情感"
        },
        {
            "english": "respect", "phonetic": "/rɪˈspekt/", "chinese": "n. 尊重", 
            "example": "Show respect.", "category": "心理情感"
        },
        {
            "english": "honor", "phonetic": "/ˈɑːnər/", "chinese": "n. 荣誉", 
            "example": "Uphold honor.", "category": "心理情感"
        },
        # 体育健身类
        {
            "english": "sport", "phonetic": "/spɔːrt/", "chinese": "n. 运动", 
            "example": "Play sport.", "category": "体育健身"
        },
        {
            "english": "game", "phonetic": "/ɡeɪm/", "chinese": "n. 比赛", 
            "example": "Win the game.", "category": "体育健身"
        },
        {
            "english": "match", "phonetic": "/mætʃ/", "chinese": "n. 比赛", 
            "example": "Watch the match.", "category": "体育健身"
        },
        {
            "english": "race", "phonetic": "/reɪs/", "chinese": "n. 比赛", 
            "example": "Run the race.", "category": "体育健身"
        },
        {
            "english": "contest", "phonetic": "/ˈkɑːntest/", "chinese": "n. 竞赛", 
            "example": "Enter the contest.", "category": "体育健身"
        },
        {
            "english": "competition", "phonetic": "/ˌkɑːmpəˈtɪʃn/", "chinese": "n. 竞争", 
            "example": "Face competition.", "category": "体育健身"
        },
        {
            "english": "tournament", "phonetic": "/ˈtʊrnəmənt/", "chinese": "n. 锦标赛", 
            "example": "Win the tournament.", "category": "体育健身"
        },
        {
            "english": "championship", "phonetic": "/ˈtʃæmpiənʃɪp/", "chinese": "n. 冠军赛", 
            "example": "Compete in championship.", "category": "体育健身"
        },
        {
            "english": "league", "phonetic": "/liːɡ/", "chinese": "n. 联赛", 
            "example": "Join the league.", "category": "体育健身"
        },
        {
            "english": "season", "phonetic": "/ˈsiːzn/", "chinese": "n. 赛季", 
            "example": "Finish the season.", "category": "体育健身"
        },
        {
            "english": "team", "phonetic": "/tiːm/", "chinese": "n. 团队", 
            "example": "Join the team.", "category": "体育健身"
        },
        {
            "english": "player", "phonetic": "/ˈpleɪər/", "chinese": "n. 球员", 
            "example": "The player scored.", "category": "体育健身"
        },
        {
            "english": "coach", "phonetic": "/koʊtʃ/", "chinese": "n. 教练", 
            "example": "The coach trained.", "category": "体育健身"
        },
        {
            "english": "trainer", "phonetic": "/ˈtreɪnər/", "chinese": "n. 训练师", 
            "example": "The trainer helped.", "category": "体育健身"
        },
        {
            "english": "referee", "phonetic": "/ˌrefəˈriː/", "chinese": "n. 裁判", 
            "example": "The referee decided.", "category": "体育健身"
        },
        {
            "english": "umpire", "phonetic": "/ˈʌmpaɪər/", "chinese": "n. 裁判", 
            "example": "The umpire called.", "category": "体育健身"
        },
        {
            "english": "judge", "phonetic": "/dʒʌdʒ/", "chinese": "n. 裁判", 
            "example": "The judge scored.", "category": "体育健身"
        },
        {
            "english": "score", "phonetic": "/skɔːr/", "chinese": "n. 分数", 
            "example": "Check the score.", "category": "体育健身"
        },
        {
            "english": "point", "phonetic": "/pɔɪnt/", "chinese": "n. 得分", 
            "example": "Score a point.", "category": "体育健身"
        },
        {
            "english": "goal", "phonetic": "/ɡoʊl/", "chinese": "n. 进球", 
            "example": "Score a goal.", "category": "体育健身"
        },
        {
            "english": "win", "phonetic": "/wɪn/", "chinese": "n. 胜利", 
            "example": "Achieve a win.", "category": "体育健身"
        },
        # 金融经济类
        {
            "english": "money", "phonetic": "/ˈmʌni/", "chinese": "n. 钱", 
            "example": "Save money.", "category": "金融经济"
        },
        {
            "english": "cash", "phonetic": "/kæʃ/", "chinese": "n. 现金", 
            "example": "Pay with cash.", "category": "金融经济"
        },
        {
            "english": "currency", "phonetic": "/ˈkɜːrənsi/", "chinese": "n. 货币", 
            "example": "Exchange currency.", "category": "金融经济"
        },
        {
            "english": "coin", "phonetic": "/kɔɪn/", "chinese": "n. 硬币", 
            "example": "Flip a coin.", "category": "金融经济"
        },
        {
            "english": "bill", "phonetic": "/bɪl/", "chinese": "n. 钞票", 
            "example": "Pay the bill.", "category": "金融经济"
        },
        {
            "english": "check", "phonetic": "/tʃek/", "chinese": "n. 支票", 
            "example": "Write a check.", "category": "金融经济"
        },
        {
            "english": "credit", "phonetic": "/ˈkredɪt/", "chinese": "n. 信用", 
            "example": "Build credit.", "category": "金融经济"
        },
        {
            "english": "debit", "phonetic": "/ˈdebɪt/", "chinese": "n. 借记", 
            "example": "Use debit.", "category": "金融经济"
        },
        {
            "english": "card", "phonetic": "/kɑːrd/", "chinese": "n. 卡", 
            "example": "Use the card.", "category": "金融经济"
        },
        {
            "english": "bank", "phonetic": "/bæŋk/", "chinese": "n. 银行", 
            "example": "Go to the bank.", "category": "金融经济"
        },
        {
            "english": "account", "phonetic": "/əˈkaʊnt/", "chinese": "n. 账户", 
            "example": "Open an account.", "category": "金融经济"
        },
        {
            "english": "deposit", "phonetic": "/dɪˈpɑːzɪt/", "chinese": "n. 存款", 
            "example": "Make a deposit.", "category": "金融经济"
        },
        {
            "english": "withdrawal", "phonetic": "/wɪðˈdrɔːəl/", "chinese": "n. 取款", 
            "example": "Make a withdrawal.", "category": "金融经济"
        },
        {
            "english": "transfer", "phonetic": "/ˈtrænsfɜːr/", "chinese": "n. 转账", 
            "example": "Make a transfer.", "category": "金融经济"
        },
        {
            "english": "payment", "phonetic": "/ˈpeɪmənt/", "chinese": "n. 支付", 
            "example": "Make payment.", "category": "金融经济"
        },
        {
            "english": "receipt", "phonetic": "/rɪˈsiːt/", "chinese": "n. 收据", 
            "example": "Get a receipt.", "category": "金融经济"
        },
        {
            "english": "invoice", "phonetic": "/ˈɪnvɔɪs/", "chinese": "n. 发票", 
            "example": "Send an invoice.", "category": "金融经济"
        },
        {
            "english": "budget", "phonetic": "/ˈbʌdʒɪt/", "chinese": "n. 预算", 
            "example": "Set a budget.", "category": "金融经济"
        },
        {
            "english": "expense", "phonetic": "/ɪkˈspens/", "chinese": "n. 费用", 
            "example": "Cover the expense.", "category": "金融经济"
        },
        {
            "english": "cost", "phonetic": "/kɔːst/", "chinese": "n. 成本", 
            "example": "Calculate cost.", "category": "金融经济"
        },
        {
            "english": "price", "phonetic": "/praɪs/", "chinese": "n. 价格", 
            "example": "Check the price.", "category": "金融经济"
        },
        # 艺术文化类
        {
            "english": "art", "phonetic": "/ɑːrt/", "chinese": "n. 艺术", 
            "example": "Create art.", "category": "艺术文化"
        },
        {
            "english": "design", "phonetic": "/dɪˈzaɪn/", "chinese": "n. 设计", 
            "example": "Make a design.", "category": "艺术文化"
        },
        {
            "english": "style", "phonetic": "/staɪl/", "chinese": "n. 风格", 
            "example": "Develop style.", "category": "艺术文化"
        },
        {
            "english": "fashion", "phonetic": "/ˈfæʃn/", "chinese": "n. 时尚", 
            "example": "Follow fashion.", "category": "艺术文化"
        },
        {
            "english": "trend", "phonetic": "/trend/", "chinese": "n. 趋势", 
            "example": "Set a trend.", "category": "艺术文化"
        },
        {
            "english": "movement", "phonetic": "/ˈmuːvmənt/", "chinese": "n. 运动", 
            "example": "Join the movement.", "category": "艺术文化"
        },
        {
            "english": "period", "phonetic": "/ˈpɪriəd/", "chinese": "n. 时期", 
            "example": "Study the period.", "category": "艺术文化"
        },
        {
            "english": "era", "phonetic": "/ˈerə/", "chinese": "n. 时代", 
            "example": "Remember the era.", "category": "艺术文化"
        },
        {
            "english": "epoch", "phonetic": "/ˈiːpɑːk/", "chinese": "n. 纪元", 
            "example": "Mark the epoch.", "category": "艺术文化"
        },
        {
            "english": "generation", "phonetic": "/ˌdʒenəˈreɪʃn/", "chinese": "n. 一代人", 
            "example": "Inspire generation.", "category": "艺术文化"
        },
        {
            "english": "influence", "phonetic": "/ˈɪnfluəns/", "chinese": "n. 影响", 
            "example": "Have influence.", "category": "艺术文化"
        },
        {
            "english": "impact", "phonetic": "/ˈɪmpækt/", "chinese": "n. 影响", 
            "example": "Make an impact.", "category": "艺术文化"
        },
        {
            "english": "effect", "phonetic": "/ɪˈfekt/", "chinese": "n. 效果", 
            "example": "See the effect.", "category": "艺术文化"
        },
        {
            "english": "result", "phonetic": "/rɪˈzʌlt/", "chinese": "n. 结果", 
            "example": "Get the result.", "category": "艺术文化"
        },
        {
            "english": "outcome", "phonetic": "/ˈaʊtkʌm/", "chinese": "n. 结果", 
            "example": "Predict the outcome.", "category": "艺术文化"
        },
        {
            "english": "consequence", "phonetic": "/ˈkɑːnsɪkwens/", "chinese": "n. 后果", 
            "example": "Face the consequence.", "category": "艺术文化"
        },
        {
            "english": "implication", "phonetic": "/ˌɪmplɪˈkeɪʃn/", "chinese": "n. 含义", 
            "example": "Understand implication.", "category": "艺术文化"
        },
        {
            "english": "significance", "phonetic": "/sɪɡˈnɪfɪkəns/", "chinese": "n. 重要性", 
            "example": "Recognize significance.", "category": "艺术文化"
        },
        {
            "english": "importance", "phonetic": "/ɪmˈpɔːrtəns/", "chinese": "n. 重要性", 
            "example": "Understand importance.", "category": "艺术文化"
        },
        {
            "english": "value", "phonetic": "/ˈvæljuː/", "chinese": "n. 价值", 
            "example": "Create value.", "category": "艺术文化"
        },
        {
            "english": "worth", "phonetic": "/wɜːrθ/", "chinese": "n. 价值", 
            "example": "Know your worth.", "category": "艺术文化"
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
    expand_to_5000_batch6()
