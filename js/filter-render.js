(() => {
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

  // Index by the two clean dimensions used for filtering.
  function buildIndexes(wordsData) {
    const indexes = { theme: new Map(), part_of_speech: new Map() };
    wordsData.forEach((word) => {
      Object.keys(indexes).forEach((field) => {
        const key = word[field] || "其他";
        if (!indexes[field].has(key)) indexes[field].set(key, []);
        indexes[field].get(key).push(word);
      });
    });
    return indexes;
  }

  // Narrow to the smallest matching bucket before the full predicate scan.
  function getFilteredBaseWords(wordsData, filters, indexes) {
    if (!indexes) return wordsData;
    const active = [
      { field: "theme", value: filters.themeFilter },
      { field: "part_of_speech", value: filters.partOfSpeechFilter },
    ].filter((f) => f.value && f.value !== "all");

    if (active.length === 0) return wordsData;

    let base = null;
    active.forEach((f) => {
      const bucket = indexes[f.field]?.get(f.value) || [];
      if (base === null || bucket.length < base.length) base = bucket;
    });
    return base || [];
  }

  function filterWordList(wordsData, wordStatus, filters, indexes) {
    const searchTerm = (filters.searchTerm || "").trim().toLowerCase();
    const base = getFilteredBaseWords(wordsData, filters, indexes);

    return base.filter((word) => {
      const english = String(word.english || "");
      const chinese = String(word.chinese || "");
      const status = wordStatus[word.__key || english] || "gray";

      const matchesSearch =
        !searchTerm ||
        english.toLowerCase().includes(searchTerm) ||
        chinese.toLowerCase().includes(searchTerm);
      const matchesTheme =
        filters.themeFilter === "all" || (word.theme || "通用") === filters.themeFilter;
      const matchesPos =
        filters.partOfSpeechFilter === "all" ||
        (word.part_of_speech || "其他") === filters.partOfSpeechFilter;
      const matchesStatus = filters.statusFilter === "all" || status === filters.statusFilter;

      return matchesSearch && matchesTheme && matchesPos && matchesStatus;
    });
  }

  function cardHtml(word, wordStatus, selectedWords, handlers) {
    const english = String(word.english || "");
    const wordKey = String(word.__key || english);
    const status = wordStatus[wordKey] || "gray";
    const isSelected = selectedWords.has(wordKey);
    const safeEnglish = escapeJsString(english);
    const safeWordKey = escapeJsString(wordKey);
    const sound = window.Icon ? window.Icon("volume", 18) : "🔊";

    const meta = [
      { cls: "pos-tag", text: word.part_of_speech },
      { cls: "theme-tag", text: word.theme === "通用" ? "" : word.theme },
      { cls: "child-tag", text: word.category },
    ]
      .filter((t, i, arr) => {
        if (!t.text || t.text === "其他") return false;
        // Drop a category tag that just repeats the theme.
        return arr.findIndex((o) => o.text === t.text) === i;
      })
      .map((t) => `<span class="word-tag ${t.cls}">${escapeHtml(t.text)}</span>`)
      .join("");

    const tier =
      word.level === 1
        ? '<span class="word-tag tier-core">高频</span>'
        : word.level === 3
          ? '<span class="word-tag tier-adv">高阶</span>'
          : "";

    return `
      <div class="word-card ${status} ${isSelected ? "selected" : ""}" data-word="${escapeHtml(english)}" data-key="${escapeHtml(wordKey)}" onclick="${handlers.click}('${safeWordKey}')">
        <div class="word-english">
          <span class="word-english-text">${escapeHtml(english)}</span>
          <button class="play-btn" onclick="event.stopPropagation(); ${handlers.speak}('${safeEnglish}')" aria-label="朗读">${sound}</button>
        </div>
        ${word.phonetic ? `<div class="word-phonetic">${escapeHtml(word.phonetic)}</div>` : ""}
        <div class="word-chinese">${escapeHtml(word.chinese || "")}</div>
        ${word.example ? `<div class="word-example">${escapeHtml(word.example)}</div>` : ""}
        <div class="word-tags">${tier}${meta}</div>
        <div class="word-actions">
          <span class="status-badge ${status === "gray" || !status ? "active" : ""}" onclick="event.stopPropagation(); ${handlers.setStatus}('${safeWordKey}', 'gray')">未学习</span>
          <span class="status-badge ${status === "green" ? "green" : ""}" onclick="event.stopPropagation(); ${handlers.setStatus}('${safeWordKey}', 'green')">已掌握</span>
          <span class="status-badge ${status === "red" ? "red" : ""}" onclick="event.stopPropagation(); ${handlers.setStatus}('${safeWordKey}', 'red')">难记</span>
        </div>
      </div>`;
  }

  function sortWords(list, mode, wordStatus) {
    if (!mode || mode === "order") return list;
    const arr = [...list];
    const statusOf = (w) => wordStatus[w.__key || w.english] || "gray";
    if (mode === "az") {
      arr.sort((a, b) => String(a.english).localeCompare(String(b.english)));
    } else if (mode === "za") {
      arr.sort((a, b) => String(b.english).localeCompare(String(a.english)));
    } else if (mode === "difficult") {
      const rank = { red: 0, gray: 1, green: 2 };
      arr.sort((a, b) => rank[statusOf(a)] - rank[statusOf(b)]);
    } else if (mode === "unlearned") {
      const rank = { gray: 0, red: 1, green: 2 };
      arr.sort((a, b) => rank[statusOf(a)] - rank[statusOf(b)]);
    } else if (mode === "freq") {
      arr.sort((a, b) => (a.level || 2) - (b.level || 2));
    }
    return arr;
  }

  function renderWords(params) {
    const {
      wordsData,
      wordStatus,
      selectedWords,
      filters,
      container,
      indexes,
      onWordClickName,
      onSpeakName,
      onSetStatusName,
      page = 1,
      pageSize = 60,
      sortMode = "order",
      onPager,
    } = params;

    const filtered = sortWords(
      filterWordList(wordsData, wordStatus, filters, indexes),
      sortMode,
      wordStatus
    );

    if (filtered.length === 0) {
      container.innerHTML =
        '<div class="empty-state"><h3>没有找到匹配的单词</h3>' +
        "<p>试着调整搜索词或筛选条件</p></div>";
      onPager && onPager({ total: 0, page: 1, pages: 0, pageSize });
      return 0;
    }

    const pages = Math.ceil(filtered.length / pageSize);
    const safePage = Math.min(Math.max(1, page), pages);
    const slice = filtered.slice((safePage - 1) * pageSize, safePage * pageSize);
    const handlers = { click: onWordClickName, speak: onSpeakName, setStatus: onSetStatusName };

    container.innerHTML = slice.map((w) => cardHtml(w, wordStatus, selectedWords, handlers)).join("");
    onPager && onPager({ total: filtered.length, page: safePage, pages, pageSize });
    return filtered.length;
  }

  function debounce(fn, delay) {
    let timer = null;
    return (...args) => {
      if (timer) clearTimeout(timer);
      timer = setTimeout(() => fn(...args), delay);
    };
  }

  window.WordFilterRender = { renderWords, buildIndexes, debounce };
})();
