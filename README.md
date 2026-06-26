# 英语单词学习系统

一个专注、优雅的纯前端英语单词学习应用：5000+ 单词分类浏览、间隔复习（SM-2）、测验 / 造句 / 听力 / 拼写多种练习模式，以及学习分析与成就系统。零依赖、零构建，一个静态服务器即可运行。

![tech](https://img.shields.io/badge/stack-Vanilla_JS-informational) ![build](https://img.shields.io/badge/build-none-success) ![theme](https://img.shields.io/badge/theme-light%2Fdark-blueviolet)

## ✨ 功能特性

- **单词 + 场景短语**：除 5000+ 单词外，内置按场景组织的「短语 / 词块」库(餐厅、机场、会议、看病…),复用同一套学习/复习引擎。流利表达靠的是成块的搭配与句型(lexical chunks),而非孤立单词。
- **分类浏览**：词性 / 主题(单词)与 类型 / 场景(短语)多维筛选，分页浏览。
- **间隔复习**：基于 SM-2 的轻量调度器，按记忆曲线安排到期复习；测验 / 听力 / 拼写 / 造句的每次作答都会反馈到复习引擎。
- **熟练度（基于表现的掌握）**：把“掌握”从点按钮升级为 0–5 级熟练度——区分「认识」(recognition) 与「会用」(production)。一个词需在拼写 / 听写 / 造句等产出技能上答对、并经间隔复习存活，才升到「会用 / 精通」。「掌握度」分析页给出等级分布与诚实的流利度说明。
- **多种练习**：词汇测验（支持 A–D / 1–4 键盘作答）、造句练习、听力听写、拼写填空。
- **学习分析**：本月学习热力图、掌握率趋势折线图、全局单词状态点图。
- **成就系统**：掌握里程碑与连续学习天数等 11 项成就。
- **每日目标**：进度环实时显示当日已学单词数 / 目标。
- **克制的设计语言**：纸感（paper & ink）配色、Fraunces 衬线词头、统一描边图标，避免堆砌 emoji 与高饱和色块。
- **浅色 / 深色主题**：跟随系统并可手动切换，选择会被记住。
- **本地持久化**：全部进度保存在浏览器 `localStorage`，无需登录与后端。

## 🗂 项目结构

```
English Words/
├── index.html              # 应用外壳（结构 + 主题预设）
├── css/
│   └── styles.css          # 设计系统（设计令牌 / 浅深双主题 / 响应式）
├── js/
│   ├── app.js              # 应用主逻辑（状态、页面、练习、分析）
│   ├── icons.js            # 内联 SVG 图标集（替代 emoji，统一描边风格）
│   ├── filter-render.js    # 单词筛选与卡片渲染
│   ├── learning-utils.js   # 采样、测验生成、SM-2 间隔复习调度
│   ├── session-renderers.js# 测验/练习/听力/拼写的视图模板
│   └── ui-feedback.js      # Toast 通知与确认对话框（替代 alert/confirm）
├── data/
│   ├── words_merged.json   # 单词主数据源
│   └── phrases.json        # 场景短语库（由 scripts/build_phrases.py 生成）
├── scripts/                # 数据生成 / 维护用的 Python 脚本
└── docs/                   # 词汇与设计文档
```

### 前端架构

应用按职责拆分为独立模块，均以 `window.*` 命名空间挂载，无打包步骤：

| 模块 | 职责 |
| --- | --- |
| `css/styles.css` | 以 CSS 变量定义的设计令牌，统一驱动浅 / 深主题与全部组件样式 |
| `js/app.js` | 状态管理、数据加载、筛选、练习流程、分析渲染、键盘快捷键 |
| `js/icons.js` | `Icon` / `hydrateIcons`：内联 SVG 图标集，替换 UI 中的 emoji |
| `js/learning-utils.js` | `WordLearningUtils`：采样、测验选项、SM-2 调度（`scheduleNext` / `collectDueKeys`） |
| `js/filter-render.js` | `WordFilterRender`：多维索引、筛选与卡片 HTML 渲染 |
| `js/session-renderers.js` | `WordSessionRenderers`：各练习模式的纯函数视图模板 |
| `js/ui-feedback.js` | `UI`：toast / Promise 化 confirm 对话框 |

数据流：单词以稳定的 `__key`（`english::chinese::category` + 去重序号）标识，单词状态、复习记录与学习历史均按该键持久化，避免重复词冲突。

## 🚀 本地运行

应用通过 `fetch` 加载 JSON，需经本地服务器访问（不能直接 `file://` 打开）：

```bash
python3 -m http.server 8000
# 然后访问 http://localhost:8000
```

## ⌨️ 键盘快捷键

| 快捷键 | 操作 |
| --- | --- |
| `Ctrl/⌘ + K` | 聚焦搜索框 |
| `Ctrl/⌘ + Q` | 开始测验 |
| `Ctrl/⌘ + P` | 造句练习 |
| `Ctrl/⌘ + R` | 智能复习 |
| `Ctrl/⌘ + L` | 听力练习 |
| `Ctrl/⌘ + S` | 学习分析 |
| `Ctrl/⌘ + A` | 成就系统 |
| `A`–`D` / `1`–`4` | 测验中选择选项 |
| `Esc` | 关闭弹窗 |

## 🛠 数据维护（可选）

`scripts/` 下的 Python 脚本用于生成与校验词库，前端运行不依赖它们。

| 脚本 | 说明 |
| --- | --- |
| `convert.py` | 将 `docs/英文单词分类大全.md` 转为 JSON |
| `init_db.py` | 初始化 SQLite 并导入单词 |
| `export_db_to_json.py` | 从数据库导出 `data/words_merged.json` |
| `check_duplicates.py` / `check_count.py` | 校验重复与统计数量 |

数据流程：`docs/*.md` → `convert.py` → `words.json` → `init_db.py` → SQLite → `export_db_to_json.py` → `data/words_merged.json` → 前端加载。

## ☁️ 部署

任意静态托管（Vercel / Netlify / GitHub Pages）均可，无需构建：

1. 推送到 GitHub；
2. 导入仓库，Framework Preset 选 **Other**，Build Command 留空，Output Directory 设为 `./`；
3. 部署完成。

运行时仅需 `index.html`、`css/`、`js/` 与 `data/words_merged.json`。
