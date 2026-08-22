import re

def update_minimal_project_modal():
    target_files = [
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/public/assets/main-B9-HtP-f.js",
        "/Users/harshityadav/.gemini/antigravity/scratch/zero-university/main-B9-HtP-f.js"
    ]

    # Cleaned minimal data definitions
    new_data = '''var YS={python:`Python`,jupyter:`Jupyter`,notebook:`Notebook`,pandas:`Pandas`,cursor:`Cursor`,codex:`Codex`,canva:`Canva`,googlesheets:`Google Sheets`,googleslides:`Google Slides`,nextjs:`Next.js`,vercel:`Vercel`,supabase:`Supabase`,gemini:`Gemini AI`,anthropic:`Claude`,react:`React`,nodejs:`Node.js`,express:`Express`,postgresql:`PostgreSQL`,typescript:`TypeScript`,threejs:`Three.js`,webgl:`WebGL`,esp32:`ESP32`,cpp:`C++`},XS=[{name:`Why Zero University website`,shortTitle:`Why Zero University`,category:`3D WEB & INTERACTIVE PLATFORM`,tagline:`Gamified 3D onboarding experience & interactive candidate portal`,logo:`/assets/brand/favicon.svg`,description:`An immersive 3D landing page built to revolutionize career discovery. It combines procedural WebGL shaders, camera navigation physics, and dynamic lighting with a gamified referral waitlist system.`,features:[`Procedural 3D WebGL world`,`Multi-stage scroll journey`,`Dynamic volumetric cloud shadows`,`Spatial audio sound design`,`Gamified waitlist scoring`],tools:[`nextjs`,`threejs`,`webgl`,`supabase`,`vercel`],url:`https://why.zero.university/`,github:`https://github.com/harshityadav/zero-university-clone`},{name:`Gym Management System`,shortTitle:`Gym Management System`,category:`FULL-STACK SAAS PLATFORM`,tagline:`Centralized SaaS membership & facility management platform`,logo:`/assets/logos/companies/gym.svg`,description:`A comprehensive full-stack management dashboard built for modern fitness centers. Streamlines membership renewals, real-time member check-ins, class schedules, and automated billing through a unified interface.`,features:[`Member management`,`Subscription tracking & billing`,`Real-time check-in logging`,`Revenue & churn analytics`,`Automated notifications`],tools:[`nextjs`,`react`,`nodejs`,`express`,`postgresql`],url:``,github:`https://github.com/harshityadav/gym-management`},{name:`Examora`,shortTitle:`Examora`,category:`AI SOFTWARE & EDTECH`,tagline:`AI-powered adaptive learning companion & exam simulator`,logo:`/assets/logos/companies/examora.svg`,description:`An intelligent academic portal that turns complex course handouts and textbooks into active-recall flashcards. Features adaptive mock exam simulations with automated step-by-step solutions powered by LLMs.`,features:[`Document concept extraction`,`Active recall flashcards`,`Adaptive exam simulator`,`Spaced-repetition review`,`Weakness diagnostic engine`],tools:[`nextjs`,`gemini`,`supabase`,`typescript`,`vercel`],url:`https://examora.ai/`,github:`https://github.com/harshityadav/examora`},{name:`GestoType`,shortTitle:`GestoType`,category:`AI & HUMAN-COMPUTER INTERACTION`,tagline:`Wearable hands-free air-writing & gesture input system`,logo:`/assets/logos/companies/gestotype.svg`,description:`An accessibility-focused hardware and software interaction system using an ESP32 microcontroller and motion sensing. Tracks 3D hand movements in real time to translate natural gestures into Bluetooth keyboard keystrokes.`,features:[`ESP32 & MPU6050 sensing`,`Real-time motion tracking`,`Bluetooth HID keyboard driver`,`High-accuracy gesture detection`,`Sub-millisecond latency`],tools:[`python`,`esp32`,`cpp`,`pandas`,`jupyter`],url:``,github:`https://github.com/harshityadav/gestotype`}],ZS=[{x:-.158,y:.135},{x:.15,y:.142},{x:-.257,y:-.249},{x:.314,y:-.073}],QS=XS.map((e,t)=>{let n=ZS[t]||{x:0,y:0};return{id:`m${t}`,x:n.x,y:n.y,company:e.name,shortTitle:e.shortTitle||e.name,category:e.category,tagline:e.tagline,logo:e.logo,description:e.description,features:e.features||[],tools:e.tools,url:e.url,github:e.github}}),$S=`'''

    # Cleaned minimal modal CSS and DOM
    new_panel_code = r'''var bD=.64,xD=1.5,SD=!1;function CD(){if(SD)return;SD=!0;let e=document.createElement(`style`);e.dataset.mapPanel=`1`,e.textContent=`
    .map-panel-backdrop {
      position: fixed; inset: 0; z-index: 98;
      background: rgba(6, 12, 9, 0.6);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      opacity: 0; pointer-events: none;
      transition: opacity 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .map-panel-backdrop.is-active {
      opacity: 1; pointer-events: auto;
    }
    .map-panel {
      position: fixed; left: 50%; top: 50%;
      width: min(520px, calc(100vw - 32px));
      max-height: min(84vh, 760px);
      box-sizing: border-box;
      color: #F4F7F5;
      background: rgba(12, 20, 16, 0.92);
      backdrop-filter: blur(24px) saturate(130%);
      -webkit-backdrop-filter: blur(24px) saturate(130%);
      border: 1px solid rgba(255, 255, 255, 0.10);
      border-radius: 24px;
      box-shadow: 0 20px 50px -10px rgba(0, 0, 0, 0.8), 0 0 35px -8px rgba(25, 216, 155, 0.18);
      opacity: 0; pointer-events: none;
      transform: translate(-50%, calc(-50% + 16px)) scale(0.97);
      transform-origin: center;
      transition: opacity 0.25s cubic-bezier(0.16, 1, 0.3, 1), transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
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
      padding: 26px 28px 22px 28px;
      overflow-y: auto;
      overflow-x: hidden;
      display: flex; flex-direction: column; gap: 18px;
      box-sizing: border-box;
      max-height: calc(min(84vh, 760px) - 2px);
    }
    .map-panel-inner::-webkit-scrollbar {
      width: 4px;
    }
    .map-panel-inner::-webkit-scrollbar-track {
      background: transparent;
    }
    .map-panel-inner::-webkit-scrollbar-thumb {
      background: rgba(255, 255, 255, 0.15);
      border-radius: 8px;
    }
    .mp-close-btn {
      position: absolute; top: 18px; right: 18px;
      width: 32px; height: 32px; border-radius: 50%;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: #A7B2AE;
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; transition: all 0.18s ease;
      z-index: 10; padding: 0; outline: none;
    }
    .mp-close-btn:hover {
      background: rgba(255, 255, 255, 0.14);
      color: #F4F7F5;
      transform: scale(1.06);
      border-color: rgba(255, 255, 255, 0.22);
    }
    .mp-close-btn:active {
      transform: scale(0.94);
    }
    .mp-header-area {
      display: flex; flex-direction: column; gap: 10px;
      padding-right: 30px;
    }
    .mp-logo-box {
      width: 48px; height: 48px; border-radius: 14px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      display: flex; align-items: center; justify-content: center;
      padding: 8px; box-sizing: border-box;
    }
    .mp-logo-box img {
      width: 100%; height: 100%; object-fit: contain; display: block;
    }
    .mp-title-group {
      display: flex; flex-direction: column; gap: 3px;
    }
    .mp-category {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 10.5px; letter-spacing: 0.08em; text-transform: uppercase;
      color: #19D89B; font-weight: 600;
    }
    .mp-title {
      font-size: 22px; font-weight: 700; color: #F4F7F5;
      letter-spacing: -0.02em; line-height: 1.2; margin: 0;
    }
    .mp-tagline {
      font-size: 13px; color: #A7B2AE; font-weight: 400; line-height: 1.4;
    }
    .mp-divider {
      height: 1px; width: 100%;
      background: rgba(255, 255, 255, 0.08);
      margin: -2px 0 0 0;
    }
    .mp-desc {
      font-size: 13px; line-height: 1.55; color: #cbd5e1;
      margin: 0;
    }
    .mp-section {
      display: flex; flex-direction: column; gap: 8px;
    }
    .mp-section-title {
      font-family: 'PP Supply Mono', 'Supply Sans', monospace;
      font-size: 10px; letter-spacing: 0.08em; text-transform: uppercase;
      color: #64748b; font-weight: 600; margin: 0;
    }
    .mp-features-list {
      display: flex; flex-wrap: wrap; gap: 8px 14px;
    }
    .mp-feature-bullet {
      display: inline-flex; align-items: center; gap: 6px;
      font-size: 12px; color: #e2e8f0; line-height: 1.4;
    }
    .mp-bullet-dot {
      width: 4px; height: 4px; border-radius: 50%;
      background: #19D89B; flex-shrink: 0;
    }
    .mp-tools-row {
      display: flex; flex-wrap: wrap; gap: 6px;
    }
    .mp-tool-pill {
      height: 26px; border-radius: 6px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.08);
      display: inline-flex; align-items: center; gap: 5px;
      padding: 0 8px; font-size: 11.5px; font-weight: 500;
      color: #e2e8f0; transition: all 0.15s ease;
    }
    .mp-tool-pill:hover {
      background: rgba(255, 255, 255, 0.08);
      border-color: rgba(25, 216, 155, 0.3);
      color: #19D89B;
    }
    .mp-tool-pill img {
      height: 12px; width: 12px; object-fit: contain;
      display: block; flex-shrink: 0;
    }
    .mp-actions-row {
      display: flex; gap: 10px; margin-top: 4px;
    }
    .mp-btn {
      flex: 1; height: 38px; border-radius: 10px;
      font-family: inherit; font-size: 13px; font-weight: 600;
      display: inline-flex; align-items: center; justify-content: center;
      gap: 6px; cursor: pointer; transition: all 0.16s ease;
      text-decoration: none; box-sizing: border-box; outline: none;
    }
    .mp-btn-primary {
      background: linear-gradient(135deg, #19D89B 0%, #0fa977 100%);
      color: #061510; border: none;
      box-shadow: 0 4px 12px rgba(25, 216, 155, 0.28);
    }
    .mp-btn-primary:hover {
      filter: brightness(1.1);
      transform: translateY(-1px);
      box-shadow: 0 6px 16px rgba(25, 216, 155, 0.4);
    }
    .mp-btn-primary:active {
      transform: scale(0.98);
    }
    .mp-btn-secondary {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #F4F7F5;
    }
    .mp-btn-secondary:hover {
      background: rgba(255, 255, 255, 0.1);
      border-color: rgba(255, 255, 255, 0.22);
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
        padding: 20px 18px;
        gap: 14px;
        max-height: calc(100vh - 38px);
      }
      .mp-actions-row {
        flex-direction: column;
      }
    }
  `,document.head.appendChild(e)}var wD=()=>window.innerWidth<=768?.8:1;function TD({onJoin:e}={}){CD();let backdrop=document.createElement(`div`);backdrop.className=`map-panel-backdrop`,document.body.appendChild(backdrop);let t=document.createElement(`div`);t.className=`map-panel`,t._backdrop=backdrop;t.innerHTML=`
    <button class="mp-close-btn" type="button" aria-label="Close modal">
      <svg width="13" height="13" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M1 1L13 13M1 13L13 1" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
      </svg>
    </button>
    <div class="map-panel-inner">
      <div class="mp-header-area">
        <div class="mp-logo-box">
          <img data-company-logo alt="" />
        </div>
        <div class="mp-title-group">
          <span class="mp-category" data-category></span>
          <h2 class="mp-title" data-project-title></h2>
          <div class="mp-tagline" data-tagline></div>
        </div>
      </div>

      <div class="mp-divider"></div>

      <p class="mp-desc" data-desc></p>

      <div class="mp-section">
        <div class="mp-section-title">FEATURES</div>
        <div class="mp-features-list" data-features></div>
      </div>

      <div class="mp-section">
        <div class="mp-section-title">BUILT WITH</div>
        <div class="mp-tools-row" data-tools></div>
      </div>

      <div class="mp-actions-row">
        <button class="mp-btn mp-btn-primary" data-url type="button">
          <span>View Live Project</span>
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </button>
        <button class="mp-btn mp-btn-secondary" data-github type="button">
          <span>GitHub</span>
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
        </button>
      </div>
    </div>
  `;let closeBtn=t.querySelector(`.mp-close-btn`);closeBtn.addEventListener(`click`,e=>{e.stopPropagation(),X.play(`click`),OD(t)}),backdrop.addEventListener(`click`,e=>{e.stopPropagation(),OD(t)});let onKeyEsc=e=>{e.key===`Escape`&&t._activeId&&OD(t)};window.addEventListener(`keydown`,onKeyEsc),t._onKeyEsc=onKeyEsc,t.addEventListener(`pointerdown`,e=>e.stopPropagation()),t.addEventListener(`pointerup`,e=>e.stopPropagation()),t.addEventListener(`click`,e=>e.stopPropagation()),t.querySelector(`[data-url]`).addEventListener(`click`,n=>{n.stopPropagation();let r=QS.find(n=>n.id===t._activeId);r&&r.url&&(X.play(`click`),window.open(r.url,`_blank`))}),t.querySelector(`[data-github]`).addEventListener(`click`,n=>{n.stopPropagation();let r=QS.find(n=>n.id===t._activeId);r&&r.github&&(X.play(`click`),window.open(r.github,`_blank`))}),document.body.appendChild(t);return t}var ED=e=>e.toLowerCase().replace(/\s+/g,`-`);function DD(e,t){X.play(`hand-entry`);let n=e.querySelector(`[data-company-logo]`);n.alt=t.company||t.shortTitle||`Project Logo`,n.style.display=``,n.onerror=()=>{n.style.display=`none`};let r=t.logo||ED(t.company);n.src=r.includes(`/`)?r:`/assets/logos/companies/${r}.webp`;let i=e.querySelector(`[data-hero-media]`);if(i){jD(i);let e=t.video?`/assets/videos/${t.video}`:``;if(i.style.display=t.video?``:`none`,i.onerror=()=>{i.style.display=`none`},t.video&&!i.src.endsWith(t.video)&&(i.src=e,i.load()),t.video){i.currentTime=0,i.muted=!X.isEnabled(),i._audioSync=()=>{i.muted=!X.isEnabled()},window.addEventListener(`audio:statechange`,i._audioSync),i.onended=()=>jD(i);let e=i.play();e&&e.catch&&e.catch(()=>{})}}X.setMuffle(1),e._muffleEngaged=!0;let cat=e.querySelector(`[data-category]`);cat&&(cat.textContent=t.category||`PROJECT`);let a=e.querySelector(`[data-project-title]`);a&&(a.textContent=t.shortTitle||t.company||``);let tagline=e.querySelector(`[data-tagline]`);tagline&&(tagline.textContent=t.tagline||``);let c=e.querySelector(`[data-desc]`),l=t.description||``;c&&(c.textContent=l);let featContainer=e.querySelector(`[data-features]`);if(featContainer){let feats=t.features||[];featContainer.innerHTML=feats.map(f=>`
      <div class="mp-feature-bullet">
        <span class="mp-bullet-dot"></span>
        <span>${f}</span>
      </div>
    `).join(``)}let u=e.querySelector(`[data-tools]`);u&&(u.innerHTML=(t.tools||[]).map(e=>`<span class="mp-tool-pill"><img src="/assets/logos/tools/${e}.svg" alt="" loading="lazy" onerror="this.style.display='none'" />${YS[e]||e}</span>`).join(``));let o=e.querySelector(`[data-url]`);o&&(o.style.display=t.url?`inline-flex`:`none`);let s=e.querySelector(`[data-github]`);s&&(s.style.display=t.github?`inline-flex`:`none`);e._backdrop&&e._backdrop.classList.add(`is-active`),e.classList.add(`is-open`),e._activeId=t.id}function OD(e){AD(e),e._backdrop&&e._backdrop.classList.remove(`is-active`),e.classList.remove(`is-open`),e._activeId=null}var kD=0;function AD(e){e&&e._muffleEngaged&&(e._muffleEngaged=!1,X.setMuffle(kD,{duration:.35}))}function jD(e){e&&(e._audioSync&&=(window.removeEventListener(`audio:statechange`,e._audioSync),null),e.onended=null,e.muted=!0)}function MD(e){let t=e&&e.querySelector(`[data-hero-media]`);if(t){try{t.pause(),t.currentTime=0}catch{}jD(t)}}function ND(e){e._worldVideoPreloads||=[...new Set(QS.map(e=>e.video).filter(Boolean))].map(e=>{let t=document.createElement(`video`);return t.muted=!0,t.playsInline=!0,t.preload=`auto`,t.src=`/assets/videos/${e}`,t.style.cssText=`position:absolute;left:-9999px;top:-9999px;width:1px;height:1px;opacity:0;pointer-events:none;`,document.body.appendChild(t),t.load(),t})}function PD(e){if(e._worldVideoPreloads){for(let t of e._worldVideoPreloads)try{t.pause(),t.removeAttribute(`src`),t.load(),t.remove()}catch{}e._worldVideoPreloads=null}}var FD=2;function ID(e,{duration:t=FD,muffle:n=!1}={}){let r=document.createElement(`div`);r.style.cssText=`
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

    for filepath in target_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Update 1: Replace data
        old_data_pattern = r'var YS=\{python:`Python`.*?,\$S=`'
        content = re.sub(old_data_pattern, lambda m: new_data, content, count=1, flags=re.DOTALL)

        # Update 2: Replace modal implementation
        old_panel_pattern = r'var bD=\.64,xD=1\.5,SD=!1;function CD\(\)\{.*?' r'function GD\(e\)\{\}'
        content = re.sub(old_panel_pattern, lambda m: new_panel_code, content, count=1, flags=re.DOTALL)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print("Updated minimal project modal in", filepath)

update_minimal_project_modal()
