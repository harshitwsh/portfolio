import re

def update_resume_modal():
    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    new_resume_code = r'''var resumeModalStylesInjected = !1;
function injectResumeModalStyles() {
  if (resumeModalStylesInjected) return;
  resumeModalStylesInjected = !0;
  let e = document.createElement("style");
  e.dataset.resumeModal = "1";
  e.textContent = `
    .resume-backdrop {
      position: fixed; inset: 0; z-index: 105;
      background: rgba(6, 12, 9, 0.65);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      opacity: 0; pointer-events: none;
      transition: opacity 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .resume-backdrop.is-active {
      opacity: 1; pointer-events: auto;
    }
    .resume-modal {
      position: fixed; left: 50%; top: 50%;
      width: min(960px, calc(100vw - 32px));
      max-height: min(88vh, 860px);
      box-sizing: border-box;
      color: #F4F7F5;
      background: rgba(10, 18, 14, 0.94);
      background-image: radial-gradient(circle at 50% 0%, rgba(32, 217, 154, 0.08) 0%, transparent 65%);
      backdrop-filter: blur(28px) saturate(130%);
      -webkit-backdrop-filter: blur(28px) saturate(130%);
      border: 1px solid rgba(255, 255, 255, 0.10);
      border-radius: 26px;
      box-shadow: 0 24px 60px -12px rgba(0, 0, 0, 0.85), 0 0 45px -10px rgba(32, 217, 154, 0.18);
      opacity: 0; pointer-events: none;
      transform: translate(-50%, calc(-50% + 18px)) scale(0.97);
      transform-origin: center;
      transition: opacity 0.28s cubic-bezier(0.16, 1, 0.3, 1), transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 110;
      font-family: 'Google Sans Flex', 'Google Sans Code', -apple-system, sans-serif;
      display: flex; flex-direction: column;
      overflow: hidden;
    }
    .resume-modal.is-open {
      opacity: 1; pointer-events: auto;
      transform: translate(-50%, -50%) scale(1);
    }
    .resume-modal-inner {
      padding: 26px 30px 24px 30px;
      overflow-y: auto;
      overflow-x: hidden;
      display: flex; flex-direction: column; gap: 16px;
      box-sizing: border-box;
      max-height: calc(min(88vh, 860px) - 2px);
    }
    .resume-modal-inner::-webkit-scrollbar {
      width: 4px;
    }
    .resume-modal-inner::-webkit-scrollbar-track {
      background: transparent;
    }
    .resume-modal-inner::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.16);
      border-radius: 8px;
    }
    .rm-close-btn {
      position: absolute; top: 18px; right: 18px;
      width: 34px; height: 34px; border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.10);
      color: #AAB5B0;
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: all 0.18s ease;
      z-index: 10; padding: 0; outline: none;
    }
    .rm-close-btn:hover {
      background: rgba(32, 217, 154, 0.15);
      border-color: rgba(32, 217, 154, 0.35);
      color: #20D99A;
      transform: scale(1.06);
    }
    .rm-close-btn:active {
      transform: scale(0.94);
    }
    .rm-header-row {
      display: flex; align-items: center; gap: 24px;
      padding-right: 36px;
    }
    .rm-photo-frame {
      width: 112px; height: 112px; flex-shrink: 0;
      border-radius: 50%;
      padding: 2.5px;
      background: linear-gradient(135deg, rgba(32, 217, 154, 0.6) 0%, rgba(32, 217, 154, 0.1) 100%);
      box-shadow: 0 0 20px rgba(32, 217, 154, 0.25);
    }
    .rm-photo-img {
      width: 100%; height: 100%; object-fit: cover; border-radius: 50%;
      display: block; background: #141c18;
    }
    .rm-header-content {
      display: flex; flex-direction: column; gap: 3px; min-width: 0; flex: 1;
    }
    .rm-badge-row {
      display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 2px;
    }
    .rm-badge-pill {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 10px; letter-spacing: 0.08em; text-transform: uppercase;
      color: #20D99A; font-weight: 600;
      background: rgba(32, 217, 154, 0.10);
      border: 1px solid rgba(32, 217, 154, 0.28);
      padding: 2px 8px; border-radius: 16px;
    }
    .rm-main-name {
      font-size: 26px; font-weight: 700; color: #F4F7F5;
      letter-spacing: -0.025em; line-height: 1.15; margin: 0;
    }
    .rm-role-sub {
      font-size: 13.5px; color: #AAB5B0; font-weight: 400; line-height: 1.35;
    }
    .rm-univ-sub {
      font-size: 12.5px; color: #788782; font-weight: 400;
    }
    .rm-quick-nav {
      display: flex; flex-wrap: wrap; gap: 7px; margin-top: 6px;
    }
    .rm-nav-btn {
      height: 27px; border-radius: 7px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.09);
      display: inline-flex; align-items: center; gap: 5px;
      padding: 0 9px; font-size: 11.5px; font-weight: 500;
      color: #e2e8f0; text-decoration: none; cursor: pointer;
      transition: all 0.15s ease;
    }
    .rm-nav-btn:hover {
      background: rgba(32, 217, 154, 0.12);
      border-color: rgba(32, 217, 154, 0.35);
      color: #20D99A;
      transform: translateY(-1px);
    }
    .rm-nav-btn svg {
      width: 12px; height: 12px; opacity: 0.85;
    }
    .rm-hr {
      height: 1px; width: 100%;
      background: rgba(255, 255, 255, 0.08);
      margin: -2px 0;
    }
    .rm-sec-title {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 10.5px; letter-spacing: 0.08em; text-transform: uppercase;
      color: #20D99A; font-weight: 600; margin: 0;
    }
    .rm-about-text {
      font-size: 13px; line-height: 1.55; color: #cbd5e1; margin: 0;
    }
    .rm-two-col {
      display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
    }
    .rm-box {
      background: rgba(255, 255, 255, 0.025);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 14px; padding: 12px 14px;
      display: flex; flex-direction: column; gap: 6px;
      box-sizing: border-box; text-align: left;
    }
    .rm-box-heading {
      font-size: 13.5px; font-weight: 600; color: #F4F7F5;
      display: flex; justify-content: space-between; align-items: baseline;
    }
    .rm-box-meta {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 10.5px; color: #20D99A;
    }
    .rm-bullets {
      margin: 0; padding-left: 16px;
      font-size: 12px; line-height: 1.45; color: #AAB5B0;
    }
    .rm-bullets li {
      margin-bottom: 3px;
    }
    .rm-projects-2x2 {
      display: grid; grid-template-columns: 1fr 1fr; gap: 8px;
    }
    .rm-proj-row {
      background: rgba(255, 255, 255, 0.025);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 12px; padding: 10px 12px;
      display: flex; align-items: center; gap: 10px;
      transition: all 0.18s ease; text-align: left;
    }
    .rm-proj-row:hover {
      background: rgba(255, 255, 255, 0.05);
      border-color: rgba(32, 217, 154, 0.3);
      transform: translateY(-1px);
    }
    .rm-proj-icon {
      width: 32px; height: 32px; border-radius: 8px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      display: flex; align-items: center; justify-content: center;
      padding: 5px; flex-shrink: 0; box-sizing: border-box;
    }
    .rm-proj-icon img {
      width: 100%; height: 100%; object-fit: contain;
    }
    .rm-proj-details {
      display: flex; flex-direction: column; gap: 2px; min-width: 0; flex: 1;
    }
    .rm-proj-title-row {
      display: flex; justify-content: space-between; align-items: baseline;
    }
    .rm-proj-title {
      font-size: 12.5px; font-weight: 600; color: #F4F7F5;
    }
    .rm-proj-tag {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 9.5px; color: #20D99A;
    }
    .rm-proj-desc-one {
      font-size: 11px; color: #AAB5B0; line-height: 1.3;
      white-space: nowrap; overflow: hidden; text-overflow: ellipsis; margin: 0;
    }
    .rm-skills-grid {
      display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px;
    }
    .rm-skill-col {
      display: flex; flex-direction: column; gap: 4px; text-align: left;
    }
    .rm-skill-col-title {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 9.5px; font-weight: 600; color: #788782; text-transform: uppercase;
    }
    .rm-skill-pills {
      display: flex; flex-wrap: wrap; gap: 4px;
    }
    .rm-pill {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 5px; padding: 2px 7px;
      font-size: 11px; font-weight: 500; color: #e2e8f0;
      transition: all 0.15s ease;
    }
    .rm-pill:hover {
      background: rgba(32, 217, 154, 0.12);
      border-color: rgba(32, 217, 154, 0.35);
      color: #20D99A;
    }
    .rm-statement-line {
      text-align: center; font-size: 12px; font-weight: 600;
      color: #cbd5e1; letter-spacing: 0.04em;
      padding: 6px 12px; border-radius: 8px;
      background: rgba(32, 217, 154, 0.04);
      border: 1px solid rgba(32, 217, 154, 0.14);
    }
    .rm-statement-arrow {
      color: #20D99A; font-weight: 700; margin: 0 4px;
    }
    .rm-bottom-bar {
      display: flex; align-items: center; justify-content: space-between;
      gap: 12px; margin-top: 2px;
    }
    .rm-btn-group {
      display: flex; gap: 10px; flex: 1;
    }
    .rm-action-button {
      flex: 1; height: 38px; border-radius: 10px;
      font-family: inherit; font-size: 13px; font-weight: 600;
      display: inline-flex; align-items: center; justify-content: center;
      gap: 6px; cursor: pointer; transition: all 0.16s ease;
      text-decoration: none; box-sizing: border-box; outline: none;
    }
    .rm-btn-primary {
      background: linear-gradient(135deg, #20D99A 0%, #10a874 100%);
      color: #061510; border: none;
      box-shadow: 0 4px 12px rgba(32, 217, 154, 0.28);
    }
    .rm-btn-primary:hover {
      filter: brightness(1.1);
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(32, 217, 154, 0.4);
    }
    .rm-btn-primary:active {
      transform: scale(0.98);
    }
    .rm-btn-secondary {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #F4F7F5;
    }
    .rm-btn-secondary:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(32, 217, 154, 0.35);
      color: #20D99A;
      transform: translateY(-1px);
    }
    .rm-btn-secondary:active {
      transform: scale(0.98);
    }
    .rm-social-icons {
      display: flex; gap: 6px; align-items: center;
    }
    .rm-social-icon-btn {
      width: 36px; height: 36px; border-radius: 8px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: #AAB5B0; display: inline-flex; align-items: center; justify-content: center;
      text-decoration: none; transition: all 0.15s ease;
    }
    .rm-social-icon-btn:hover {
      background: rgba(32, 217, 154, 0.12);
      border-color: rgba(32, 217, 154, 0.35);
      color: #20D99A;
      transform: translateY(-1px);
    }
    .rm-social-icon-btn svg {
      width: 15px; height: 15px;
    }
    @media (max-width: 768px) {
      .resume-modal {
        width: calc(100vw - 20px);
        max-height: calc(100vh - 36px);
        border-radius: 20px;
      }
      .resume-modal-inner {
        padding: 20px 18px; gap: 14px;
        max-height: calc(100vh - 38px);
      }
      .rm-header-row {
        flex-direction: column; align-items: flex-start; gap: 12px;
      }
      .rm-photo-frame {
        width: 80px; height: 80px;
      }
      .rm-main-name {
        font-size: 22px;
      }
      .rm-two-col, .rm-projects-2x2, .rm-skills-grid {
        grid-template-columns: 1fr;
      }
      .rm-bottom-bar {
        flex-direction: column; align-items: stretch;
      }
      .rm-btn-group {
        flex-direction: column;
      }
      .rm-social-icons {
        justify-content: center;
      }
    }
  `;
  document.head.appendChild(e);
}

function createResumeModal() {
  injectResumeModalStyles();
  let backdrop = document.createElement("div");
  backdrop.className = "resume-backdrop";
  document.body.appendChild(backdrop);

  let modal = document.createElement("div");
  modal.className = "resume-modal";
  modal._backdrop = backdrop;
  modal.innerHTML = `
    <button class="rm-close-btn" type="button" aria-label="Close profile">
      <svg width="13" height="13" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M1 1L13 13M1 13L13 1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
      </svg>
    </button>
    <div class="resume-modal-inner">
      <!-- HEADER -->
      <div class="rm-header-row">
        <div class="rm-photo-frame">
          <img class="rm-photo-img" src="/assets/brand/harshit.png" alt="Harshit Yadav" onerror="this.src='/assets/brand/favicon.svg'" />
        </div>
        <div class="rm-header-content">
          <div class="rm-badge-row">
            <span class="rm-badge-pill">B.TECH CSE STUDENT</span>
            <span class="rm-badge-pill">FULL-STACK & AI DEVELOPER</span>
          </div>
          <h1 class="rm-main-name">HARSHIT YADAV</h1>
          <div class="rm-role-sub">B.Tech CSE Student · Full-Stack Developer</div>
          <div class="rm-univ-sub">BML Munjal University (BMU)</div>
          <div class="rm-quick-nav">
            <a class="rm-nav-btn" href="https://why.zero.university/" target="_blank">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
              <span>Portfolio</span>
            </a>
            <a class="rm-nav-btn" href="https://github.com/harshityadav" target="_blank">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
              <span>GitHub</span>
            </a>
            <a class="rm-nav-btn" href="https://linkedin.com/in/harshityadav" target="_blank">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
              <span>LinkedIn</span>
            </a>
            <a class="rm-nav-btn" href="mailto:harshit@zero.university">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              <span>Email</span>
            </a>
          </div>
        </div>
      </div>

      <div class="rm-hr"></div>

      <!-- ABOUT ME -->
      <div style="display:flex; flex-direction:column; gap:4px; text-align:left;">
        <div class="rm-sec-title">ABOUT ME</div>
        <p class="rm-about-text">
          Computer Science & Engineering student and full-stack developer who builds real-world web applications, interactive experiences, and AI-assisted products. I enjoy taking ideas from concept to deployment and combining modern development tools with creative UI/UX.
        </p>
      </div>

      <!-- EXPERIENCE + EDUCATION -->
      <div class="rm-two-col">
        <div class="rm-box">
          <div class="rm-sec-title">EXPERIENCE</div>
          <div class="rm-box-heading">
            <span>Freelance Full-Stack Developer</span>
            <span class="rm-box-meta">2025 – Present</span>
          </div>
          <ul class="rm-bullets">
            <li>Build web applications and SaaS products for real-world use cases.</li>
            <li>Develop frontend, backend, databases, APIs, authentication, and deployments.</li>
            <li>Use modern AI-assisted development workflows to accelerate product development.</li>
          </ul>
        </div>

        <div class="rm-box">
          <div class="rm-sec-title">EDUCATION</div>
          <div class="rm-box-heading">
            <span>B.Tech — Computer Science & Engineering</span>
            <span class="rm-box-meta">Current</span>
          </div>
          <div style="font-size:12.5px; color:#cbd5e1; font-weight:500; margin-top:2px;">BML Munjal University (BMU)</div>
          <p style="font-size:11.5px; color:#AAB5B0; line-height:1.45; margin:4px 0 0 0;">
            Specializing in full-stack web architectures, distributed software design, and applied AI systems.
          </p>
        </div>
      </div>

      <!-- SELECTED WORK -->
      <div style="display:flex; flex-direction:column; gap:6px; text-align:left;">
        <div class="rm-sec-title">SELECTED WORK</div>
        <div class="rm-projects-2x2">
          <div class="rm-proj-row">
            <div class="rm-proj-icon">
              <img src="/assets/brand/favicon.svg" alt="" />
            </div>
            <div class="rm-proj-details">
              <div class="rm-proj-title-row">
                <span class="rm-proj-title">Why Zero University</span>
                <span class="rm-proj-tag">3D WEB · WebGL</span>
              </div>
              <p class="rm-proj-desc-one">Interactive 3D onboarding experience & candidate discovery portal.</p>
            </div>
          </div>

          <div class="rm-proj-row">
            <div class="rm-proj-icon">
              <img src="/assets/logos/companies/gym.svg" alt="" onerror="this.src='/assets/brand/favicon.svg'" />
            </div>
            <div class="rm-proj-details">
              <div class="rm-proj-title-row">
                <span class="rm-proj-title">Gym Management System</span>
                <span class="rm-proj-tag">FULL-STACK SAAS</span>
              </div>
              <p class="rm-proj-desc-one">Centralized SaaS membership, check-in, and billing platform.</p>
            </div>
          </div>

          <div class="rm-proj-row">
            <div class="rm-proj-icon">
              <img src="/assets/logos/companies/examora.svg" alt="" onerror="this.src='/assets/brand/favicon.svg'" />
            </div>
            <div class="rm-proj-details">
              <div class="rm-proj-title-row">
                <span class="rm-proj-title">Examora</span>
                <span class="rm-proj-tag">AI EDTECH</span>
              </div>
              <p class="rm-proj-desc-one">AI study portal with active-recall flashcards & exam simulations.</p>
            </div>
          </div>

          <div class="rm-proj-row">
            <div class="rm-proj-icon">
              <img src="/assets/logos/companies/gestotype.svg" alt="" onerror="this.src='/assets/brand/favicon.svg'" />
            </div>
            <div class="rm-proj-details">
              <div class="rm-proj-title-row">
                <span class="rm-proj-title">GestoType</span>
                <span class="rm-proj-tag">HARDWARE / HCI</span>
              </div>
              <p class="rm-proj-desc-one">Wearable ESP32 air-writing gesture recognition & Bluetooth keyboard.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- TECH STACK -->
      <div style="display:flex; flex-direction:column; gap:6px; text-align:left;">
        <div class="rm-sec-title">TECH STACK</div>
        <div class="rm-skills-grid">
          <div class="rm-skill-col">
            <div class="rm-skill-col-title">DEVELOPMENT</div>
            <div class="rm-skill-pills">
              <span class="rm-pill">Python</span>
              <span class="rm-pill">JavaScript</span>
              <span class="rm-pill">TypeScript</span>
              <span class="rm-pill">React</span>
              <span class="rm-pill">Next.js</span>
              <span class="rm-pill">Node.js</span>
            </div>
          </div>

          <div class="rm-skill-col">
            <div class="rm-skill-col-title">DATA & CLOUD</div>
            <div class="rm-skill-pills">
              <span class="rm-pill">PostgreSQL</span>
              <span class="rm-pill">MongoDB</span>
              <span class="rm-pill">SQLite</span>
              <span class="rm-pill">Supabase</span>
              <span class="rm-pill">Vercel</span>
              <span class="rm-pill">Git</span>
            </div>
          </div>

          <div class="rm-skill-col">
            <div class="rm-skill-col-title">CREATIVE / AI</div>
            <div class="rm-skill-pills">
              <span class="rm-pill">Three.js</span>
              <span class="rm-pill">WebGL</span>
              <span class="rm-pill">AI Workflows</span>
              <span class="rm-pill">LLM Integration</span>
              <span class="rm-pill">ESP32</span>
            </div>
          </div>
        </div>
      </div>

      <!-- STATEMENT -->
      <div class="rm-statement-line">
        I BUILD <span class="rm-statement-arrow">→</span> FROM IDEA TO DEPLOYED PRODUCT
      </div>

      <!-- FOOTER ACTIONS -->
      <div class="rm-bottom-bar">
        <div class="rm-btn-group">
          <a class="rm-action-button rm-btn-primary" href="https://why.zero.university/" target="_blank">
            <span>Download Resume ↓</span>
          </a>
          <a class="rm-action-button rm-btn-secondary" href="mailto:harshit@zero.university">
            <span>Contact Me →</span>
          </a>
        </div>
        <div class="rm-social-icons">
          <a class="rm-social-icon-btn" href="https://github.com/harshityadav" target="_blank" aria-label="GitHub">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
          </a>
          <a class="rm-social-icon-btn" href="https://linkedin.com/in/harshityadav" target="_blank" aria-label="LinkedIn">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
          </a>
        </div>
      </div>
    </div>
  `;

  let closeBtn = modal.querySelector(".rm-close-btn");
  closeBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    X.play("click");
    closeResumeModal(modal);
  });
  backdrop.addEventListener("click", (e) => {
    e.stopPropagation();
    closeResumeModal(modal);
  });
  let onKeyEsc = (e) => {
    if (e.key === "Escape" && modal._isOpen) closeResumeModal(modal);
  };
  window.addEventListener("keydown", onKeyEsc);
  modal._onKeyEsc = onKeyEsc;
  modal.addEventListener("pointerdown", (e) => e.stopPropagation());
  modal.addEventListener("pointerup", (e) => e.stopPropagation());
  modal.addEventListener("click", (e) => e.stopPropagation());

  document.body.appendChild(modal);
  return modal;
}

var globalResumeModal = null;
function openResumeModal() {
  if (!globalResumeModal) globalResumeModal = createResumeModal();
  X.play("hand-entry");
  globalResumeModal._backdrop.classList.add("is-active");
  globalResumeModal.classList.add("is-open");
  globalResumeModal._isOpen = !0;
}
function closeResumeModal(modal) {
  let m = modal || globalResumeModal;
  if (!m) return;
  m._backdrop.classList.remove("is-active");
  m.classList.remove("is-open");
  m._isOpen = !1;
}
window.openResumeModal = openResumeModal;
window.closeResumeModal = closeResumeModal;
window.addEventListener("zero:openResume", openResumeModal);
'''

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        start_marker = "var resumeModalStylesInjected = !1;"
        end_marker = "function CD(){"

        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker, start_idx)

        if start_idx != -1 and end_idx != -1:
            content = content[:start_idx] + new_resume_code + "\n\n" + content[end_idx:]
            print("Successfully replaced resume modal in", filepath)
        else:
            print("Could not find markers in", filepath, start_idx, end_idx)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    print("Finished updating resume modal.")

update_resume_modal()
