/* ============================================================
   UI Feedback — toasts & confirm dialog
   Replaces the browser's alert()/confirm() with refined,
   theme-aware components. Exposed via window.UI.
   ============================================================ */
(() => {
  const ICONS = { success: "✓", error: "✕", warning: "!", info: "i" };
  const TITLES = { success: "成功", error: "出错了", warning: "提示", info: "提示" };

  function ensureStack() {
    let stack = document.getElementById("toastStack");
    if (!stack) {
      stack = document.createElement("div");
      stack.id = "toastStack";
      stack.className = "toast-stack";
      stack.setAttribute("role", "status");
      stack.setAttribute("aria-live", "polite");
      document.body.appendChild(stack);
    }
    return stack;
  }

  function toast(message, options = {}) {
    const type = options.type || "info";
    const title = options.title || TITLES[type];
    const duration = options.duration ?? 3200;

    const stack = ensureStack();
    const el = document.createElement("div");
    el.className = `toast ${type}`;
    el.innerHTML = `
      <span class="toast-icon">${ICONS[type] || "i"}</span>
      <div class="toast-body">
        <div class="toast-title"></div>
        <div class="toast-msg"></div>
      </div>`;
    el.querySelector(".toast-title").textContent = title;
    el.querySelector(".toast-msg").textContent = message;
    stack.appendChild(el);

    const remove = () => {
      el.classList.add("leaving");
      el.addEventListener("animationend", () => el.remove(), { once: true });
      setTimeout(() => el.remove(), 400);
    };
    el.addEventListener("click", remove);
    if (duration > 0) setTimeout(remove, duration);
    return el;
  }

  const success = (m, o = {}) => toast(m, { ...o, type: "success" });
  const error = (m, o = {}) => toast(m, { ...o, type: "error" });
  const warning = (m, o = {}) => toast(m, { ...o, type: "warning" });
  const info = (m, o = {}) => toast(m, { ...o, type: "info" });

  /* ---- Confirm dialog (Promise-based) ---- */
  function confirm(message, options = {}) {
    const title = options.title || "确认操作";
    const confirmText = options.confirmText || "确定";
    const cancelText = options.cancelText || "取消";
    const danger = options.danger || false;

    return new Promise((resolve) => {
      const overlay = document.createElement("div");
      overlay.className = "confirm-dialog active";
      overlay.innerHTML = `
        <div class="confirm-box" role="alertdialog" aria-modal="true">
          <div class="confirm-title"></div>
          <div class="confirm-msg"></div>
          <div class="confirm-actions">
            <button class="action-btn btn-secondary" data-act="cancel"></button>
            <button class="action-btn ${danger ? "btn-danger" : "btn-primary"}" data-act="ok"></button>
          </div>
        </div>`;
      overlay.querySelector(".confirm-title").textContent = title;
      overlay.querySelector(".confirm-msg").textContent = message;
      overlay.querySelector('[data-act="cancel"]').textContent = cancelText;
      overlay.querySelector('[data-act="ok"]').textContent = confirmText;

      const close = (result) => {
        document.removeEventListener("keydown", onKey);
        overlay.remove();
        resolve(result);
      };
      const onKey = (e) => {
        if (e.key === "Escape") close(false);
        if (e.key === "Enter") close(true);
      };

      overlay.addEventListener("click", (e) => {
        const act = e.target.getAttribute?.("data-act");
        if (act === "ok") close(true);
        else if (act === "cancel" || e.target === overlay) close(false);
      });
      document.addEventListener("keydown", onKey);

      document.body.appendChild(overlay);
      overlay.querySelector('[data-act="ok"]').focus();
    });
  }

  window.UI = { toast, success, error, warning, info, confirm };
})();
