import re

def update_resume_modal():
    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    resume_code = r'''
var resumeModalStylesInjected = !1;
function injectResumeModalStyles() {
  if (resumeModalStylesInjected) return;
  resumeModalStylesInjected = !0;
  let e = document.createElement("style");
  e.dataset.resumeModal = "1";
  e.textContent = `
    .resume-backdrop {
      position: fixed; inset: 0; z-index: 105;
      background: rgba(8, 14, 11, 0.65);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      opacity: 0; pointer-events: none;
      transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .resume-backdrop.is-active {
      opacity: 1; pointer-events: auto;
    }
    .resume-modal {
      position: fixed; left: 50%; top: 50%;
      width: min(840px, calc(100vw - 32px));
      max-height: min(88vh, 880px);
      box-sizing: border-box;
      color: #F5F7F6;
      background: rgba(17, 20, 18, 0.88);
      background-image: radial-gradient(circle at 50% 0%, rgba(124, 255, 178, 0.12) 0%, transparent 70%);
      backdrop-filter: blur(30px) saturate(140%);
      -webkit-backdrop-filter: blur(30px) saturate(140%);
      border: 1px solid rgba(124, 255, 178, 0.2);
      border-radius: 28px;
      box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.06), 0 28px 70px -15px rgba(0, 0, 0, 0.85), 0 0 50px -10px rgba(124, 255, 178, 0.22);
      opacity: 0; pointer-events: none;
      transform: translate(-50%, calc(-50% + 22px)) scale(0.96);
      transform-origin: center;
      transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1), transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
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
      padding: 28px 30px 24px 30px;
      overflow-y: auto;
      overflow-x: hidden;
      display: flex; flex-direction: column; gap: 20px;
      box-sizing: border-box;
      max-height: calc(min(88vh, 880px) - 2px);
    }
    .resume-modal-inner::-webkit-scrollbar {
      width: 5px;
    }
    .resume-modal-inner::-webkit-scrollbar-track {
      background: transparent;
    }
    .resume-modal-inner::-webkit-scrollbar-thumb {
      background: rgba(124, 255, 178, 0.2);
      border-radius: 10px;
    }
    .resume-modal-inner::-webkit-scrollbar-thumb:hover {
      background: rgba(124, 255, 178, 0.4);
    }
    .rm-close-btn {
      position: absolute; top: 20px; right: 20px;
      width: 36px; height: 36px; border-radius: 50%;
      background: rgba(255, 255, 255, 0.07);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: rgba(255, 255, 255, 0.7);
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: all 0.18s ease;
      z-index: 10; padding: 0; outline: none;
    }
    .rm-close-btn:hover {
      background: rgba(124, 255, 178, 0.15);
      border-color: rgba(124, 255, 178, 0.35);
      color: #7CFFB2;
      transform: scale(1.08);
    }
    .rm-close-btn:active {
      transform: scale(0.94);
    }
    .rm-header {
      display: flex; align-items: center; gap: 22px;
      padding-right: 40px;
    }
    .rm-photo-wrap {
      position: relative; width: 88px; height: 88px; flex-shrink: 0;
      border-radius: 50%;
      padding: 3px;
      background: linear-gradient(135deg, #7CFFB2 0%, rgba(124, 255, 178, 0.2) 100%);
      box-shadow: 0 0 24px rgba(124, 255, 178, 0.3);
    }
    .rm-photo {
      width: 100%; height: 100%; object-fit: cover; border-radius: 50%;
      display: block; background: #161a18;
    }
    .rm-header-info {
      display: flex; flex-direction: column; gap: 4px; min-width: 0;
    }
    .rm-tag-row {
      display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin-bottom: 2px;
    }
    .rm-badge {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase;
      color: #7CFFB2; font-weight: 600;
      background: rgba(124, 255, 178, 0.1);
      border: 1px solid rgba(124, 255, 178, 0.25);
      padding: 2px 9px; border-radius: 20px;
    }
    .rm-name {
      font-size: 28px; font-weight: 700; color: #F5F7F6;
      letter-spacing: -0.025em; line-height: 1.15; margin: 0;
    }
    .rm-subtitle {
      font-size: 14px; color: #AAB4B0; font-weight: 400; line-height: 1.4;
    }
    .rm-quick-links {
      display: flex; flex-wrap: wrap; gap: 8px; margin-top: 4px;
    }
    .rm-link-chip {
      height: 28px; border-radius: 8px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      display: inline-flex; align-items: center; gap: 6px;
      padding: 0 10px; font-size: 12px; font-weight: 500;
      color: #e2e8f0; text-decoration: none; cursor: pointer;
      transition: all 0.15s ease;
    }
    .rm-link-chip:hover {
      background: rgba(124, 255, 178, 0.12);
      border-color: rgba(124, 255, 178, 0.35);
      color: #7CFFB2;
      transform: translateY(-1px);
    }
    .rm-link-chip svg {
      width: 13px; height: 13px; opacity: 0.85;
    }
    .rm-card {
      background: rgba(255, 255, 255, 0.028);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 18px; padding: 16px 18px;
      display: flex; flex-direction: column; gap: 8px;
      text-align: left; box-sizing: border-box;
    }
    .rm-card-highlight {
      background: linear-gradient(135deg, rgba(124, 255, 178, 0.06) 0%, rgba(255, 255, 255, 0.02) 100%);
      border-color: rgba(124, 255, 178, 0.2);
    }
    .rm-section-label {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase;
      color: #7CFFB2; font-weight: 600;
      display: flex; align-items: center; gap: 6px; margin: 0;
    }
    .rm-section-label svg {
      width: 13px; height: 13px;
    }
    .rm-body-text {
      font-size: 13.5px; line-height: 1.55; color: #cbd5e1; margin: 0;
    }
    .rm-grid-2 {
      display: grid; grid-template-columns: 1fr 1fr; gap: 14px;
    }
    .rm-exp-item {
      display: flex; flex-direction: column; gap: 4px;
    }
    .rm-item-title {
      font-size: 14.5px; font-weight: 600; color: #F5F7F6;
    }
    .rm-item-meta {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 11px; color: #7CFFB2;
    }
    .rm-bullet-list {
      margin: 4px 0 0 0; padding-left: 18px;
      font-size: 12.5px; line-height: 1.5; color: #AAB4B0;
    }
    .rm-bullet-list li {
      margin-bottom: 3px;
    }
    .rm-projects-grid {
      display: grid; grid-template-columns: 1fr 1fr; gap: 10px;
    }
    .rm-proj-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 14px; padding: 12px 14px;
      display: flex; flex-direction: column; gap: 4px;
      transition: all 0.2s ease;
    }
    .rm-proj-card:hover {
      background: rgba(255, 255, 255, 0.05);
      border-color: rgba(124, 255, 178, 0.3);
      transform: translateY(-1px);
    }
    .rm-proj-head {
      display: flex; justify-content: space-between; align-items: baseline;
    }
    .rm-proj-name {
      font-size: 13.5px; font-weight: 600; color: #F5F7F6;
    }
    .rm-proj-cat {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 10px; color: #7CFFB2; text-transform: uppercase;
    }
    .rm-proj-desc {
      font-size: 12px; color: #AAB4B0; line-height: 1.4; margin: 0;
    }
    .rm-proj-focus {
      font-size: 11px; color: #94a3b8; font-style: italic; margin-top: 2px;
    }
    .rm-skills-container {
      display: flex; flex-direction: column; gap: 10px;
    }
    .rm-skill-group {
      display: flex; flex-direction: column; gap: 4px;
    }
    .rm-skill-title {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 11px; font-weight: 600; color: #94a3b8; text-transform: uppercase;
    }
    .rm-chips-row {
      display: flex; flex-wrap: wrap; gap: 6px;
    }
    .rm-skill-chip {
      background: rgba(255, 255, 255, 0.045);
      border: 1px solid rgba(255, 255, 255, 0.09);
      border-radius: 7px; padding: 3px 9px;
      font-size: 12px; font-weight: 500; color: #e2e8f0;
      transition: all 0.15s ease;
    }
    .rm-skill-chip:hover {
      background: rgba(124, 255, 178, 0.12);
      border-color: rgba(124, 255, 178, 0.35);
      color: #7CFFB2;
    }
    .rm-focus-card {
      background: linear-gradient(135deg, rgba(124, 255, 178, 0.1) 0%, rgba(124, 255, 178, 0.02) 100%);
      border: 1px solid rgba(124, 255, 178, 0.28);
      border-radius: 16px; padding: 14px 18px;
      display: flex; align-items: center; gap: 12px;
    }
    .rm-focus-dot {
      width: 10px; height: 10px; border-radius: 50%;
      background: #7CFFB2; box-shadow: 0 0 10px #7CFFB2;
      flex-shrink: 0;
    }
    .rm-focus-text {
      font-size: 13.5px; font-weight: 500; color: #F5F7F6; line-height: 1.45;
    }
    .rm-footer-actions {
      display: flex; gap: 10px; margin-top: 4px;
    }
    .rm-action-btn {
      flex: 1; height: 42px; border-radius: 12px;
      font-family: inherit; font-size: 13.5px; font-weight: 600;
      display: inline-flex; align-items: center; justify-content: center;
      gap: 7px; cursor: pointer; transition: all 0.18s ease;
      text-decoration: none; box-sizing: border-box; outline: none;
    }
    .rm-btn-primary {
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: #ffffff; border: none;
      box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35), inset 0 1px 1px rgba(255,255,255,0.25);
    }
    .rm-btn-primary:hover {
      filter: brightness(1.12);
      transform: translateY(-1px);
      box-shadow: 0 6px 20px rgba(16, 185, 129, 0.48);
    }
    .rm-btn-secondary {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: #ffffff;
    }
    .rm-btn-secondary:hover {
      background: rgba(255, 255, 255, 0.12);
      border-color: rgba(124, 255, 178, 0.35);
      color: #7CFFB2;
      transform: translateY(-1px);
    }
    @media (max-width: 768px) {
      .resume-modal {
        width: calc(100vw - 20px);
        max-height: calc(100vh - 36px);
        border-radius: 22px;
      }
      .resume-modal-inner {
        padding: 20px 16px; gap: 16px;
        max-height: calc(100vh - 38px);
      }
      .rm-header {
        flex-direction: column; align-items: flex-start; gap: 14px;
      }
      .rm-photo-wrap {
        width: 72px; height: 72px;
      }
      .rm-name {
        font-size: 22px;
      }
      .rm-grid-2, .rm-projects-grid {
        grid-template-columns: 1fr;
      }
      .rm-footer-actions {
        flex-direction: column;
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
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M1 1L13 13M1 13L13 1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
      </svg>
    </button>
    <div class="resume-modal-inner">
      <div class="rm-header">
        <div class="rm-photo-wrap">
          <img class="rm-photo" src="/assets/brand/harshit.png" alt="Harshit Yadav" onerror="this.src='/assets/brand/favicon.svg'" />
        </div>
        <div class="rm-header-info">
          <div class="rm-tag-row">
            <span class="rm-badge">B.Tech CSE Student</span>
            <span class="rm-badge">Full-Stack & AI Developer</span>
          </div>
          <h1 class="rm-name">HARSHIT YADAV</h1>
          <div class="rm-subtitle">Computer Science & Engineering · BML Munjal University (BMU)</div>
          <div class="rm-quick-links">
            <a class="rm-link-chip" href="https://why.zero.university/" target="_blank">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
              <span>why.zero.university</span>
            </a>
            <a class="rm-link-chip" href="https://github.com/harshityadav" target="_blank">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
              <span>GitHub</span>
            </a>
            <a class="rm-link-chip" href="https://linkedin.com/in/harshityadav" target="_blank">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
              <span>LinkedIn</span>
            </a>
            <a class="rm-link-chip" href="mailto:harshit@zero.university">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
              <span>Contact Email</span>
            </a>
          </div>
        </div>
      </div>

      <div class="rm-card rm-card-highlight">
        <div class="rm-section-label">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
          PROFILE OVERVIEW
        </div>
        <p class="rm-body-text">
          Computer Science & Engineering student and full-stack developer with hands-on experience building websites, web applications, dashboards, and interactive digital experiences. Experienced in developing projects from concept to deployment, with a strong interest in AI-assisted development, modern web technologies, and creative UI/UX. I enjoy turning ideas into functional products and experimenting with emerging development tools to build polished, real-world applications.
        </p>
      </div>

      <div class="rm-grid-2">
        <div class="rm-card">
          <div class="rm-section-label">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
            EXPERIENCE
          </div>
          <div class="rm-exp-item">
            <div class="rm-item-title">Freelance Full-Stack Developer</div>
            <div class="rm-item-meta">2025 – Present</div>
            <ul class="rm-bullet-list">
              <li>Build and develop web apps & SaaS products for real-world use cases.</li>
              <li>Engineer frontend, backend, databases, authentication, APIs, and cloud deployments.</li>
              <li>Develop responsive, interactive user interfaces with modern WebGL and React stacks.</li>
              <li>Leverage AI workflows to accelerate end-to-end product delivery.</li>
            </ul>
          </div>
        </div>

        <div class="rm-card">
          <div class="rm-section-label">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
            EDUCATION
          </div>
          <div class="rm-exp-item">
            <div class="rm-item-title">B.Tech — Computer Science & Engineering</div>
            <div class="rm-item-meta">BML Munjal University (BMU)</div>
            <p class="rm-body-text" style="font-size:12.5px; color:#AAB4B0; margin-top:6px;">
              Core coursework in Data Structures & Algorithms, Operating Systems, Database Management Systems, Computer Networks, and Object-Oriented Software Engineering.
            </p>
          </div>
        </div>
      </div>

      <div class="rm-card">
        <div class="rm-section-label">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          SELECTED PROJECTS
        </div>
        <div class="rm-projects-grid">
          <div class="rm-proj-card">
            <div class="rm-proj-head">
              <span class="rm-proj-name">Why Zero University</span>
              <span class="rm-proj-cat">3D WEB & PLATFORM</span>
            </div>
            <p class="rm-proj-desc">Interactive 3D web platform featuring procedural WebGL shaders, camera physics, and an immersive onboarding experience.</p>
            <div class="rm-proj-focus">Focus: Web Development · UI/UX · WebGL Experience</div>
          </div>

          <div class="rm-proj-card">
            <div class="rm-proj-head">
              <span class="rm-proj-name">Gym Management System</span>
              <span class="rm-proj-cat">FULL-STACK SAAS</span>
            </div>
            <p class="rm-proj-desc">Centralized platform for gym owners to manage memberships, recurring subscriptions, check-ins, and financial dashboards.</p>
            <div class="rm-proj-focus">Stack: Next.js · Node.js · Express · PostgreSQL · Auth</div>
          </div>

          <div class="rm-proj-card">
            <div class="rm-proj-head">
              <span class="rm-proj-name">Examora</span>
              <span class="rm-proj-cat">AI ACADEMIC PLATFORM</span>
            </div>
            <p class="rm-proj-desc">Academic portal designed to simplify study materials, syllabus digestion, and personalized mock exam simulations using LLMs.</p>
            <div class="rm-proj-focus">Focus: AI Digestion · Next.js · Automation · EdTech</div>
          </div>

          <div class="rm-proj-card">
            <div class="rm-proj-head">
              <span class="rm-proj-name">GestoType</span>
              <span class="rm-proj-cat">AI / HARDWARE HCI</span>
            </div>
            <p class="rm-proj-desc">Wearable air-writing interaction system using ESP32, MPU6050 motion sensing, and BLE HID to translate hand gestures to keystrokes.</p>
            <div class="rm-proj-focus">Hardware: ESP32 · MPU6050 · Bluetooth HID · HCI</div>
          </div>

          <div class="rm-proj-card" style="grid-column: 1 / -1;">
            <div class="rm-proj-head">
              <span class="rm-proj-name">Jarvis 3D</span>
              <span class="rm-proj-cat">CREATIVE 3D WEB</span>
            </div>
            <p class="rm-proj-desc">Experimental 3D interactive web environment combining visual shaders, spatial audio, and gesture-driven UI controls.</p>
            <div class="rm-proj-focus">Focus: Three.js · Shaders · Interactive UI · Creative Engineering</div>
          </div>
        </div>
      </div>

      <div class="rm-card">
        <div class="rm-section-label">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          TECHNICAL SKILLS
        </div>
        <div class="rm-skills-container">
          <div class="rm-skill-group">
            <div class="rm-skill-title">Languages</div>
            <div class="rm-chips-row">
              <span class="rm-skill-chip">Python</span>
              <span class="rm-skill-chip">Java</span>
              <span class="rm-skill-chip">C</span>
              <span class="rm-skill-chip">JavaScript</span>
              <span class="rm-skill-chip">TypeScript</span>
              <span class="rm-skill-chip">HTML5 / CSS3</span>
            </div>
          </div>

          <div class="rm-skill-group">
            <div class="rm-skill-title">Web Development & Backend</div>
            <div class="rm-chips-row">
              <span class="rm-skill-chip">React</span>
              <span class="rm-skill-chip">Next.js</span>
              <span class="rm-skill-chip">Node.js</span>
              <span class="rm-skill-chip">Express.js</span>
              <span class="rm-skill-chip">Three.js / WebGL</span>
              <span class="rm-skill-chip">REST APIs</span>
            </div>
          </div>

          <div class="rm-skill-group">
            <div class="rm-skill-title">Databases & Cloud Platforms</div>
            <div class="rm-chips-row">
              <span class="rm-skill-chip">PostgreSQL</span>
              <span class="rm-skill-chip">MongoDB</span>
              <span class="rm-skill-chip">SQLite</span>
              <span class="rm-skill-chip">Supabase</span>
              <span class="rm-skill-chip">Vercel</span>
              <span class="rm-skill-chip">Render</span>
              <span class="rm-skill-chip">Git / GitHub</span>
            </div>
          </div>

          <div class="rm-skill-group">
            <div class="rm-skill-title">Specializations & Emerging Tech</div>
            <div class="rm-chips-row">
              <span class="rm-skill-chip">AI-assisted Workflows</span>
              <span class="rm-skill-chip">LLM Integration</span>
              <span class="rm-skill-chip">Creative UI/UX</span>
              <span class="rm-skill-chip">Embedded Systems (ESP32)</span>
              <span class="rm-skill-chip">Human-Computer Interaction</span>
            </div>
          </div>
        </div>
      </div>

      <div class="rm-focus-card">
        <div class="rm-focus-dot"></div>
        <div class="rm-focus-text">
          <strong>Current Focus:</strong> Building real-world products with modern web technologies, AI-assisted development, and creative interactive experiences.
        </div>
      </div>

      <div class="rm-footer-actions">
        <button class="rm-action-btn rm-btn-primary" type="button" onclick="window.open('https://why.zero.university/','_blank')">
          <span>Explore Projects in 3D City</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </button>
        <button class="rm-action-btn rm-btn-secondary" type="button" onclick="navigator.clipboard.writeText('harshit@zero.university'); alert('Copied email: harshit@zero.university');">
          <span>Copy Contact Email</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
        </button>
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
'''

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Check if already injected
        if "function createResumeModal" not in content:
            # Place it before function CD()
            content = content.replace("function CD(){", resume_code + "\nfunction CD(){", 1)
            print("Injected createResumeModal in", filepath)

        # Wire up ring click in stage5: replace $D(e) click handler
        old_ring_click = r'}else if($D(e)){if(!e._waitlistOpen&&e._waitlistFlow&&e._waitlistFlow.openEmail){X.play(`click`),e._waitlistFlow.openEmail();let t=e.components.ringHit;t&&(e._mapPanTarget.x=t.position.x,e._mapPanTarget.y=t.position.y,e._mapVelocity.x=0,e._mapVelocity.y=0)}}'
        new_ring_click = r'}else if($D(e)){X.play(`click`),openResumeModal();let t=e.components.ringHit;t&&(e._mapPanTarget.x=t.position.x,e._mapPanTarget.y=t.position.y,e._mapVelocity.x=0,e._mapVelocity.y=0)}'

        if old_ring_click in content:
            content = content.replace(old_ring_click, new_ring_click, 1)
            print("Wired up $D(e) ring click in", filepath)
        else:
            print("Note: old_ring_click not found verbatim in", filepath)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    print("Finished updating resume modal.")

update_resume_modal()
