import sys

def update_resume_page():
    modal_css = """
    .resume-backdrop {
      position: fixed; inset: 0; z-index: 105;
      background: rgba(6, 10, 8, 0.65);
      opacity: 0; pointer-events: none;
      transition: opacity 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .resume-backdrop.is-active {
      opacity: 1; pointer-events: auto;
    }
    .resume-modal {
      position: fixed; top: 50%; left: 50%;
      transform: translate(-50%, -50%) scale(0.96);
      z-index: 106;
      width: min(1040px, calc(100vw - 32px));
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
    .resume-modal::-webkit-scrollbar {
      width: 5px;
    }
    .resume-modal::-webkit-scrollbar-thumb {
      background: rgba(34, 197, 94, 0.3);
      border-radius: 4px;
    }
    .resume-modal.is-open {
      opacity: 1; pointer-events: auto;
      transform: translate(-50%, -50%) scale(1);
    }
    .rm-close-btn {
      position: absolute; top: 20px; right: 20px; z-index: 10;
      width: 36px; height: 36px; border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #AAB4B0; display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: all 0.2s ease;
    }
    .rm-close-btn:hover {
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
      transform: scale(1.05);
    }
    .resume-modal-inner {
      padding: 28px 32px;
      display: flex; flex-direction: column; gap: 14px;
    }

    /* HEADER */
    .rm-header-row {
      display: flex; align-items: center; gap: 24px;
      padding-right: 48px;
    }
    .rm-photo-frame {
      width: 105px; height: 105px; border-radius: 50%;
      flex-shrink: 0; position: relative;
      border: 2.5px solid #22c55e;
      box-shadow: 0 0 20px rgba(34, 197, 94, 0.35);
      background: #08100c;
      overflow: hidden;
    }
    .rm-photo-img {
      width: 100%; height: 100%; object-fit: cover; object-position: center top;
      display: block;
    }
    .rm-header-content {
      flex: 1; min-width: 0;
    }
    .rm-badge-row {
      display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 6px;
    }
    .rm-badge-pill {
      font-size: 11px; font-weight: 700; letter-spacing: 0.08em;
      text-transform: uppercase;
      padding: 3.5px 12px; border-radius: 999px;
      color: #4ade80;
      background: rgba(34, 197, 94, 0.09);
      border: 1px solid rgba(34, 197, 94, 0.35);
    }
    .rm-main-name {
      margin: 0; font-size: 32px; font-weight: 800; letter-spacing: -0.02em;
      color: #ffffff; line-height: 1.15;
    }
    .rm-role-sub {
      font-size: 14.5px; font-weight: 500; color: #d1d5db;
      margin-top: 3px;
    }
    .rm-univ-sub {
      font-size: 13.5px; font-weight: 400; color: #9ca3af;
      margin-top: 2px;
    }
    .rm-quick-nav {
      display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;
    }
    .rm-nav-btn {
      display: inline-flex; align-items: center; gap: 7px;
      padding: 5.5px 13px; border-radius: 999px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #e5e7eb; font-size: 12.5px; font-weight: 500;
      text-decoration: none; transition: all 0.2s ease;
    }
    .rm-nav-btn:hover {
      background: rgba(34, 197, 94, 0.12);
      border-color: rgba(34, 197, 94, 0.45);
      color: #4ade80;
      transform: translateY(-1px);
    }
    .rm-nav-btn svg {
      width: 14px; height: 14px; flex-shrink: 0;
    }

    /* ROW 1: ABOUT, EXPERIENCE, EDUCATION */
    .rm-row-1 {
      display: grid;
      grid-template-columns: 1.15fr 1.25fr 0.95fr;
      gap: 14px;
    }
    .rm-card {
      background: rgba(20, 26, 22, 0.55);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 16px;
      padding: 16px 18px;
      display: flex; flex-direction: column;
    }
    .rm-card-header {
      color: #4ade80; font-size: 12px; font-weight: 700; letter-spacing: 0.06em;
      display: flex; align-items: center; gap: 7px;
      text-transform: uppercase;
    }
    .rm-card-header svg {
      width: 14px; height: 14px; flex-shrink: 0;
    }
    .rm-about-text {
      margin: 10px 0 0 0; font-size: 12.5px; line-height: 1.55; color: #9ca3af;
    }
    .rm-exp-title {
      font-size: 13.5px; font-weight: 700; color: #ffffff; margin-top: 10px;
    }
    .rm-exp-meta {
      font-size: 12px; font-weight: 600; color: #4ade80; margin-top: 2px;
    }
    .rm-exp-bullets {
      margin: 6px 0 0 0; padding-left: 14px;
      display: flex; flex-direction: column; gap: 4px;
    }
    .rm-exp-bullets li {
      font-size: 12px; line-height: 1.42; color: #9ca3af;
    }
    .rm-exp-bullets li::marker {
      color: #4ade80;
    }
    .rm-edu-title {
      font-size: 13.5px; font-weight: 700; color: #ffffff; margin-top: 10px; line-height: 1.35;
    }
    .rm-edu-univ {
      font-size: 12px; font-weight: 600; color: #4ade80; margin-top: 6px;
    }
    .rm-edu-status {
      font-size: 12px; font-weight: 600; color: #4ade80; margin-top: 2px;
    }

    /* ROW 2: SELECTED WORK */
    .rm-selected-work-box {
      background: rgba(20, 26, 22, 0.4);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 18px;
      padding: 14px 18px;
    }
    .rm-projects-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-top: 10px;
    }
    .rm-project-card {
      background: rgba(26, 34, 29, 0.55);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 14px;
      padding: 12px;
      display: flex; flex-direction: column; justify-content: space-between;
      transition: all 0.2s ease;
      text-decoration: none;
      color: inherit;
    }
    .rm-project-card:hover {
      background: rgba(32, 42, 36, 0.75);
      border-color: rgba(34, 197, 94, 0.3);
      transform: translateY(-2px);
    }
    .rm-pcard-top {
      display: flex; align-items: flex-start; gap: 10px;
    }
    .rm-pcard-icon {
      width: 34px; height: 34px; border-radius: 50%; flex-shrink: 0;
      display: flex; align-items: center; justify-content: center;
    }
    .rm-pcard-icon.whyzero {
      background: #163828; color: #4ade80;
    }
    .rm-pcard-icon.gym {
      background: #11221b; color: #4ade80;
    }
    .rm-pcard-icon.examora {
      background: #162438; color: #60a5fa;
    }
    .rm-pcard-icon.gesto {
      background: #262928; color: #ffffff;
    }
    .rm-pcard-info {
      flex: 1; min-width: 0;
    }
    .rm-pcard-title {
      font-size: 12.8px; font-weight: 700; color: #ffffff;
      white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }
    .rm-pcard-tagline {
      font-size: 11px; color: #9ca3af; margin-top: 2px;
      line-height: 1.25;
    }
    .rm-pcard-tech {
      font-size: 10px; color: #6b7280; margin-top: 8px;
      letter-spacing: 0.02em;
    }

    /* ROW 3: TECH STACK & I BUILD */
    .rm-row-3 {
      display: grid;
      grid-template-columns: 2.2fr 1fr;
      gap: 14px;
    }
    .rm-tech-box {
      background: rgba(20, 26, 22, 0.55);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 16px;
      padding: 14px 18px;
    }
    .rm-tech-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 14px;
      margin-top: 8px;
    }
    .rm-tech-col-title {
      font-size: 10px; font-weight: 700; color: #9ca3af;
      letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 6px;
    }
    .rm-tech-pills {
      display: flex; flex-wrap: wrap; gap: 4px;
    }
    .rm-tech-pill {
      font-size: 10.5px; font-weight: 500; color: #d1d5db;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.09);
      padding: 3px 8px; border-radius: 999px;
      white-space: nowrap;
    }
    .rm-ibuild-box {
      background: rgba(20, 26, 22, 0.55);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 16px;
      padding: 16px 18px;
      display: flex; flex-direction: column; justify-content: center;
    }
    .rm-ibuild-header {
      color: #4ade80; font-size: 12px; font-weight: 700; letter-spacing: 0.06em;
      display: flex; align-items: center; gap: 6px; margin-bottom: 6px;
    }
    .rm-ibuild-header svg {
      width: 14px; height: 14px;
    }
    .rm-ibuild-title {
      font-size: 15px; font-weight: 800; color: #ffffff;
      letter-spacing: 0.02em; line-height: 1.3;
    }

    /* FOOTER */
    .rm-footer-row {
      display: flex; align-items: center; justify-content: space-between;
      gap: 14px; margin-top: 2px;
    }
    .rm-footer-left {
      display: flex; align-items: center; gap: 12px;
    }
    .rm-btn-primary {
      display: inline-flex; align-items: center; gap: 8px;
      background: #22c55e; color: #08100c;
      font-size: 13px; font-weight: 700;
      padding: 9px 18px; border-radius: 999px;
      border: none; text-decoration: none; cursor: pointer;
      box-shadow: 0 4px 18px rgba(34, 197, 94, 0.35);
      transition: all 0.2s ease;
    }
    .rm-btn-primary:hover {
      background: #4ade80;
      transform: translateY(-1px);
      box-shadow: 0 6px 24px rgba(34, 197, 94, 0.5);
    }
    .rm-btn-primary svg {
      width: 15px; height: 15px;
    }
    .rm-btn-secondary {
      display: inline-flex; align-items: center; gap: 8px;
      background: rgba(255, 255, 255, 0.04);
      color: #ffffff;
      font-size: 13px; font-weight: 600;
      padding: 9px 16px; border-radius: 999px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      text-decoration: none; cursor: pointer;
      transition: all 0.2s ease;
    }
    .rm-btn-secondary:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.25);
      transform: translateY(-1px);
    }
    .rm-btn-secondary svg {
      width: 14px; height: 14px;
    }
    .rm-footer-socials {
      display: flex; align-items: center; gap: 10px;
    }
    .rm-social-icon-btn {
      width: 36px; height: 36px; border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.09);
      color: #9ca3af; text-decoration: none;
      transition: all 0.2s ease;
    }
    .rm-social-icon-btn:hover {
      background: rgba(34, 197, 94, 0.12);
      border-color: rgba(34, 197, 94, 0.4);
      color: #4ade80;
      transform: translateY(-1px);
    }
    .rm-social-icon-btn svg {
      width: 15px; height: 15px;
    }

    @media (max-width: 900px) {
      .rm-row-1 {
        grid-template-columns: 1fr;
      }
      .rm-projects-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .rm-row-3 {
        grid-template-columns: 1fr;
      }
      .rm-tech-grid {
        grid-template-columns: 1fr;
      }
    }
    @media (max-width: 600px) {
      .resume-modal-inner {
        padding: 18px 14px;
      }
      .rm-header-row {
        flex-direction: column; align-items: flex-start; gap: 12px;
        padding-right: 32px;
      }
      .rm-projects-grid {
        grid-template-columns: 1fr;
      }
      .rm-footer-row {
        flex-direction: column; align-items: stretch;
      }
      .rm-footer-left {
        flex-direction: column;
      }
      .rm-footer-socials {
        justify-content: center; margin-top: 6px;
      }
    }
    """

    modal_html = """
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
            <span class="rm-badge-pill">FULL-STACK &amp; AI DEVELOPER</span>
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
            <a class="rm-nav-btn" href="mailto:harshit.yadav@example.com">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              <span>Email</span>
            </a>
          </div>
        </div>
      </div>

      <!-- ROW 1: ABOUT ME | EXPERIENCE | EDUCATION -->
      <div class="rm-row-1">
        <!-- ABOUT ME -->
        <div class="rm-card">
          <div class="rm-card-header">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            <span>ABOUT ME</span>
          </div>
          <p class="rm-about-text">
            Computer Science &amp; Engineering student and full-stack developer who builds real-world web applications, interactive experiences, and AI-assisted products. I enjoy taking ideas from concept to deployment and combining modern development tools with creative UI/UX.
          </p>
        </div>

        <!-- EXPERIENCE -->
        <div class="rm-card">
          <div class="rm-card-header">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
            <span>EXPERIENCE</span>
          </div>
          <div class="rm-exp-title">Freelance Full-Stack Developer</div>
          <div class="rm-exp-meta">2025 — Present</div>
          <ul class="rm-exp-bullets">
            <li>Build web applications and SaaS products for real-world use cases.</li>
            <li>Develop frontend, backend, databases, APIs, authentication, and deployments.</li>
            <li>Use modern AI-assisted development workflows to accelerate product development.</li>
          </ul>
        </div>

        <!-- EDUCATION -->
        <div class="rm-card">
          <div class="rm-card-header">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
            <span>EDUCATION</span>
          </div>
          <div class="rm-edu-title">B.Tech — Computer Science &amp; Engineering</div>
          <div class="rm-edu-univ">BML Munjal University (BMU)</div>
          <div class="rm-edu-status">Current</div>
        </div>
      </div>

      <!-- ROW 2: SELECTED WORK -->
      <div class="rm-selected-work-box">
        <div class="rm-card-header">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg>
          <span>SELECTED WORK</span>
        </div>
        <div class="rm-projects-grid">
          <!-- PROJECT 1: Why Zero University -->
          <div class="rm-project-card">
            <div class="rm-pcard-top">
              <div class="rm-pcard-icon whyzero">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"></circle><path d="M3.6 9h16.8M3.6 15h16.8M12 3a14.5 14.5 0 0 0 0 18M12 3a14.5 14.5 0 0 1 0 18"></path></svg>
              </div>
              <div class="rm-pcard-info">
                <div class="rm-pcard-title">Why Zero University</div>
                <div class="rm-pcard-tagline">Interactive 3D Web Experience</div>
              </div>
            </div>
            <div class="rm-pcard-tech">Next.js · Three.js · WebGL</div>
          </div>

          <!-- PROJECT 2: Gym Management System -->
          <div class="rm-project-card">
            <div class="rm-pcard-top">
              <div class="rm-pcard-icon gym">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 5v14M18 5v14M2 9v6M22 9v6M6 12h12"></path></svg>
              </div>
              <div class="rm-pcard-info">
                <div class="rm-pcard-title">Gym Management System</div>
                <div class="rm-pcard-tagline">Full-Stack SaaS Application</div>
              </div>
            </div>
            <div class="rm-pcard-tech">Next.js · Node.js · PostgreSQL</div>
          </div>

          <!-- PROJECT 3: Examora -->
          <div class="rm-project-card">
            <div class="rm-pcard-top">
              <div class="rm-pcard-icon examora">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"></rect><path d="M7 8h10M7 12h7M7 16h10"></path></svg>
              </div>
              <div class="rm-pcard-info">
                <div class="rm-pcard-title">Examora</div>
                <div class="rm-pcard-tagline">Academic / AI Platform</div>
              </div>
            </div>
            <div class="rm-pcard-tech">Next.js · AI · Automation</div>
          </div>

          <!-- PROJECT 4: GestoType -->
          <div class="rm-project-card">
            <div class="rm-pcard-top">
              <div class="rm-pcard-icon gesto">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M18 11V6a2 2 0 0 0-4 0v5M14 10V4a2 2 0 0 0-4 0v7M10 10.5V6a2 2 0 0 0-4 0v8a6 6 0 0 0 6 6h2a6 6 0 0 0 6-6v-3a2 2 0 0 0-4 0"></path></svg>
              </div>
              <div class="rm-pcard-info">
                <div class="rm-pcard-title">GestoType</div>
                <div class="rm-pcard-tagline">Hardware + HCI Project</div>
              </div>
            </div>
            <div class="rm-pcard-tech">ESP32 · MPU6050 · BLE HID</div>
          </div>
        </div>
      </div>

      <!-- ROW 3: TECH STACK & I BUILD -->
      <div class="rm-row-3">
        <!-- TECH STACK -->
        <div class="rm-tech-box">
          <div class="rm-card-header">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
            <span>TECH STACK</span>
          </div>
          <div class="rm-tech-grid">
            <div>
              <div class="rm-tech-col-title">DEVELOPMENT</div>
              <div class="rm-tech-pills">
                <span class="rm-tech-pill">Python</span>
                <span class="rm-tech-pill">JavaScript</span>
                <span class="rm-tech-pill">TypeScript</span>
                <span class="rm-tech-pill">React</span>
                <span class="rm-tech-pill">Next.js</span>
                <span class="rm-tech-pill">Node.js</span>
              </div>
            </div>
            <div>
              <div class="rm-tech-col-title">DATA &amp; CLOUD</div>
              <div class="rm-tech-pills">
                <span class="rm-tech-pill">PostgreSQL</span>
                <span class="rm-tech-pill">MongoDB</span>
                <span class="rm-tech-pill">SQLite</span>
                <span class="rm-tech-pill">Supabase</span>
                <span class="rm-tech-pill">Vercel</span>
                <span class="rm-tech-pill">Git</span>
              </div>
            </div>
            <div>
              <div class="rm-tech-col-title">CREATIVE / AI</div>
              <div class="rm-tech-pills">
                <span class="rm-tech-pill">Three.js</span>
                <span class="rm-tech-pill">WebGL</span>
                <span class="rm-tech-pill">AI Workflows</span>
                <span class="rm-tech-pill">LLM Integration</span>
                <span class="rm-tech-pill">ESP32</span>
              </div>
            </div>
          </div>
        </div>

        <!-- I BUILD -->
        <div class="rm-ibuild-box">
          <div class="rm-ibuild-header">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18h6"></path><path d="M10 22h4"></path><path d="M15.09 14c.18-.98.65-1.74 1.41-2.5A4.65 4.65 0 0 0 18 8 6 6 0 0 0 6 8c0 1 .23 2.23 1.5 3.5A4.61 4.61 0 0 1 8.91 14"></path></svg>
            <span>I BUILD →</span>
          </div>
          <div class="rm-ibuild-title">FROM IDEA TO DEPLOYED PRODUCT</div>
        </div>
      </div>

      <!-- FOOTER ACTIONS -->
      <div class="rm-footer-row">
        <div class="rm-footer-left">
          <a class="rm-btn-primary" href="mailto:harshit.yadav@example.com?subject=Resume%20Request">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            <span>Download Resume</span>
          </a>
          <a class="rm-btn-secondary" href="mailto:harshit.yadav@example.com">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
            <span>Contact Me</span>
          </a>
        </div>
        <div class="rm-footer-socials">
          <a class="rm-social-icon-btn" href="https://github.com/harshityadav" target="_blank" aria-label="GitHub">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
          </a>
          <a class="rm-social-icon-btn" href="https://linkedin.com/in/harshityadav" target="_blank" aria-label="LinkedIn">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
          </a>
          <a class="rm-social-icon-btn" href="https://why.zero.university/" target="_blank" aria-label="Portfolio">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
          </a>
        </div>
      </div>
    </div>
    """

    replacement_js = f"""var resumeModalStylesInjected = !1;
function injectResumeModalStyles() {{
  if (resumeModalStylesInjected) return;
  resumeModalStylesInjected = !0;
  let e = document.createElement("style");
  e.dataset.resumeModal = "1";
  e.textContent = `{modal_css}`;
  document.head.appendChild(e);
}}

function createResumeModal() {{
  injectResumeModalStyles();
  let backdrop = document.createElement("div");
  backdrop.className = "resume-backdrop";
  document.body.appendChild(backdrop);

  let modal = document.createElement("div");
  modal.className = "resume-modal";
  modal._backdrop = backdrop;
  modal.innerHTML = `{modal_html}`;

  let closeBtn = modal.querySelector(".rm-close-btn");
  closeBtn.addEventListener("click", (e) => {{
    e.stopPropagation();
    X.play("click");
    closeResumeModal(modal);
  }});
  backdrop.addEventListener("click", (e) => {{
    e.stopPropagation();
    closeResumeModal(modal);
  }});
  let onKeyEsc = (e) => {{
    if (e.key === "Escape" && modal._isOpen) closeResumeModal(modal);
  }};
  window.addEventListener("keydown", onKeyEsc);
  modal._onKeyEsc = onKeyEsc;
  modal.addEventListener("pointerdown", (e) => e.stopPropagation());
  modal.addEventListener("click", (e) => e.stopPropagation());

  document.body.appendChild(modal);
  return modal;
}}

var globalResumeModal = null;
function openResumeModal() {{
  if (!globalResumeModal) globalResumeModal = createResumeModal();
  X.play("hand-entry");
  globalResumeModal._backdrop.classList.add("is-active");
  globalResumeModal.classList.add("is-open");
  globalResumeModal._isOpen = !0;
}}
function closeResumeModal(modal) {{
  let m = modal || globalResumeModal;
  if (!m) return;
  m._backdrop.classList.remove("is-active");
  m.classList.remove("is-open");
  m._isOpen = !1;
}}
window.openResumeModal = openResumeModal;
window.closeResumeModal = closeResumeModal;
window.addEventListener("zero:openResume", openResumeModal);"""

    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            code = f.read()

        start = code.find("var resumeModalStylesInjected")
        if start == -1:
            start = code.find("function injectResumeModalStyles()")
        
        end_marker = 'window.addEventListener("zero:openResume", openResumeModal);'
        end = code.find(end_marker)
        
        if start != -1 and end != -1:
            end_pos = end + len(end_marker)
            new_code = code[:start] + replacement_js + code[end_pos:]
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_code)
            print("Successfully updated resume modal in:", filepath)
        else:
            print("Error: start or end marker not found in:", filepath)

update_resume_page()
