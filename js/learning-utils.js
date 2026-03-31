(() => {
  function shuffle(list) {
    const arr = [...list];
    for (let i = arr.length - 1; i > 0; i -= 1) {
      const j = Math.floor(Math.random() * (i + 1));
      const tmp = arr[i];
      arr[i] = arr[j];
      arr[j] = tmp;
    }
    return arr;
  }

  function sample(list, count) {
    if (!Array.isArray(list) || list.length === 0 || count <= 0) {
      return [];
    }
    return shuffle(list).slice(0, count);
  }

  function pickReviewPool(wordsData, wordStatus, totalCount, difficultCount) {
    const difficultWords = wordsData.filter(
      (w) => wordStatus[w.__key || w.english] === "red"
    );
    const unlearnedWords = wordsData.filter(
      (w) =>
        !wordStatus[w.__key || w.english] ||
        wordStatus[w.__key || w.english] === "gray"
    );

    let selected = sample(difficultWords, difficultCount);
    if (selected.length < totalCount) {
      const used = new Set(selected.map((w) => w.english));
      const candidates = unlearnedWords.filter((w) => !used.has(w.english));
      const remaining = totalCount - selected.length;
      selected = [...selected, ...sample(candidates, remaining)];
    }

    return selected;
  }

  function buildQuizOptions(wordsData, currentWord, optionCount = 4) {
    const wrongCount = Math.max(0, optionCount - 1);
    const wrongOptions = sample(
      wordsData.filter((w) => w.chinese !== currentWord.chinese).map((w) => w.chinese),
      wrongCount
    );
    return shuffle([currentWord.chinese, ...wrongOptions]);
  }

  function getMasteredCount(wordStatus) {
    return Object.values(wordStatus).filter((s) => s === "green").length;
  }

  function buildTrendData(learningHistory, totalWords, fallbackPercentage = 0) {
    const dates = Object.keys(learningHistory).sort();
    const dataPoints = dates.map((date) => {
      const item = learningHistory[date] || {};
      const snapshot =
        typeof item.masteredPercentage === "number"
          ? item.masteredPercentage
          : typeof item.mastered === "number" && totalWords > 0
            ? Math.round((item.mastered / totalWords) * 100)
            : fallbackPercentage;
      return { date, percentage: snapshot };
    });
    return { dates, dataPoints };
  }

  window.WordLearningUtils = {
    sample,
    pickReviewPool,
    buildQuizOptions,
    getMasteredCount,
    buildTrendData,
  };
})();
