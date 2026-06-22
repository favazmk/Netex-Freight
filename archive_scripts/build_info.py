desktop_html = ''
mobile_html = ''

data = [
    {'title': 'Request Quote', 'desc': 'Submit your cargo dimensions through our rate estimator.', 'icon': 'search', 'step': '01'},
    {'title': 'Cargo Assessment', 'desc': 'Verify container compliance and HS classification codes.', 'icon': 'file-check', 'step': '02'},
    {'title': 'Packing Prep', 'desc': 'Secure shrink-wrap packaging and expert crating.', 'icon': 'package', 'step': '03'},
    {'title': 'Transportation', 'desc': 'Smooth transit execution across chosen premium channels.', 'icon': 'clock', 'step': '04'},
    {'title': 'Delivery Secure', 'desc': 'Efficient drop-off at target terminal docks securely.', 'icon': 'target', 'step': '05'}
]

# --- DESKTOP ---
desktop_html += '''
<div class="hidden md:block relative w-full max-w-6xl mx-auto h-[400px]">
  <!-- SVG Sine Wave -->
  <svg class="absolute inset-0 w-full h-[200px] pointer-events-none" viewBox="0 0 1000 200" preserveAspectRatio="none">
    <path d="M 100 100 C 150 0, 250 0, 300 100 C 350 200, 450 200, 500 100 C 550 0, 650 0, 700 100 C 750 200, 850 200, 900 100" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="4" stroke-linecap="round"/>
  </svg>
'''

x_positions = [10, 30, 50, 70, 90]
for i, item in enumerate(data):
    x = x_positions[i]
    desktop_html += f'''
  <!-- Node {i+1} -->
  <div class="absolute top-[100px] -translate-y-1/2 -translate-x-1/2 z-10 flex flex-col items-center group" style="left: {x}%;">
    <div class="w-24 h-24 rounded-full border-2 border-white/20 p-1 transition-all duration-300 group-hover:border-white/60 group-hover:scale-105">
      <div class="w-full h-full rounded-full flex items-center justify-center transition-all duration-300 group-hover:bg-white/20" style="background-color: rgba(255,255,255,0.1); backdrop-filter: blur(4px);">
        <i data-lucide="{item['icon']}" class="w-8 h-8 text-white"></i>
      </div>
    </div>
  </div>
  
  <!-- Text {i+1} -->
  <div class="absolute top-[170px] -translate-x-1/2 text-center w-[18%]" style="left: {x}%;">
    <h4 class="font-display font-bold text-white tracking-widest uppercase mb-2 text-sm">{item['title']}</h4>
    <p class="text-white/80 text-xs leading-relaxed font-sans">{item['desc']}</p>
  </div>
'''

badge_x = [20, 40, 60, 80]
badge_y = [25, 175, 25, 175]
for i in range(4):
    desktop_html += f'''
  <!-- Badge {i+1} -->
  <div class="absolute -translate-y-1/2 -translate-x-1/2 z-20 w-8 h-8 bg-white rounded-full flex items-center justify-center shadow-lg" style="left: {badge_x[i]}%; top: {badge_y[i]}px;">
    <span class="font-mono text-brand-blue font-bold text-xs">0{i+1}</span>
  </div>
'''
desktop_html += '</div>\n'

# --- MOBILE ---
mobile_html += '''
<div class="md:hidden relative border-l-2 border-white/20 ml-6 pl-8 space-y-12 py-4">
'''
for i, item in enumerate(data):
    mobile_html += f'''
  <div class="relative z-10">
    <div class="absolute -left-[50px] top-0 w-10 h-10 rounded-full border-2 border-brand-blue bg-white flex items-center justify-center shadow-md">
      <span class="font-mono text-brand-blue font-bold text-xs">0{i+1}</span>
    </div>
    <div class="bg-white/5 border border-white/10 rounded-xl p-6 backdrop-blur-sm">
      <div class="w-12 h-12 rounded-full bg-white/10 flex items-center justify-center mb-4">
        <i data-lucide="{item['icon']}" class="w-6 h-6 text-white"></i>
      </div>
      <h4 class="font-display font-bold text-white tracking-widest uppercase mb-2 text-sm">{item['title']}</h4>
      <p class="text-white/80 text-xs leading-relaxed font-sans">{item['desc']}</p>
    </div>
  </div>
'''
mobile_html += '</div>\n'

with open('c:/Users/favaz/Netex-Freight/Netex-Freigh/infographic.html', 'w', encoding='utf-8') as f:
    f.write(desktop_html + mobile_html)
