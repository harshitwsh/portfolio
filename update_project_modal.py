import re

def update_project_modal():
    modal_css = """
    .map-panel-backdrop {
      position: fixed; inset: 0; z-index: 105;
      background: rgba(6, 10, 8, 0.65);
      opacity: 0; pointer-events: none;
      transition: opacity 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .map-panel-backdrop.is-active {
      opacity: 1; pointer-events: auto;
    }
    .map-panel {
      position: fixed; top: 50%; left: 50%;
      transform: translate(-50%, -50%) scale(0.96);
      z-index: 106;
      width: min(780px, calc(100vw - 32px));
      max-height: calc(100vh - 32px);
      box-sizing: border-box;
      color: #F4F7F5;
      background: rgba(13, 17, 15, 0.96);
      background-image: radial-gradient(circle at 50% 0%, rgba(34, 197, 94, 0.08) 0%, transparent 65%);
      border: 1px solid rgba(255, 255, 255, 0.10);
      border-radius: 26px;
      box-shadow: 0 24px 60px -12px rgba(0, 0, 0, 0.9), 0 0 45px -10px rgba(34, 197, 94, 0.15);
      opacity: 0; pointer-events: none;
      transition: opacity 0.25s cubic-bezier(0.16, 1, 0.3, 1), transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      font-family: 'Inter', system-ui, -apple-system, sans-serif;
      overflow-y: auto;
      overflow-x: hidden;
      scrollbar-width: thin;
      scrollbar-color: rgba(34, 197, 94, 0.3) transparent;
    }
    .map-panel::-webkit-scrollbar {
      width: 5px;
    }
    .map-panel::-webkit-scrollbar-thumb {
      background: rgba(34, 197, 94, 0.3);
      border-radius: 4px;
    }
    .map-panel.is-open {
      opacity: 1; pointer-events: auto;
      transform: translate(-50%, -50%) scale(1);
    }
    .mp-close-btn {
      position: absolute; top: 20px; right: 20px; z-index: 10;
      width: 36px; height: 36px; border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #AAB4B0; display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: all 0.2s ease;
    }
    .mp-close-btn:hover {
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
      transform: scale(1.05);
    }
    .map-panel-inner {
      padding: 28px 32px;
      display: flex; flex-direction: column; gap: 14px;
    }

    /* HEADER */
    .mp-header {
      display: flex; align-items: center; gap: 20px;
      padding-right: 44px;
    }
    .mp-logo-box {
      width: 68px; height: 68px; border-radius: 18px;
      flex-shrink: 0; position: relative;
      border: 2px solid #22c55e;
      box-shadow: 0 0 18px rgba(34, 197, 94, 0.3);
      background: #08100c;
      display: flex; align-items: center; justify-content: center;
      overflow: hidden;
    }
    .mp-logo-img {
      width: 40px; height: 40px; object-fit: contain;
      display: block;
    }
    .mp-header-info {
      flex: 1; min-width: 0;
    }
    .mp-meta-row {
      display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 6px;
    }
    .mp-category {
      font-size: 11px; font-weight: 700; letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 3.5px 12px; border-radius: 999px;
      color: #4ade80;
      background: rgba(34, 197, 94, 0.09);
      border: 1px solid rgba(34, 197, 94, 0.35);
    }
    .mp-status-pill {
      font-size: 11px; font-weight: 700; letter-spacing: 0.06em;
      text-transform: uppercase;
      padding: 3.5px 10px; border-radius: 999px;
      color: #d1d5db;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      display: inline-flex; align-items: center; gap: 6px;
    }
    .mp-status-dot {
      width: 6px; height: 6px; border-radius: 50%;
      background: #22c55e;
      box-shadow: 0 0 8px #22c55e;
    }
    .mp-title {
      margin: 0; font-size: 26px; font-weight: 800; letter-spacing: -0.02em;
      color: #ffffff; line-height: 1.2;
    }
    .mp-tagline {
      font-size: 13.5px; font-weight: 500; color: #d1d5db;
      margin-top: 3px;
    }

    /* CARD SECTIONS */
    .mp-card {
      background: rgba(20, 26, 22, 0.55);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 16px;
      padding: 16px 18px;
      display: flex; flex-direction: column;
    }
    .mp-card-label {
      color: #4ade80; font-size: 12px; font-weight: 700; letter-spacing: 0.06em;
      display: flex; align-items: center; gap: 7px;
      text-transform: uppercase;
    }
    .mp-card-label svg {
      width: 14px; height: 14px; flex-shrink: 0;
    }
    .mp-card-text {
      margin: 10px 0 0 0; font-size: 12.8px; line-height: 1.55; color: #9ca3af;
    }

    /* FEATURES GRID */
    .mp-features-list {
      margin: 10px 0 0 0; padding-left: 14px;
      display: grid; grid-template-columns: repeat(2, 1fr);
      gap: 6px 16px;
    }
    .mp-features-list li {
      font-size: 12.2px; line-height: 1.45; color: #9ca3af;
    }
    .mp-features-list li::marker {
      color: #4ade80;
    }

    /* TECH PILLS */
    .mp-tools-row {
      display: flex; flex-wrap: wrap; gap: 5px; margin-top: 10px;
    }
    .mp-tool-badge {
      font-size: 11px; font-weight: 500; color: #d1d5db;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.09);
      padding: 3.5px 10px; border-radius: 999px;
      display: inline-flex; align-items: center; gap: 6px;
      white-space: nowrap;
    }
    .mp-tool-badge img {
      width: 13px; height: 13px; object-fit: contain;
    }

    /* ACTIONS */
    .mp-actions-row {
      display: flex; align-items: center; gap: 12px; margin-top: 2px;
    }
    .mp-btn-primary {
      display: inline-flex; align-items: center; gap: 8px;
      background: #22c55e; color: #08100c;
      font-size: 13px; font-weight: 700;
      padding: 9px 20px; border-radius: 999px;
      border: none; text-decoration: none; cursor: pointer;
      box-shadow: 0 4px 18px rgba(34, 197, 94, 0.35);
      transition: all 0.2s ease;
    }
    .mp-btn-primary:hover {
      background: #4ade80;
      transform: translateY(-1px);
      box-shadow: 0 6px 24px rgba(34, 197, 94, 0.5);
    }
    .mp-btn-primary svg {
      width: 14px; height: 14px;
    }
    .mp-btn-secondary {
      display: inline-flex; align-items: center; gap: 8px;
      background: rgba(255, 255, 255, 0.04);
      color: #ffffff;
      font-size: 13px; font-weight: 600;
      padding: 9px 18px; border-radius: 999px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      text-decoration: none; cursor: pointer;
      transition: all 0.2s ease;
    }
    .mp-btn-secondary:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.25);
      transform: translateY(-1px);
    }
    .mp-btn-secondary svg {
      width: 14px; height: 14px;
    }

    @media (max-width: 768px) {
      .map-panel-inner {
        padding: 20px 16px;
      }
      .mp-header {
        flex-direction: column; align-items: flex-start; gap: 12px;
        padding-right: 32px;
      }
      .mp-features-list {
        grid-template-columns: 1fr;
      }
      .mp-actions-row {
        flex-direction: column; align-items: stretch;
      }
    }
    """

    panel_html = """
    <button class="mp-close-btn" type="button" aria-label="Close modal">
      <svg width="13" height="13" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M1 1L13 13M1 13L13 1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
      </svg>
    </button>
    <div class="map-panel-inner">
      <!-- HEADER -->
      <div class="mp-header">
        <div class="mp-logo-box">
          <img class="mp-logo-img" data-company-logo alt="" />
        </div>
        <div class="mp-header-info">
          <div class="mp-meta-row">
            <span class="mp-category" data-category>PROJECT</span>
            <span class="mp-status-pill" data-status-wrap>
              <span class="mp-status-dot"></span>
              <span data-status>ACTIVE</span>
            </span>
          </div>
          <h2 class="mp-title" data-project-title></h2>
          <div class="mp-tagline" data-tagline></div>
        </div>
      </div>

      <!-- ABOUT PROJECT -->
      <div class="mp-card">
        <div class="mp-card-label">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
          <span>ABOUT PROJECT</span>
        </div>
        <p class="mp-card-text" data-desc></p>
      </div>

      <!-- KEY FEATURES -->
      <div class="mp-card">
        <div class="mp-card-label">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
          <span>KEY FEATURES &amp; CAPABILITIES</span>
        </div>
        <ul class="mp-features-list" data-features></ul>
      </div>

      <!-- TECH STACK -->
      <div class="mp-card">
        <div class="mp-card-label">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          <span>TECH STACK &amp; TOOLS</span>
        </div>
        <div class="mp-tools-row" data-tools></div>
      </div>

      <!-- ACTIONS -->
      <div class="mp-actions-row">
        <a class="mp-btn-primary" data-url href="#" target="_blank">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
          <span>View Live Project</span>
        </a>
        <a class="mp-btn-secondary" data-github href="#" target="_blank">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
          <span>GitHub Repo</span>
        </a>
      </div>
    </div>
    """

    new_functions_js = f"""var SD = !1;
function CD() {{
  if (SD) return;
  SD = !0;
  let e = document.createElement("style");
  e.dataset.mapPanel = "1";
  e.textContent = `{modal_css}`;
  document.head.appendChild(e);
}}

function TD({{ onJoin: e }} = {{}}) {{
  CD();
  let backdrop = document.createElement("div");
  backdrop.className = "map-panel-backdrop";
  document.body.appendChild(backdrop);

  let t = document.createElement("div");
  t.className = "map-panel";
  t._backdrop = backdrop;
  t.innerHTML = `{panel_html}`;

  let closeBtn = t.querySelector(".mp-close-btn");
  closeBtn.addEventListener("click", (e) => {{
    e.stopPropagation();
    X.play("click");
    OD(t);
  }});
  backdrop.addEventListener("click", (e) => {{
    e.stopPropagation();
    OD(t);
  }});

  let onKeyEsc = (e) => {{
    if (e.key === "Escape" && t.classList.contains("is-open")) OD(t);
  }};
  window.addEventListener("keydown", onKeyEsc);
  t._onKeyEsc = onKeyEsc;
  t.addEventListener("pointerdown", (e) => e.stopPropagation());
  t.addEventListener("click", (e) => e.stopPropagation());

  document.body.appendChild(t);
  return t;
}}

function DD(e, t) {{
  X.play("hand-entry");
  
  let logoImg = e.querySelector("[data-company-logo]");
  if (logoImg) {{
    logoImg.alt = t.company || t.shortTitle || "Project Logo";
    logoImg.style.display = "";
    logoImg.onerror = () => {{ logoImg.style.display = "none"; }};
    let src = t.logo || ED(t.company);
    logoImg.src = src.includes("/") ? src : `/assets/logos/companies/${{src}}.webp`;
  }}

  let cat = e.querySelector("[data-category]");
  if (cat) cat.textContent = t.category || "DEVELOPMENT";

  let statusText = e.querySelector("[data-status]");
  if (statusText) statusText.textContent = t.status || "ACTIVE";

  let title = e.querySelector("[data-project-title]");
  if (title) title.textContent = t.shortTitle || t.company || "";

  let tagline = e.querySelector("[data-tagline]");
  if (tagline) tagline.textContent = t.tagline || t.scenario || "";

  let desc = e.querySelector("[data-desc]");
  if (desc) desc.textContent = t.description || "";

  let featList = e.querySelector("[data-features]");
  if (featList) {{
    let feats = t.features || [];
    featList.innerHTML = feats.map(f => {{
      let text = typeof f === "string" ? f : `${{f.title || ""}}: ${{f.desc || ""}}`;
      return `<li>${{text}}</li>`;
    }}).join("");
  }}

  let toolsContainer = e.querySelector("[data-tools]");
  if (toolsContainer) {{
    let tools = t.tools || [];
    toolsContainer.innerHTML = tools.map(tool => `
      <span class="mp-tool-badge">
        <img src="/assets/logos/tools/${{tool}}.svg" alt="" loading="lazy" onerror="this.style.display='none'" />
        ${{YS[tool] || tool}}
      </span>
    `).join("");
  }}

  let urlBtn = e.querySelector("[data-url]");
  if (urlBtn) {{
    if (t.url) {{
      urlBtn.href = t.url;
      urlBtn.style.display = "inline-flex";
    }} else {{
      urlBtn.style.display = "none";
    }}
  }}

  let githubBtn = e.querySelector("[data-github]");
  if (githubBtn) {{
    if (t.github) {{
      githubBtn.href = t.github;
      githubBtn.style.display = "inline-flex";
    }} else {{
      githubBtn.style.display = "none";
    }}
  }}

  if (e._backdrop) e._backdrop.classList.add("is-active");
  e.classList.add("is-open");
  e._activeId = t.id;
}}"""

    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        start = code.find("function CD()")
        end = code.find("function OD(", start)
        
        if start != -1 and end != -1:
            new_code = code[:start] + new_functions_js + "\n\n" + code[end:]
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_code)
            print("Successfully updated project modal in:", filepath)
        else:
            print("Error: CD or OD marker not found in:", filepath)

update_project_modal()
