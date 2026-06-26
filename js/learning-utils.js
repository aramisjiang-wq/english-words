/* ============================================================
   Learning utilities — sampling, quiz building, and a
   lightweight SM-2 spaced-repetition scheduler.
   Exposed via window.WordLearningUtils.
   ============================================================ */
(() => {
  function shuffle(list) {
    const arr = [...list];
    for (let i = arr.length - 1; i > 0; i -= 1) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }

  function sample(list, count) {
    if (!Array.isArray(list) || list.length === 0 || count <= 0) return [];
    return shuffle(list).slice(0, count);
  }

  /* ---- Stable per-word key (mirrors app's __key) ---- */
  function keyOf(word) {
    return word.__key || word.english;
  }

  /* ---- Date helpers (local-day granularity) ---- */
  function dayStr(date = new Date()) {
    const d = new Date(date);
    return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
  }

  function addDays(dateStr, days) {
    const d = new Date(dateStr + "T00:00:00");
    d.setDate(d.getDate() + days);
    return dayStr(d);
  }

  function daysBetween(fromStr, toStr) {
    const a = new Date(fromStr + "T00:00:00");
    const b = new Date(toStr + "T00:00:00");
    return Math.round((b - a) / 86400000);
  }

  /* ---- Spaced repetition (SM-2 lite) ----
     A record looks like:
       { reps, ease, interval, due, lastReviewed, lapses }
     `remembered` is a boolean recall outcome. */
  function newRecord() {
    return { reps: 0, ease: 2.5, interval: 0, due: dayStr(), lastReviewed: null, lapses: 0 };
  }

  function migrateRecord(old) {
    // Upgrade legacy { reviewDates:[], level } shape.
    if (old && typeof old.ease === "number") return { ...newRecord(), ...old };
    const rec = newRecord();
    if (old && Array.isArray(old.reviewDates) && old.reviewDates.length) {
      rec.reps = old.level || old.reviewDates.length;
      const last = old.reviewDates[old.reviewDates.length - 1];
      rec.lastReviewed = last;
      const intervals = [1, 2, 4, 7, 15, 30];
      rec.interval = intervals[Math.min(rec.reps, intervals.length - 1)];
      rec.due = addDays(last, rec.interval);
    }
    return rec;
  }

  function scheduleNext(record, remembered, today = dayStr()) {
    const r = { ...newRecord(), ...(record || {}) };
    if (remembered) {
      r.reps += 1;
      if (r.reps === 1) r.interval = 1;
      else if (r.reps === 2) r.interval = 3;
      else r.interval = Math.max(1, Math.round(r.interval * r.ease));
      r.ease = Math.min(2.8, r.ease + 0.05);
    } else {
      r.reps = 0;
      r.interval = 1;
      r.ease = Math.max(1.3, r.ease - 0.2);
      r.lapses += 1;
    }
    r.lastReviewed = today;
    r.due = addDays(today, r.interval);
    return r;
  }

  function isDue(record, today = dayStr()) {
    if (!record || !record.due) return false;
    return daysBetween(today, record.due) <= 0;
  }

  function collectDueKeys(reviewData, today = dayStr()) {
    const due = [];
    Object.entries(reviewData || {}).forEach(([key, rec]) => {
      if (isDue(migrateRecord(rec), today)) due.push(key);
    });
    return due;
  }

  /* ---- Build a practice pool: prioritise difficult, then due,
         then unlearned words. ---- */
  function pickReviewPool(wordsData, wordStatus, totalCount, difficultCount, reviewData = {}) {
    const today = dayStr();
    const dueKeys = new Set(collectDueKeys(reviewData, today));

    const difficult = wordsData.filter((w) => wordStatus[keyOf(w)] === "red");
    const dueWords = wordsData.filter((w) => dueKeys.has(keyOf(w)) && wordStatus[keyOf(w)] !== "green");
    const unlearned = wordsData.filter((w) => {
      const s = wordStatus[keyOf(w)];
      return !s || s === "gray";
    });

    const picked = [];
    const used = new Set();
    const take = (pool, n) => {
      for (const w of sample(pool.filter((w) => !used.has(keyOf(w))), n)) {
        picked.push(w);
        used.add(keyOf(w));
      }
    };

    take(difficult, difficultCount);
    if (picked.length < totalCount) take(dueWords, totalCount - picked.length);
    if (picked.length < totalCount) take(unlearned, totalCount - picked.length);
    return picked;
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
    shuffle,
    keyOf,
    dayStr,
    addDays,
    daysBetween,
    newRecord,
    migrateRecord,
    scheduleNext,
    isDue,
    collectDueKeys,
    pickReviewPool,
    buildQuizOptions,
    getMasteredCount,
    buildTrendData,
  };
})();
