// PURE VANILLA LOGISTIC CONTROLLER - Netex Freight Static Core
// Fully responsive data arrays and DOM binds

// ==========================================
// 1. DATA MODELS & ARRAYS
// ==========================================

const SERVICES_DATA = [
  {
    id: 'air-freight',
    title: 'Air Freight',
    icon: 'plane',
    shortDesc: 'Fast, secure, and reliable air freight services for urgent and time-sensitive cargo worldwide.',
    longDesc: 'Our Air Freight division is custom-engineered to handle precious, time-critical, and highly sensitive goods. By leveraging key commercial gateways and direct air carrier relationships, we provide rapid transits with guaranteed space allocations.',
    image: 'https://images.unsplash.com/photo-1578575437130-527eed3abbec?auto=format&fit=crop&w=1200&q=80',
    bulletPoints: [
      'Express & Next-Flight-Out (NFO) solutions',
      'Temperature-controlled container shipping (active and passive)',
      'Global network of primary and regional airport hubs',
      'Comprehensive airport-to-door transit management',
      'Dangerous goods, oversized machinery, and high-value cargo handling'
    ]
  },
  {
    id: 'sea-freight',
    title: 'Sea Freight',
    icon: 'ship',
    shortDesc: 'Cost-effective global ocean freight solutions including both FCL and LCL container services.',
    longDesc: 'As the bedrock of international trade, our Sea Freight services provide cost-effective scheduling, dependable slot allocations, and seamless cargo handling on all prominent global shipping lanes.',
    image: 'https://images.unsplash.com/photo-1494412574643-ff11b0a5c1c3?auto=format&fit=crop&w=1200&q=80',
    bulletPoints: [
      'Full Container Load (FCL) with contract carrier rates',
      'Less Than Container Load (LCL) consolidation services',
      'Reefer (refrigerated) container operations for perishables',
      'Break Bulk and Roll-on/Roll-off (RoRo) vessels',
      'Intermodal ocean-to-rail and ocean-to-road services'
    ]
  },
  {
    id: 'land-freight',
    title: 'Land Freight',
    icon: 'truck',
    shortDesc: 'Dependable land transportation services across the UAE, GCC countries, and international highways.',
    longDesc: 'Boasting a robust fleet of GPS-tracked, modern, heavy-duty trailers and express delivery vehicles, our Land Freight service bridges major industrial corridors across the UAE and GCC borders.',
    image: 'https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&w=1200&q=80',
    bulletPoints: [
      'Less Than Truckload (LTL) and Full Truckload (FTL) services',
      'GCC-wide cross-border transportation with customs clearance',
      'GPS-tracked heavy-haul fleets with 24/7 telematics monitoring',
      'Curtainside high-volume trailers (110m³ volume standard)',
      'Multi-driver express land transport for fast domestic transits'
    ]
  },
  {
    id: 'packing-solutions',
    title: 'Packing Solutions',
    icon: 'package',
    shortDesc: 'High-quality, secure packaging methods designed to protect sensitive cargo during transit.',
    longDesc: 'From heavy-duty industrial wooden crating to delicate retail shock-absorptive buffering, our professional packing services ensure maximum safety, preventing drop and vibration damage.',
    image: 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1200&q=80',
    bulletPoints: [
      'On-site industrial wood crating and vacuum sealing',
      'ESD anti-static packaging for sophisticated technology',
      'Hazardous material certified compliance boxing',
      'Palletization, shrink wrapping, and load reinforcing',
      'Moisture, shock, and tilt tracking indicator installations'
    ]
  },
  {
    id: 'customs-clearance',
    title: 'Customs Clearance',
    icon: 'file-text',
    shortDesc: 'Smooth and hassle-free import/export customs clearance handled by expert brokers.',
    longDesc: 'We navigate complex local and international customs tariffs and regulations. Our experienced clearance brokers expedite imports and exports through UAE ports easily, minimizing duty obligations.',
    image: 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1200&q=80',
    bulletPoints: [
      'Pre-shipment documentation audit and cargo classification',
      'Harmonized System (HS) code assignment optimization',
      'Duty exemption processing for industrial and raw elements',
      'Customs bond filing and cargo release management',
      'Rapid air-cargo or free-zone clearance specialists'
    ]
  },
  {
    id: 'warehousing',
    title: 'Warehousing & Supply Chain',
    icon: 'database',
    shortDesc: 'Secure, modern inventory warehousing and complete supply chain distribution hubs.',
    longDesc: 'Operate your logistics layout through our secure, temperature-monitored warehouse facilities located strategically within primary transport junctions in Dubai, UAE.',
    image: 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?auto=format&fit=crop&w=1200&q=80',
    bulletPoints: [
      'Ambient, chilled, and frozen storage sections available',
      'WMS inventory management with real-time tracking access',
      'Cross-docking and container de-consolidation actions',
      'Value-added barcoding, labeling, and retail repackaging',
      '24/7 security forces and high-definition CCTV coverage'
    ]
  },
  {
    id: 'project-cargo',
    title: 'Break Bulk & Project Cargo',
    icon: 'anchor',
    shortDesc: 'Professional engineering logistics for out-of-gauge heavy machinery and industrial loads.',
    longDesc: 'When cargo exceeds standard shapes and standard parameters, our special engineering department designs logistics pathways, secures special equipment, and handles the crane maneuvers.',
    image: 'https://images.unsplash.com/photo-1506015391300-4802dc74de2e?auto=format&fit=crop&w=1200&q=80',
    bulletPoints: [
      'Heavy-lift crane cargo handling surveys',
      'Out-Of-Gauge (OOG) container slots booking',
      'Chartering of multi-purpose and breakbulk ocean liners',
      'Industrial relocation and assembly engineering services',
      'Route clearance analysis, escort planning, and multi-modal transfers'
    ]
  }
];

const destinations = [
  { name: 'GLOBAL HUB', id: 'global', loc: [20.0, 45.0], zoom: 2, type: 'Global Network', service: 'Active Multimodal Trade corridors', est: '24/7 Global Dispatch' },
  { name: 'DUBAI (HQ)', id: 'dubai', loc: [25.2048, 55.2708], zoom: 8, type: 'Corporate HQ', service: 'Main Dispatch & Customs Corridor', est: 'Immediate Dispatch' },
  { name: 'LONDON', id: 'london', loc: [51.5074, -0.1278], zoom: 5, type: 'Sea Freight', service: 'European Gateway Channel', est: '7.2 Days Transit' },
  { name: 'NEW YORK', id: 'new_york', loc: [40.7128, -74.0060], zoom: 5, type: 'Priority Air', service: 'North America Trade Link', est: '1.8 Days Transit' },
  { name: 'SINGAPORE', id: 'singapore', loc: [1.3521, 103.8198], zoom: 5, type: 'Fast Sea Link', service: 'Southeast Asia Hub Connect', est: '4.5 Days Transit' },
  { name: 'TOKYO', id: 'tokyo', loc: [35.6762, 139.6503], zoom: 5, type: 'Express Cargo', service: 'East Asia Gateway Terminal', est: '3.1 Days Transit' },
  { name: 'MUMBAI', id: 'mumbai', loc: [19.0760, 72.8777], zoom: 5, type: 'Direct Road/Sea', service: 'Indian Subcontinent Channel', est: '2.8 Days Transit' },
  { name: 'SYDNEY', id: 'sydney', loc: [-33.8688, 151.2093], zoom: 5, type: 'Ocean Consolidations', service: 'Oceania Distribution Hub', est: '9.4 Days Transit' }
];

const INDUSTRIES = [
  { name: 'Manufacturing', icon: 'settings', desc: 'Expediting raw materials, metal parts, assembly units, and industrial products.' },
  { name: 'Retail & E-commerce', icon: 'shopping-cart', desc: 'Warehousing distributions and swift consumer logistics for high-volume traders.' },
  { name: 'Construction', icon: 'hammer', desc: 'Heavy equipment shipments, machinery parts, steel pipes, and out-of-gauge elements.' },
  { name: 'Automotive', icon: 'truck', desc: 'Commercial vehicles chassis, luxury hypercars, and premium wheels transport configurations.' },
  { name: 'Industrial Equipment', icon: 'building-2', desc: 'Moving factory turbines, heavy drill assets, turbines, and large boilers safely.' },
  { name: 'Import & Export Businesses', icon: 'globe', desc: 'Supporting international trading accounts with professional HS customs clearance.' }
];

const INDUSTRIES_SERVED_SUB = [
  {
    name: 'Marine & Offshore Logistics',
    icon: 'anchor',
    desc: 'Supplying floating rigs, machinery elements, marine gear, and dry docks with premium on-time delivery schedules.',
  },
  {
    name: 'Automotive & Logistics',
    icon: 'truck',
    desc: 'Transporting luxury roll-on/roll-off hypercars and bulk commercial vehicle chassis across Middle East borders safely.',
  },
  {
    name: 'Retail & Consumer Goods',
    icon: 'layers',
    desc: 'Handling warehouse distributions, bulk palletization, and swift inventory replenishment hubs in Dubai free zones.',
  },
  {
    name: 'Heavy Industrial Equipment',
    icon: 'tool',
    desc: 'Break bulk project cargo, moving giant excavators, towers, and turbine components with engineered customs escort crews.',
  }
];

const SERVICE_PROCESS_DATA = [
  {
    step: '01',
    title: 'Request a Quote',
    desc: 'Submit your cargo dimensions through our rate estimator or contact our desks. We analyze parameters instantly.'
  },
  {
    step: '02',
    title: 'Cargo Assessment',
    desc: 'Verify container compliance, HS classification codes, customs documentation, and duty exemption certificates.'
  },
  {
    step: '03',
    title: 'Packing Prep',
    desc: 'Secure shrink-wrap packaging, temperature stabilization, and expert crating carried out by terminal workers.'
  },
  {
    step: '04',
    title: 'Transportation',
    desc: 'Smooth transit execution across chosen premium channels (air, ocean vessels, or regional GCC highways).'
  },
  {
    step: '05',
    title: 'Delivery Secure',
    desc: 'Efficient drop-off at target terminal docks or coordinate complete door-to-door cargo final landing.'
  }
];

const WHY_CHOOSE_US_DATA = [
  {
    title: 'Reliable Logistics Partner',
    desc: 'We provide dependable cargo transport services with direct accountability.',
    bullets: ['✓ Professional handling', '✓ Timely delivery']
  },
  {
    title: 'Global Freight Network',
    desc: 'Strong international connections across primary sea shipping and air freight paths.',
    bullets: ['✓ Worldwide connections', '✓ International reach']
  },
  {
    title: 'Competitive Pricing',
    desc: 'Cost-effective consolidated operations (LTL/LCL) matching high-speed criteria.',
    bullets: ['✓ Cost-effective solutions', '✓ Direct fair tariffs']
  },
  {
    title: 'Experienced Team',
    desc: 'A committed team of certified logistics experts and experienced customs brokers.',
    bullets: ['✓ Dedicated experts', '✓ 24/7 dispatch desk']
  }
];

const SIMULATED_WORLD_LINKS = [
  { city: 'Rotterdam (Europe)', x: '46%', y: '18%', code: 'RTM' },
  { city: 'Singapore (Asia East)', x: '75%', y: '65%', code: 'SIN' },
  { city: 'Shanghai (China)', x: '82%', y: '42%', code: 'PVG' },
  { city: 'New York (USA East)', x: '24%', y: '28%', code: 'JFK' },
  { city: 'London (UK)', x: '44%', y: '14%', code: 'LHR' },
  { city: 'Frankfurt (Germany)', x: '48%', y: '20%', code: 'FRA' }
];

// ==========================================
// 2. STATE MANAGER VARIABLES
// ==========================================
let activeServiceId = 'air-freight';
let activeMapHubId = 'global';
let activeStandardsTab = 'why-us';
let activeIndustrySubIdx = 0;
let mapInstance = null;

// ==========================================
// 3. PAGE ROUTER SYSTEM (HASH ROUTING)
// ==========================================
function executePageRouting() {
  const hash = window.location.hash.replace('#', '') || 'home';
  const validPages = ['home', 'about-us', 'services', 'why-choose-us', 'contact-us', 'tracking'];
  const targetPage = validPages.includes(hash) ? hash : 'home';

  // Toggle page-view wrapper visibility
  document.querySelectorAll('.page-view').forEach((view) => {
    view.classList.add('hidden');
    view.classList.remove('block');
  });

  const targetNode = document.getElementById(`page-${targetPage}`);
  if (targetNode) {
    targetNode.classList.remove('hidden');
    targetNode.classList.add('block');
  }

  // Update header navigation active styles
  document.querySelectorAll('nav a').forEach((link) => {
    link.classList.remove('text-brand-blue', 'border-b', 'border-brand-blue', 'font-bold');
  });
  
  const activeDesktopLink = document.getElementById(`nav-${targetPage === 'about-us' ? 'about' : targetPage === 'why-choose-us' ? 'why-us' : targetPage === 'contact-us' ? 'contact' : targetPage}`);
  if (activeDesktopLink) {
    activeDesktopLink.classList.add('text-brand-blue', 'border-b', 'border-brand-blue', 'font-bold');
  }

  // If map needs to refresh its size context when displaying home page
  if (targetPage === 'home' && mapInstance) {
    setTimeout(() => {
      mapInstance.invalidateSize();
    }, 150);
  }

  // Close mobile navigation drawer if open
  const drawer = document.getElementById('mobile-navigation-drawer');
  const burgerIcon = document.getElementById('menu-icon-burger');
  const closeIcon = document.getElementById('menu-icon-close');
  if (drawer && !drawer.classList.contains('hidden')) {
    drawer.classList.add('hidden');
    burgerIcon?.classList.remove('hidden');
    closeIcon?.classList.add('hidden');
  }

  // Scroll to absolute page top
  window.scrollTo({ top: 0, behavior: 'instant' });
}

// ==========================================
// 4. INTERACTIVE LEAFLET MAP HANDLERS
// ==========================================
function initLeafletMap() {
  const mapContainer = document.getElementById('hero-map-frame-container');
  if (!mapContainer || typeof window === 'undefined' || !window.L) return;

  const L = window.L;

  // Cleanup past instances
  if (mapInstance) {
    mapInstance.remove();
    mapInstance = null;
  }

  const dubaiCoords = [25.2048, 55.2708];

  // Config Leaflet map without zoom or scroll friction
  mapInstance = L.map('hero-map-frame-container', {
    zoomControl: false,
    dragging: true,
    scrollWheelZoom: false,
    doubleClickZoom: false,
    boxZoom: false,
    attributionControl: false
  }).setView([20.0, 45.0], 2);

  // Carto Light tiles layer
  L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    maxZoom: 18,
  }).addTo(mapInstance);

  // Dubai Glowing Central Marker divIcon
  const dubaiIcon = L.divIcon({
    html: `
      <div class="relative flex items-center justify-center">
        <span class="absolute inline-flex h-8 w-8 rounded-full bg-brand-blue/30 animate-ping"></span>
        <span class="absolute inline-flex h-5 w-5 rounded-full bg-brand-blue/50 animate-pulse"></span>
        <span class="relative inline-flex rounded-full h-3.5 w-3.5 bg-brand-blue border border-white font-black shadow-[0_0_8px_rgba(15,58,140,0.6)]"></span>
      </div>
    `,
    className: 'custom-map-marker-dubai',
    iconSize: [24, 24],
    iconAnchor: [12, 12]
  });

  L.marker(dubaiCoords, { icon: dubaiIcon })
    .addTo(mapInstance)
    .bindTooltip(`
      <div class="bg-white border border-brand-blue/50 p-2 text-zinc-900 uppercase tracking-wider font-sans text-[10px]">
        <div class="text-brand-blue font-bold">// NETEX GLOBAL HQ</div>
        <div class="text-zinc-950 font-bold mt-0.5">DUBAI CORE TERMINAL</div>
      </div>
    `, {
      className: 'custom-map-tooltip',
      direction: 'top',
      permanent: true,
      opacity: 0.95
    });

  // Plot Destination networks
  destinations.forEach((city) => {
    if (city.id === 'global' || city.id === 'dubai') return;

    const cityIcon = L.divIcon({
      html: `
        <div class="relative flex items-center justify-center">
          <span class="absolute inline-flex h-3.5 w-3.5 rounded-full bg-brand-blue/15 animate-ping"></span>
          <span class="relative inline-flex rounded-full h-2 w-2 bg-white border border-brand-blue"></span>
        </div>
      `,
      className: 'custom-map-marker-city',
      iconSize: [16, 16],
      iconAnchor: [8, 8]
    });

    L.marker(city.loc, { icon: cityIcon })
      .addTo(mapInstance)
      .bindTooltip(`
        <div class="bg-white border border-zinc-200 p-1.5 font-sans text-[9px] text-zinc-900 uppercase tracking-widest">
          <div class="text-zinc-950 font-bold">${city.name}</div>
        </div>
      `, {
        className: 'custom-map-tooltip-city',
        direction: 'bottom',
        opacity: 0.95
      });

    // Create polyline trade path from Dubai to location
    L.polyline([dubaiCoords, city.loc], {
      color: '#011d50',
      weight: 1.5,
      opacity: 0.75,
      className: 'map-route-line',
      lineCap: 'round',
      lineJoin: 'round'
    }).addTo(mapInstance);
  });

  // Hotkey sliding buttons creator
  renderMapSliderControls();
  
  setTimeout(() => {
    mapInstance.invalidateSize();
  }, 300);
}

function renderMapSliderControls() {
  const container = document.getElementById('map-nav-slider-hubs');
  if (!container) return;

  container.innerHTML = '';
  destinations.forEach((dest) => {
    const btn = document.createElement('button');
    btn.className = `px-3 py-1.5 font-sans text-[9px] tracking-widest uppercase transition-all shrink-0 rounded-sm cursor-pointer border ${
      activeMapHubId === dest.id 
        ? 'bg-brand-blue text-white font-bold shadow-[0_0_10px_rgba(15,58,140,0.4)] border-brand-blue' 
        : 'bg-zinc-100 text-zinc-600 hover:text-zinc-900 border-zinc-200 hover:border-zinc-300'
    }`;
    btn.textContent = dest.name.replace(' PORT', '');
    btn.addEventListener('click', () => triggerMapFly(dest));
    container.appendChild(btn);
  });
}

function triggerMapFly(dest) {
  activeMapHubId = dest.id;
  renderMapSliderControls();

  // Dynamically update terminal feed card
  const feedCity = document.getElementById('terminal-feed-city');
  const feedService = document.getElementById('terminal-feed-service');
  const feedType = document.getElementById('terminal-feed-type');
  const feedEst = document.getElementById('terminal-feed-est');

  if (feedCity) feedCity.textContent = dest.name;
  if (feedService) feedService.textContent = dest.service;
  if (feedType) feedType.textContent = dest.type;
  if (feedEst) feedEst.textContent = dest.est;

  if (mapInstance) {
    mapInstance.flyTo(dest.loc, dest.zoom, {
      animate: true,
      duration: 1.5
    });
  }
}

// ==========================================
// 5. RENDERING STATIC BLOCKS DYNAMICALLY
// ==========================================

// Render 4 Why Choose Us Cards on Home Tab
function renderWhyChooseUsCards() {
  const container = document.getElementById('why-us-grid-container');
  const pageContainer = document.getElementById('why-choose-page-grid');

  const cardHtml = WHY_CHOOSE_US_DATA.map((item, idx) => `
    <div class="p-6 bg-white border border-zinc-200 rounded-sm relative overflow-hidden group hover:border-brand-blue transition-all cursor-default shadow-xs z-10">
      <div class="absolute top-0 left-0 w-1 h-full bg-zinc-200 group-hover:bg-brand-blue transition-colors"></div>
      <div class="w-10 h-10 rounded-full bg-zinc-50 border border-zinc-200 flex items-center justify-center text-brand-blue mb-5 font-mono text-xs font-bold shadow-xs">
        0${idx + 1}
      </div>
      <h4 class="font-mono text-xs font-bold tracking-wider uppercase text-zinc-900 mb-2.5">${item.title}</h4>
      <p class="text-zinc-600 text-xs leading-relaxed font-sans mb-4">${item.desc}</p>
      <div class="pt-2 border-t border-zinc-100 flex flex-col gap-1">
        ${item.bullets.map(b => `<span class="font-mono text-[10px] text-brand-blue font-bold tracking-tight">${b}</span>`).join('')}
      </div>
    </div>
  `).join('');

  if (container) container.innerHTML = cardHtml;
  if (pageContainer) pageContainer.innerHTML = cardHtml;
}

// Render dynamic process timelines (3 cards)
function renderProcessTimeline() {
  const container = document.getElementById('process-timeline-container');
  const pageContainer = document.getElementById('about-page-workflow-timeline');

  // Sub-group items
  const timelineHtml = SERVICE_PROCESS_DATA.map((item) => `
    <div class="p-6 bg-white border border-zinc-200 rounded-sm relative overflow-hidden flex flex-col justify-between min-h-[200px] group hover:border-brand-blue transition-all cursor-default shadow-xs z-10">
      <div class="absolute -right-2 -top-5 font-mono text-8xl font-black text-zinc-100/70 select-none pointer-events-none -z-10">
        ${item.step}
      </div>
      <div class="relative z-10 space-y-3">
        <span class="font-mono text-[9px] text-brand-blue font-bold tracking-widest block">// ROADMAP PHASE ${item.step}</span>
        <h4 class="font-mono text-xs uppercase text-zinc-900 font-bold tracking-wider">${item.title}</h4>
        <p class="text-zinc-600 text-xs leading-relaxed font-sans pr-4">${item.desc}</p>
      </div>
      <div class="mt-5 flex items-center gap-1.5 text-[10px] font-mono text-brand-blue group-hover:translate-x-1 transition-transform">
        <span>NEXT DISPATCH PHASE</span>
        <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
      </div>
    </div>
  `).join('');

  if (container) container.innerHTML = timelineHtml;

  const pipelineHtml = SERVICE_PROCESS_DATA.map((item, index) => `
    <div class="relative z-10 flex flex-col items-start md:items-center text-left md:text-center animate-fade-in pb-4">
      <div class="w-14 h-14 bg-white border border-white hover:border-blue-100 rounded-full flex items-center justify-center text-brand-blue font-mono text-sm font-black transition-colors md:mx-auto mb-4 relative shadow-xs z-10">
        ${item.step}
        <div class="absolute inset-1 rounded-full border border-brand-blue/10"></div>
      </div>
      <h4 class="font-mono text-xs font-bold text-white uppercase tracking-wider mb-2 md:max-w-[145px] md:mx-auto relative z-10">
        ${item.title}
      </h4>
      <p class="text-white opacity-80 text-xs leading-relaxed font-sans md:mx-auto md:max-w-[190px] relative z-10">
        ${item.desc}
      </p>
    </div>
  `).join('');

  if (pageContainer) {
    pageContainer.innerHTML = `
      ${pipelineHtml}
    `;
  }
}

// Sub-industries Tab panel renderer Inside corporate grid
function renderIndustriesTabSwitcher() {
  const listContainer = document.getElementById('industry-tab-selector-list');
  if (!listContainer) return;

  listContainer.innerHTML = '';
  INDUSTRIES_SERVED_SUB.forEach((ind, idx) => {
    const btn = document.createElement('button');
    btn.className = `p-3 text-left rounded-sm border font-mono text-xs flex items-center justify-between transition-all cursor-pointer ${
      activeIndustrySubIdx === idx 
        ? 'bg-brand-blue/10 border-brand-blue text-brand-blue font-bold' 
        : 'bg-white border-zinc-200 text-zinc-600 hover:text-brand-blue'
    }`;
    btn.innerHTML = `
      <span class="truncate pr-2">${ind.name}</span>
      <i data-lucide="chevron-right" class="w-3.5 h-3.5 shrink-0"></i>
    `;
    btn.addEventListener('click', () => {
      activeIndustrySubIdx = idx;
      renderIndustriesTabSwitcher();
      // Update details card
      const showTitle = document.getElementById('ind-showcase-title');
      const showDesc = document.getElementById('ind-showcase-desc');
      if (showTitle) showTitle.textContent = ind.name;
      if (showDesc) showDesc.textContent = ind.desc;
    });
    listContainer.appendChild(btn);
  });
  if (window.lucide) window.lucide.createIcons();
}

// Render 6 industries grids on home/why-us
function renderIndustriesGrid() {
  const container = document.getElementById('industries-serve-grid');
  const pageContainer = document.getElementById('why-choose-page-industries-grid');

  const html = INDUSTRIES.map((ind) => `
    <div class="bg-zinc-50 border border-zinc-200 p-6 rounded-sm hover:border-brand-blue/60 transition-colors flex gap-4 items-start cursor-default shadow-sm">
      <div class="p-2.5 bg-white border border-zinc-200 rounded-sm text-brand-blue shadow-xs shrink-0">
        <i data-lucide="${ind.icon}" class="w-5 h-5"></i>
      </div>
      <div class="space-y-2">
        <h4 class="font-mono text-xs font-bold uppercase text-zinc-900 tracking-wider">
          ${ind.name}
        </h4>
        <p class="text-zinc-650 text-xs leading-relaxed font-sans">
          ${ind.desc}
        </p>
      </div>
    </div>
  `).join('');

  if (container) container.innerHTML = html;
  if (pageContainer) pageContainer.innerHTML = html;
}

// Render dynamic workflow timelines
function renderWorkflowTimelineRow() {
  const container = document.getElementById('global-workflow-section-timeline');
  if (!container) return;

  container.innerHTML = `
    <div class="hidden md:block absolute top-[28px] left-[10%] right-[10%] h-px bg-zinc-200 -z-0"></div>
    ${SERVICE_PROCESS_DATA.map((step, index) => `
      <div class="relative z-10 flex flex-col items-start md:items-center text-left md:text-center animate-fade-in pb-4">
        <div class="w-14 h-14 bg-zinc-50 border border-zinc-200 hover:border-brand-blue rounded-full flex items-center justify-center text-brand-blue font-mono text-sm font-black transition-colors md:mx-auto mb-4 relative shadow-xs z-10">
          ${step.step}
          <div class="absolute inset-1 rounded-full border border-brand-blue/10"></div>
        </div>
        <h4 class="font-mono text-xs font-bold text-zinc-900 uppercase tracking-wider mb-2 md:max-w-[140px] md:mx-auto relative z-10">
          ${step.title}
        </h4>
        <p class="text-zinc-500 text-xs leading-relaxed font-sans md:mx-auto md:max-w-[190px] relative z-10">
          ${step.desc}
        </p>
      </div>
    `).join('')}
  `;
}

// ==========================================
// 6. SERVICES HUB INTERACTIVE SWITCHERS
// ==========================================
function renderServicesGrid() {
  const gridHome = document.getElementById('services-summary-grid');
  const gridPage = document.getElementById('services-page-summary-grid');

  const cardHtml = SERVICES_DATA.map((srv) => `
    <div class="bg-zinc-50 border border-zinc-200 rounded-sm p-6 hover:border-brand-blue transition-all flex flex-col justify-between group cursor-default shadow-sm">
      <div class="space-y-4">
        <div class="w-10 h-10 rounded-full bg-white border border-zinc-200 flex items-center justify-center text-brand-blue group-hover:text-white group-hover:bg-brand-blue transition-colors shadow-xs">
          <i data-lucide="${srv.icon}" class="w-4.5 h-4.5"></i>
        </div>
        <h3 class="font-mono text-xs font-bold uppercase text-zinc-900 tracking-wider">
          ${srv.title}
        </h3>
        <p class="text-zinc-650 text-xs leading-relaxed font-sans">
          ${srv.shortDesc}
        </p>
      </div>

      <div class="mt-6 pt-4 border-t border-zinc-200 flex justify-end">
        <button
          onclick="window.openServiceHubDivision('${srv.id}')"
          class="text-[10px] font-mono font-bold text-brand-blue hover:text-brand-blue-hover flex items-center gap-1 uppercase transition-colors cursor-pointer"
        >
          <span>Learn More</span>
          <i data-lucide="arrow-right" class="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform"></i>
        </button>
      </div>
    </div>
  `).join('');

  if (gridHome) gridHome.innerHTML = cardHtml;
  if (gridPage) gridPage.innerHTML = cardHtml;
}


// State for mobile accordion
let activeMobileServiceId = null;

function toggleMobileServiceHub(id) {
  activeMobileServiceId = (activeMobileServiceId === id) ? null : id;
  renderServicesMobileAccordion();
}

function renderServicesMobileAccordion() {
  const container = document.getElementById('services-mobile-accordion');
  if (!container) return;
  
  container.innerHTML = '';
  SERVICES_DATA.forEach((srv) => {
    const isExpanded = activeMobileServiceId === srv.id;
    
    // Create button header
    const btn = document.createElement('button');
    btn.id = `mobile-accordion-${srv.id}`;
    btn.className = `w-full p-4 rounded-sm text-left font-mono text-xs flex items-center justify-between border cursor-pointer transition-all duration-200 ${
      isExpanded
        ? 'bg-brand-blue border-brand-blue text-white font-bold'
        : 'bg-white border-zinc-200 text-zinc-600 hover:text-brand-blue hover:bg-zinc-50'
    }`;
    
    btn.innerHTML = `
      <div class="flex items-center gap-3.5">
        <div class="w-9 h-9 rounded-full flex items-center justify-center shrink-0 border transition-colors ${
          isExpanded ? 'bg-zinc-100 border-white text-zinc-950' : 'bg-zinc-100 border-zinc-200 text-zinc-500'
        }">
          <i data-lucide="${srv.icon}" class="w-4 h-4"></i>
        </div>
        <span class="text-xs uppercase tracking-widest">${srv.title}</span>
      </div>
      <i data-lucide="${isExpanded ? 'chevron-up' : 'chevron-down'}" class="w-4 h-4 transition-transform"></i>
    `;
    
    btn.addEventListener('click', () => {
      toggleMobileServiceHub(srv.id);
    });
    container.appendChild(btn);

    // Create Details Panel if expanded
    if (isExpanded) {
      const panel = document.createElement('div');
      panel.className = 'bg-white border border-t-0 border-zinc-200 rounded-b-sm p-5 md:p-6 mb-2 animate-fade-in shadow-sm -mt-1 space-y-5';
      
      panel.innerHTML = `
        <!-- Image Banner -->
        <div class="h-40 relative overflow-hidden rounded-sm w-full">
          <div class="absolute inset-0 bg-gradient-to-t from-white via-white/20 to-transparent z-10"></div>
          <img src="${srv.image}" alt="${srv.title}" class="w-full h-full object-cover" />
        </div>
        
        <div class="space-y-2">
          <span class="text-[9px] font-mono text-brand-blue uppercase tracking-widest font-semibold block">// CARRIER DIVISION CHARTER</span>
          <p class="text-sm font-display text-zinc-800 font-bold leading-relaxed">${srv.shortDesc}</p>
        </div>
        
        <p class="text-zinc-500 text-xs leading-relaxed font-sans">${srv.longDesc}</p>
        
        <div class="space-y-3 pt-2 border-t border-zinc-100">
          <h4 class="text-[10px] font-mono text-zinc-500 uppercase tracking-wider font-semibold">Service Parameters</h4>
          <div class="flex flex-col gap-2">
            ${srv.bulletPoints.map(point => `
              <div class="flex items-start gap-2 text-xs text-zinc-600">
                <i data-lucide="check" class="w-3.5 h-3.5 text-brand-blue mt-0.5 shrink-0"></i>
                <span class="font-sans leading-relaxed">${point}</span>
              </div>
            `).join('')}
          </div>
        </div>
        
        <a href="#contact-us" class="mt-4 px-6 py-3 bg-brand-blue hover:bg-brand-blue-hover font-mono text-[10px] font-bold text-white uppercase tracking-widest transition-colors rounded-sm shadow-xs inline-flex items-center gap-2 w-full justify-center">
          Get Custom Quote <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
        </a>
      `;
      
      container.appendChild(panel);
    }
  });
  
  if (window.lucide) window.lucide.createIcons();
}

// Dynamic left selection buttons for Services Hub
function renderServicesHubRail() {
  const container = document.getElementById('services-hubs-button-rail');
  if (!container) return;

  container.innerHTML = '';
  SERVICES_DATA.forEach((srv) => {
    const isSelected = activeServiceId === srv.id;
    const btn = document.createElement('button');
    btn.className = `w-full p-4 rounded-sm text-left font-mono text-xs flex items-center justify-between border cursor-pointer transition-all duration-200 ${
      isSelected
        ? 'bg-brand-blue border-brand-blue text-white font-bold'
        : 'bg-white border-zinc-200 text-zinc-600 hover:text-brand-blue hover:bg-zinc-50'
    }`;
    
    // Circle Preview thumb inner structure
    btn.innerHTML = `
      <div class="flex items-center gap-3.5">
        <div class="w-9 h-9 rounded-full flex items-center justify-center shrink-0 border transition-colors ${
          isSelected ? 'bg-zinc-100 border-white text-zinc-950' : 'bg-zinc-100 border-zinc-200 text-zinc-500'
        }">
          <i data-lucide="${srv.icon}" class="w-4 h-4"></i>
        </div>
        <span class="text-xs uppercase tracking-widest">${srv.title}</span>
      </div>
      <i data-lucide="chevron-right" class="w-4 h-4 transition-transform ${isSelected ? 'translate-x-1' : 'opacity-30'}"></i>
    `;

    btn.addEventListener('click', () => {
      selectServiceHubDivision(srv.id);
    });
    container.appendChild(btn);
  });
  if (window.lucide) window.lucide.createIcons();
}

// Show selected division profile right details showcase panel
function selectServiceHubDivision(id) {
  activeServiceId = id;
  renderServicesHubRail();

  const board = document.getElementById('service-details-board-viewport');
  if (!board) return;

  const currentItem = SERVICES_DATA.find(s => s.id === id) || SERVICES_DATA[0];

  // Render specifications layout inside Board view with a transition feel
  board.innerHTML = `
    <!-- Image Top Banner -->
    <div class="h-56 relative overflow-hidden group border-b border-zinc-200 w-full">
      <div class="absolute inset-0 bg-gradient-to-t from-white via-white/20 to-transparent z-10"></div>
      <img 
         src="${currentItem.image}" 
         alt="${currentItem.title}" 
         class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
         referrerPolicy="no-referrer"
      />
      <div class="absolute bottom-5 left-6 z-20 flex items-center gap-3">
        <div class="w-8 h-8 rounded-full bg-brand-blue flex items-center justify-center text-white">
          <i data-lucide="${currentItem.icon}" class="w-4 h-4"></i>
        </div>
        <h3 class="font-display text-xl md:text-2xl font-black text-zinc-950 tracking-tight uppercase">
          ${currentItem.title}
        </h3>
      </div>
    </div>

    <!-- Specifications Content Columns -->
    <div class="p-6 md:p-8 space-y-6 flex-grow flex flex-col justify-center animate-fade-in">
      
      <div class="space-y-2">
        <span class="text-[9px] font-mono text-brand-blue uppercase tracking-widest font-semibold block">// CARRIER DIVISION CHARTER STATEMENT</span>
        <p class="text-base font-display text-zinc-800 font-bold leading-relaxed">
          ${currentItem.shortDesc}
        </p>
        <div class="h-px w-full bg-zinc-200 mt-2"></div>
      </div>

      <div class="space-y-2">
        <h4 class="text-[10px] font-mono text-zinc-500 uppercase tracking-wider font-semibold">Division Logistics Profile</h4>
        <p class="text-zinc-650 text-xs md:text-sm leading-relaxed font-sans text-zinc-500">
          ${currentItem.longDesc}
        </p>
      </div>

      <!-- Bullet points Targets checklist -->
      <div class="space-y-3 pt-2">
        <h4 class="text-[10px] font-mono text-zinc-500 uppercase tracking-wider font-semibold">Service Parameters & Dubai SLA Targets</h4>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-x-4 gap-y-2">
          ${currentItem.bulletPoints.map(point => `
            <div class="flex items-start gap-2 text-xs text-zinc-600">
              <div class="mt-1.5 w-1.5 h-1.5 rounded-full bg-brand-blue shrink-0"></div>
              <span class="font-sans text-[11px] leading-relaxed text-zinc-500">${point}</span>
            </div>
          `).join('')}
        </div>
      </div>

    </div>

    <!-- Bottom verification status tag strip -->
    <div class="p-5 bg-zinc-50 border-t border-zinc-200 flex flex-col sm:flex-row sm:items-center justify-between gap-4 text-xs font-mono">
      <span class="text-zinc-500">
        DISPATCH DIVISION: <strong class="text-brand-blue uppercase">ACTIVE ONLINE</strong>
      </span>
    </div>
  `;
  
  if (window.lucide) window.lucide.createIcons();
}

// Select active tabs under "Operational Standards" (About Segment)
function setupOperationalStandardsTabs() {
  document.querySelectorAll('.tab-btn-selector').forEach((btn) => {
    btn.addEventListener('click', (e) => {
      const targetBtn = e.currentTarget;
      const tabName = targetBtn.getAttribute('data-tab');
      if (!tabName) return;

      activeStandardsTab = tabName;

      // Update button selectors active styling classes
      document.querySelectorAll('.tab-btn-selector').forEach((el) => {
        el.classList.remove('bg-brand-blue', 'text-white', 'font-bold');
        el.classList.add('text-zinc-600', 'hover:text-brand-blue');
      });
      targetBtn.classList.add('bg-brand-blue', 'text-white', 'font-bold');
      targetBtn.classList.remove('text-zinc-600', 'hover:text-brand-blue');

      // Update content panel blocks visibility
      document.querySelectorAll('.tab-panel-block').forEach((panel) => {
        panel.classList.add('hidden');
        panel.classList.remove('block');
      });

      const activePanel = document.getElementById(`tab-panel-${tabName}`);
      if (activePanel) {
        activePanel.classList.remove('hidden');
        activePanel.classList.add('block');
      }
    });
  });
}

// ==========================================
// 7. BEZIER INTERACTIVE TRAJECTORIES SVG LINES
// ==========================================
function renderSVGPathHotspots() {
  const container = document.getElementById('trajectory-hotspots-container');
  if (!container) return;

  container.innerHTML = '';
  SIMULATED_WORLD_LINKS.forEach((link, idx) => {
    const button = document.createElement('button');
    button.className = "absolute p-1 cursor-pointer flex flex-col items-center group z-15";
    button.style.left = link.x;
    button.style.top = link.y;
    button.style.transform = "translate(-50%, -50%)";

    button.innerHTML = `
      <div class="w-3 h-3 rounded-full border border-white bg-brand-blue/65 transition-all duration-300 group-hover:bg-brand-blue group-hover:scale-125 hover-circle-node" data-idx="${idx}"></div>
      <span class="hidden group-hover:block absolute top-4 bg-white border border-zinc-200 text-[9px] font-mono py-1 px-2 rounded-sm whitespace-nowrap text-zinc-900 z-50 shadow-xl">
        ${link.city} (${link.code})
      </span>
    `;

    // High fidelity path hover binds
    button.addEventListener('mouseenter', () => spotlightTrajectoryLine(idx));
    button.addEventListener('mouseleave', () => clearTrajectoryLinesHighlight());

    container.appendChild(button);
  });
}

function spotlightTrajectoryLine(hoveredIdx) {
  const paths = document.querySelectorAll('.active-vector-trajectory');
  paths.forEach((pathNode) => {
    const idxAttr = pathNode.getAttribute('data-idx');
    if (idxAttr === String(hoveredIdx)) {
      pathNode.classList.remove('opacity-20');
      pathNode.classList.add('opacity-100', 'stroke-2', 'stroke-brand-blue');
    } else {
      pathNode.classList.add('opacity-10');
      pathNode.classList.remove('opacity-20', 'opacity-100');
    }
  });

  // Circle nodes
  document.querySelectorAll('.hover-circle-node').forEach((circleNode) => {
    const targetIdx = circleNode.getAttribute('data-idx');
    if (targetIdx === String(hoveredIdx)) {
      circleNode.classList.add('bg-brand-blue', 'scale-125');
      circleNode.classList.remove('bg-brand-blue/65');
    }
  });
}

function clearTrajectoryLinesHighlight() {
  const paths = document.querySelectorAll('.active-vector-trajectory');
  paths.forEach((pathNode) => {
    pathNode.classList.add('opacity-20');
    pathNode.classList.remove('opacity-10', 'opacity-100', 'stroke-2', 'stroke-brand-blue');
  });

  document.querySelectorAll('.hover-circle-node').forEach((circleNode) => {
    circleNode.classList.remove('bg-brand-blue', 'scale-125');
    circleNode.classList.add('bg-brand-blue/65');
  });
}

// ==========================================
// 8. CONTACT SUBMISSIONS DESKTOP INQUIRY
// ==========================================
function setupContactForms() {
  const form = document.getElementById('contact-inquiry-direct-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const name = document.getElementById('inquiry-field-name')?.value;
    const email = document.getElementById('inquiry-field-email')?.value;
    const phone = document.getElementById('inquiry-field-phone')?.value;
    const message = document.getElementById('inquiry-field-message')?.value;

    if (!name || !email || !phone || !message) {
      alert('Kindly fill out all dispatch message metrics.');
      return;
    }

    // Build JSON payload for FormSubmit
    const payload = {
      name: name,
      email: email,
      phone: phone,
      message: message,
      _subject: "New Inquiry from Netex Freight Website!"
    };

    // Show loading state on button
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalBtnText = submitBtn.innerText;
    submitBtn.innerText = "SENDING...";
    submitBtn.disabled = true;

    // Send via FormSubmit AJAX
    fetch("https://formsubmit.co/ajax/info@netexfreight.com", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(payload)
    })
    .then(response => response.json())
    .then(data => {
      submitBtn.innerText = originalBtnText;
      submitBtn.disabled = false;
      
      // Show success message
      const successAlert = document.getElementById('contact-form-success-alert');
      if (successAlert) {
        successAlert.classList.remove('hidden');
      }
      form.reset();
      
      // Note: First time submission requires email activation.
      if(data.success === "false" || (data.message && data.message.includes("activate"))) {
        alert("Action Required: Please check info@netexfreight.com to activate this form!");
      }
    })
    .catch(error => {
      submitBtn.innerText = originalBtnText;
      submitBtn.disabled = false;
      alert("There was an error sending your inquiry. Please try again.");
      console.log(error);
    });



    // Auto dismiss after 5 seconds
    setTimeout(() => {
      const successAlert = document.getElementById('contact-form-success-alert');
      if (successAlert) {
        successAlert.classList.add('hidden');
      }
    }, 5500);
  });
}



// ==========================================
// 9. BROCHURE PDF PREVIEW MODAL
// ==========================================
function setupBrochureModalControls() {
  const modal = document.getElementById('brochure-modal');
  const modalCard = document.getElementById('brochure-modal-card');
  const revealBtn = document.getElementById('btn-brochure-modal-reveal');
  const closeBtn = document.getElementById('btn-brochure-modal-close');
  const dismissBtn = document.getElementById('btn-brochure-modal-dismiss');
  const simulateBtn = document.getElementById('btn-simulate-download');

  const openModal = () => {
    if (!modal || !modalCard) return;
    modal.classList.remove('hidden');
    // Tick delay to execute CSS frame states smoothly
    setTimeout(() => {
      modal.classList.remove('opacity-0');
      modal.classList.add('opacity-100');
      modalCard.classList.remove('scale-95');
      modalCard.classList.add('scale-100');
    }, 15);
    document.body.classList.add('overflow-hidden');
  };

  const closeModal = () => {
    if (!modal || !modalCard) return;
    modal.classList.add('opacity-0');
    modal.classList.remove('opacity-100');
    modalCard.classList.add('scale-95');
    modalCard.classList.remove('scale-100');
    
    // Hidden execution delayed till fade finishes
    setTimeout(() => {
      modal.classList.add('hidden');
    }, 300);
    document.body.classList.remove('overflow-hidden');
  };

  revealBtn?.addEventListener('click', openModal);
  closeBtn?.addEventListener('click', closeModal);
  dismissBtn?.addEventListener('click', closeModal);
  modal?.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  simulateBtn?.addEventListener('click', () => {
    alert('Thank you for downloading the official NEFTEX Freight digital brief copy (PDF Mock simulation). Contact our Dubai dispatch desk for active routing manifests.');
    closeModal();
  });
}

// ==========================================
// 10. MOBILE HAMBURGER MENU HANDLER
// ==========================================
function setupMobileMenu() {
  const toggleBtn = document.getElementById('mobile-menu-toggle-btn');
  const drawer = document.getElementById('mobile-navigation-drawer');
  const burgerIcon = document.getElementById('menu-icon-burger');
  const closeIcon = document.getElementById('menu-icon-close');

  if (!toggleBtn || !drawer) return;

  toggleBtn.addEventListener('click', () => {
    const isHidden = drawer.classList.contains('hidden');
    if (isHidden) {
      drawer.classList.remove('hidden');
      burgerIcon?.classList.add('hidden');
      closeIcon?.classList.remove('hidden');
    } else {
      drawer.classList.add('hidden');
      burgerIcon?.classList.remove('hidden');
      closeIcon?.classList.add('hidden');
    }
  });

  // Mobile menu items click dismiss
  document.querySelectorAll('.mobile-nav-link').forEach((link) => {
    link.addEventListener('click', () => {
      drawer.classList.add('hidden');
      burgerIcon?.classList.remove('hidden');
      closeIcon?.classList.add('hidden');
    });
  });

  // Close mobile menu when clicking or touching outside of it
  const closeMenuOnOutsideInteraction = (event) => {
    if (!drawer.classList.contains('hidden') && 
        !drawer.contains(event.target) && 
        !toggleBtn.contains(event.target)) {
      drawer.classList.add('hidden');
      burgerIcon?.classList.remove('hidden');
      closeIcon?.classList.add('hidden');
    }
  };

  document.addEventListener('click', closeMenuOnOutsideInteraction);
  document.addEventListener('touchstart', closeMenuOnOutsideInteraction, { passive: true });

  // Close mobile menu when scrolling the page
  const closeMenuOnScroll = () => {
    if (!drawer.classList.contains('hidden')) {
      drawer.classList.add('hidden');
      burgerIcon?.classList.remove('hidden');
      closeIcon?.classList.add('hidden');
    }
  };

  window.addEventListener('scroll', closeMenuOnScroll, { passive: true });
  document.addEventListener('touchmove', closeMenuOnScroll, { passive: true });
}

// Scroll navigation back to top shortcut
function setupScrollToTopButton() {
  const btn = document.getElementById('btn-scroll-top-navigation');
  btn?.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

// Bind direct navigation learn more clicks from grid to Services selection
window.selectServiceHubDivision = selectServiceHubDivision;

// ==========================================
// 11. INITIALIZATION DISPATCH DESK
// ==========================================
document.addEventListener('DOMContentLoaded', () => {
  // Page hash-routers listening
  window.addEventListener('hashchange', executePageRouting);

  // Handle clicking links that point to the current active page
  document.querySelectorAll('a[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
      const targetHash = link.getAttribute('href').replace('#', '') || 'home';
      const currentHash = window.location.hash.replace('#', '') || 'home';
      
      if (targetHash === currentHash) {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
        
        // Also ensure mobile menu is closed
        const drawer = document.getElementById('mobile-navigation-drawer');
        const burgerIcon = document.getElementById('menu-icon-burger');
        const closeIcon = document.getElementById('menu-icon-close');
        if (drawer && !drawer.classList.contains('hidden')) {
          drawer.classList.add('hidden');
          burgerIcon?.classList.remove('hidden');
          closeIcon?.classList.add('hidden');
        }
      }
    });
  });

  // Initial routers execute
  executePageRouting();

  // Rendering static grids & timeline components
  renderWhyChooseUsCards();
  renderProcessTimeline();
  setupOperationalStandardsTabs();
  renderIndustriesTabSwitcher();
  renderIndustriesGrid();
  renderWorkflowTimelineRow();
  renderServicesGrid();
  renderServicesHubRail();
  renderServicesMobileAccordion();
  selectServiceHubDivision('air-freight');

  // Interactive vectors mapping
  renderSVGPathHotspots();

  // Dialog Brochure modals controls
  setupBrochureModalControls();

  // Contact form triggers
  setupContactForms();

  // Sticky Widget Logic
  const stickyBtn = document.getElementById('sticky-contact-btn');
  const stickyMenu = document.getElementById('sticky-contact-menu');
  const iconHeadphones = document.getElementById('sticky-icon-headphones');
  const iconClose = document.getElementById('sticky-icon-close');

  if (stickyBtn && stickyMenu) {
    stickyBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      stickyMenu.classList.toggle('hidden');
      stickyMenu.classList.toggle('flex');
      iconHeadphones.classList.toggle('hidden');
      iconClose.classList.toggle('hidden');
    });

    document.addEventListener('click', (e) => {
      if (!stickyBtn.contains(e.target) && !stickyMenu.contains(e.target)) {
        if (!stickyMenu.classList.contains('hidden')) {
          stickyMenu.classList.add('hidden');
          stickyMenu.classList.remove('flex');
          iconHeadphones.classList.remove('hidden');
          iconClose.classList.add('hidden');
        }
      }
    });
  }

  // Duplication bindings for separate pages


  // Mobile and utility menus
  setupMobileMenu();
  setupScrollToTopButton();

  // Leaflet.js mapping activations
  initLeafletMap();

  // Complete Lucide Icons parsing
  if (window.lucide) {
    window.lucide.createIcons();
  }
});


// Global function to open a service from anywhere
window.openServiceHubDivision = function(id) {
  // Navigate to services page
  window.location.hash = '#services';
  
  // Set desktop active ID
  if (typeof selectServiceHubDivision === 'function') {
    selectServiceHubDivision(id);
  }
  
  // Set mobile active ID to open the accordion
  if (typeof activeMobileServiceId !== 'undefined') {
    activeMobileServiceId = id;
    if (typeof renderServicesMobileAccordion === 'function') {
      renderServicesMobileAccordion();
    }
  }
  
  // Scroll to precise interactive element depending on layout size
  setTimeout(() => {
    if (window.innerWidth < 1024) {
      // Mobile: scroll the specific opened accordion panel into the center of the screen
      const mobileItem = document.getElementById(`mobile-accordion-${id}`);
      if (mobileItem) {
        mobileItem.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    } else {
      // Desktop: scroll the interactive hub board into the center of the screen
      const desktopHub = document.getElementById('services-desktop-hub');
      if (desktopHub) {
        desktopHub.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  }, 100);
};


document.addEventListener('DOMContentLoaded', () => {
    // Automatically apply reveal animation to all major sections
    document.querySelectorAll('section').forEach(sec => sec.classList.add('reveal-step'));

    const steps = document.querySelectorAll('.reveal-step');
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                entry.target.classList.add('revealed');
                observer.unobserve(entry.target); // Only animate once per load
            }
        });
    }, { threshold: 0.12 });

    steps.forEach((step) => {
        observer.observe(step);
    });
});

// Fancy Parallax Scroll Effects for Hero Headings
document.addEventListener('DOMContentLoaded', () => {
    const bgText = document.querySelector('.hero-bg-text');
    const bottomHeadline = document.querySelector('.hero-bottom-headline');
    const containerImg = document.querySelector('.hero-container-img');
    
    let ticking = false;
    
    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                const scrolled = window.scrollY;
                
                // Parallax the giant background text (moves up faster, keeping its centering)
                if (bgText) {
                    bgText.style.transform = `translate(-50%, -50%) translateY(${scrolled * 0.35}px)`;
                }
                
                // Parallax the bottom headline (fades out, moves up and slightly scales down)
                if (bottomHeadline) {
                    bottomHeadline.style.transform = `translateX(-50%) translateY(${scrolled * 0.15}px) scale(${Math.max(0.85, 1 - scrolled * 0.0004)})`;
                    bottomHeadline.style.opacity = Math.max(0, 1 - scrolled * 0.0015);
                }
                
                // Float the 3D container up slightly
                if (containerImg) {
                    containerImg.style.transform = `translate(-50%, -45%) translateY(${scrolled * 0.1}px)`;
                }
                
                ticking = false;
            });
            ticking = true;
        }
    });
});
