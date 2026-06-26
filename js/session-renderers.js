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

  function buildCompletionHtml(title, buttonText, buttonAction) {
    return `<div class="session-complete">
      <h3>${escapeHtml(title)}</h3>
      <button class="action-btn btn-primary" onclick="${escapeJsString(
        buttonAction
      )}">${escapeHtml(buttonText)}</button>
    </div>`;
  }

  function buildQuizQuestionHtml(word, options, index, total) {
    const safeWord = escapeHtml(word.english);
    const safePhonetic = escapeHtml(word.phonetic || "");
    const safeCorrect = escapeJsString(word.chinese);
    const safeEnglishJs = escapeJsString(word.english);
    const letters = ["A", "B", "C", "D", "E", "F"];
    const optionHtml = options
      .map((opt, i) => {
        const safeOpt = escapeHtml(opt);
        const safeOptJs = escapeJsString(opt);
        const safeOptAttr = escapeHtml(opt);
        return `<div class="quiz-option" data-opt="${safeOptAttr}" onclick="checkQuizAnswer('${safeOptJs}', '${safeCorrect}')">
          <span class="opt-key">${letters[i] || i + 1}</span>
          <span class="opt-text">${safeOpt}</span>
        </div>`;
      })
      .join("");

    return `<div class="session-card center">
      <p class="session-progress">问题 ${index + 1} / ${total}</p>
      <div class="session-word-head" style="justify-content:center">
        <h2 class="session-title" style="margin-bottom:6px">${safeWord}</h2>
        <button class="play-btn session-play-btn" onclick="speak('${safeEnglishJs}')">${window.Icon ? window.Icon("volume", 18) : "🔊"}</button>
      </div>
      <p class="session-phonetic">${safePhonetic}</p>
      <div class="session-options">
        ${optionHtml}
      </div>
    </div>`;
  }

  function buildPracticeWordHtml(word, index, total) {
    const safeEnglish = escapeHtml(word.english);
    const safePhonetic = escapeHtml(word.phonetic || "");
    const safeExample = escapeHtml(word.example || "");
    const safeEnglishJs = escapeJsString(word.english);
    const safeExampleJs = escapeJsString(word.example || "");

    return `<div class="session-card">
      <p class="session-progress">练习 ${index + 1}/${total}</p>
      <div class="session-word-head">
        <h2 class="session-title">${safeEnglish}</h2>
        <button class="play-btn session-play-btn" onclick="speak('${safeEnglishJs}')">${window.Icon ? window.Icon("volume", 18) : "🔊"}</button>
      </div>
      <p class="session-phonetic">${safePhonetic}</p>
      <div class="session-example-box">
        <p class="session-example-label">例句：</p>
        <p class="session-example-text">${safeExample}</p>
      </div>
      <div class="session-input-wrap">
        <label class="session-input-label">造句练习：</label>
        <textarea class="practice-input session-input-textarea" id="practiceInput" placeholder="用 ${safeEnglish} 造一个句子..." rows="3"></textarea>
      </div>
      <div class="session-actions">
        <button class="action-btn btn-primary" onclick="checkSentence('${safeEnglishJs}')">检查句子</button>
        <button class="action-btn" onclick="showExampleSentence('${safeExampleJs}')">查看例句</button>
        <button class="action-btn" onclick="speak('${safeEnglishJs}')">朗读</button>
      </div>
      <div id="sentenceFeedback" class="session-feedback"></div>
    </div>`;
  }

  function buildListeningWordHtml(word, index, total) {
    const safeEnglish = escapeHtml(word.english);
    const safeEnglishJs = escapeJsString(word.english);

    return `<div class="session-card">
      <p class="session-progress">练习 ${index + 1}/${total}</p>
      <div class="session-audio-box">
        <p class="session-audio-label">点击播放，听音输入单词</p>
        <div class="session-word-center">
          <h2 class="session-title session-title-muted">请先听音，再输入答案</h2>
          <button class="play-btn session-play-btn-lg" onclick="speak('${safeEnglishJs}')">${window.Icon ? window.Icon("volume", 18) : "🔊"}</button>
        </div>
        <p id="listeningRevealWord" class="session-reveal-word hidden">正确单词：${safeEnglish}</p>
      </div>
      <div class="session-input-wrap">
        <label class="session-input-label">你听到的单词是：</label>
        <input type="text" class="practice-input session-input-center" id="listeningInput" placeholder="输入你听到的单词...">
      </div>
      <div class="session-actions">
        <button class="action-btn btn-primary" onclick="checkListeningAnswer('${safeEnglishJs}')">检查答案</button>
        <button class="action-btn" onclick="speak('${safeEnglishJs}')">再听一次</button>
      </div>
      <div id="listeningFeedback" class="session-feedback"></div>
    </div>`;
  }

  function buildSpellingWordHtml(word, maskedWord, index, total) {
    const safeEnglish = escapeHtml(word.english);
    const safeMasked = escapeHtml(maskedWord);
    const safeEnglishJs = escapeJsString(word.english);

    return `<div class="session-card">
      <p class="session-progress">练习 ${index + 1}/${total}</p>
      <div class="session-audio-box">
        <p class="session-audio-label">根据发音补全拼写</p>
        <div class="session-word-center">
          <h2 class="session-title session-title-spaced">${safeMasked}</h2>
          <button class="play-btn session-play-btn-lg" onclick="speak('${safeEnglishJs}')">${window.Icon ? window.Icon("volume", 18) : "🔊"}</button>
        </div>
      </div>
      <div class="session-input-wrap">
        <label class="session-input-label">输入完整拼写：</label>
        <input type="text" class="practice-input session-input-center" id="spellingInput" placeholder="输入单词的完整拼写...">
      </div>
      <div class="session-actions">
        <button class="action-btn btn-primary" onclick="checkSpellingAnswer('${safeEnglishJs}')">检查拼写</button>
        <button class="action-btn" onclick="speak('${safeEnglishJs}')">再听一次</button>
      </div>
      <div id="spellingFeedback" class="session-feedback"></div>
    </div>`;
  }

  function buildStudyCardHtml(word, index, total) {
    const eng = escapeHtml(word.english);
    const engJs = escapeJsString(word.english);
    const sound = window.Icon ? window.Icon("volume", 20) : "🔊";
    const tag = (cls, t) =>
      t && t !== "其他" && t !== "通用"
        ? `<span class="word-tag ${cls}">${escapeHtml(t)}</span>`
        : "";

    return `<div class="session-card center study">
      <p class="session-progress">学习 ${index + 1} / ${total}</p>
      <div class="session-word-head" style="justify-content:center">
        <h2 class="session-title" style="margin:0">${eng}</h2>
        <button class="play-btn session-play-btn" onclick="speak('${engJs}')" aria-label="朗读">${sound}</button>
      </div>
      <p class="session-phonetic">${escapeHtml(word.phonetic || "")}</p>
      <div id="studyBack" class="study-back hidden">
        <div class="study-tags">${tag("pos-tag", word.part_of_speech)}${tag("theme-tag", word.theme)}</div>
        <p class="study-cn">${escapeHtml(word.chinese || "")}</p>
        ${word.example ? `<div class="session-example-box"><p class="session-example-text">${escapeHtml(word.example)}</p></div>` : ""}
      </div>
      <div class="study-controls">
        <button class="action-btn btn-primary study-reveal-btn" id="studyRevealBtn" onclick="revealStudy()">显示释义</button>
        <div id="studyRate" class="study-rate hidden">
          <button class="action-btn study-rate-unknown" onclick="rateStudy('unknown')"><span class="study-key">1</span>不认识</button>
          <button class="action-btn study-rate-vague" onclick="rateStudy('vague')"><span class="study-key">2</span>模糊</button>
          <button class="action-btn study-rate-known" onclick="rateStudy('known')"><span class="study-key">3</span>认识</button>
        </div>
        <p class="study-hint">空格显示释义 · 1 / 2 / 3 评分</p>
      </div>
    </div>`;
  }

  function buildSpeakingHtml(word, index, total) {
    const eng = escapeHtml(word.english);
    const engJs = escapeJsString(word.english);
    const sound = window.Icon ? window.Icon("volume", 20) : "🔊";
    const mic = window.Icon ? window.Icon("mic", 22) : "🎤";
    return `<div class="session-card center speaking">
      <p class="session-progress">跟读 ${index + 1} / ${total}</p>
      <div class="session-word-head" style="justify-content:center">
        <h2 class="session-title" style="margin:0">${eng}</h2>
        <button class="play-btn session-play-btn" onclick="speak('${engJs}')" aria-label="朗读">${sound}</button>
      </div>
      <p class="session-phonetic">${escapeHtml(word.phonetic || "")}</p>
      <p class="speak-cn">${escapeHtml(word.chinese || "")}</p>
      <button class="mic-btn" id="micBtn" onclick="toggleSpeechRec()">${mic}<span id="micLabel">点击朗读</span></button>
      <div id="speakFeedback" class="session-feedback"></div>
      <div class="session-actions" style="justify-content:center;margin-top:16px">
        <button class="action-btn" onclick="speak('${engJs}')">先听一遍</button>
        <button class="action-btn btn-primary" onclick="nextSpeaking()">下一个 →</button>
      </div>
    </div>`;
  }

  function buildStudyCompleteHtml(stats) {
    return `<div class="session-complete">
      <h3>本组学习完成</h3>
      <p class="session-complete-score">认识 ${stats.known} · 模糊 ${stats.vague} · 不认识 ${stats.unknown}</p>
      <div class="session-actions" style="justify-content:center">
        <button class="action-btn btn-primary" onclick="startStudy()">再来一组</button>
        <button class="action-btn" onclick="closeStudyModal()">完成</button>
      </div>
    </div>`;
  }

  window.WordSessionRenderers = {
    buildCompletionHtml,
    buildQuizQuestionHtml,
    buildPracticeWordHtml,
    buildListeningWordHtml,
    buildSpellingWordHtml,
    buildStudyCardHtml,
    buildStudyCompleteHtml,
    buildSpeakingHtml,
  };
})();
