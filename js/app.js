/* ============================================================
   英语单词学习系统 — application logic
   Depends on: filter-render.js, learning-utils.js,
   session-renderers.js, ui-feedback.js
   ============================================================ */
(() => {
  "use strict";

  const LU = window.WordLearningUtils;
  const UI = window.UI;
  const $ = (id) => document.getElementById(id);

  /* ---------- State ---------- */
  let wordsData = [];
  let wordByKey = new Map();
  let wordStatus = {};
  let quizWords = [];
  let currentQuizIndex = 0;
  let quizScore = 0;
  let learningHistory = {};
  let wordReviewData = {};
  let isReviewMode = false;
  let achievements = {};
  let wordIndexes = null;
  let batchMode = false;
  let selectedWords = new Set();
  let dailyGoal = 20;

  let selectedVoice = null;
  let speechRate = 0.9;
  let availableVoices = [];

  /* ---------- Storage helpers ---------- */
  const store = {
    get(key, fallback) {
      try {
        const raw = localStorage.getItem(key);
        return raw === null ? fallback : JSON.parse(raw);
      } catch {
        return fallback;
      }
    },
    set(key, value) {
      localStorage.setItem(key, JSON.stringify(value));
    },
    remove(key) {
      localStorage.removeItem(key);
    },
  };

  const saveStatus = () => store.set("wordStatus", wordStatus);
  const saveLearningHistory = () => store.set("learningHistory", learningHistory);
  const saveReviewData = () => store.set("wordReviewData", wordReviewData);
  const saveAchievements = () => store.set("achievements", achievements);

  /* ---------- Word keys & migration ---------- */
  function buildWordKey(word, counter) {
    const base = `${word.english || ""}::${word.chinese || ""}::${word.category || ""}`;
    const count = (counter[base] || 0) + 1;
    counter[base] = count;
    return count === 1 ? base : `${base}::${count}`;
  }

  function initializeWordKeys(words) {
    const counter = {};
    return words.map((word) => ({ ...word, __key: buildWordKey(word, counter) }));
  }

  function migrateWordStatusIfNeeded() {
    const migrated = {};
    wordsData.forEach((word) => {
      const key = word.__key;
      if (Object.prototype.hasOwnProperty.call(wordStatus, key)) {
        migrated[key] = wordStatus[key];
      } else if (Object.prototype.hasOwnProperty.call(wordStatus, word.english)) {
        migrated[key] = wordStatus[word.english];
      }
    });
    wordStatus = migrated;
    saveStatus();
  }

  /* ---------- Data load ---------- */
  async function loadWords() {
    const grid = $("wordGrid");
    grid.innerHTML =
      '<div class="empty-state"><div class="spinner"></div><h3>正在加载单词…</h3></div>';
    try {
      const response = await fetch("data/words_merged.json?v=3");
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      const rawWords = await response.json();
      wordsData = initializeWordKeys(rawWords);
      wordByKey = new Map(wordsData.map((w) => [w.__key, w]));
      wordIndexes = window.WordFilterRender.buildIndexes(wordsData);
      migrateWordStatusIfNeeded();
      populateCategories();
      renderWords();
      updateStats();
    } catch (error) {
      console.error("加载单词失败:", error);
      grid.innerHTML =
        '<div class="empty-state">' +
        "<h3>无法加载单词数据</h3>" +
        "<p>请通过本地服务器访问，并确保 data/words_merged.json 存在</p></div>";
    }
  }

  /* ---------- Achievements ---------- */
  const ACHIEVEMENTS = [
    { id: "first_word", name: "初学者", desc: "掌握第一个单词", icon: "🌱", test: (m) => m.mastered >= 1 },
    { id: "ten_words", name: "入门", desc: "掌握 10 个单词", icon: "📚", test: (m) => m.mastered >= 10 },
    { id: "fifty_words", name: "进阶", desc: "掌握 50 个单词", icon: "🎓", test: (m) => m.mastered >= 50 },
    { id: "hundred_words", name: "高手", desc: "掌握 100 个单词", icon: "🏆", test: (m) => m.mastered >= 100 },
    { id: "five_hundred_words", name: "大师", desc: "掌握 500 个单词", icon: "👑", test: (m) => m.mastered >= 500 },
    { id: "thousand_words", name: "传奇", desc: "掌握 1000 个单词", icon: "🌟", test: (m) => m.mastered >= 1000 },
    { id: "first_review", name: "复习达人", desc: "完成第一次复习", icon: "🔄", test: (m) => m.reviews >= 1 },
    { id: "ten_reviews", name: "复习专家", desc: "复习 10 个单词", icon: "⭐", test: (m) => m.reviews >= 10 },
    { id: "streak_3", name: "坚持 3 天", desc: "连续学习 3 天", icon: "🔥", test: () => checkStreak(3) },
    { id: "streak_7", name: "坚持 7 天", desc: "连续学习 7 天", icon: "💪", test: () => checkStreak(7) },
    { id: "streak_30", name: "坚持 30 天", desc: "连续学习 30 天", icon: "🏅", test: () => checkStreak(30) },
  ];

  function checkAchievements() {
    const metrics = {
      mastered: LU.getMasteredCount(wordStatus),
      reviews: Object.keys(wordReviewData).length,
    };
    const unlocked = [];
    ACHIEVEMENTS.forEach((a) => {
      if (a.test(metrics) && !achievements[a.id]) {
        achievements[a.id] = { name: a.name, desc: a.desc, icon: a.icon, date: new Date().toISOString() };
        unlocked.push(a);
      }
    });
    if (unlocked.length) {
      saveAchievements();
      showAchievementNotification(unlocked);
    }
  }

  function checkStreak(days) {
    let streak = 0;
    const today = new Date();
    for (let i = 0; i < days; i += 1) {
      const d = new Date(today);
      d.setDate(d.getDate() - i);
      if (learningHistory[LU.dayStr(d)]) streak += 1;
      else break;
    }
    return streak >= days;
  }

  function showAchievementNotification(list) {
    const el = document.createElement("div");
    el.className = "achievement-toast";
    el.innerHTML =
      '<div class="achievement-toast-title">新成就解锁</div>' +
      list
        .map(
          (a) =>
            `<div class="achievement-toast-item"><span class="achievement-toast-icon">${a.icon}</span>` +
            `<div><div class="achievement-toast-name">${a.name}</div>` +
            `<div class="achievement-toast-desc">${a.desc}</div></div></div>`
        )
        .join("");
    document.body.appendChild(el);
    setTimeout(() => {
      el.classList.add("leaving");
      setTimeout(() => el.remove(), 400);
    }, 5000);
  }

  function showAchievementsModal() {
    const content = $("achievementsContent");
    content.innerHTML = ACHIEVEMENTS.map((a) => {
      const u = achievements[a.id];
      return (
        `<div class="achievement-item ${u ? "unlocked" : "locked"}">` +
        `<div class="achievement-icon">${u ? a.icon : "🔒"}</div>` +
        `<div class="achievement-info"><div class="achievement-name">${a.name}</div>` +
        `<div class="achievement-desc">${a.desc}</div>` +
        (u ? `<div class="achievement-date">解锁于 ${new Date(u.date).toLocaleDateString()}</div>` : "") +
        "</div></div>"
      );
    }).join("");
    $("achievementsModal").classList.add("active");
  }
  const closeAchievementsModal = () => $("achievementsModal").classList.remove("active");

  /* ---------- Learning activity & spaced repetition ---------- */
  function recordLearningActivity(wordKey) {
    const today = LU.dayStr();
    const day = learningHistory[today] || (learningHistory[today] = { words: [], count: 0 });
    day.count += 1;
    if (wordKey && !day.words.includes(wordKey)) day.words.push(wordKey);
    const mastered = LU.getMasteredCount(wordStatus);
    day.mastered = mastered;
    day.masteredPercentage = wordsData.length ? Math.round((mastered / wordsData.length) * 100) : 0;
    saveLearningHistory();
    updateGoalRing();
  }

  function recordReviewOutcome(word, remembered) {
    const key = LU.keyOf(word);
    wordReviewData[key] = LU.scheduleNext(LU.migrateRecord(wordReviewData[key]), remembered);
    saveReviewData();
    recordLearningActivity(key);
  }

  function getDueReviewWords() {
    return LU.collectDueKeys(wordReviewData)
      .map((k) => wordByKey.get(k))
      .filter(Boolean);
  }

  /* ---------- Categories / filters ---------- */
  function fillSelect(select, placeholder, values) {
    const opts = [`<option value="all">${placeholder}</option>`];
    values.forEach((v) => opts.push(`<option value="${v}">${v}</option>`));
    select.innerHTML = opts.join("");
  }

  function sortedByCount(field, fallback) {
    const counts = new Map();
    wordsData.forEach((w) => {
      const k = w[field] || fallback;
      counts.set(k, (counts.get(k) || 0) + 1);
    });
    return [...counts.entries()].sort((a, b) => b[1] - a[1]);
  }

  function populateCategories() {
    const themes = sortedByCount("theme", "通用");
    const pos = sortedByCount("part_of_speech", "其他");
    fillSelect($("themeFilter"), "全部主题", themes.map(([k]) => k));
    fillSelect($("partOfSpeechFilter"), "全部词性", pos.map(([k]) => k));

    // Theme tabs — "通用" is the bulk/default view, so it's the "全部" tab.
    const tabThemes = themes.filter(([k]) => k !== "通用");
    $("categoryTabs").innerHTML =
      `<div class="category-tab active" onclick="selectTheme('all', this)">全部</div>` +
      tabThemes
        .map(
          ([k, n]) =>
            `<div class="category-tab" onclick="selectTheme('${escapeJsString(k)}', this)">${escapeHtml(k)}<span class="tab-count">${n}</span></div>`
        )
        .join("");
  }

  function selectTheme(theme, element) {
    document.querySelectorAll(".category-tab").forEach((t) => t.classList.remove("active"));
    if (element) element.classList.add("active");
    $("themeFilter").value = theme;
    updateBreadcrumb(theme === "all" ? null : theme);
    filterWords();
  }

  function updateBreadcrumb(category) {
    const breadcrumb = $("breadcrumb");
    breadcrumb.innerHTML =
      category && category !== "all"
        ? '<span class="breadcrumb-item" onclick="resetFilters()">全部单词</span>' +
          '<span class="breadcrumb-separator">›</span>' +
          `<span class="breadcrumb-item active">${escapeHtml(category)}</span>`
        : '<span class="breadcrumb-item active">全部单词</span>';
  }

  const FILTER_IDS = ["themeFilter", "partOfSpeechFilter", "statusFilter"];
  const PAGE_SIZE = 60;
  let currentPage = 1;

  function markFirstTabActive() {
    document.querySelectorAll(".category-tab").forEach((t, i) => t.classList.toggle("active", i === 0));
  }

  function resetFilters() {
    $("searchBox").value = "";
    FILTER_IDS.forEach((id) => ($(id).value = "all"));
    $("presetFilter").value = "all";
    markFirstTabActive();
    updateBreadcrumb(null);
    filterWords();
  }

  function applyPresetFilter(preset) {
    $("searchBox").value = "";
    FILTER_IDS.forEach((id) => ($(id).value = "all"));
    document.querySelectorAll(".category-tab").forEach((t) => t.classList.remove("active"));

    const presets = {
      "business-nouns": { themeFilter: "商业", partOfSpeechFilter: "名词" },
      "daily-verbs": { themeFilter: "日常生活", partOfSpeechFilter: "动词" },
      "science-adjectives": { themeFilter: "科学", partOfSpeechFilter: "形容词" },
      "learning-words": { statusFilter: "gray" },
      "difficult-words": { statusFilter: "red" },
      "unlearned-words": { statusFilter: "gray" },
    };
    Object.entries(presets[preset] || {}).forEach(([id, value]) => ($(id).value = value));
    updateBreadcrumb(presets[preset]?.themeFilter || null);
    filterWords();
  }

  function getFilters() {
    return {
      searchTerm: $("searchBox").value,
      themeFilter: $("themeFilter").value,
      partOfSpeechFilter: $("partOfSpeechFilter").value,
      statusFilter: $("statusFilter").value,
    };
  }

  function renderWords() {
    window.WordFilterRender.renderWords({
      wordsData,
      wordStatus,
      selectedWords,
      filters: getFilters(),
      container: $("wordGrid"),
      indexes: wordIndexes,
      onWordClickName: "handleWordClick",
      onSpeakName: "speak",
      onSetStatusName: "setStatus",
      page: currentPage,
      pageSize: PAGE_SIZE,
      onPager: renderPager,
    });
  }

  function filterWords() {
    currentPage = 1;
    saveFilterPreferences();
    renderWords();
  }

  function setPage(n) {
    currentPage = n;
    renderWords();
    const grid = $("wordGrid");
    const top = grid.getBoundingClientRect().top + window.scrollY - 80;
    window.scrollTo({ top, behavior: "smooth" });
  }

  function renderPager({ total, page, pages }) {
    const el = $("pager");
    if (!el) return;
    if (pages <= 1) {
      el.innerHTML = total ? `<span class="pager-info">共 ${total} 个单词</span>` : "";
      return;
    }
    const btn = (label, target, { active = false, disabled = false } = {}) =>
      `<button class="pager-btn${active ? " active" : ""}" ${disabled ? "disabled" : `onclick="setPage(${target})"`}>${label}</button>`;
    const gap = '<span class="pager-gap">…</span>';

    const end = Math.min(pages, Math.max(5, page + 2));
    const start = Math.max(1, end - 4);
    const nums = [];
    for (let i = start; i <= end; i += 1) nums.push(i);

    el.innerHTML =
      `<span class="pager-info">共 ${total} 个 · 第 ${page}/${pages} 页</span>` +
      '<div class="pager-controls">' +
      btn("‹", page - 1, { disabled: page <= 1 }) +
      (start > 1 ? btn("1", 1) + (start > 2 ? gap : "") : "") +
      nums.map((i) => btn(String(i), i, { active: i === page })).join("") +
      (end < pages ? (end < pages - 1 ? gap : "") + btn(String(pages), pages) : "") +
      btn("›", page + 1, { disabled: page >= pages }) +
      "</div>";
  }

  function saveFilterPreferences() {
    const prefs = { presetFilter: $("presetFilter").value };
    FILTER_IDS.forEach((id) => (prefs[id] = $(id).value));
    store.set("filterPreferences", prefs);
  }

  function loadFilterPreferences() {
    const prefs = store.get("filterPreferences", null);
    if (!prefs) return;
    FILTER_IDS.forEach((id) => ($(id).value = prefs[id] || "all"));
    $("presetFilter").value = prefs.presetFilter || "all";
  }

  /* ---------- Word status ---------- */
  function handleWordClick(wordKey) {
    if (batchMode) toggleWordSelection(wordKey);
    else cycleStatus(wordKey);
  }

  function cycleStatus(wordKey) {
    const status = wordStatus[wordKey] || "gray";
    const next = status === "gray" ? "green" : status === "green" ? "red" : "gray";
    setStatus(wordKey, next);
  }

  function setStatus(wordKey, status) {
    wordStatus[wordKey] = status;
    saveStatus();
    recordLearningActivity(wordKey);
    renderWords();
    updateStats();
  }

  /* ---------- Batch ---------- */
  const BATCH_BTNS = ["batchMarkMastered", "batchMarkDifficult", "batchMarkUnlearned"];

  function setBatchButtonsEnabled(enabled) {
    BATCH_BTNS.forEach((id) => ($(id).disabled = !enabled));
  }

  function updateBatchCount() {
    const el = $("batchCount");
    if (el) el.textContent = selectedWords.size ? `已选 ${selectedWords.size}` : "";
  }

  function setBatchButtonLabel() {
    const btn = $("batchModeBtn");
    btn.innerHTML = batchMode
      ? `${window.Icon("close", 18)}退出批量`
      : `${window.Icon("layers", 18)}批量选择`;
    btn.classList.toggle("btn-primary", batchMode);
    btn.classList.toggle("btn-quiet", !batchMode);
  }

  function toggleBatchMode() {
    batchMode = !batchMode;
    setBatchButtonLabel();
    $("batchBar").classList.toggle("hidden", !batchMode);
    if (batchMode) {
      setBatchButtonsEnabled(false);
      UI.info("点击单词卡片进行多选");
    } else {
      selectedWords.clear();
      setBatchButtonsEnabled(false);
      document.querySelectorAll(".word-card.selected").forEach((c) => c.classList.remove("selected"));
    }
    updateBatchCount();
  }

  function toggleWordSelection(wordKey) {
    if (!batchMode) return;
    const card = document.querySelector(`.word-card[data-key="${CSS.escape(wordKey)}"]`);
    if (selectedWords.has(wordKey)) {
      selectedWords.delete(wordKey);
      card?.classList.remove("selected");
    } else {
      selectedWords.add(wordKey);
      card?.classList.add("selected");
    }
    setBatchButtonsEnabled(selectedWords.size > 0);
    updateBatchCount();
  }

  function batchSetStatus(status) {
    if (selectedWords.size === 0) {
      UI.warning("请先选择要操作的单词");
      return;
    }
    const count = selectedWords.size;
    selectedWords.forEach((key) => {
      wordStatus[key] = status;
    });
    saveStatus();
    selectedWords.clear();
    batchMode = false;
    setBatchButtonLabel();
    $("batchBar").classList.add("hidden");
    setBatchButtonsEnabled(false);
    updateBatchCount();
    renderWords();
    updateStats();
    recordLearningActivity();
    const label = { green: "已掌握", red: "难记", gray: "未学习" }[status] || status;
    UI.success(`已将 ${count} 个单词标记为「${label}」`);
  }

  /* ---------- Stats & goal ---------- */
  function updateStats() {
    const total = wordsData.length;
    const mastered = Object.values(wordStatus).filter((s) => s === "green").length;
    const difficult = Object.values(wordStatus).filter((s) => s === "red").length;
    const learning = total - mastered - difficult;

    $("totalWords").textContent = total;
    $("masteredWords").textContent = mastered;
    $("difficultWords").textContent = difficult;
    $("learningWords").textContent = learning;

    const percentage = total > 0 ? Math.round((mastered / total) * 100) : 0;
    $("progressPercentage").textContent = `${percentage}%`;
    $("progressBar").style.width = `${percentage}%`;
    $("progressSegments").innerHTML =
      `<div class="segment green" style="flex:${mastered}"></div>` +
      `<div class="segment red" style="flex:${difficult}"></div>` +
      `<div class="segment gray" style="flex:${learning}"></div>`;

    $("reviewCount").textContent = getDueReviewWords().length;
    updateGoalRing();
    checkAchievements();
  }

  function updateGoalRing() {
    const today = LU.dayStr();
    const done = (learningHistory[today]?.words || []).length;
    const target = Math.max(1, dailyGoal);
    const ratio = Math.min(1, done / target);

    $("goalCurrent").textContent = done;
    $("goalTarget").textContent = target;

    const fill = $("goalRingFill");
    if (fill) {
      const r = Number(fill.getAttribute("r"));
      const c = 2 * Math.PI * r;
      fill.style.strokeDasharray = `${c}`;
      fill.style.strokeDashoffset = `${c * (1 - ratio)}`;
    }
    $("goalRing")?.classList.toggle("done", done >= target);
  }

  /* ---------- Speech ---------- */
  function getPreferredEnglishVoice(voices) {
    if (!voices || voices.length === 0) return null;
    return (
      voices.find((v) => v.name === "Google US English") ||
      voices.find((v) => v.name.includes("Google US English")) ||
      voices.find((v) => v.lang === "en-US") ||
      voices.find((v) => v.lang && v.lang.startsWith("en")) ||
      null
    );
  }

  function loadVoices() {
    if (!("speechSynthesis" in window)) return;
    availableVoices = speechSynthesis.getVoices().filter((v) => v.lang.startsWith("en"));
    const savedVoice = store.get("selectedVoice", null);
    const savedRate = store.get("speechRate", null);
    if (savedVoice && availableVoices.length) {
      selectedVoice = availableVoices.find((v) => v.name === savedVoice) || null;
    } else {
      selectedVoice = getPreferredEnglishVoice(availableVoices);
      if (selectedVoice) store.set("selectedVoice", selectedVoice.name);
    }
    if (savedRate !== null) speechRate = parseFloat(savedRate);
  }

  function speak(text) {
    if (!("speechSynthesis" in window)) {
      UI.warning("您的浏览器不支持语音合成功能");
      return;
    }
    loadVoices();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = "en-US";
    u.rate = speechRate;
    u.pitch = 1;
    if (selectedVoice) u.voice = selectedVoice;
    speechSynthesis.cancel();
    speechSynthesis.speak(u);
  }

  /* ---------- Quiz ---------- */
  function startQuiz() {
    quizWords = LU.sample(wordsData, 10);
    currentQuizIndex = 0;
    quizScore = 0;
    isReviewMode = false;
    $("quizModal").classList.add("active");
    showQuizQuestion();
  }

  function showQuizQuestion() {
    if (currentQuizIndex >= quizWords.length) {
      const html = window.WordSessionRenderers.buildCompletionHtml("测验完成！", "再来一次", "startQuiz()");
      $("quizContent").innerHTML = `${html}<p class="session-complete-score">得分: ${quizScore}/${quizWords.length}</p>`;
      isReviewMode = false;
      return;
    }
    const word = quizWords[currentQuizIndex];
    const options = LU.buildQuizOptions(wordsData, word, 4);
    $("quizContent").innerHTML = window.WordSessionRenderers.buildQuizQuestionHtml(
      word,
      options,
      currentQuizIndex,
      quizWords.length
    );
  }

  function checkQuizAnswer(selected, correct) {
    const options = document.querySelectorAll(".quiz-option");
    options.forEach((opt) => {
      const value = opt.dataset.opt;
      if (value === correct) opt.classList.add("correct");
      else if (value === selected && selected !== correct) opt.classList.add("incorrect");
      opt.style.pointerEvents = "none";
    });

    const word = quizWords[currentQuizIndex];
    const remembered = selected === correct;
    if (remembered) quizScore += 1;
    if (word) recordReviewOutcome(word, remembered);

    setTimeout(() => {
      currentQuizIndex += 1;
      showQuizQuestion();
    }, 1100);
  }

  const closeQuizModal = () => $("quizModal").classList.remove("active");

  function startSmartReview() {
    const due = getDueReviewWords();
    if (due.length === 0) {
      UI.info("今天没有到期复习的单词，继续学习新词吧！", { title: "复习" });
      return;
    }
    quizWords = LU.sample(due, Math.min(10, due.length));
    currentQuizIndex = 0;
    quizScore = 0;
    isReviewMode = true;
    $("quizModal").classList.add("active");
    showQuizQuestion();
  }

  /* ---------- Practice (sentence) ---------- */
  function startPractice() {
    const words = LU.pickReviewPool(wordsData, wordStatus, 5, 3, wordReviewData);
    if (words.length === 0) {
      UI.success("恭喜！所有单词都已掌握！");
      return;
    }
    $("practiceModal").classList.add("active");
    showPracticeWord(words, 0);
  }

  function showPracticeWord(words, index) {
    if (index >= words.length) {
      $("practiceContent").innerHTML = window.WordSessionRenderers.buildCompletionHtml(
        "练习完成！",
        "再来一次",
        "startPractice()"
      );
      return;
    }
    $("practiceContent").innerHTML = window.WordSessionRenderers.buildPracticeWordHtml(
      words[index],
      index,
      words.length
    );
  }

  function checkSentence(word) {
    const input = $("practiceInput");
    const feedback = $("sentenceFeedback");
    const sentence = input.value.trim();
    if (!sentence) {
      showFeedback(feedback, "warning", '<p class="session-feedback-title warning">请先输入句子</p>');
      return;
    }
    if (!sentence.toLowerCase().includes(word.toLowerCase())) {
      showFeedback(
        feedback,
        "error",
        `<p class="session-feedback-title error">句子中需要包含单词 “${escapeHtml(word)}”</p>`
      );
      return;
    }
    showFeedback(
      feedback,
      "success",
      `<p class="session-feedback-title success">很好，你用 “${escapeHtml(word)}” 造了句子</p>
       <p class="session-feedback-text">你的句子：${escapeHtml(sentence)}</p>
       <p class="session-feedback-hint">多练习造句能帮助你掌握单词用法</p>`
    );
    const target = wordsData.find((w) => w.english === word);
    if (target) recordReviewOutcome(target, true);
    speak(sentence);
  }

  function showExampleSentence(example) {
    showFeedback(
      $("sentenceFeedback"),
      "info",
      `<p class="session-feedback-title info">例句参考</p>
       <p class="session-feedback-text"><em>${escapeHtml(example)}</em></p>
       <p class="session-feedback-hint">试着模仿例句的结构来造句</p>`
    );
  }

  const closePracticeModal = () => $("practiceModal").classList.remove("active");

  function showFeedback(el, type, html) {
    el.className = `session-feedback show ${type}`;
    el.innerHTML = html;
  }

  /* ---------- Listening ---------- */
  function startListening() {
    const words = LU.pickReviewPool(wordsData, wordStatus, 5, 5, wordReviewData);
    if (words.length === 0) {
      UI.success("恭喜！所有单词都已掌握！");
      return;
    }
    $("listeningModal").classList.add("active");
    showListeningWord(words, 0);
  }

  function showListeningWord(words, index) {
    if (index >= words.length) {
      $("listeningContent").innerHTML = window.WordSessionRenderers.buildCompletionHtml(
        "听力练习完成！",
        "再来一次",
        "startListening()"
      );
      return;
    }
    listeningQueue = words;
    listeningIndex = index;
    $("listeningContent").innerHTML = window.WordSessionRenderers.buildListeningWordHtml(
      words[index],
      index,
      words.length
    );
    setTimeout(() => speak(words[index].english), 350);
  }

  let listeningQueue = [];
  let listeningIndex = 0;

  function checkListeningAnswer(correct) {
    const input = $("listeningInput");
    const feedback = $("listeningFeedback");
    const reveal = $("listeningRevealWord");
    const answer = input.value.trim().toLowerCase();
    if (!answer) {
      showFeedback(feedback, "warning", '<p class="session-feedback-title warning">请先输入答案</p>');
      return;
    }
    reveal?.classList.remove("hidden");
    const remembered = answer === correct.toLowerCase();
    const word = wordsData.find((w) => w.english === correct);
    if (word) recordReviewOutcome(word, remembered);

    if (remembered) {
      showFeedback(
        feedback,
        "success",
        `<p class="session-feedback-title success">正确</p>
         <p class="session-feedback-text">正确答案：${escapeHtml(correct)}</p>
         <p class="session-feedback-hint">下一个单词即将开始</p>`
      );
      setTimeout(() => showListeningWord(listeningQueue, listeningIndex + 1), 1100);
    } else {
      showFeedback(
        feedback,
        "error",
        `<p class="session-feedback-title error">再听一次</p>
         <p class="session-feedback-text">你的答案：${escapeHtml(input.value)}</p>
         <p class="session-feedback-hint">正确答案：${escapeHtml(correct)}</p>
         <p class="session-feedback-hint">注意发音细节</p>`
      );
    }
  }

  const closeListeningModal = () => $("listeningModal").classList.remove("active");

  /* ---------- Spelling ---------- */
  let spellingQueue = [];
  let spellingIndex = 0;

  function startSpelling() {
    const words = LU.pickReviewPool(wordsData, wordStatus, 5, 5, wordReviewData);
    if (words.length === 0) {
      UI.success("恭喜！所有单词都已掌握！");
      return;
    }
    $("spellingModal").classList.add("active");
    showSpellingWord(words, 0);
  }

  function showSpellingWord(words, index) {
    if (index >= words.length) {
      $("spellingContent").innerHTML = window.WordSessionRenderers.buildCompletionHtml(
        "拼写练习完成！",
        "再来一次",
        "startSpelling()"
      );
      return;
    }
    spellingQueue = words;
    spellingIndex = index;
    const word = words[index];
    const masked = word.english
      .split("")
      .map((ch, i) => (i === 0 || i === word.english.length - 1 ? ch : "_"))
      .join("");
    $("spellingContent").innerHTML = window.WordSessionRenderers.buildSpellingWordHtml(
      word,
      masked,
      index,
      words.length
    );
    setTimeout(() => speak(word.english), 350);
  }

  function checkSpellingAnswer(correct) {
    const input = $("spellingInput");
    const feedback = $("spellingFeedback");
    const answer = input.value.trim().toLowerCase();
    if (!answer) {
      showFeedback(feedback, "warning", '<p class="session-feedback-title warning">请先输入拼写</p>');
      return;
    }
    const remembered = answer === correct.toLowerCase();
    const word = wordsData.find((w) => w.english === correct);
    if (word) recordReviewOutcome(word, remembered);

    if (remembered) {
      showFeedback(
        feedback,
        "success",
        `<p class="session-feedback-title success">拼写正确</p>
         <p class="session-feedback-text">正确拼写：${escapeHtml(correct)}</p>
         <p class="session-feedback-hint">下一个单词即将开始</p>`
      );
      setTimeout(() => showSpellingWord(spellingQueue, spellingIndex + 1), 1100);
    } else {
      showFeedback(
        feedback,
        "error",
        `<p class="session-feedback-title error">拼写有误</p>
         <p class="session-feedback-text">你的拼写：${escapeHtml(input.value)}</p>
         <p class="session-feedback-hint">正确拼写：${escapeHtml(correct)}</p>
         <p class="session-feedback-hint">注意字母顺序与拼写规则</p>`
      );
    }
  }

  const closeSpellingModal = () => $("spellingModal").classList.remove("active");

  /* ---------- Settings ---------- */
  function getDefaultVoiceLabel() {
    return selectedVoice?.name ? `默认语音（${selectedVoice.name}）` : "默认语音（Google US English）";
  }

  function showSettingsModal() {
    loadVoices();
    const voiceOptions = availableVoices
      .map((v, i) => {
        const sel = selectedVoice && selectedVoice.name === v.name ? "selected" : "";
        return `<option value="${i}" ${sel}>${v.name} (${v.lang})</option>`;
      })
      .join("");
    const defaultOption = selectedVoice ? "" : `<option value="" selected>${getDefaultVoiceLabel()}</option>`;

    $("settingsContent").innerHTML = `
      <div class="settings-panel">
        <div class="settings-block">
          <label class="settings-label">外观主题</label>
          <div class="settings-row">
            <button class="action-btn settings-full" onclick="toggleTheme()" id="themeSettingBtn"></button>
          </div>
          <p class="settings-help">浅色 / 深色模式，选择会被记住</p>
        </div>

        <div class="settings-block">
          <label class="settings-label">每日目标</label>
          <input type="number" id="goalInput" class="goal-input" min="1" max="500" value="${dailyGoal}">
          <p class="settings-help">设定每天想学习的单词数量</p>
        </div>

        <div class="settings-divider"></div>

        <div class="settings-block">
          <label class="settings-label">发音音色</label>
          <select id="voiceSelect" class="settings-select">${defaultOption}${voiceOptions}</select>
          <p class="settings-help">选择你偏好的英语发音</p>
        </div>

        <div class="settings-block">
          <label class="settings-label">语速</label>
          <div class="settings-row">
            <span class="settings-muted">慢</span>
            <input type="range" id="rateSlider" min="0.5" max="1.5" step="0.1" value="${speechRate}" class="settings-range">
            <span class="settings-muted">快</span>
            <span id="rateValue" class="settings-rate">${speechRate}x</span>
          </div>
          <p class="settings-help">调整发音速度，0.5–1.5 倍速</p>
        </div>

        <div class="settings-block">
          <button class="action-btn settings-full" onclick="testVoice()">试听发音</button>
        </div>

        <div class="settings-actions">
          <button class="action-btn btn-primary" onclick="saveSettings()">保存设置</button>
          <button class="action-btn" onclick="resetSettings()">恢复默认</button>
        </div>

        <div class="settings-divider"></div>
        <button class="action-btn btn-danger settings-full" onclick="resetProgress()">重置全部学习进度</button>
      </div>`;

    updateThemeSettingButton();
    $("voiceSelect").addEventListener("change", function () {
      selectedVoice = this.value === "" ? null : availableVoices[this.value];
    });
    $("rateSlider").addEventListener("input", function () {
      speechRate = parseFloat(this.value);
      $("rateValue").textContent = `${speechRate}x`;
    });
    $("settingsModal").classList.add("active");
  }

  const closeSettingsModal = () => $("settingsModal").classList.remove("active");

  function testVoice() {
    speak("Hello! This is a test of the voice settings.");
  }

  function saveSettings() {
    if (selectedVoice) store.set("selectedVoice", selectedVoice.name);
    else store.remove("selectedVoice");
    store.set("speechRate", speechRate.toString());
    const goalEl = $("goalInput");
    if (goalEl) {
      const v = Math.max(1, Math.min(500, parseInt(goalEl.value, 10) || dailyGoal));
      dailyGoal = v;
      store.set("dailyGoal", v);
      updateGoalRing();
    }
    UI.success("设置已保存");
    closeSettingsModal();
  }

  async function resetSettings() {
    const ok = await UI.confirm("确定要恢复默认的语音与语速设置吗？", { title: "恢复默认" });
    if (!ok) return;
    selectedVoice = null;
    speechRate = 0.9;
    store.remove("selectedVoice");
    store.remove("speechRate");
    showSettingsModal();
    UI.info("已恢复默认设置");
  }

  async function resetProgress() {
    const ok = await UI.confirm("此操作将清空所有单词状态、复习记录与学习历史，且不可撤销。确定继续吗？", {
      title: "重置学习进度",
      confirmText: "全部重置",
      danger: true,
    });
    if (!ok) return;
    wordStatus = {};
    wordReviewData = {};
    learningHistory = {};
    achievements = {};
    store.remove("wordStatus");
    store.remove("wordReviewData");
    store.remove("learningHistory");
    store.remove("achievements");
    renderWords();
    updateStats();
    closeSettingsModal();
    UI.success("学习进度已重置");
  }

  /* ---------- Theme ---------- */
  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    store.set("theme", theme);
    const btn = $("themeToggle");
    if (btn && window.Icon) {
      btn.innerHTML = window.Icon(theme === "dark" ? "sun" : "moon");
      btn.setAttribute("aria-label", theme === "dark" ? "切换到浅色模式" : "切换到深色模式");
    }
    updateThemeSettingButton();
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute("data-theme") === "dark" ? "dark" : "light";
    applyTheme(current === "dark" ? "light" : "dark");
  }

  function updateThemeSettingButton() {
    const b = $("themeSettingBtn");
    if (b && window.Icon) {
      const dark = document.documentElement.getAttribute("data-theme") === "dark";
      b.innerHTML = dark
        ? `${window.Icon("sun", 18)}当前：深色模式（点击切换）`
        : `${window.Icon("moon", 18)}当前：浅色模式（点击切换）`;
    }
  }

  /* ---------- Pages / nav ---------- */
  function setActiveNav(page) {
    document.querySelectorAll(".nav-item").forEach((i) => i.classList.remove("active"));
    document.querySelector(`.nav-item[data-page="${page}"]`)?.classList.add("active");
  }

  function switchPage(page) {
    if (page === "stats") {
      showAnalytics();
      return;
    }
    if (page === "settings") {
      showSettingsModal();
      return;
    }
    document.querySelectorAll(".modal.active").forEach((m) => m.classList.remove("active"));
    setActiveNav("learn");
  }

  /* ---------- Analytics ---------- */
  function showAnalytics() {
    $("analyticsModal").classList.add("active");
    switchAnalyticsTab("heatmap", document.querySelector(".analytics-tab"));
  }
  const closeAnalyticsModal = () => $("analyticsModal").classList.remove("active");

  function switchAnalyticsTab(tab, element) {
    document.querySelectorAll(".analytics-tab").forEach((t) => t.classList.remove("active"));
    element?.classList.add("active");
    if (tab === "heatmap") renderHeatmap();
    else if (tab === "trend") renderTrendChart();
    else if (tab === "dot") renderDotChart();
  }

  function renderHeatmap() {
    const content = $("analyticsContent");
    const today = new Date();
    const daysInMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate();

    content.innerHTML =
      '<div class="analytics-title-inline">本月学习热力图</div>' +
      '<div class="heatmap-container" id="heatmapGrid"></div>' +
      '<div class="heatmap-legend"><span>少</span>' +
      '<div class="legend-cell level-0"></div><div class="legend-cell level-1"></div>' +
      '<div class="legend-cell level-2"></div><div class="legend-cell level-3"></div>' +
      '<div class="legend-cell level-4"></div><span>多</span></div>';

    let html = "";
    for (let day = 1; day <= daysInMonth; day += 1) {
      const dateStr = `${today.getFullYear()}-${String(today.getMonth() + 1).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
      const activity = learningHistory[dateStr] ? learningHistory[dateStr].count : 0;
      let level = 0;
      if (activity > 0) level = 1;
      if (activity > 5) level = 2;
      if (activity > 10) level = 3;
      if (activity > 20) level = 4;
      html += `<div class="heatmap-cell level-${level}" onmouseover="showHeatmapTooltip(event, '${dateStr}', ${activity})" onmouseout="hideHeatmapTooltip()"></div>`;
    }
    $("heatmapGrid").innerHTML = html;
  }

  function showHeatmapTooltip(event, date, activity) {
    const tip = document.createElement("div");
    tip.className = "heatmap-tooltip";
    tip.innerHTML = `<strong>${date}</strong><br/>学习次数: ${activity}`;
    tip.style.left = `${event.pageX + 10}px`;
    tip.style.top = `${event.pageY - 30}px`;
    document.body.appendChild(tip);
  }
  const hideHeatmapTooltip = () => document.querySelectorAll(".heatmap-tooltip").forEach((t) => t.remove());

  function renderTrendChart() {
    const content = $("analyticsContent");
    const total = wordsData.length;
    const currentMastered = LU.getMasteredCount(wordStatus);
    const fallback = total > 0 ? Math.round((currentMastered / total) * 100) : 0;
    const { dates, dataPoints } = LU.buildTrendData(learningHistory, total, fallback);

    if (dates.length === 0) {
      content.innerHTML = '<div class="analytics-empty">暂无学习数据，开始学习后这里会展示掌握率趋势</div>';
      return;
    }

    content.innerHTML =
      '<div class="analytics-title-inline">掌握率趋势</div>' +
      '<div class="trend-chart-container"><canvas id="trendCanvas" class="trend-canvas"></canvas></div>';

    const canvas = $("trendCanvas");
    const ctx = canvas.getContext("2d");
    const styles = getComputedStyle(document.documentElement);
    const accent = styles.getPropertyValue("--accent").trim() || "#4F46E5";
    const gridColor = styles.getPropertyValue("--border").trim() || "#E5E7EB";
    const textColor = styles.getPropertyValue("--text-muted").trim() || "#6B7280";
    const surface = styles.getPropertyValue("--surface").trim() || "#fff";

    canvas.width = canvas.offsetWidth * 2;
    canvas.height = canvas.offsetHeight * 2;
    ctx.scale(2, 2);
    const width = canvas.offsetWidth;
    const height = canvas.offsetHeight;
    const padding = 40;
    const maxPercentage = Math.max(...dataPoints.map((p) => p.percentage), 100);

    ctx.clearRect(0, 0, width, height);
    ctx.strokeStyle = gridColor;
    ctx.lineWidth = 1;
    for (let i = 0; i <= 5; i += 1) {
      const y = padding + (height - 2 * padding) * (1 - i / 5);
      ctx.beginPath();
      ctx.moveTo(padding, y);
      ctx.lineTo(width - padding, y);
      ctx.stroke();
      ctx.fillStyle = textColor;
      ctx.font = "12px Inter";
      ctx.textAlign = "right";
      ctx.fillText(`${i * 20}%`, padding - 6, y + 4);
    }

    const xAt = (i) => padding + (width - 2 * padding) * (i / (dataPoints.length - 1 || 1));
    const yAt = (p) => padding + (height - 2 * padding) * (1 - p / maxPercentage);

    ctx.strokeStyle = accent;
    ctx.lineWidth = 3;
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
    ctx.beginPath();
    dataPoints.forEach((p, i) => (i === 0 ? ctx.moveTo(xAt(i), yAt(p.percentage)) : ctx.lineTo(xAt(i), yAt(p.percentage))));
    ctx.stroke();

    dataPoints.forEach((p, i) => {
      ctx.beginPath();
      ctx.arc(xAt(i), yAt(p.percentage), 5, 0, Math.PI * 2);
      ctx.fillStyle = accent;
      ctx.fill();
      ctx.strokeStyle = surface;
      ctx.lineWidth = 2;
      ctx.stroke();
    });

    ctx.fillStyle = textColor;
    ctx.font = "11px Inter";
    ctx.textAlign = "center";
    const step = Math.ceil(dates.length / 6);
    dates.forEach((date, i) => {
      if (i % step === 0) {
        const d = new Date(date);
        ctx.fillText(`${d.getMonth() + 1}/${d.getDate()}`, xAt(i), height - padding + 20);
      }
    });
  }

  function renderDotChart() {
    const content = $("analyticsContent");
    content.innerHTML =
      '<div class="analytics-title-inline">全局单词状态分布</div>' +
      '<div class="dot-legend">' +
      '<div class="legend-item"><div class="legend-dot gray"></div><span>未学习</span></div>' +
      '<div class="legend-item"><div class="legend-dot green"></div><span>已掌握</span></div>' +
      '<div class="legend-item"><div class="legend-dot red"></div><span>难记</span></div></div>' +
      '<div class="dot-chart-container" id="dotChart"></div>';

    $("dotChart").innerHTML = wordsData
      .map((word) => {
        const status = wordStatus[LU.keyOf(word)] || "gray";
        return `<div class="dot ${status}" onclick="showWordDetail('${escapeJsString(LU.keyOf(word))}')" title="${escapeHtml(word.english)} - ${escapeHtml(word.chinese)}"></div>`;
      })
      .join("");
  }

  function showWordDetail(key) {
    const word = wordByKey.get(key) || wordsData.find((w) => w.english === key);
    if (word) {
      UI.toast(`${word.phonetic || ""}  ${word.chinese}`, { title: word.english, type: "info", duration: 4200 });
    }
  }

  /* ---------- Escaping (for app-built HTML) ---------- */
  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }
  function escapeJsString(value) {
    return String(value).replace(/\\/g, "\\\\").replace(/'/g, "\\'");
  }

  /* ---------- Keyboard shortcuts ---------- */
  function onKeyDown(e) {
    if (e.key === "Escape") {
      document.querySelectorAll(".modal.active").forEach((m) => m.classList.remove("active"));
    }

    // Quiz answer keys (A–D / 1–4) when the quiz is open
    if ($("quizModal").classList.contains("active")) {
      const opts = document.querySelectorAll(".quiz-option");
      const map = { a: 0, b: 1, c: 2, d: 3, 1: 0, 2: 1, 3: 2, 4: 3 };
      const idx = map[e.key.toLowerCase()];
      if (idx !== undefined && opts[idx]) {
        opts[idx].click();
        return;
      }
    }

    if (e.ctrlKey || e.metaKey) {
      const actions = {
        k: () => $("searchBox").focus(),
        q: startQuiz,
        p: startPractice,
        r: startSmartReview,
        l: startListening,
        a: showAchievementsModal,
        s: showAnalytics,
        ",": showSettingsModal,
      };
      const action = actions[e.key.toLowerCase()];
      if (action) {
        e.preventDefault();
        action();
      }
    }
  }

  /* ---------- Bootstrap ---------- */
  function init() {
    // Theme first (avoid flash handled inline in <head>)
    const savedTheme =
      store.get("theme", null) ||
      (window.matchMedia?.("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    applyTheme(savedTheme);

    wordStatus = store.get("wordStatus", {});
    learningHistory = store.get("learningHistory", {});
    wordReviewData = store.get("wordReviewData", {});
    achievements = store.get("achievements", {});
    dailyGoal = store.get("dailyGoal", 20);

    loadWords();
    loadVoices();
    if ("speechSynthesis" in window && "onvoiceschanged" in speechSynthesis) {
      speechSynthesis.onvoiceschanged = () => loadVoices();
    }
    loadFilterPreferences();

    const debouncedFilter = window.WordFilterRender.debounce(filterWords, 180);
    $("searchBox").addEventListener("input", debouncedFilter);
    FILTER_IDS.forEach((id) => $(id).addEventListener("change", filterWords));

    document.addEventListener("keydown", onKeyDown);
  }

  /* ---------- Expose handlers used by inline HTML / renderers ---------- */
  Object.assign(window, {
    switchPage,
    applyPresetFilter,
    resetFilters,
    selectTheme,
    populateCategories,
    setPage,
    handleWordClick,
    setStatus,
    speak,
    toggleBatchMode,
    batchSetStatus,
    startQuiz,
    showQuizQuestion,
    checkQuizAnswer,
    closeQuizModal,
    startSmartReview,
    startPractice,
    checkSentence,
    showExampleSentence,
    closePracticeModal,
    startListening,
    checkListeningAnswer,
    closeListeningModal,
    startSpelling,
    checkSpellingAnswer,
    closeSpellingModal,
    showSettingsModal,
    closeSettingsModal,
    testVoice,
    saveSettings,
    resetSettings,
    resetProgress,
    toggleTheme,
    showAnalytics,
    closeAnalyticsModal,
    switchAnalyticsTab,
    showHeatmapTooltip,
    hideHeatmapTooltip,
    showWordDetail,
    showAchievementsModal,
    closeAchievementsModal,
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
