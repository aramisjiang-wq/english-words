import sqlite3

def expand_to_5000_batch8():
    conn = sqlite3.connect('../words.db')
    cursor = conn.cursor()
    
    new_words = [
        # 科学研究类
        {
            "english": "hypothesis", "phonetic": "/haɪˈpɑːθəsɪs/", "chinese": "n. 假设", 
            "example": "Test hypothesis.", "category": "科学研究"
        },
        {
            "english": "theory", "phonetic": "/ˈθiːəri/", "chinese": "n. 理论", 
            "example": "Develop a theory.", "category": "科学研究"
        },
        {
            "english": "principle", "phonetic": "/ˈprɪnsəpl/", "chinese": "n. 原理", 
            "example": "Apply principle.", "category": "科学研究"
        },
        {
            "english": "concept", "phonetic": "/ˈkɑːnsept/", "chinese": "n. 概念", 
            "example": "Understand concept.", "category": "科学研究"
        },
        {
            "english": "framework", "phonetic": "/ˈfreɪmwɜːrk/", "chinese": "n. 框架", 
            "example": "Build framework.", "category": "科学研究"
        },
        {
            "english": "model", "phonetic": "/ˈmɑːdl/", "chinese": "n. 模型", 
            "example": "Create a model.", "category": "科学研究"
        },
        {
            "english": "simulation", "phonetic": "/ˌsɪmjuˈleɪʃn/", "chinese": "n. 模拟", 
            "example": "Run a simulation.", "category": "科学研究"
        },
        {
            "english": "calculation", "phonetic": "/ˌkælkjuˈleɪʃn/", "chinese": "n. 计算", 
            "example": "Perform calculation.", "category": "科学研究"
        },
        {
            "english": "equation", "phonetic": "/ɪˈkweɪʒn/", "chinese": "n. 方程", 
            "example": "Solve equation.", "category": "科学研究"
        },
        {
            "english": "formula", "phonetic": "/ˈfɔːrmjələ/", "chinese": "n. 公式", 
            "example": "Use formula.", "category": "科学研究"
        },
        {
            "english": "variable", "phonetic": "/ˈveriəbl/", "chinese": "n. 变量", 
            "example": "Change variable.", "category": "科学研究"
        },
        {
            "english": "constant", "phonetic": "/ˈkɑːnstənt/", "chinese": "n. 常量", 
            "example": "The constant is fixed.", "category": "科学研究"
        },
        {
            "english": "parameter", "phonetic": "/pəˈræmɪtər/", "chinese": "n. 参数", 
            "example": "Set parameter.", "category": "科学研究"
        },
        {
            "english": "factor", "phonetic": "/ˈfæktər/", "chinese": "n. 因素", 
            "example": "Consider factor.", "category": "科学研究"
        },
        {
            "english": "element", "phonetic": "/ˈelɪmənt/", "chinese": "n. 元素", 
            "example": "The element is rare.", "category": "科学研究"
        },
        {
            "english": "component", "phonetic": "/kəmˈpoʊnənt/", "chinese": "n. 组件", 
            "example": "Replace component.", "category": "科学研究"
        },
        {
            "english": "structure", "phonetic": "/ˈstrʌktʃər/", "chinese": "n. 结构", 
            "example": "Analyze structure.", "category": "科学研究"
        },
        {
            "english": "function", "phonetic": "/ˈfʌŋkʃn/", "chinese": "n. 功能", 
            "example": "Test function.", "category": "科学研究"
        },
        {
            "english": "mechanism", "phonetic": "/ˈmekənɪzəm/", "chinese": "n. 机制", 
            "example": "Study mechanism.", "category": "科学研究"
        },
        {
            "english": "process", "phonetic": "/ˈprɑːses/", "chinese": "n. 过程", 
            "example": "Follow process.", "category": "科学研究"
        },
        # 商业管理类
        {
            "english": "strategy", "phonetic": "/ˈstrætədʒi/", "chinese": "n. 战略", 
            "example": "Develop a strategy.", "category": "商业管理"
        },
        {
            "english": "tactic", "phonetic": "/ˈtæktɪk/", "chinese": "n. 战术", 
            "example": "Use a tactic.", "category": "商业管理"
        },
        {
            "english": "plan", "phonetic": "/plæn/", "chinese": "n. 计划", 
            "example": "Make a plan.", "category": "商业管理"
        },
        {
            "english": "schedule", "phonetic": "/ˈskedʒuːl/", "chinese": "n. 时间表", 
            "example": "Follow schedule.", "category": "商业管理"
        },
        {
            "english": "deadline", "phonetic": "/ˈdedlaɪn/", "chinese": "n. 截止日期", 
            "example": "Meet deadline.", "category": "商业管理"
        },
        {
            "english": "milestone", "phonetic": "/ˈmaɪlstoʊn/", "chinese": "n. 里程碑", 
            "example": "Reach a milestone.", "category": "商业管理"
        },
        {
            "english": "objective", "phonetic": "/əbˈdʒektɪv/", "chinese": "n. 目标", 
            "example": "Set an objective.", "category": "商业管理"
        },
        {
            "english": "target", "phonetic": "/ˈtɑːrɡɪt/", "chinese": "n. 目标", 
            "example": "Hit target.", "category": "商业管理"
        },
        {
            "english": "goal", "phonetic": "/ɡoʊl/", "chinese": "n. 目标", 
            "example": "Achieve goal.", "category": "商业管理"
        },
        {
            "english": "purpose", "phonetic": "/ˈpɜːrpəs/", "chinese": "n. 目的", 
            "example": "Clarify purpose.", "category": "商业管理"
        },
        {
            "english": "mission", "phonetic": "/ˈmɪʃn/", "chinese": "n. 使命", 
            "example": "Fulfill mission.", "category": "商业管理"
        },
        {
            "english": "vision", "phonetic": "/ˈvɪʒn/", "chinese": "n. 愿景", 
            "example": "Share vision.", "category": "商业管理"
        },
        {
            "english": "value", "phonetic": "/ˈvæljuː/", "chinese": "n. 价值", 
            "example": "Create value.", "category": "商业管理"
        },
        {
            "english": "benefit", "phonetic": "/ˈbenɪfɪt/", "chinese": "n. 利益", 
            "example": "Provide a benefit.", "category": "商业管理"
        },
        {
            "english": "advantage", "phonetic": "/ədˈvæntɪdʒ/", "chinese": "n. 优势", 
            "example": "Gain an advantage.", "category": "商业管理"
        },
        {
            "english": "opportunity", "phonetic": "/ˌɑːpərˈtuːnəti/", "chinese": "n. 机会", 
            "example": "Seize opportunity.", "category": "商业管理"
        },
        {
            "english": "challenge", "phonetic": "/ˈtʃælɪndʒ/", "chinese": "n. 挑战", 
            "example": "Face challenge.", "category": "商业管理"
        },
        {
            "english": "risk", "phonetic": "/rɪsk/", "chinese": "n. 风险", 
            "example": "Manage risk.", "category": "商业管理"
        },
        {
            "english": "reward", "phonetic": "/rɪˈwɔːrd/", "chinese": "n. 回报", 
            "example": "Earn a reward.", "category": "商业管理"
        },
        {
            "english": "profit", "phonetic": "/ˈprɑːfɪt/", "chinese": "n. 利润", 
            "example": "Increase profit.", "category": "商业管理"
        },
        # 法律政治类
        {
            "english": "law", "phonetic": "/lɔː/", "chinese": "n. 法律", 
            "example": "Obey law.", "category": "法律政治"
        },
        {
            "english": "rule", "phonetic": "/ruːl/", "chinese": "n. 规则", 
            "example": "Follow rule.", "category": "法律政治"
        },
        {
            "english": "regulation", "phonetic": "/ˌreɡjuˈleɪʃn/", "chinese": "n. 法规", 
            "example": "Comply with regulation.", "category": "法律政治"
        },
        {
            "english": "policy", "phonetic": "/ˈpɑːləsi/", "chinese": "n. 政策", 
            "example": "Implement policy.", "category": "法律政治"
        },
        {
            "english": "procedure", "phonetic": "/prəˈsiːdʒər/", "chinese": "n. 程序", 
            "example": "Follow procedure.", "category": "法律政治"
        },
        {
            "english": "protocol", "phonetic": "/ˈproʊtəkɑːl/", "chinese": "n. 协议", 
            "example": "Adhere to protocol.", "category": "法律政治"
        },
        {
            "english": "standard", "phonetic": "/ˈstændərd/", "chinese": "n. 标准", 
            "example": "Meet standard.", "category": "法律政治"
        },
        {
            "english": "requirement", "phonetic": "/rɪˈkwaɪərmənt/", "chinese": "n. 要求", 
            "example": "Satisfy requirement.", "category": "法律政治"
        },
        {
            "english": "obligation", "phonetic": "/ˌɑːblɪˈɡeɪʃn/", "chinese": "n. 义务", 
            "example": "Fulfill obligation.", "category": "法律政治"
        },
        {
            "english": "responsibility", "phonetic": "/rɪˌspɑːnsəˈbɪləti/", "chinese": "n. 责任", 
            "example": "Accept responsibility.", "category": "法律政治"
        },
        {
            "english": "accountability", "phonetic": "/əˌkaʊntəˈbɪləti/", "chinese": "n. 问责制", 
            "example": "Ensure accountability.", "category": "法律政治"
        },
        {
            "english": "authority", "phonetic": "/əˈθɔːrəti/", "chinese": "n. 权威", 
            "example": "Exercise authority.", "category": "法律政治"
        },
        {
            "english": "power", "phonetic": "/ˈpaʊər/", "chinese": "n. 权力", 
            "example": "Wield power.", "category": "法律政治"
        },
        {
            "english": "influence", "phonetic": "/ˈɪnfluəns/", "chinese": "n. 影响", 
            "example": "Use influence.", "category": "法律政治"
        },
        {
            "english": "control", "phonetic": "/kənˈtroʊl/", "chinese": "n. 控制", 
            "example": "Maintain control.", "category": "法律政治"
        },
        {
            "english": "supervision", "phonetic": "/ˌsuːpərˈvɪʒn/", "chinese": "n. 监督", 
            "example": "Provide supervision.", "category": "法律政治"
        },
        {
            "english": "oversight", "phonetic": "/ˈoʊvərsaɪt/", "chinese": "n. 监管", 
            "example": "Exercise oversight.", "category": "法律政治"
        },
        {
            "english": "monitoring", "phonetic": "/ˈmɑːnɪtərɪŋ/", "chinese": "n. 监控", 
            "example": "Conduct monitoring.", "category": "法律政治"
        },
        {
            "english": "inspection", "phonetic": "/ɪnˈspekʃn/", "chinese": "n. 检查", 
            "example": "Perform inspection.", "category": "法律政治"
        },
        {
            "english": "audit", "phonetic": "/ˈɔːdɪt/", "chinese": "n. 审计", 
            "example": "Conduct an audit.", "category": "法律政治"
        },
        # 医疗健康类
        {
            "english": "health", "phonetic": "/helθ/", "chinese": "n. 健康", 
            "example": "Maintain health.", "category": "医疗健康"
        },
        {
            "english": "wellness", "phonetic": "/ˈwelnəs/", "chinese": "n. 健康", 
            "example": "Promote wellness.", "category": "医疗健康"
        },
        {
            "english": "fitness", "phonetic": "/ˈfɪtnəs/", "chinese": "n. 健身", 
            "example": "Improve fitness.", "category": "医疗健康"
        },
        {
            "english": "exercise", "phonetic": "/ˈeksərsaɪz/", "chinese": "n. 运动", 
            "example": "Do exercise.", "category": "医疗健康"
        },
        {
            "english": "nutrition", "phonetic": "/nuːˈtrɪʃn/", "chinese": "n. 营养", 
            "example": "Focus on nutrition.", "category": "医疗健康"
        },
        {
            "english": "diet", "phonetic": "/ˈdaɪət/", "chinese": "n. 饮食", 
            "example": "Follow a diet.", "category": "医疗健康"
        },
        {
            "english": "supplement", "phonetic": "/ˈsʌplɪmənt/", "chinese": "n. 补充剂", 
            "example": "Take a supplement.", "category": "医疗健康"
        },
        {
            "english": "vitamin", "phonetic": "/ˈvaɪtəmɪn/", "chinese": "n. 维生素", 
            "example": "Get enough vitamins.", "category": "医疗健康"
        },
        {
            "english": "mineral", "phonetic": "/ˈmɪnərəl/", "chinese": "n. 矿物质", 
            "example": "Consume minerals.", "category": "医疗健康"
        },
        {
            "english": "protein", "phonetic": "/ˈproʊtiːn/", "chinese": "n. 蛋白质", 
            "example": "Eat protein.", "category": "医疗健康"
        },
        {
            "english": "carbohydrate", "phonetic": "/ˌkɑːrboʊˈhaɪdreɪt/", "chinese": "n. 碳水化合物", 
            "example": "Limit carbohydrates.", "category": "医疗健康"
        },
        {
            "english": "fat", "phonetic": "/fæt/", "chinese": "n. 脂肪", 
            "example": "Reduce fat.", "category": "医疗健康"
        },
        {
            "english": "fiber", "phonetic": "/ˈfaɪbər/", "chinese": "n. 纤维", 
            "example": "Eat fiber.", "category": "医疗健康"
        },
        {
            "english": "hydration", "phonetic": "/haɪˈdreɪʃn/", "chinese": "n. 水分", 
            "example": "Maintain hydration.", "category": "医疗健康"
        },
        {
            "english": "sleep", "phonetic": "/sliːp/", "chinese": "n. 睡眠", 
            "example": "Get enough sleep.", "category": "医疗健康"
        },
        {
            "english": "rest", "phonetic": "/rest/", "chinese": "n. 休息", 
            "example": "Take a rest.", "category": "医疗健康"
        },
        {
            "english": "recovery", "phonetic": "/rɪˈkʌvəri/", "chinese": "n. 恢复", 
            "example": "Speed up recovery.", "category": "医疗健康"
        },
        {
            "english": "rehabilitation", "phonetic": "/ˌriːəˌbɪlɪˈteɪʃn/", "chinese": "n. 康复", 
            "example": "Complete rehabilitation.", "category": "医疗健康"
        },
        {
            "english": "therapy", "phonetic": "/ˈθerəpi/", "chinese": "n. 疗法", 
            "example": "Attend therapy.", "category": "医疗健康"
        },
        {
            "english": "treatment", "phonetic": "/ˈtriːtmənt/", "chinese": "n. 治疗", 
            "example": "Receive treatment.", "category": "医疗健康"
        },
        # 教育学习类
        {
            "english": "knowledge", "phonetic": "/ˈnɑːlɪdʒ/", "chinese": "n. 知识", 
            "example": "Gain knowledge.", "category": "教育学习"
        },
        {
            "english": "wisdom", "phonetic": "/ˈwɪzdəm/", "chinese": "n. 智慧", 
            "example": "Seek wisdom.", "category": "教育学习"
        },
        {
            "english": "insight", "phonetic": "/ˈɪnsaɪt/", "chinese": "n. 洞察", 
            "example": "Gain insight.", "category": "教育学习"
        },
        {
            "english": "understanding", "phonetic": "/ˌʌndərˈstændɪŋ/", "chinese": "n. 理解", 
            "example": "Show understanding.", "category": "教育学习"
        },
        {
            "english": "comprehension", "phonetic": "/ˌkɑːmprɪˈhenʃn/", "chinese": "n. 理解", 
            "example": "Test comprehension.", "category": "教育学习"
        },
        {
            "english": "perception", "phonetic": "/pərˈsepʃn/", "chinese": "n. 感知", 
            "example": "Change perception.", "category": "教育学习"
        },
        {
            "english": "awareness", "phonetic": "/əˈwernəs/", "chinese": "n. 意识", 
            "example": "Raise awareness.", "category": "教育学习"
        },
        {
            "english": "consciousness", "phonetic": "/ˈkɑːnʃəsnəs/", "chinese": "n. 意识", 
            "example": "Expand consciousness.", "category": "教育学习"
        },
        {
            "english": "mindfulness", "phonetic": "/ˈmaɪndfʊlnəs/", "chinese": "n. 正念", 
            "example": "Practice mindfulness.", "category": "教育学习"
        },
        {
            "english": "attention", "phonetic": "/əˈtenʃn/", "chinese": "n. 注意力", 
            "example": "Pay attention.", "category": "教育学习"
        },
        {
            "english": "focus", "phonetic": "/ˈfoʊkəs/", "chinese": "n. 焦点", 
            "example": "Maintain focus.", "category": "教育学习"
        },
        {
            "english": "concentration", "phonetic": "/ˌkɑːnsənˈtreɪʃn/", "chinese": "n. 专注", 
            "example": "Improve concentration.", "category": "教育学习"
        },
        {
            "english": "memory", "phonetic": "/ˈmeməri/", "chinese": "n. 记忆", 
            "example": "Improve memory.", "category": "教育学习"
        },
        {
            "english": "recall", "phonetic": "/rɪˈkɔːl/", "chinese": "n. 回忆", 
            "example": "Test recall.", "category": "教育学习"
        },
        {
            "english": "recognition", "phonetic": "/ˌrekəɡˈnɪʃn/", "chinese": "n. 识别", 
            "example": "Show recognition.", "category": "教育学习"
        },
        {
            "english": "retention", "phonetic": "/rɪˈtenʃn/", "chinese": "n. 保持", 
            "example": "Improve retention.", "category": "教育学习"
        },
        {
            "english": "application", "phonetic": "/ˌæplɪˈkeɪʃn/", "chinese": "n. 应用", 
            "example": "Apply knowledge.", "category": "教育学习"
        },
        {
            "english": "practice", "phonetic": "/ˈpræktɪs/", "chinese": "n. 练习", 
            "example": "Regular practice.", "category": "教育学习"
        },
        {
            "english": "experience", "phonetic": "/ɪkˈspɪriəns/", "chinese": "n. 经验", 
            "example": "Gain experience.", "category": "教育学习"
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
            "english": "advancement", "phonetic": "/ədˈvænsmənt/", "chinese": "n. 进步", 
            "example": "Make advancement.", "category": "技术创新"
        },
        {
            "english": "breakthrough", "phonetic": "/ˈbreɪkθruː/", "chinese": "n. 突破", 
            "example": "Achieve breakthrough.", "category": "技术创新"
        },
        {
            "english": "discovery", "phonetic": "/dɪsˈkʌvəri/", "chinese": "n. 发现", 
            "example": "Make a discovery.", "category": "技术创新"
        },
        {
            "english": "invention", "phonetic": "/ɪnˈvenʃn/", "chinese": "n. 发明", 
            "example": "Create an invention.", "category": "技术创新"
        },
        {
            "english": "creation", "phonetic": "/kriˈeɪʃn/", "chinese": "n. 创造", 
            "example": "Make a creation.", "category": "技术创新"
        },
        {
            "english": "development", "phonetic": "/dɪˈveləpmənt/", "chinese": "n. 开发", 
            "example": "Complete development.", "category": "技术创新"
        },
        {
            "english": "implementation", "phonetic": "/ˌɪmplɪmenˈteɪʃn/", "chinese": "n. 实施", 
            "example": "Start implementation.", "category": "技术创新"
        },
        {
            "english": "deployment", "phonetic": "/dɪˈplɔɪmənt/", "chinese": "n. 部署", 
            "example": "Complete deployment.", "category": "技术创新"
        },
        {
            "english": "integration", "phonetic": "/ˌɪntɪˈɡreɪʃn/", "chinese": "n. 集成", 
            "example": "Achieve integration.", "category": "技术创新"
        },
        {
            "english": "optimization", "phonetic": "/ˌɑːptɪməˈzeɪʃn/", "chinese": "n. 优化", 
            "example": "Perform optimization.", "category": "技术创新"
        },
        {
            "english": "enhancement", "phonetic": "/ɪnˈhænsmənt/", "chinese": "n. 增强", 
            "example": "Provide enhancement.", "category": "技术创新"
        },
        {
            "english": "improvement", "phonetic": "/ɪmˈpruːvmənt/", "chinese": "n. 改进", 
            "example": "Make improvement.", "category": "技术创新"
        },
        {
            "english": "modification", "phonetic": "/ˌmɑːdɪfɪˈkeɪʃn/", "chinese": "n. 修改", 
            "example": "Apply modification.", "category": "技术创新"
        },
        {
            "english": "adaptation", "phonetic": "/ˌædæpˈteɪʃn/", "chinese": "n. 适应", 
            "example": "Make adaptation.", "category": "技术创新"
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
            "english": "automation", "phonetic": "/ˌɔːtəˈmeɪʃn/", "chinese": "n. 自动化", 
            "example": "Implement automation.", "category": "技术创新"
        },
        {
            "english": "digitization", "phonetic": "/ˌdɪdʒɪtaɪˈzeɪʃn/", "chinese": "n. 数字化", 
            "example": "Complete digitization.", "category": "技术创新"
        },
        # 自然地理类
        {
            "english": "nature", "phonetic": "/ˈneɪtʃər/", "chinese": "n. 自然", 
            "example": "Respect nature.", "category": "自然地理"
        },
        {
            "english": "environment", "phonetic": "/ɪnˈvaɪrənmənt/", "chinese": "n. 环境", 
            "example": "Protect environment.", "category": "自然地理"
        },
        {
            "english": "ecosystem", "phonetic": "/ˈiːkoʊsɪstəm/", "chinese": "n. 生态系统", 
            "example": "Study ecosystem.", "category": "自然地理"
        },
        {
            "english": "habitat", "phonetic": "/ˈhæbɪtæt/", "chinese": "n. 栖息地", 
            "example": "Preserve habitat.", "category": "自然地理"
        },
        {
            "english": "species", "phonetic": "/ˈspiːʃiːz/", "chinese": "n. 物种", 
            "example": "Protect species.", "category": "自然地理"
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
            "english": "clean", "phonetic": "/kliːn/", "chinese": "adj. 清洁的", 
            "example": "Clean energy.", "category": "自然地理"
        },
        {
            "english": "green", "phonetic": "/ɡriːn/", "chinese": "adj. 绿色的", 
            "example": "Green technology.", "category": "自然地理"
        },
        {
            "english": "eco-friendly", "phonetic": "/ˈiːkoʊ ˈfrendli/", "chinese": "adj. 环保的", 
            "example": "Eco-friendly products.", "category": "自然地理"
        },
        {
            "english": "organic", "phonetic": "/ɔːrˈɡænɪk/", "chinese": "adj. 有机的", 
            "example": "Organic food.", "category": "自然地理"
        },
        {
            "english": "natural", "phonetic": "/ˈnætʃrəl/", "chinese": "adj. 自然的", 
            "example": "Natural resources.", "category": "自然地理"
        },
        {
            "english": "wild", "phonetic": "/waɪld/", "chinese": "adj. 野生的", 
            "example": "Wild animals.", "category": "自然地理"
        },
        {
            "english": "native", "phonetic": "/ˈneɪtɪv/", "chinese": "adj. 本土的", 
            "example": "Native species.", "category": "自然地理"
        },
        {
            "english": "indigenous", "phonetic": "/ɪnˈdɪdʒənəs/", "chinese": "adj. 土著的", 
            "example": "Indigenous plants.", "category": "自然地理"
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
            "example": "See landmark.", "category": "社会文化"
        },
        {
            "english": "symbol", "phonetic": "/ˈsɪmbl/", "chinese": "n. 象征", 
            "example": "The symbol represents.", "category": "社会文化"
        },
        {
            "english": "icon", "phonetic": "/ˈaɪkɑːn/", "chinese": "n. 图标", 
            "example": "Cultural icon.", "category": "社会文化"
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
        # 旅行交通类
        {
            "english": "travel", "phonetic": "/ˈtrævl/", "chinese": "n. 旅行", 
            "example": "Love to travel.", "category": "旅行交通"
        },
        {
            "english": "trip", "phonetic": "/trɪp/", "chinese": "n. 旅行", 
            "example": "Take a trip.", "category": "旅行交通"
        },
        {
            "english": "tour", "phonetic": "/tʊr/", "chinese": "n. 旅游", 
            "example": "Go on a tour.", "category": "旅行交通"
        },
        {
            "english": "vacation", "phonetic": "/veɪˈkeɪʃn/", "chinese": "n. 假期", 
            "example": "Enjoy vacation.", "category": "旅行交通"
        },
        {
            "english": "holiday", "phonetic": "/ˈhɑːlədeɪ/", "chinese": "n. 假日", 
            "example": "Celebrate holiday.", "category": "旅行交通"
        },
        {
            "english": "break", "phonetic": "/breɪk/", "chinese": "n. 休息", 
            "example": "Take a break.", "category": "旅行交通"
        },
        {
            "english": "getaway", "phonetic": "/ˈɡetəweɪ/", "chinese": "n. 短途旅行", 
            "example": "Plan a getaway.", "category": "旅行交通"
        },
        {
            "english": "escape", "phonetic": "/ɪˈskeɪp/", "chinese": "n. 逃避", 
            "example": "Need an escape.", "category": "旅行交通"
        },
        {
            "english": "adventure", "phonetic": "/ədˈventʃər/", "chinese": "n. 冒险", 
            "example": "Seek adventure.", "category": "旅行交通"
        },
        {
            "english": "expedition", "phonetic": "/ˌekspəˈdɪʃn/", "chinese": "n. 探险", 
            "example": "Join expedition.", "category": "旅行交通"
        },
        {
            "english": "journey", "phonetic": "/ˈdʒɜːrni/", "chinese": "n. 旅程", 
            "example": "Begin the journey.", "category": "旅行交通"
        },
        {
            "english": "voyage", "phonetic": "/ˈvɔɪɪdʒ/", "chinese": "n. 航行", 
            "example": "Complete the voyage.", "category": "旅行交通"
        },
        {
            "english": "cruise", "phonetic": "/kruːz/", "chinese": "n. 巡航", 
            "example": "Go on a cruise.", "category": "旅行交通"
        },
        {
            "english": "safari", "phonetic": "/səˈfɑːri/", "chinese": "n. 狩猎旅行", 
            "example": "Go on safari.", "category": "旅行交通"
        },
        {
            "english": "trek", "phonetic": "/trek/", "chinese": "n. 徒步旅行", 
            "example": "Go on a trek.", "category": "旅行交通"
        },
        {
            "english": "hike", "phonetic": "/haɪk/", "chinese": "n. 徒步", 
            "example": "Take a hike.", "category": "旅行交通"
        },
        {
            "english": "camping", "phonetic": "/ˈkæmpɪŋ/", "chinese": "n. 露营", 
            "example": "Go camping.", "category": "旅行交通"
        },
        {
            "english": "backpacking", "phonetic": "/ˈbækpækɪŋ/", "chinese": "n. 背包旅行", 
            "example": "Go backpacking.", "category": "旅行交通"
        },
        {
            "english": "road trip", "phonetic": "/roʊd trɪp/", "chinese": "n. 公路旅行", 
            "example": "Take a road trip.", "category": "旅行交通"
        },
        # 食物烹饪类
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
            "english": "stewing", "phonetic": "/ˈstjuːɪŋ/", "chinese": "n. 炖", 
            "example": "Start stewing.", "category": "食物烹饪"
        },
        {
            "english": "braising", "phonetic": "/ˈbreɪzɪŋ/", "chinese": "n. 炖煮", 
            "example": "Try braising.", "category": "食物烹饪"
        },
        {
            "english": "poaching", "phonetic": "/ˈpoʊtʃɪŋ/", "chinese": "n. 水煮", 
            "example": "Practice poaching.", "category": "食物烹饪"
        },
        {
            "english": "blanching", "phonetic": "/ˈblæntʃɪŋ/", "chinese": "n. 焯水", 
            "example": "Try blanching.", "category": "食物烹饪"
        },
        {
            "english": "glazing", "phonetic": "/ˈɡleɪzɪŋ/", "chinese": "n. 上光", 
            "example": "Apply glazing.", "category": "食物烹饪"
        },
        {
            "english": "caramelizing", "phonetic": "/ˈkærəməlaɪzɪŋ/", "chinese": "n. 焦糖化", 
            "example": "Caramelize the sugar.", "category": "食物烹饪"
        },
        {
            "english": "fermenting", "phonetic": "/fərˈmentɪŋ/", "chinese": "n. 发酵", 
            "example": "Start fermenting.", "category": "食物烹饪"
        },
        {
            "english": "curing", "phonetic": "/ˈkjʊrɪŋ/", "chinese": "n. 腌制", 
            "example": "Practice curing.", "category": "食物烹饪"
        },
        {
            "english": "smoking", "phonetic": "/ˈsmoʊkɪŋ/", "chinese": "n. 熏制", 
            "example": "Try smoking.", "category": "食物烹饪"
        },
        {
            "english": "drying", "phonetic": "/ˈdraɪɪŋ/", "chinese": "n. 干燥", 
            "example": "Start drying.", "category": "食物烹饪"
        },
        {
            "english": "pickling", "phonetic": "/ˈpɪklɪŋ/", "chinese": "n. 腌制", 
            "example": "Practice pickling.", "category": "食物烹饪"
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
            "english": "temperament", "phonetic": "/ˈtempərəmənt/", "chinese": "n. 气质", 
            "example": "Show temperament.", "category": "心理情感"
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
            "english": "nature", "phonetic": "/ˈneɪtʃər/", "chinese": "n. 本性", 
            "example": "Human nature.", "category": "心理情感"
        },
        {
            "english": "disposition", "phonetic": "/ˌdɪspəˈzɪʃn/", "chinese": "n. 性情", 
            "example": "Show disposition.", "category": "心理情感"
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
            "example": "Use card.", "category": "金融经济"
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
            "example": "Cover expense.", "category": "金融经济"
        },
        {
            "english": "cost", "phonetic": "/kɔːst/", "chinese": "n. 成本", 
            "example": "Calculate cost.", "category": "金融经济"
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
            "example": "Predict outcome.", "category": "艺术文化"
        },
        {
            "english": "consequence", "phonetic": "/ˈkɑːnsɪkwens/", "chinese": "n. 后果", 
            "example": "Face consequence.", "category": "艺术文化"
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
    expand_to_5000_batch8()
