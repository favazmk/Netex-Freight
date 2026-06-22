import re

with open('src/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

mobile_accordion_code = """
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
"""

# 1. Insert mobile_accordion_code before renderServicesHubRail
content = content.replace('// Dynamic left selection buttons for Services Hub\nfunction renderServicesHubRail() {', mobile_accordion_code + 'function renderServicesHubRail() {')

# 2. Add renderServicesMobileAccordion() to initialization
content = content.replace('renderServicesHubRail();\n  selectServiceHubDivision', 'renderServicesHubRail();\n  renderServicesMobileAccordion();\n  selectServiceHubDivision')


with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated JS with mobile accordion.")
