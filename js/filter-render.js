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

  function buildIndexes(wordsData) {
    const indexFields = [
      "parent_category",
      "child_category",
      "category",
      "part_of_speech",
      "theme",
    ];
    const indexes = {};
    indexFields.forEach((field) => {
      indexes[field] = new Map();
    });

    wordsData.forEach((word) => {
      indexFields.forEach((field) => {
        const fallback =
          field === "parent_category" || field === "child_category" || field === "theme" || field === "part_of_speech"
            ? "其他"
            : "";
        const key = word[field] || fallback;
        if (!indexes[field].has(key)) {
          indexes[field].set(key, []);
        }
        indexes[field].get(key).push(word);
      });
    });

    return indexes;
  }

  function getFilteredBaseWords(wordsData, filters, indexes) {
    if (!indexes) {
      return wordsData;
    }

    const activeFilters = [
      { field: "parent_category", value: filters.parentCategoryFilter },
      { field: "child_category", value: filters.childCategoryFilter },
      { field: "category", value: filters.categoryFilter },
      { field: "part_of_speech", value: filters.partOfSpeechFilter },
      { field: "theme", value: filters.themeFilter },
    ].filter((item) => item.value !== "all");

    if (activeFilters.length === 0) {
      return wordsData;
    }

    let base = null;
    activeFilters.forEach((item) => {
      const bucket = indexes[item.field]?.get(item.value) || [];
      if (base === null || bucket.length < base.length) {
        base = bucket;
      }
    });

    if (!base || base.length === 0) {
      return [];
    }

    return base;
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
    } = params;

    const searchTerm = (filters.searchTerm || "").toLowerCase();

    const baseWords = getFilteredBaseWords(wordsData, filters, indexes);
    const filteredWords = baseWords.filter((word) => {
      const english = String(word.english || "");
      const chinese = String(word.chinese || "");
      const wordKey = word.__key || english;
      const status = wordStatus[wordKey] || "gray";

      const matchesSearch =
        english.toLowerCase().includes(searchTerm) || chinese.includes(searchTerm);
      const matchesParentCategory =
        filters.parentCategoryFilter === "all" ||
        (word.parent_category || "其他") === filters.parentCategoryFilter;
      const matchesChildCategory =
        filters.childCategoryFilter === "all" ||
        (word.child_category || "其他") === filters.childCategoryFilter;
      const matchesCategory =
        filters.categoryFilter === "all" || word.category === filters.categoryFilter;
      const matchesPartOfSpeech =
        filters.partOfSpeechFilter === "all" ||
        (word.part_of_speech || "其他") === filters.partOfSpeechFilter;
      const matchesTheme =
        filters.themeFilter === "all" || (word.theme || "其他") === filters.themeFilter;
      const matchesStatus =
        filters.statusFilter === "all" || status === filters.statusFilter;

      return (
        matchesSearch &&
        matchesParentCategory &&
        matchesChildCategory &&
        matchesCategory &&
        matchesPartOfSpeech &&
        matchesTheme &&
        matchesStatus
      );
    });

    if (filteredWords.length === 0) {
      container.innerHTML =
        '<div class="empty-state">' +
        "<h3>没有找到匹配的单词</h3>" +
        "<p>试着调整搜索词或筛选条件</p>" +
        "</div>";
      return;
    }

    container.innerHTML = filteredWords
      .map((word) => {
        const english = String(word.english || "");
        const wordKey = String(word.__key || english);
        const chinese = String(word.chinese || "");
        const phonetic = String(word.phonetic || "");
        const example = String(word.example || "");
        const status = wordStatus[wordKey] || "gray";
        const partOfSpeech = word.part_of_speech || "其他";
        const theme = word.theme || "其他";
        const parentCategory = word.parent_category || "其他";
        const childCategory = word.child_category || "其他";
        const isSelected = selectedWords.has(wordKey);
        const safeEnglish = escapeJsString(english);
        const safeWordKey = escapeJsString(wordKey);

        const sound = window.Icon ? window.Icon("volume", 18) : "🔊";
        const meta = [
          { cls: "pos-tag", text: partOfSpeech },
          { cls: "theme-tag", text: theme },
          { cls: "child-tag", text: childCategory },
        ]
          .filter((t) => t.text && t.text !== "其他")
          .map((t) => `<span class="word-tag ${t.cls}">${escapeHtml(t.text)}</span>`)
          .join("");

        return `
          <div class="word-card ${status} ${isSelected ? "selected" : ""}" data-word="${escapeHtml(english)}" data-key="${escapeHtml(wordKey)}" onclick="${onWordClickName}('${safeWordKey}')">
            <div class="word-english">
              <span class="word-english-text">${escapeHtml(english)}</span>
              <button class="play-btn" onclick="event.stopPropagation(); ${onSpeakName}('${safeEnglish}')" aria-label="朗读">${sound}</button>
            </div>
            <div class="word-phonetic">${escapeHtml(phonetic)}</div>
            <div class="word-chinese">${escapeHtml(chinese)}</div>
            ${example ? `<div class="word-example">${escapeHtml(example)}</div>` : ""}
            <div class="word-tags">${meta}</div>
            <div class="word-actions">
              <span class="status-badge ${status === "gray" || !status ? "active" : ""}" onclick="event.stopPropagation(); ${onSetStatusName}('${safeWordKey}', 'gray')">未学习</span>
              <span class="status-badge ${status === "green" ? "green" : ""}" onclick="event.stopPropagation(); ${onSetStatusName}('${safeWordKey}', 'green')">已掌握</span>
              <span class="status-badge ${status === "red" ? "red" : ""}" onclick="event.stopPropagation(); ${onSetStatusName}('${safeWordKey}', 'red')">难记</span>
            </div>
          </div>
        `;
      })
      .join("");
  }

  function debounce(fn, delay) {
    let timer = null;
    return (...args) => {
      if (timer) {
        clearTimeout(timer);
      }
      timer = setTimeout(() => {
        fn(...args);
      }, delay);
    };
  }

  window.WordFilterRender = {
    renderWords,
    buildIndexes,
    debounce,
  };
})();
