<!doctype html>
<html lang="ar" dir="rtl">
 <head><script>window["__codeletBootstrap__"]=JSON.parse('{"A":"A","B":"20260810-01-d2eaec1","C":{"Abril Fatface":"YACgEZbkUVE,0","Alfa Slab One":"YACgEYS9sJU,0","Anton":"YACgEcYqQ-A,0","Archivo":"YAHO2-t-jNE,0","Arial":"YAGyDvJ_4Ts,0","Bebas Neue":"YACgESME5ew,0","Bricolage Grotesque":"YAFyMcdwzpc,0","Canva Sans":"YAFLd8sKbwc,2","Caveat":"YALBs2ploWQ,0","Comic Sans MS":"YAHO2VMiyZo,0","Cormorant Garamond":"YAFdJhX-538,0","Courier New":"YAGzXiGs0_8,0","DM Sans":"YAD1aU3sLnI,0","DM Serif Display":"YAD1aYG82rc,0","Forum":"YACgEcnnqB4,0","Fraunces":"YAEul-FRQw4,0","Georgia":"YAGzXkO0pEM,0","Helvetica Neue":"YAFcf6CtJfI,0","Impact":"YAFcfnjI7Vk,0","Inter":"YAFdJvSyp_k,3","Iowan Old Style":"YAGNIFa8j9o,0","Jacques Francois":"YAHO2a5g66Q,0","JetBrains Mono":"YAFdJksXcAk,0","Libre Baskerville":"YACgEUFdPdA,0","Manrope":"YAHO2b2feC4,0","Merriweather":"YACgEXvHxxs,0","Montserrat":"YADLjI9qxTA,0","Nunito":"YACgEX8C5Gg,0","Oleo Script":"YACgEQQ14jI,0","Phantom Sans":"YAHO2E8Pb88,0","Playfair Display":"YACgEYmuCJE,0","Poppins":"YAFdJjbTu24,1","Press Start 2P":"YAFyGr-8pmQ,0","Quicksand":"YADWjpfPmdk,0","Raleway":"YACgEVg3xZg,0","Segoe UI":"YAHNdRD1Klw,0","Source Sans 3":"YAG4lO1Mj10,0","Spectral":"YAHO2rVUHIM,0","Times New Roman":"YAGzXW3gftg,0","Times":"YAGzXW3gftg,0","Ubuntu":"YACgERDU--Q,0","Work Sans":"YAGXhLOKv44,0","Yellowtail":"YACgEYG4kG4,0","ui-monospace":"YADlN8CFZ8Q,0","ui-sans-serif":"YACkoN-xg4g,0"}}');</script><script src="/_sdk/7949ff62d67710d5.telemetry_sdk.js" integrity="sha512-KIvXA82Di44YY/RH9/63A9MuTuavYgDFG8PfErJn7Wli4K0LAOk+coo/aPXk3+ZNL96nHh9VYD4PE+fLes+laQ=="></script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>منصة إدارة الطاقة الذكية</title>
  <script src="https://cdn.tailwindcss.com/3.4.17"></script>
  <script src="https://cdn.jsdelivr.net/npm/lucide@0.263.0/dist/umd/lucide.min.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700&amp;display=swap" rel="stylesheet">
  <style>
    body { font-family: 'Tajawal', sans-serif; }
    .tab-active { background: rgba(99,102,241,0.2); border-color: #818cf8; color: #a5b4fc; }
    .tab-btn { transition: all 0.2s; }
    .card { backdrop-filter: blur(12px); background: rgba(15,20,40,0.75); border: 1px solid rgba(99,102,241,0.2); }
    .toggle-on { background: #6366f1; }
    .toggle-off { background: #374151; }
    .toggle-dot { transition: transform 0.2s; }
    .toggle-on .toggle-dot { transform: translateX(-100%); }
    .pulse-dot { animation: pd 2s infinite; }
    @keyframes pd { 0%,100%{ opacity:1 } 50%{ opacity:0.3 } }
    .chat-msg { animation: fadeIn 0.3s; }
    @keyframes fadeIn { from { opacity:0; transform:translateY(8px) } to { opacity:1; transform:translateY(0) } }
    .glow { box-shadow: 0 0 20px rgba(99,102,241,0.2); }
    .bar { transition: height 0.5s; }
    .nav-scroll { overflow-x: auto; scrollbar-width: none; }
    .nav-scroll::-webkit-scrollbar { display: none; }
  </style>
  <script src="/_sdk/0e8d3a91e1c6f495.data_sdk.js" type="text/javascript" integrity="sha512-c00oDoGjsMgluCLLEyVl3suwEkgjOGGplVFbsilUoBg4aMKNmsL3mwsc9r0dPn95qiSZyjBousQXgROkAW7p/w=="></script>
  <script src="/_sdk/04cc6185e046f597.resizing_sdk.js" type="text/javascript" integrity="sha512-CiE/G92aQF0nxneFg1kdOvXih8sQ1Z2a2QI3+r/WvzJwQqH6+IyB3iL07OkJmpm3ABAaf07+FnqWny98f5sR6w=="></script>
 </head>
 <body data-template-id="__page-root" class="min-h-screen text-white overflow-x-hidden"><img data-template-id="hero-img" class="canva-image fixed inset-0 w-full h-full object-cover opacity-20 pointer-events-none" loading="lazy">
  <div class="relative z-10">
   <header class="p-5 pb-3">
    <div class="flex items-center gap-2 mb-1">
     <div class="w-2.5 h-2.5 rounded-full bg-indigo-400 pulse-dot"></div><span class="text-indigo-300 text-xs">النظام يعمل</span>
    </div>
    <h1 data-template-id="main-title" class="canva-text text-2xl md:text-3xl font-bold"></h1>
    <p data-template-id="subtitle" class="canva-text mt-1 text-sm"></p>
   </header>
   <nav class="sticky top-0 z-50 bg-slate-900/90 backdrop-blur-md border-b border-indigo-500/20 px-3 py-2 nav-scroll flex gap-1.5"><button class="tab-btn tab-active shrink-0 py-2 px-3 rounded-lg border border-transparent text-xs font-medium flex items-center gap-1" onclick="switchTab(0)"><i data-lucide="layout-dashboard" style="width:14px;height:14px"></i><span data-template-id="nav-tab1" class="canva-text"></span></button> <button class="tab-btn shrink-0 py-2 px-3 rounded-lg border border-transparent text-slate-400 text-xs font-medium flex items-center gap-1" onclick="switchTab(1)"><i data-lucide="toggle-right" style="width:14px;height:14px"></i><span data-template-id="nav-tab2" class="canva-text"></span></button> <button class="tab-btn shrink-0 py-2 px-3 rounded-lg border border-transparent text-slate-400 text-xs font-medium flex items-center gap-1" onclick="switchTab(2)"><i data-lucide="bot" style="width:14px;height:14px"></i><span data-template-id="nav-tab3" class="canva-text"></span></button> <button class="tab-btn shrink-0 py-2 px-3 rounded-lg border border-transparent text-slate-400 text-xs font-medium flex items-center gap-1" onclick="switchTab(3)"><i data-lucide="wrench" style="width:14px;height:14px"></i><span data-template-id="nav-tab4" class="canva-text"></span></button> <button class="tab-btn shrink-0 py-2 px-3 rounded-lg border border-transparent text-slate-400 text-xs font-medium flex items-center gap-1" onclick="switchTab(4)"><i data-lucide="bar-chart-3" style="width:14px;height:14px"></i><span data-template-id="nav-tab5" class="canva-text"></span></button> <button class="tab-btn shrink-0 py-2 px-3 rounded-lg border border-transparent text-slate-400 text-xs font-medium flex items-center gap-1" onclick="switchTab(5)"><i data-lucide="leaf" style="width:14px;height:14px"></i><span data-template-id="nav-tab6" class="canva-text"></span></button> <button class="tab-btn shrink-0 py-2 px-3 rounded-lg border border-transparent text-slate-400 text-xs font-medium flex items-center gap-1" onclick="switchTab(6)"><i data-lucide="file-text" style="width:14px;height:14px"></i><span data-template-id="nav-tab7" class="canva-text"></span></button> <button class="tab-btn shrink-0 py-2 px-3 rounded-lg border border-transparent text-slate-400 text-xs font-medium flex items-center gap-1" onclick="switchTab(7)"><i data-lucide="settings" style="width:14px;height:14px"></i><span data-template-id="nav-tab8" class="canva-text"></span></button>
   </nav><!-- Tab 0: Dashboard -->
   <div id="tab-0" class="max-w-6xl mx-auto px-4 py-6">
    <section class="grid grid-cols-2 lg:grid-cols-4 gap-3 mb-6">
     <div class="card rounded-xl p-3">
      <div class="flex items-center gap-1.5 text-xs text-slate-400 mb-1">
       <i data-lucide="zap" style="width:14px;height:14px;color:#fbbf24"></i><span data-template-id="stat1-label" class="canva-text"></span>
      </div>
      <div id="stat-total" class="text-xl font-bold text-amber-400">
       0 kWh
      </div>
     </div>
     <div class="card rounded-xl p-3">
      <div class="flex items-center gap-1.5 text-xs text-slate-400 mb-1">
       <i data-lucide="trending-up" style="width:14px;height:14px;color:#a78bfa"></i><span data-template-id="stat2-label" class="canva-text"></span>
      </div>
      <div id="stat-eff" class="text-xl font-bold text-violet-400">
       0%
      </div>
     </div>
     <div class="card rounded-xl p-3">
      <div class="flex items-center gap-1.5 text-xs text-slate-400 mb-1">
       <i data-lucide="brain" style="width:14px;height:14px;color:#6366f1"></i><span data-template-id="stat3-label" class="canva-text"></span>
      </div>
      <div id="stat-predict" class="text-xl font-bold text-indigo-400">
       0 kWh
      </div>
     </div>
     <div class="card rounded-xl p-3">
      <div class="flex items-center gap-1.5 text-xs text-slate-400 mb-1">
       <i data-lucide="thermometer" style="width:14px;height:14px;color:#fb923c"></i><span data-template-id="stat4-label" class="canva-text"></span>
      </div>
      <div id="stat-temp" class="text-xl font-bold text-orange-400">
       0°C
      </div>
     </div>
    </section><!-- Extra stat row -->
    <section class="grid grid-cols-2 lg:grid-cols-4 gap-3 mb-6">
     <div class="card rounded-xl p-3">
      <div class="flex items-center gap-1.5 text-xs text-slate-400 mb-1">
       <i data-lucide="dollar-sign" style="width:14px;height:14px;color:#34d399"></i><span data-template-id="stat5-label" class="canva-text"></span>
      </div>
      <div id="stat-cost" class="text-xl font-bold text-emerald-400">
       0 د.ع
      </div>
     </div>
     <div class="card rounded-xl p-3">
      <div class="flex items-center gap-1.5 text-xs text-slate-400 mb-1">
       <i data-lucide="activity" style="width:14px;height:14px;color:#f472b6"></i><span data-template-id="stat6-label" class="canva-text"></span>
      </div>
      <div id="stat-voltage" class="text-xl font-bold text-pink-400">
       0 V
      </div>
     </div>
     <div class="card rounded-xl p-3">
      <div class="flex items-center gap-1.5 text-xs text-slate-400 mb-1">
       <i data-lucide="cloud" style="width:14px;height:14px;color:#22d3ee"></i><span data-template-id="stat7-label" class="canva-text"></span>
      </div>
      <div id="stat-carbon" class="text-xl font-bold text-cyan-400">
       0 kg
      </div>
     </div>
     <div class="card rounded-xl p-3">
      <div class="flex items-center gap-1.5 text-xs text-slate-400 mb-1">
       <i data-lucide="timer" style="width:14px;height:14px;color:#facc15"></i><span data-template-id="stat8-label" class="canva-text"></span>
      </div>
      <div id="stat-uptime" class="text-xl font-bold text-yellow-400">
       0%
      </div>
     </div>
    </section>
    <h2 data-template-id="buildings-title" class="canva-text text-lg font-bold mb-3"></h2>
    <div id="buildings-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3 mb-6"></div>
    <h2 data-template-id="chart-title" class="canva-text text-lg font-bold mb-3"></h2>
    <div class="card rounded-xl p-4 mb-6">
     <canvas id="chart" width="800" height="200" class="w-full"></canvas>
    </div>
    <h2 data-template-id="alerts-title" class="canva-text text-lg font-bold mb-3"></h2>
    <div id="alerts-list" class="space-y-2"></div>
   </div><!-- Tab 1: Controls -->
   <div id="tab-1" class="max-w-6xl mx-auto px-4 py-6 hidden">
    <h2 data-template-id="controls-title" class="canva-text text-lg font-bold mb-4"></h2>
    <div id="controls-grid" class="space-y-3"></div>
   </div><!-- Tab 2: AI -->
   <div id="tab-2" class="max-w-6xl mx-auto px-4 py-6 hidden">
    <h2 data-template-id="ai-title" class="canva-text text-lg font-bold mb-3"></h2>
    <div class="card rounded-xl p-4 mb-4">
     <h3 data-template-id="predict-title" class="canva-text font-bold mb-2"></h3>
     <div id="predict-content" class="text-sm text-slate-300 space-y-1"></div>
    </div>
    <div class="card rounded-xl flex flex-col" style="height: calc(50 * min(var(--vh, 1vh), 1vh))">
     <div class="p-3 border-b border-indigo-500/20 flex items-center gap-2">
      <i data-lucide="bot" style="width:18px;height:18px;color:#818cf8"></i><span data-template-id="chat-header" class="canva-text text-sm font-medium"></span>
     </div>
     <div id="chat-messages" class="flex-1 overflow-y-auto p-3 space-y-2"></div>
     <form id="chat-form" class="p-3 border-t border-indigo-500/20 flex gap-2"><input id="chat-input" data-template-id="chat-input" class="canva-input flex-1 bg-slate-800 border border-slate-600 rounded-lg px-3 py-2 text-sm text-white outline-none focus:border-indigo-500" type="text"> <button type="submit" class="bg-indigo-600 hover:bg-indigo-500 rounded-lg px-4 py-2 text-sm font-medium transition"><i data-lucide="send" style="width:16px;height:16px"></i></button>
     </form>
    </div>
   </div><!-- Tab 3: Maintenance -->
   <div id="tab-3" class="max-w-6xl mx-auto px-4 py-6 hidden">
    <h2 data-template-id="maint-title" class="canva-text text-lg font-bold mb-4"></h2>
    <div id="maint-table" class="space-y-2"></div>
   </div><!-- Tab 4: Comparison -->
   <div id="tab-4" class="max-w-6xl mx-auto px-4 py-6 hidden">
    <h2 data-template-id="compare-title" class="canva-text text-lg font-bold mb-4"></h2>
    <div class="card rounded-xl p-4 mb-4">
     <div id="compare-bars" class="flex items-end justify-around gap-2" style="height:220px"></div>
    </div>
    <h2 data-template-id="cost-title" class="canva-text text-lg font-bold mb-3"></h2>
    <div id="cost-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3"></div>
   </div><!-- Tab 5: Carbon -->
   <div id="tab-5" class="max-w-6xl mx-auto px-4 py-6 hidden">
    <h2 data-template-id="carbon-title" class="canva-text text-lg font-bold mb-4"></h2>
    <div class="card rounded-xl p-6 text-center mb-4">
     <div id="carbon-ring" class="inline-block relative w-40 h-40 mb-3">
      <svg viewbox="0 0 100 100" class="w-full h-full -rotate-90"><circle cx="50" cy="50" r="42" fill="none" stroke="#1e293b" stroke-width="8" /> <circle id="carbon-arc" cx="50" cy="50" r="42" fill="none" stroke="#22d3ee" stroke-width="8" stroke-linecap="round" stroke-dasharray="264" stroke-dashoffset="80" />
      </svg>
      <div class="absolute inset-0 flex items-center justify-center flex-col"><span id="carbon-pct" class="text-2xl font-bold text-cyan-400">70%</span> <span class="text-xs text-slate-400">نظيف</span>
      </div>
     </div>
     <p data-template-id="carbon-desc" class="canva-text text-sm"></p>
    </div>
    <h2 data-template-id="events-title" class="canva-text text-lg font-bold mb-3"></h2>
    <div id="events-log" class="space-y-2 max-h-64 overflow-y-auto"></div>
   </div><!-- Tab 6: Reports -->
   <div id="tab-6" class="max-w-6xl mx-auto px-4 py-6 hidden">
    <h2 data-template-id="reports-title" class="canva-text text-lg font-bold mb-4"></h2>
    <div id="reports-grid" class="grid grid-cols-1 sm:grid-cols-2 gap-3"></div>
   </div><!-- Tab 7: Settings -->
   <div id="tab-7" class="max-w-6xl mx-auto px-4 py-6 hidden">
    <h2 data-template-id="settings-title" class="canva-text text-lg font-bold mb-4"></h2>
    <div class="space-y-3">
     <div class="card rounded-xl p-4">
      <h3 data-template-id="settings-alerts-label" class="canva-text font-bold mb-2"></h3>
      <div class="flex items-center justify-between"><span class="text-sm text-slate-300">تفعيل التنبيهات الصوتية</span> <button id="toggle-sound" onclick="toggleSetting('sound')" class="w-10 h-5 rounded-full relative toggle-on">
        <div class="toggle-dot absolute top-0.5 right-0.5 w-4 h-4 bg-white rounded-full shadow"></div></button>
      </div>
      <div class="flex items-center justify-between mt-2"><span class="text-sm text-slate-300">إشعارات البريد الإلكتروني</span> <button id="toggle-email" onclick="toggleSetting('email')" class="w-10 h-5 rounded-full relative toggle-off">
        <div class="toggle-dot absolute top-0.5 left-0.5 w-4 h-4 bg-white rounded-full shadow"></div></button>
      </div>
     </div>
     <div class="card rounded-xl p-4">
      <h3 data-template-id="settings-threshold-label" class="canva-text font-bold mb-2"></h3>
      <div class="flex items-center gap-3"><span class="text-sm text-slate-300">حد الاستهلاك الأقصى</span> <input type="range" min="500" max="2000" value="1200" id="threshold-slider" class="flex-1 accent-indigo-500"> <span id="threshold-val" class="text-indigo-300 font-bold text-sm">1200 kWh</span>
      </div>
     </div>
     <div class="card rounded-xl p-4">
      <h3 data-template-id="settings-priority-label" class="canva-text font-bold mb-2"></h3>
      <div id="priority-list" class="space-y-2"></div>
     </div>
     <div class="card rounded-xl p-4">
      <h3 data-template-id="settings-emergency-label" class="canva-text font-bold mb-2"></h3>
      <div id="emergency-panel" class="space-y-2"></div>
     </div>
    </div>
   </div>
  </div>
  <script src="/_sdk/a21fbee0f546ac94.editing_sdk.js" integrity="sha512-kYZrL0cHzR5BHnhrx8zxpQsDJHP1kmWVYeL0jhNBDl9VSYhmXdjMxDbk/u1ACh2xFuSYLc6XAPsKs3BInegRgw=="></script>
  <script>
    lucide.createIcons();

    const buildings = [
      { id:'eng', name:'كلية الهندسة', base:180, icon:'🏗️', devices:{lights:3,fans:2,acs:4} },
      { id:'med', name:'كلية الطب', base:220, icon:'🏥', devices:{lights:5,fans:3,acs:6} },
      { id:'lib', name:'المكتبة المركزية', base:90, icon:'📚', devices:{lights:4,fans:2,acs:3} },
      { id:'admin', name:'مبنى الإدارة', base:60, icon:'🏢', devices:{lights:2,fans:1,acs:2} },
      { id:'lab', name:'مختبر الحاسبات', base:150, icon:'💻', devices:{lights:3,fans:2,acs:5} },
      { id:'hall', name:'القاعات الدراسية', base:130, icon:'🎓', devices:{lights:6,fans:4,acs:4} },
    ];

    const deviceStates = {};
    buildings.forEach(b => { deviceStates[b.id] = { lights:true, fans:true, acs:true }; });

    const settings = { sound:true, email:false };

    const allTabs = Array.from({length:8},(_,i)=>document.getElementById('tab-'+i));
    const navBtns = document.querySelectorAll('nav button');

    function switchTab(i) {
      allTabs.forEach((t,idx) => t.classList.toggle('hidden', idx!==i));
      navBtns.forEach((btn,idx) => { btn.classList.toggle('tab-active', idx===i); btn.classList.toggle('text-slate-400', idx!==i); });
      if(i===3) renderMaintenance();
      if(i===4) { renderComparison(); renderCostAnalysis(); }
      if(i===5) { renderCarbon(); renderEvents(); }
      if(i===6) renderReports();
      if(i===7) { renderPriority(); renderEmergency(); }
    }

    function getConsumption(b) {
      const s = deviceStates[b.id];
      let mult = 1;
      if(!s.acs) mult -= 0.4;
      if(!s.lights) mult -= 0.15;
      if(!s.fans) mult -= 0.1;
      return (b.base + Math.random()*30) * Math.max(mult,0.2);
    }

    function renderBuildings() {
      const grid = document.getElementById('buildings-grid');
      grid.innerHTML = '';
      buildings.forEach(b => {
        const consumption = getConsumption(b).toFixed(1);
        const s = deviceStates[b.id];
        const el = document.createElement('div');
        el.className = 'card rounded-xl p-4 glow';
        el.innerHTML = `<div class="flex justify-between items-start"><div><span class="text-2xl">${b.icon}</span><h3 class="font-bold mt-1 text-sm">${b.name}</h3></div><span class="w-2 h-2 rounded-full bg-indigo-400 pulse-dot"></span></div><div class="mt-2"><span class="text-xl font-bold text-indigo-300">${consumption}</span><span class="text-slate-400 text-xs mr-1">kWh</span></div><div class="mt-2 flex gap-2 text-xs"><span class="${s.lights?'text-yellow-400':'text-slate-600'}">💡${b.devices.lights}</span><span class="${s.fans?'text-cyan-400':'text-slate-600'}">🌀${b.devices.fans}</span><span class="${s.acs?'text-blue-400':'text-slate-600'}">❄️${b.devices.acs}</span></div>`;
        grid.appendChild(el);
      });
    }

    function renderControls() {
      const grid = document.getElementById('controls-grid');
      grid.innerHTML = '';
      buildings.forEach(b => {
        const s = deviceStates[b.id];
        const el = document.createElement('div');
        el.className = 'card rounded-xl p-4';
        el.innerHTML = `<div class="flex items-center gap-2 mb-3"><span class="text-xl">${b.icon}</span><h3 class="font-bold text-sm">${b.name}</h3></div><div class="grid grid-cols-3 gap-2">${makeToggle(b.id,'lights','💡 مصابيح',s.lights)}${makeToggle(b.id,'fans','🌀 مراوح',s.fans)}${makeToggle(b.id,'acs','❄️ مكيفات',s.acs)}</div>`;
        grid.appendChild(el);
      });
    }

    function makeToggle(bid,type,label,on) {
      return `<div class="flex flex-col items-center gap-1"><span class="text-xs text-slate-300">${label}</span><button onclick="toggleDevice('${bid}','${type}')" class="w-10 h-5 rounded-full relative ${on?'toggle-on':'toggle-off'}"><div class="toggle-dot absolute top-0.5 ${on?'right-0.5':'left-0.5'} w-4 h-4 bg-white rounded-full shadow"></div></button><span class="text-[10px] ${on?'text-indigo-300':'text-slate-500'}">${on?'تشغيل':'إيقاف'}</span></div>`;
    }

    window.toggleDevice = function(bid,type) { deviceStates[bid][type] = !deviceStates[bid][type]; renderControls(); renderBuildings(); };

    function updateStats() {
      let total = 0;
      buildings.forEach(b => { total += getConsumption(b); });
      document.getElementById('stat-total').textContent = total.toFixed(0) + ' kWh';
      document.getElementById('stat-eff').textContent = (75+Math.random()*15).toFixed(1) + '%';
      document.getElementById('stat-predict').textContent = (total*1.08).toFixed(0) + ' kWh';
      document.getElementById('stat-temp').textContent = (43+Math.random()*5).toFixed(1) + '°C';
      document.getElementById('stat-cost').textContent = (total*0.12).toFixed(0) + ' د.ع';
      document.getElementById('stat-voltage').textContent = (218+Math.random()*8).toFixed(1) + ' V';
      document.getElementById('stat-carbon').textContent = (total*0.42).toFixed(0) + ' kg';
      document.getElementById('stat-uptime').textContent = (97+Math.random()*2.5).toFixed(1) + '%';
    }

    let chartData = Array.from({length:24},(_,i)=>350+Math.sin(i/3)*120+Math.random()*40);
    function drawChart() {
      const canvas = document.getElementById('chart');
      const ctx = canvas.getContext('2d');
      const w=canvas.width, h=canvas.height;
      ctx.clearRect(0,0,w,h);
      const max = Math.max(...chartData)*1.1;
      const step = w/(chartData.length-1);
      ctx.beginPath(); ctx.strokeStyle='#6366f1'; ctx.lineWidth=2.5;
      chartData.forEach((v,i)=>{ const x=i*step, y=h-(v/max)*h+10; i===0?ctx.moveTo(x,y):ctx.lineTo(x,y); });
      ctx.stroke();
      ctx.lineTo((chartData.length-1)*step,h); ctx.lineTo(0,h); ctx.closePath();
      const grad=ctx.createLinearGradient(0,0,0,h);
      grad.addColorStop(0,'rgba(99,102,241,0.25)'); grad.addColorStop(1,'rgba(99,102,241,0)');
      ctx.fillStyle=grad; ctx.fill();
    }

    const aiAlerts = [
      {type:'warning',msg:'مختبر 4: المكيف يعمل 6 ساعات بدون إشغال'},
      {type:'info',msg:'توصية: تأخير تشغيل التكييف 15 دقيقة لتقليل الذروة'},
      {type:'danger',msg:'ارتفاع مفاجئ بالتيار - كلية الهندسة'},
      {type:'success',msg:'كفاءة الطاقة تحسنت 12% هذا الأسبوع'},
      {type:'warning',msg:'انخفاض الجهد في مبنى الإدارة - يحتاج صيانة'},
      {type:'info',msg:'الطاقة الشمسية توفر 18% من الاستهلاك اليوم'},
    ];
    let alertIdx=0;
    function addAlert() {
      const list = document.getElementById('alerts-list');
      const a = aiAlerts[alertIdx++%aiAlerts.length];
      const colors={warning:'border-amber-500/60 bg-amber-500/10',danger:'border-red-500/60 bg-red-500/10',info:'border-indigo-500/60 bg-indigo-500/10',success:'border-emerald-500/60 bg-emerald-500/10'};
      const icons={warning:'⚠️',danger:'🚨',info:'💡',success:'✅'};
      const el=document.createElement('div');
      el.className=`chat-msg border-r-4 ${colors[a.type]} rounded-lg p-2.5 flex items-center gap-2 text-sm`;
      el.innerHTML=`<span>${icons[a.type]}</span><span>${a.msg}</span>`;
      list.prepend(el);
      if(list.children.length>6) list.lastChild.remove();
    }

    function renderPrediction() {
      const el=document.getElementById('predict-content');
      let total=0, html='<div class="grid grid-cols-2 gap-2">';
      buildings.forEach(b=>{ const pred=(b.base*(1.05+Math.random()*0.1)).toFixed(0); total+=+pred; html+=`<div class="flex justify-between bg-slate-800/50 rounded px-2 py-1"><span>${b.icon} ${b.name}</span><span class="text-indigo-300 font-bold">${pred} kWh</span></div>`; });
      html+=`</div><div class="mt-3 pt-2 border-t border-slate-700 text-center"><span class="text-indigo-400 font-bold text-lg">${total} kWh</span> <span class="text-slate-400">إجمالي الحمل المتوقع للغد</span></div>`;
      el.innerHTML=html;
    }

    // Chat
    const chatResponses=['بناءً على تحليل البيانات، أنصح بإيقاف مكيفات المكتبة بعد الساعة 8 مساءً لتوفير 15% من الطاقة.','الحمل الحالي ضمن الحدود الطبيعية. لا توجد مخاطر على الدوائر الكهربائية.','تم تحليل أنماط الاستهلاك: كلية الطب تستهلك أعلى طاقة بسبب أجهزة التبريد المتعددة.','يمكنك توفير 20% بتشغيل المراوح بدلاً من المكيفات في الفترات المعتدلة.','أتوقع ارتفاع الاستهلاك غداً بنسبة 8% بسبب ارتفاع درجات الحرارة المتوقعة.','البصمة الكربونية اليوم أقل بنسبة 5% مقارنة بالأسبوع الماضي.'];
    document.getElementById('chat-form').addEventListener('submit',function(e){
      e.preventDefault();
      const input=document.getElementById('chat-input');
      const msg=input.value.trim(); if(!msg) return;
      appendChat(msg,'user'); input.value='';
      setTimeout(()=>{ appendChat(chatResponses[Math.floor(Math.random()*chatResponses.length)],'bot'); },800);
    });
    function appendChat(text,who) {
      const c=document.getElementById('chat-messages');
      const el=document.createElement('div');
      el.className=`chat-msg flex ${who==='user'?'justify-start':'justify-end'}`;
      el.innerHTML=`<div class="max-w-[80%] rounded-xl px-3 py-2 text-sm ${who==='user'?'bg-indigo-600/30 text-white':'bg-slate-700 text-indigo-200'}">${text}</div>`;
      c.appendChild(el); c.scrollTop=c.scrollHeight;
    }

    // Maintenance
    const maintItems=[
      {building:'كلية الهندسة',task:'صيانة المكيفات المركزية',date:'2026-08-12',status:'مجدول'},
      {building:'المكتبة المركزية',task:'فحص الأسلاك الكهربائية',date:'2026-08-15',status:'مجدول'},
      {building:'مختبر الحاسبات',task:'تبديل مصابيح LED',date:'2026-08-08',status:'مكتمل'},
      {building:'كلية الطب',task:'صيانة المولد الاحتياطي',date:'2026-08-20',status:'مجدول'},
      {building:'القاعات الدراسية',task:'فحص نظام الإنذار',date:'2026-08-18',status:'متأخر'},
    ];
    function renderMaintenance(){
      const el=document.getElementById('maint-table'); el.innerHTML='';
      maintItems.forEach(m=>{
        const statusColor = m.status==='مكتمل'?'text-emerald-400':m.status==='متأخر'?'text-red-400':'text-indigo-300';
        const d=document.createElement('div');
        d.className='card rounded-xl p-3 flex flex-col sm:flex-row sm:items-center justify-between gap-2';
        d.innerHTML=`<div><h4 class="font-bold text-sm">${m.building}</h4><p class="text-xs text-slate-400">${m.task}</p></div><div class="flex items-center gap-3"><span class="text-xs text-slate-400">${m.date}</span><span class="text-xs font-bold ${statusColor}">${m.status}</span></div>`;
        el.appendChild(d);
      });
    }

    // Comparison
    function renderComparison(){
      const el=document.getElementById('compare-bars'); el.innerHTML='';
      buildings.forEach(b=>{
        const val=b.base+Math.random()*50;
        const pct=(val/270)*100;
        const bar=document.createElement('div');
        bar.className='flex flex-col items-center gap-1 flex-1';
        bar.innerHTML=`<span class="text-xs font-bold text-indigo-300">${val.toFixed(0)}</span><div class="w-full bg-indigo-600/80 rounded-t bar" style="height:${pct}%"></div><span class="text-[10px] text-slate-400 text-center mt-1">${b.icon}</span>`;
        el.appendChild(bar);
      });
    }

    // Cost
    function renderCostAnalysis(){
      const el=document.getElementById('cost-grid'); el.innerHTML='';
      buildings.forEach(b=>{
        const kwh=b.base+Math.random()*40;
        const cost=(kwh*0.12).toFixed(0);
        const d=document.createElement('div');
        d.className='card rounded-xl p-3';
        d.innerHTML=`<div class="flex items-center gap-2 mb-1"><span>${b.icon}</span><span class="font-bold text-sm">${b.name}</span></div><div class="flex justify-between text-sm"><span class="text-slate-400">${kwh.toFixed(0)} kWh</span><span class="text-emerald-400 font-bold">${cost} د.ع</span></div>`;
        el.appendChild(d);
      });
    }

    // Carbon
    function renderCarbon(){
      const pct=65+Math.random()*20;
      document.getElementById('carbon-pct').textContent=pct.toFixed(0)+'%';
      document.getElementById('carbon-arc').setAttribute('stroke-dashoffset', 264-(264*pct/100));
    }

    // Events
    const eventTypes=['تشغيل تلقائي للمكيفات','إيقاف المصابيح - عدم إشغال','تنبيه ارتفاع الحمل','تبديل إلى المولد الاحتياطي','تحديث جدول الصيانة','فحص دوري للجهد'];
    function renderEvents(){
      const el=document.getElementById('events-log'); el.innerHTML='';
      for(let i=0;i<8;i++){
        const d=document.createElement('div');
        d.className='card rounded-lg p-2.5 flex items-center gap-2 text-sm';
        const hr=Math.floor(Math.random()*24), min=Math.floor(Math.random()*60);
        d.innerHTML=`<span class="text-xs text-slate-500">${String(hr).padStart(2,'0')}:${String(min).padStart(2,'0')}</span><span class="text-slate-300">${eventTypes[i%eventTypes.length]}</span>`;
        el.appendChild(d);
      }
    }

    // Reports
    function renderReports(){
      const el=document.getElementById('reports-grid'); el.innerHTML='';
      const months=['يناير','فبراير','مارس','أبريل','مايو','يونيو','يوليو','أغسطس'];
      months.slice(-4).forEach(m=>{
        const kwh=(800+Math.random()*400).toFixed(0);
        const cost=(kwh*0.12).toFixed(0);
        const eff=(70+Math.random()*20).toFixed(0);
        const d=document.createElement('div');
        d.className='card rounded-xl p-4';
        d.innerHTML=`<h4 class="font-bold text-indigo-300 mb-2">${m} 2026</h4><div class="grid grid-cols-3 gap-2 text-center text-xs"><div><span class="block text-lg font-bold text-amber-400">${kwh}</span>kWh</div><div><span class="block text-lg font-bold text-emerald-400">${cost}</span>د.ع</div><div><span class="block text-lg font-bold text-violet-400">${eff}%</span>كفاءة</div></div>`;
        el.appendChild(d);
      });
    }

    // Settings
    window.toggleSetting = function(key){
      settings[key]=!settings[key];
      const btn=document.getElementById('toggle-'+key);
      btn.className=`w-10 h-5 rounded-full relative ${settings[key]?'toggle-on':'toggle-off'}`;
      btn.querySelector('.toggle-dot').className=`toggle-dot absolute top-0.5 ${settings[key]?'right-0.5':'left-0.5'} w-4 h-4 bg-white rounded-full shadow`;
    };
    document.getElementById('threshold-slider').addEventListener('input',function(){ document.getElementById('threshold-val').textContent=this.value+' kWh'; });

    function renderPriority(){
      const el=document.getElementById('priority-list'); el.innerHTML='';
      const priorities=['التكييف - أولوية قصوى','الإضاءة - أولوية عالية','المراوح - أولوية متوسطة','الأجهزة المكتبية - أولوية منخفضة'];
      priorities.forEach((p,i)=>{
        const d=document.createElement('div');
        const colors=['text-red-400','text-amber-400','text-indigo-300','text-slate-400'];
        d.className='flex items-center gap-2 text-sm';
        d.innerHTML=`<span class="w-5 h-5 rounded-full bg-slate-700 flex items-center justify-center text-xs font-bold">${i+1}</span><span class="${colors[i]}">${p}</span>`;
        el.appendChild(d);
      });
    }

    function renderEmergency(){
      const el=document.getElementById('emergency-panel'); el.innerHTML='';
      const items=['قطع الطاقة الطارئ - جميع المباني','تفعيل المولد الاحتياطي','إخلاء وإيقاف تشغيل كامل'];
      items.forEach(item=>{
        const d=document.createElement('div');
        d.className='flex items-center justify-between';
        d.innerHTML=`<span class="text-sm text-slate-300">${item}</span><button onclick="this.textContent=this.textContent==='تفعيل'?'✓ مفعّل':'تفعيل'" class="text-xs bg-red-600/20 border border-red-500/40 text-red-400 rounded px-2 py-1 hover:bg-red-600/40 transition">تفعيل</button>`;
        el.appendChild(d);
      });
    }

    // Init
    renderBuildings(); renderControls(); updateStats(); drawChart(); addAlert(); renderPrediction();
    setInterval(()=>{ updateStats(); renderBuildings(); chartData.shift(); chartData.push(350+Math.sin(Date.now()/5000)*120+Math.random()*40); drawChart(); },4000);
    setInterval(addAlert,6000);
  </script>
 </body>
</html>
