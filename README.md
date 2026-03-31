# 英语单词学习系统 - 项目结构

## 文件结构

```
English Words/
├── index.html              # 主页面（前端应用）
├── words.db               # SQLite 数据库
├── data/                 # 数据文件目录
│   ├── words_merged.json   # 合并后的单词数据（主数据源）
│   ├── words.json         # 原始单词数据
│   ├── expanded_words.json
│   └── expanded_words_part2.json
├── scripts/              # Python 脚本目录
│   ├── init_db.py        # 数据库初始化
│   ├── export_db_to_json.py # 导出数据库到 JSON
│   ├── check_duplicates.py # 检查重复单词
│   ├── check_count.py     # 统计单词数量
│   ├── check_words_table.py # 检查数据库表结构
│   ├── check_table_structure.py # 检查表结构
│   ├── convert.py        # Markdown 转 JSON
│   ├── expand_to_5000.py # 扩展词汇到 5000
│   ├── expand_to_5000_part2.py
│   ├── expand_to_5000_part3.py
│   ├── expand_to_5000_final.py
│   ├── expand_common_words.py
│   ├── expand_comprehensive.py
│   ├── expand_massive.py
│   ├── expand_vocabulary.py
│   ├── expand_vocabulary_part2.py
│   └── expand_vocabulary_part3.py
└── docs/                # 文档目录
    ├── VOCABULARY_SUMMARY.md
    └── 英文单词分类大全.md
```

## 使用说明

### 运行前端应用
直接在浏览器中打开 `index.html`，或使用本地服务器：
```bash
python3 -m http.server 8000
```
然后访问 `http://localhost:8000`

### 运行 Python 脚本
所有脚本都需要在 `scripts/` 目录下运行：
```bash
cd scripts
python3 script_name.py
```

### 主要脚本说明

- **init_db.py**: 初始化数据库并导入单词数据
- **export_db_to_json.py**: 从数据库导出单词到 JSON（供前端使用）
- **check_duplicates.py**: 检查数据库中是否有重复单词
- **check_count.py**: 统计数据库中的单词数量
- **convert.py**: 将 Markdown 格式的单词列表转换为 JSON

### 数据流程

1. **原始数据**: `docs/英文单词分类大全.md` (Markdown 格式)
2. **转换**: `scripts/convert.py` → `data/words.json`
3. **导入数据库**: `scripts/init_db.py` → `words.db`
4. **导出 JSON**: `scripts/export_db_to_json.py` → `data/words_merged.json`
5. **前端使用**: `index.html` 加载 `data/words_merged.json`

## 部署到 Vercel

1. 将项目推送到 GitHub
2. 在 Vercel 中导入仓库
3. 配置：
   - Framework Preset: Other
   - Root Directory: ./
   - Build Command: (留空)
   - Output Directory: ./
4. 部署完成

注意：部署时只需上传 `index.html` 和 `data/words_merged.json`，其他文件用于开发和管理。
