import re

def update_js_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replacement 1: YS, XS, ZS, QS
    old_data_pattern = r'var YS=\{python:`Python`.*?,\$S=`'
    new_data = '''var YS={python:`Python`,jupyter:`Jupyter`,notebook:`Notebook`,pandas:`Pandas`,cursor:`Cursor`,codex:`Codex`,canva:`Canva`,googlesheets:`Google Sheets`,googleslides:`Google Slides`,nextjs:`Next.js`,vercel:`Vercel`,supabase:`Supabase`,gemini:`Gemini`,anthropic:`Claude`,react:`React`,nodejs:`Node.js`,postgresql:`PostgreSQL`,typescript:`TypeScript`,threejs:`Three.js`,webgl:`WebGL`},XS=[{name:`Why Zero University website`,shortTitle:`Why Zero University`,category:`CREATIVE FRONT-END & 3D WEB`,tagline:`Gamified 3D interactive web onboarding experience & candidate discovery platform`,status:`LIVE`,statusType:`live`,logo:`/assets/brand/favicon.svg`,video:``,role:`Creative Front-End Developer`,roleSummary:`Designed and developed procedural WebGL shader pipeline, interactive 3D camera physics rig, custom audio engine, dynamic volumetric cloud shadows, and responsive onboarding flow.`,scenario:`Interactive 3D Web Experience`,description:`An immersive 3D web experience built to revolutionize career onboarding. It combines real-time procedural WebGL rendering, custom camera navigation physics, dynamic lighting, and a gamified waitlist engine to showcase skills through immersive storytelling.`,features:[{title:`Procedural 3D WebGL World`,desc:`Custom GLSL shaders, camera rig, and procedural lighting.`},{title:`Interactive Multi-Stage Journey`,desc:`Seamless scroll-driven stage transitions with state persistence.`},{title:`Dynamic Volumetric Shadows`,desc:`Real-time drifting cloud shadows with GPU texture tiling.`},{title:`Spatial Audio & Sound Design`,desc:`Contextual ambient soundscapes with low-pass audio muffling.`},{title:`Gamified Waitlist Engine`,desc:`Dynamic referral scoring, queue ranking, and user verification.`},{title:`Adaptive Responsive Design`,desc:`Tailored touch joystick & swipe controls for mobile devices.`}],tools:[`nextjs`,`threejs`,`webgl`,`supabase`,`vercel`,`gemini`],url:`https://why.zero.university/`,github:`https://github.com/harshityadav/zero-university-clone`},{name:`Gym Management System`,shortTitle:`Gym Management System`,category:`FULL-STACK SAAS PLATFORM`,tagline:`SaaS membership & facility management platform for modern fitness clubs`,status:`COMPLETED`,statusType:`completed`,logo:`/assets/logos/companies/gym.svg`,video:``,role:`Full-Stack Developer`,roleSummary:`Engineered end-to-end full-stack architecture, PostgreSQL relational schema, JWT authentication, automated subscription billing, and real-time member check-ins.`,scenario:`SaaS Membership Dashboard`,description:`A comprehensive full-stack SaaS platform built for modern fitness centers. Replaces fragmented spreadsheets and manual registers with automated membership renewals, attendance tracking, trainer schedules, and real-time financial reporting.`,features:[{title:`Automated Member Check-Ins`,desc:`Instant QR code & RFID validation with attendance logging.`},{title:`Subscription & Recurring Billing`,desc:`Automated invoice generation, payment processing, and overdue alerts.`},{title:`Financial & Growth Analytics`,desc:`Real-time revenue metrics, churn rate forecasting, and profit graphs.`},{title:`Trainer & Class Scheduler`,desc:`Interactive booking calendar for personal trainers and group sessions.`},{title:`Automated Expiry Alerts`,desc:`WhatsApp & SMS notifications before membership expiration.`},{title:`Role-Based Access Control`,desc:`Distinct permission portals for admins, trainers, and members.`}],tools:[`cursor`,`nextjs`,`react`,`nodejs`,`supabase`,`postgresql`,`vercel`],url:``,github:`https://github.com/harshityadav/gym-management`},{name:`Examora`,shortTitle:`Examora`,category:`AI SOFTWARE & EDTECH`,tagline:`AI-powered adaptive learning companion, document synthesizer & exam simulator`,status:`LIVE`,statusType:`live`,logo:`/assets/logos/companies/examora.svg`,video:``,role:`AI Software Engineer`,roleSummary:`Architected LLM document digestion pipelines, vector semantic embeddings, automated quiz generation engine, and spaced-repetition frontend.`,scenario:`AI Study & Exam Portal`,description:`An intelligent AI study portal designed to turn complex course material into masterable knowledge. It analyzes uploaded PDFs, textbooks, and notes to automatically generate active-recall flashcards, mock exam simulations, and personalized spaced-repetition schedules.`,features:[{title:`Multi-Document AI Summarizer`,desc:`Extracts core concepts, formulas, and definitions from PDFs and slides.`},{title:`Active Recall Flashcards`,desc:`AI-generated question-answer decks optimized for memory retention.`},{title:`Adaptive Exam Simulator`,desc:`Timed mock tests with instant AI grading and step-by-step solutions.`},{title:`Spaced-Repetition Scheduler`,desc:`Algorithmic review intervals based on individual retention curves.`},{title:`Weakness Diagnostic Engine`,desc:`Pinpoints conceptual gaps and suggests targeted review topics.`},{title:`Multi-Device Cloud Sync`,desc:`Instant cross-platform study synchronization and progress saving.`}],tools:[`cursor`,`nextjs`,`gemini`,`anthropic`,`supabase`,`vercel`,`typescript`],url:`https://examora.ai/`,github:`https://github.com/harshityadav/examora`},{name:`GestoType`,shortTitle:`GestoType`,category:`MACHINE LEARNING & COMPUTER VISION`,tagline:`Hands-free gesture-to-text input method powered by real-time computer vision`,status:`COMPLETED`,statusType:`completed`,logo:`/assets/logos/companies/gestotype.svg`,video:``,role:`ML / Computer Vision Dev`,roleSummary:`Trained spatial gesture classification models, built sub-millisecond hand landmark pipeline for webcams, and built virtual keyboard driver.`,scenario:`Gesture-to-Text Input Method`,description:`An accessibility-focused human-computer interface enabling touchless typing using an ordinary webcam. Employs lightweight deep learning architectures to track finger landmarks in real time, translating natural hand gestures into high-accuracy keystrokes and system commands without external hardware.`,features:[{title:`Real-Time Landmark Tracking`,desc:`Sub-millisecond 21-point 3D hand skeletal coordinate extraction.`},{title:`Custom Gesture Recognition`,desc:`High-accuracy spatial gesture classifier trained on diverse hand shapes.`},{title:`Standard Webcam Compatible`,desc:`Runs entirely in software on commodity RGB cameras with zero sensor lag.`},{title:`Virtual Dynamic Keyboard`,desc:`Predictive on-screen keyboard overlay with gesture hover dwell triggers.`},{title:`Integrated Predictive Typing`,desc:`N-gram language modeling for word suggestions and error correction.`},{title:`Custom Calibration Tool`,desc:`User-specific hand size adaptation and sensitivity tuning.`}],tools:[`python`,`pandas`,`jupyter`,`notebook`,`cursor`],url:``,github:`https://github.com/harshityadav/gestotype`}],ZS=[{x:-.158,y:.135},{x:.15,y:.142},{x:-.257,y:-.249},{x:.314,y:-.073}],QS=XS.map((e,t)=>{let n=ZS[t]||{x:0,y:0};return{id:`m${t}`,x:n.x,y:n.y,company:e.name,shortTitle:e.shortTitle||e.name,category:e.category||`PROJECT SHOWCASE`,tagline:e.tagline||e.scenario||``,status:e.status||`COMPLETED`,statusType:e.statusType||`completed`,logo:e.logo,video:e.video,role:e.role,roleSummary:e.roleSummary||``,scenario:e.scenario,description:e.description,features:e.features||[],tools:e.tools,url:e.url,github:e.github}}),$S=`'''

    if not re.search(old_data_pattern, content, flags=re.DOTALL):
        print("ERROR: old_data_pattern not matched in", filepath)
        return False

    content = re.sub(old_data_pattern, lambda m: new_data, content, count=1, flags=re.DOTALL)

    # Replacement 2: CD, TD, DD, OD, GD
    old_panel_pattern = r'var bD=\.64,xD=1\.5,SD=!1;function CD\(\)\{.*?' r'function GD\(e\)\{.*?\}'
    
    new_panel_code = r'''var bD=.64,xD=1.5,SD=!1;function CD(){if(SD)return;SD=!0;let e=document.createElement(`style`);e.dataset.mapPanel=`1`,e.textContent=`
    .map-panel-backdrop {
      position: fixed; inset: 0; z-index: 98;
      background: rgba(8, 14, 11, 0.55);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      opacity: 0; pointer-events: none;
      transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .map-panel-backdrop.is-active {
      opacity: 1; pointer-events: auto;
    }
    .map-panel {
      position: fixed; left: 50%; top: 50%;
      width: min(690px, calc(100vw - 32px));
      max-height: min(88vh, 840px);
      box-sizing: border-box;
      color: #ffffff;
      background: rgba(14, 20, 17, 0.85);
      background-image: radial-gradient(circle at 50% 0%, rgba(16, 185, 129, 0.09) 0%, transparent 65%);
      backdrop-filter: blur(28px) saturate(140%);
      -webkit-backdrop-filter: blur(28px) saturate(140%);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 26px;
      box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.05), 0 24px 60px -12px rgba(0, 0, 0, 0.75), 0 0 45px -10px rgba(16, 185, 129, 0.2);
      opacity: 0; pointer-events: none;
      transform: translate(-50%, calc(-50% + 20px)) scale(0.96);
      transform-origin: center;
      transition: opacity 0.28s cubic-bezier(0.16, 1, 0.3, 1), transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
      z-index: 100;
      font-family: 'Google Sans Flex', 'Google Sans Code', -apple-system, sans-serif;
      display: flex; flex-direction: column;
      overflow: hidden;
    }
    .map-panel.is-open {
      opacity: 1; pointer-events: auto;
      transform: translate(-50%, -50%) scale(1);
    }
    .map-panel-inner {
      padding: 24px 26px 22px 26px;
      overflow-y: auto;
      overflow-x: hidden;
      display: flex; flex-direction: column; gap: 16px;
      box-sizing: border-box;
      max-height: calc(min(88vh, 840px) - 2px);
    }
    .map-panel-inner::-webkit-scrollbar {
      width: 5px;
    }
    .map-panel-inner::-webkit-scrollbar-track {
      background: transparent;
    }
    .map-panel-inner::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.16);
      border-radius: 10px;
    }
    .map-panel-inner::-webkit-scrollbar-thumb:hover {
      background: rgba(255, 255, 255, 0.28);
    }
    .mp-close-btn {
      position: absolute; top: 18px; right: 18px;
      width: 34px; height: 34px; border-radius: 50%;
      background: rgba(255, 255, 255, 0.07);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: rgba(255, 255, 255, 0.7);
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: all 0.18s ease;
      z-index: 10; padding: 0; outline: none;
    }
    .mp-close-btn:hover {
      background: rgba(255, 255, 255, 0.16);
      color: #ffffff;
      transform: scale(1.08);
      border-color: rgba(255, 255, 255, 0.28);
    }
    .mp-close-btn:active {
      transform: scale(0.94);
    }
    .mp-header {
      display: flex; align-items: flex-start; gap: 18px;
      padding-right: 36px;
    }
    .mp-logo-box {
      width: 64px; height: 64px; border-radius: 18px;
      background: linear-gradient(135deg, rgba(255,255,255,0.08) 0%, rgba(255,255,255,0.02) 100%);
      border: 1px solid rgba(255, 255, 255, 0.14);
      box-shadow: inset 0 1px 1px rgba(255,255,255,0.15), 0 8px 24px rgba(0,0,0,0.35);
      display: flex; align-items: center; justify-content: center;
      padding: 10px; flex-shrink: 0; box-sizing: border-box;
    }
    .mp-logo-box img {
      width: 100%; height: 100%; object-fit: contain; display: block;
      filter: drop-shadow(0 2px 6px rgba(0,0,0,0.3));
    }
    .mp-header-info {
      display: flex; flex-direction: column; gap: 3px; min-width: 0;
    }
    .mp-meta-row {
      display: flex; align-items: center; gap: 10px; flex-wrap: wrap; margin-bottom: 2px;
    }
    .mp-category {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase;
      color: #34d399; font-weight: 600;
    }
    .mp-status-pill {
      display: inline-flex; align-items: center; gap: 5px;
      padding: 2px 8px; border-radius: 20px;
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 10px; font-weight: 600; letter-spacing: 0.05em;
      text-transform: uppercase;
      background: rgba(16, 185, 129, 0.12);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: #6ee7b7;
    }
    .mp-status-pill.is-completed {
      background: rgba(59, 130, 246, 0.12);
      border-color: rgba(59, 130, 246, 0.3);
      color: #93c5fd;
    }
    .mp-status-dot {
      width: 6px; height: 6px; border-radius: 50%;
      background: #10b981;
      box-shadow: 0 0 8px #10b981;
      animation: mp-pulse 2s infinite ease-in-out;
    }
    .mp-status-pill.is-completed .mp-status-dot {
      background: #60a5fa;
      box-shadow: 0 0 6px #60a5fa;
      animation: none;
    }
    @keyframes mp-pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.8); }
    }
    .mp-title {
      font-size: 24px; font-weight: 700; color: #ffffff;
      letter-spacing: -0.025em; line-height: 1.2;
      margin: 0; text-align: left;
    }
    .mp-tagline {
      font-size: 13.5px; color: #94a3b8; font-weight: 400;
      line-height: 1.4; text-align: left;
    }
    .mp-grid-cards {
      display: grid; grid-template-columns: 1fr 1fr; gap: 12px;
    }
    .mp-card {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.07);
      border-radius: 16px; padding: 14px 16px;
      display: flex; flex-direction: column; gap: 6px;
      text-align: left; box-sizing: border-box;
    }
    .mp-card-label {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 10.5px; letter-spacing: 0.08em; text-transform: uppercase;
      color: #64748b; font-weight: 600;
      display: flex; align-items: center; gap: 6px;
    }
    .mp-card-label svg {
      width: 13px; height: 13px; opacity: 0.85;
    }
    .mp-card-text {
      font-size: 12.5px; line-height: 1.5; color: #cbd5e1;
      margin: 0;
    }
    .mp-role-highlight {
      color: #34d399; font-weight: 600; font-size: 13px;
      margin-bottom: 1px;
    }
    .mp-section {
      display: flex; flex-direction: column; gap: 8px;
    }
    .mp-section-title {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase;
      color: #64748b; font-weight: 600; text-align: left;
      display: flex; align-items: center; gap: 6px; margin: 0;
    }
    .mp-features-grid {
      display: grid; grid-template-columns: 1fr 1fr; gap: 8px;
    }
    .mp-feature-item {
      background: rgba(255, 255, 255, 0.025);
      border: 1px solid rgba(255, 255, 255, 0.06);
      border-radius: 12px; padding: 10px 12px;
      display: flex; flex-direction: column; gap: 2px;
      text-align: left; transition: all 0.2s ease;
    }
    .mp-feature-item:hover {
      background: rgba(255, 255, 255, 0.05);
      border-color: rgba(52, 211, 153, 0.3);
      transform: translateY(-1px);
    }
    .mp-feature-title {
      font-size: 12px; font-weight: 600; color: #f1f5f9;
      display: flex; align-items: center; gap: 6px;
    }
    .mp-feature-dot {
      width: 5px; height: 5px; border-radius: 50%;
      background: #10b981; flex-shrink: 0;
    }
    .mp-feature-desc {
      font-size: 11px; color: #94a3b8; line-height: 1.35;
      padding-left: 11px;
    }
    .mp-tools-wrap {
      display: flex; flex-wrap: wrap; gap: 7px;
    }
    .mp-tool-badge {
      height: 29px; border-radius: 8px;
      background: rgba(255, 255, 255, 0.045);
      border: 1px solid rgba(255, 255, 255, 0.09);
      display: inline-flex; align-items: center; gap: 6px;
      padding: 0 10px; font-size: 12px; font-weight: 500;
      color: #e2e8f0; letter-spacing: -0.01em;
      transition: all 0.15s ease; box-sizing: border-box;
    }
    .mp-tool-badge:hover {
      background: rgba(255, 255, 255, 0.09);
      border-color: rgba(52, 211, 153, 0.4);
      transform: translateY(-1px);
      color: #ffffff;
    }
    .mp-tool-badge img {
      height: 14px; width: 14px; object-fit: contain;
      display: block; flex-shrink: 0;
    }
    .mp-actions-row {
      display: flex; gap: 10px; margin-top: 4px;
    }
    .mp-btn-action {
      flex: 1; height: 42px; border-radius: 12px;
      font-family: inherit; font-size: 13.5px; font-weight: 600;
      display: inline-flex; align-items: center; justify-content: center;
      gap: 7px; cursor: pointer; transition: all 0.18s ease;
      text-decoration: none; box-sizing: border-box; outline: none;
    }
    .mp-btn-primary {
      background: linear-gradient(135deg, #10b981 0%, #059669 100%);
      color: #ffffff; border: none;
      box-shadow: 0 4px 14px rgba(16, 185, 129, 0.35), inset 0 1px 1px rgba(255,255,255,0.25);
    }
    .mp-btn-primary:hover {
      filter: brightness(1.12);
      transform: translateY(-1px);
      box-shadow: 0 6px 20px rgba(16, 185, 129, 0.48);
    }
    .mp-btn-primary:active {
      transform: scale(0.98);
    }
    .mp-btn-secondary {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.14);
      color: #ffffff;
      box-shadow: inset 0 1px 1px rgba(255,255,255,0.05);
    }
    .mp-btn-secondary:hover {
      background: rgba(255, 255, 255, 0.12);
      border-color: rgba(255, 255, 255, 0.25);
      transform: translateY(-1px);
    }
    .mp-btn-secondary:active {
      transform: scale(0.98);
    }
    @media (max-width: 768px) {
      .map-panel {
        width: calc(100vw - 20px);
        max-height: calc(100vh - 36px);
        border-radius: 20px;
      }
      .map-panel-inner {
        padding: 18px 16px;
        gap: 14px;
        max-height: calc(100vh - 38px);
      }
      .mp-grid-cards, .mp-features-grid {
        grid-template-columns: 1fr;
      }
      .mp-header {
        gap: 14px;
      }
      .mp-logo-box {
        width: 52px; height: 52px; border-radius: 14px; padding: 8px;
      }
      .mp-title {
        font-size: 20px;
      }
      .mp-actions-row {
        flex-direction: column;
      }
    }
  `,document.head.appendChild(e)}var wD=()=>window.innerWidth<=768?.8:1;function TD({onJoin:e}={}){CD();let backdrop=document.createElement(`div`);backdrop.className=`map-panel-backdrop`,document.body.appendChild(backdrop);let t=document.createElement(`div`);t.className=`map-panel`,t._backdrop=backdrop;t.innerHTML=`
    <button class="mp-close-btn" type="button" aria-label="Close modal">
      <svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M1 1L13 13M1 13L13 1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
      </svg>
    </button>
    <div class="map-panel-inner">
      <div class="mp-header">
        <div class="mp-logo-box">
          <img data-company-logo alt="" />
        </div>
        <div class="mp-header-info">
          <div class="mp-meta-row">
            <span class="mp-category" data-category></span>
            <span class="mp-status-pill" data-status-wrap>
              <span class="mp-status-dot"></span>
              <span data-status></span>
            </span>
          </div>
          <h2 class="mp-title" data-project-title></h2>
          <div class="mp-tagline" data-tagline></div>
        </div>
      </div>

      <div class="mp-grid-cards">
        <div class="mp-card">
          <div class="mp-card-label">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
            PROJECT OVERVIEW
          </div>
          <p class="mp-card-text" data-desc></p>
        </div>

        <div class="mp-card">
          <div class="mp-card-label">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
            MY ROLE
          </div>
          <div class="mp-role-highlight" data-role></div>
          <p class="mp-card-text" data-role-desc></p>
        </div>
      </div>

      <div class="mp-section">
        <div class="mp-section-title">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          KEY FEATURES
        </div>
        <div class="mp-features-grid" data-features></div>
      </div>

      <div class="mp-section">
        <div class="mp-section-title">
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
          TECHNOLOGY STACK
        </div>
        <div class="mp-tools-wrap" data-tools></div>
      </div>

      <div class="mp-actions-row">
        <button class="mp-btn-action mp-btn-primary" data-url type="button">
          <span>View Live Project</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </button>
        <button class="mp-btn-action mp-btn-secondary" data-github type="button">
          <span>View Source</span>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
        </button>
      </div>
    </div>
  `;let closeBtn=t.querySelector(`.mp-close-btn`);closeBtn.addEventListener(`click`,e=>{e.stopPropagation(),X.play(`click`),OD(t)}),backdrop.addEventListener(`click`,e=>{e.stopPropagation(),OD(t)});let onKeyEsc=e=>{e.key===`Escape`&&t._activeId&&OD(t)};window.addEventListener(`keydown`,onKeyEsc),t._onKeyEsc=onKeyEsc,t.addEventListener(`pointerdown`,e=>e.stopPropagation()),t.addEventListener(`pointerup`,e=>e.stopPropagation()),t.addEventListener(`click`,e=>e.stopPropagation()),t.querySelector(`[data-url]`).addEventListener(`click`,n=>{n.stopPropagation();let r=QS.find(n=>n.id===t._activeId);r&&r.url&&(X.play(`click`),window.open(r.url,`_blank`))}),t.querySelector(`[data-github]`).addEventListener(`click`,n=>{n.stopPropagation();let r=QS.find(n=>n.id===t._activeId);r&&r.github&&(X.play(`click`),window.open(r.github,`_blank`))}),document.body.appendChild(t);return t}var ED=e=>e.toLowerCase().replace(/\s+/g,`-`);function DD(e,t){X.play(`hand-entry`);let n=e.querySelector(`[data-company-logo]`);n.alt=t.company||t.shortTitle||`Project Logo`,n.style.display=``,n.onerror=()=>{n.style.display=`none`};let r=t.logo||ED(t.company);n.src=r.includes(`/`)?r:`/assets/logos/companies/${r}.webp`;let i=e.querySelector(`[data-hero-media]`);if(i){jD(i);let e=t.video?`/assets/videos/${t.video}`:``;if(i.style.display=t.video?``:`none`,i.onerror=()=>{i.style.display=`none`},t.video&&!i.src.endsWith(t.video)&&(i.src=e,i.load()),t.video){i.currentTime=0,i.muted=!X.isEnabled(),i._audioSync=()=>{i.muted=!X.isEnabled()},window.addEventListener(`audio:statechange`,i._audioSync),i.onended=()=>jD(i);let e=i.play();e&&e.catch&&e.catch(()=>{})}}X.setMuffle(1),e._muffleEngaged=!0;let cat=e.querySelector(`[data-category]`);cat&&(cat.textContent=t.category||`DEVELOPMENT`);let statusWrap=e.querySelector(`[data-status-wrap]`),statusText=e.querySelector(`[data-status]`);if(statusWrap&&statusText){let st=t.status||`COMPLETED`;statusText.textContent=st,statusWrap.classList.toggle(`is-completed`,st.toUpperCase()!==`LIVE`)}let a=e.querySelector(`[data-project-title]`);a&&(a.textContent=t.shortTitle||t.company||``);let tagline=e.querySelector(`[data-tagline]`);tagline&&(tagline.textContent=t.tagline||t.scenario||``);let c=e.querySelector(`[data-desc]`),l=t.description||``;c&&(c.textContent=l);let role=e.querySelector(`[data-role]`);role&&(role.textContent=t.role||`Developer`);let roleDesc=e.querySelector(`[data-role-desc]`);roleDesc&&(roleDesc.textContent=t.roleSummary||`Designed and developed the application architecture and features.`);let featContainer=e.querySelector(`[data-features]`);if(featContainer){let feats=t.features||[];featContainer.innerHTML=feats.map(f=>`
      <div class="mp-feature-item">
        <div class="mp-feature-title">
          <span class="mp-feature-dot"></span>
          ${f.title}
        </div>
        <div class="mp-feature-desc">${f.desc}</div>
      </div>
    `).join(``)}let u=e.querySelector(`[data-tools]`);u&&(u.innerHTML=(t.tools||[]).map(e=>`<span class="mp-tool-badge"><img src="/assets/logos/tools/${e}.svg" alt="" loading="lazy" onerror="this.style.display='none'" />${YS[e]||e}</span>`).join(``));let o=e.querySelector(`[data-url]`);o&&(o.style.display=t.url?`inline-flex`:`none`);let s=e.querySelector(`[data-github]`);s&&(s.style.display=t.github?`inline-flex`:`none`);e._backdrop&&e._backdrop.classList.add(`is-active`),e.classList.add(`is-open`),e._activeId=t.id}function OD(e){AD(e),e._backdrop&&e._backdrop.classList.remove(`is-active`),e.classList.remove(`is-open`),e._activeId=null}var kD=0;function AD(e){e&&e._muffleEngaged&&(e._muffleEngaged=!1,X.setMuffle(kD,{duration:.35}))}function jD(e){e&&(e._audioSync&&=(window.removeEventListener(`audio:statechange`,e._audioSync),null),e.onended=null,e.muted=!0)}function MD(e){let t=e&&e.querySelector(`[data-hero-media]`);if(t){try{t.pause(),t.currentTime=0}catch{}jD(t)}}function ND(e){e._worldVideoPreloads||=[...new Set(QS.map(e=>e.video).filter(Boolean))].map(e=>{let t=document.createElement(`video`);return t.muted=!0,t.playsInline=!0,t.preload=`auto`,t.src=`/assets/videos/${e}`,t.style.cssText=`position:absolute;left:-9999px;top:-9999px;width:1px;height:1px;opacity:0;pointer-events:none;`,document.body.appendChild(t),t.load(),t})}function PD(e){if(e._worldVideoPreloads){for(let t of e._worldVideoPreloads)try{t.pause(),t.removeAttribute(`src`),t.load(),t.remove()}catch{}e._worldVideoPreloads=null}}var FD=2;function ID(e,{duration:t=FD,muffle:n=!1}={}){let r=document.createElement(`div`);r.style.cssText=`
    position: fixed;
    inset: 0;
    pointer-events: none;
    border-radius: 0px;
    box-shadow: 0 0 0 100vmax #ffffff;
    z-index: 50;
  `,document.body.appendChild(r),document.documentElement.style.setProperty(`--navbar-backdrop-dur`,`${t}s`),document.body.classList.add(`frame-open`),n&&X.setMuffle(.5,{duration:t});let i=document.createElement(`div`),a=document.createElement(`div`),o=document.createElement(`div`),s=document.createElement(`div`),c=`
    position: fixed;
    pointer-events: auto;
    z-index: 51;
    background: transparent;
  `;i.style.cssText=`${c} top: 0; left: 0; right: 0; height: 0px;`,a.style.cssText=`${c} bottom: 0; left: 0; right: 0; height: 0px;`,o.style.cssText=`${c} left: 0; top: 0; bottom: 0; width: 0px;`,s.style.cssText=`${c} right: 0; top: 0; bottom: 0; width: 0px;`,document.body.appendChild(i),document.body.appendChild(a),document.body.appendChild(o),document.body.appendChild(s);let l=[i,a,o,s],u=[e.ui._leftGroup,e.ui._rightGroup].filter(Boolean),d=e.ui._rightGroup||null,f=!!d&&window.matchMedia(`(max-width: 768px)`).matches,p=f?getComputedStyle(d):null,m=f&&parseFloat(p.left)||0,h=f&&parseFloat(p.right)||0,g=e._rulerEl&&e._rulerEl.classList.contains(`scroll-ruler`)?e._rulerEl:null,_={inset:0,radius:0};return document.documentElement.style.setProperty(`--stage5-frame-inset`,`0px`),{el:r,navTargets:u,rulerEl:g,tween:Y.to(_,{inset:10,radius:32,duration:t,ease:`power2.out`,onUpdate:()=>{r.style.inset=`${_.inset}px`,r.style.borderRadius=`${_.radius}px`,document.documentElement.style.setProperty(`--stage5-frame-inset`,`${_.inset}px`),i.style.height=`${_.inset}px`,a.style.height=`${_.inset}px`,o.style.width=`${_.inset}px`,s.style.width=`${_.inset}px`;for(let t of u){if(t===d&&f){d.style.left=`${m+_.inset}px`,d.style.right=`${h+_.inset}px`,d.style.transform=`translateY(${_.inset}px)`;continue}let n=``;t===e.ui._leftGroup?n=`translateX(${_.inset}px) `:t===e.ui._rightGroup&&(n=`translateX(${-_.inset}px) `),t.style.transform=`${n}translateY(${_.inset}px)`}g&&(g.style.transform=`translateX(-50%) translateY(${_.inset}px)`)}}),borderCatchers:l,muffled:n}}function LD(e){if(e){e.tween&&e.tween.kill();for(let t of e.navTargets)t&&(t.style.transform=``,t.style.left=``,t.style.right=``);if(e.rulerEl&&(e.rulerEl.style.transform=``),document.documentElement.style.removeProperty(`--stage5-frame-inset`),e.borderCatchers)for(let t of e.borderCatchers)t.remove();e.el.style.transition=`opacity 0.3s ease`,e.el.style.opacity=`0`,setTimeout(()=>e.el.remove(),300),document.body.classList.remove(`frame-open`),e.muffled&&X.setMuffle(0,{duration:.45})}}var RD=()=>({name:``,age:``,city:``,education:``,university:``,notes:``}),zD={step:1,email:``,asset:null,registered:!1,referralUrl:null,memberNumber:null,aheadCount:null,formData:RD()},BD=()=>{let e=(zD.formData.education||``).trim();return e===`graduate`||e===`other`?`so-called university`:(zD.formData.university||``).trim()};function VD(e,t,{onAllStepsComplete:n=null,onJoinFormClose:r=null,onCloseStart:i=null,showEntryAnimation:a=!0,entryAnimationDuration:o=2,autoExpandEmail:s=!1,onDismiss:c=null,muffleFloor:l=0,gate:u=null,routeEmail:d=null}={}){let f=null,p=null,m=null,h=null,g=(e,{skipToEnd:t=!1,assetUrl:n=null,aoUrl:r=null}={})=>{m=PT({host:e,skipToEnd:t,assetUrl:n,aoUrl:r,university:BD(),userName:(zD.formData.name||``).trim(),onComplete:i=>{zD.step=3,h=_E({host:e,sceneSlot:i.sceneEl,skipFlip:t,setSceneAutoRotate:i.setAutoRotate,pauseScene:i.pause,resumeScene:i.resume,userName:(zD.formData.name||``).trim(),university:BD(),assetUrl:n,aoUrl:r,referralUrl:zD.referralUrl||null,aheadCount:zD.aheadCount??null,memberNumber:zD.memberNumber??null})}}),zD.step<2&&(zD.step=2)},_=()=>{f&&(f.collapse(),f.show())},v=()=>{let e=!!(m||h);h&&typeof h.destroy==`function`&&h.destroy(),m&&typeof m.destroy==`function`&&m.destroy(),h=null,m=null,p=null,e?n?n():_():r?r():_()},y=({hideStep1:e,onSubmitSuccess:n=null})=>Zw({frameEl:t,email:zD.email,autoOpen:!0,initialFormData:zD.formData,hideStep1Content:e,muffleFloor:l,onFormDataChange:e=>{zD.formData={...zD.formData,...e}},onCloseStart:i,onClose:v,onSubmitSuccess:n}),b=()=>{f&&f.hide(),p=y({hideStep1:!1,onSubmitSuccess:({panel:e,asset:t,position:n})=>{t!=null&&(zD.asset=t),n!=null&&(zD.aheadCount=n);let r=zD.asset;g(e,{assetUrl:wb(r),aoUrl:Tb(r)})}})},x=e=>{f&&f.hide(),zD.step=3,p=y({hideStep1:!0});let t=e.asset;g(p.panel,{skipToEnd:!0,assetUrl:t==null?null:wb(t),aoUrl:t==null?null:Tb(t)})},S=async e=>{e!==zD.email&&(zD.formData=RD(),zD.asset=null,zD.step=1),zD.email=e,f&&f.setBusy(!0);let t;try{t=await Fw(e)}catch{t={registered:!1,profileComplete:!1}}f&&f.setBusy(!1),zD.asset=t.asset,zD.referralUrl=t.referralUrl||null,zD.memberNumber=t.memberNumber??null,zD.aheadCount=t.aheadCount??null,zD.registered=!!t.profileComplete;let n=!!(t.name||t.university||t.city||t.education||t.notes);t.uuid&&n&&(zD.formData={name:t.name||``,age:t.age||``,city:t.city||``,education:t.education||``,university:t.university||``,notes:t.notes||``}),t.profileComplete?x(t):b()};return u?(f=u,f.setOnEmail(S),f.setOnBack(c?()=>(c(),!0):null),zD.email&&f.setInitialEmail(zD.email)):(f=$E({onEmail:S,initialEmail:zD.email,showEntryAnimation:a,entryAnimationDuration:o,onBack:c?()=>(c(),!0):null}),s&&requestAnimationFrame(()=>f&&f.expandToInput())),d&&S(d),{emailGate:f,openEmail:()=>{f&&f.expandToInput()},getForm:()=>p,destroy:()=>{h&&typeof h.destroy==`function`&&h.destroy(),m&&typeof m.destroy==`function`&&m.destroy(),p&&typeof p.destroy==`function`&&p.destroy(),!u&&f&&typeof f.destroy==`function`&&f.destroy(),f=null}}}var HD=new K,UD=24,WD=26;function GD(e){}'''

    if not re.search(old_panel_pattern, content, flags=re.DOTALL):
        print("ERROR: old_panel_pattern not matched in", filepath)
        return False

    content = re.sub(old_panel_pattern, lambda m: new_panel_code, content, count=1, flags=re.DOTALL)

    # Replacement 3: Teardown cleanup of backdrop and onKeyEsc
    old_teardown = 'e._mapPanel&&(MD(e._mapPanel),AD(e._mapPanel),e._mapPanel.remove(),delete e._mapPanel)'
    new_teardown = 'e._mapPanel&&(MD(e._mapPanel),AD(e._mapPanel),e._mapPanel._backdrop&&e._mapPanel._backdrop.remove(),e._mapPanel._onKeyEsc&&window.removeEventListener(`keydown`,e._mapPanel._onKeyEsc),e._mapPanel.remove(),delete e._mapPanel)'
    
    if old_teardown in content:
        content = content.replace(old_teardown, new_teardown, 1)
        print("Teardown replaced in", filepath)
    else:
        print("Note: old_teardown not found in", filepath)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print("SUCCESS: Updated", filepath)
    return True

update_js_file("/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js")
update_js_file("/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js")
