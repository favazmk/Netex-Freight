import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update text copy
content = content.replace('// CONNECT CODES', '// CONTACT INFORMATION')
content = content.replace('// COLD CHANNEL INQUIRY FLOW', '// SUBMIT YOUR INQUIRY')

# 2. Update Map Opacity
content = content.replace('<g opacity="0.04">', '<g opacity="0.08">')
content = content.replace('opacity-45">EQUATOR', '">EQUATOR')
content = content.replace('opacity-45">PRIME MERIDIAN', '">PRIME MERIDIAN')

# 3. Swap Services Sections
# Extract the whole page-services block
match = re.search(r'(<div id="page-services"[^>]*>)(.*?)(      </div>\n\n\n      <!-- ==================== PAGE Stack: ABOUT US)', content, re.DOTALL)
if match:
    prefix = match.group(1)
    services_content = match.group(2)
    suffix = match.group(3)

    # In services_content, find the two sections.
    # section1 is from <section class="edge-tab-white bg-transparent w-full py-20 px-6 md:px-12 relative"> to </section>
    # section2 is from <!-- Grid Cards block --> to </section> before the end of the match.
    
    sec1_match = re.search(r'(        <!-- SECTOR SELECTION HUB SYSTEM -->\n        <section.*?)(        <!-- Grid Cards block -->)', services_content, re.DOTALL)
    if sec1_match:
        sec1 = sec1_match.group(1)
        sec2 = sec1_match.group(2) + services_content[sec1_match.end(2):]
        
        # Swap them
        new_services_content = "\n" + sec2 + "\n" + sec1
        content = content[:match.start()] + prefix + new_services_content + suffix + content[match.end():]

# 4. Premium styling for the features grid (lines ~328-370)
# We will use regex to find the HERO FLOATING BADGES ROW container
grid_regex = r'(<!-- HERO FLOATING BADGES ROW -->\n\s*<div class="w-full bg-zinc-50/40">)(.*?)(?=\n\s*</div>\n\s*</div>\n\s*</section>)'
grid_match = re.search(grid_regex, content, re.DOTALL)
if grid_match:
    premium_grid = """
            <div class="w-full max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 py-12 relative z-20">
              
              <!-- Premium Card 1 -->
              <div class="bg-white rounded-md shadow-[0_4px_20px_rgba(0,0,0,0.04)] border border-zinc-100 p-8 flex flex-col hover:shadow-xl hover:-translate-y-1 transition-all duration-300 relative overflow-hidden group">
                <div class="w-12 h-12 rounded-full bg-brand-blue/5 flex items-center justify-center text-brand-blue mb-5 group-hover:scale-110 group-hover:bg-brand-blue group-hover:text-white transition-all duration-300">
                  <i data-lucide="shield-check" class="w-5 h-5"></i>
                </div>
                <div class="font-display font-bold text-[13px] text-zinc-900 uppercase tracking-widest mb-3 relative z-10">RELIABLE & SAFE</div>
                <div class="text-xs text-zinc-500 leading-relaxed relative z-10">Secure asset handling guaranteed at every step of global transit.</div>
                <div class="absolute bottom-0 left-0 h-1 w-0 bg-brand-blue group-hover:w-full transition-all duration-500 ease-out"></div>
              </div>

              <!-- Premium Card 2 -->
              <div class="bg-white rounded-md shadow-[0_4px_20px_rgba(0,0,0,0.04)] border border-zinc-100 p-8 flex flex-col hover:shadow-xl hover:-translate-y-1 transition-all duration-300 relative overflow-hidden group">
                <div class="w-12 h-12 rounded-full bg-brand-blue/5 flex items-center justify-center text-brand-blue mb-5 group-hover:scale-110 group-hover:bg-brand-blue group-hover:text-white transition-all duration-300">
                  <i data-lucide="clock" class="w-5 h-5"></i>
                </div>
                <div class="font-display font-bold text-[13px] text-zinc-900 uppercase tracking-widest mb-3 relative z-10">ON-TIME DELIVERY</div>
                <div class="text-xs text-zinc-500 leading-relaxed relative z-10">Timely priority shipping solutions keeping your supply chain ahead.</div>
                <div class="absolute bottom-0 left-0 h-1 w-0 bg-brand-blue group-hover:w-full transition-all duration-500 ease-out"></div>
              </div>

              <!-- Premium Card 3 -->
              <div class="bg-white rounded-md shadow-[0_4px_20px_rgba(0,0,0,0.04)] border border-zinc-100 p-8 flex flex-col hover:shadow-xl hover:-translate-y-1 transition-all duration-300 relative overflow-hidden group">
                <div class="w-12 h-12 rounded-full bg-brand-blue/5 flex items-center justify-center text-brand-blue mb-5 group-hover:scale-110 group-hover:bg-brand-blue group-hover:text-white transition-all duration-300">
                  <i data-lucide="globe" class="w-5 h-5"></i>
                </div>
                <div class="font-display font-bold text-[13px] text-zinc-900 uppercase tracking-widest mb-3 relative z-10">GLOBAL NETWORK</div>
                <div class="text-xs text-zinc-500 leading-relaxed relative z-10">Strong direct alliances with global ocean carriers & air lines.</div>
                <div class="absolute bottom-0 left-0 h-1 w-0 bg-brand-blue group-hover:w-full transition-all duration-500 ease-out"></div>
              </div>

              <!-- Premium Card 4 -->
              <div class="bg-white rounded-md shadow-[0_4px_20px_rgba(0,0,0,0.04)] border border-zinc-100 p-8 flex flex-col hover:shadow-xl hover:-translate-y-1 transition-all duration-300 relative overflow-hidden group">
                <div class="w-12 h-12 rounded-full bg-brand-blue/5 flex items-center justify-center text-brand-blue mb-5 group-hover:scale-110 group-hover:bg-brand-blue group-hover:text-white transition-all duration-300">
                  <i data-lucide="headphones" class="w-5 h-5"></i>
                </div>
                <div class="font-display font-bold text-[13px] text-zinc-900 uppercase tracking-widest mb-3 relative z-10">DEDICATED SUPPORT</div>
                <div class="text-xs text-zinc-500 leading-relaxed relative z-10">Dubai operations desk available 24/7/365 to manage dispatch.</div>
                <div class="absolute bottom-0 left-0 h-1 w-0 bg-brand-blue group-hover:w-full transition-all duration-500 ease-out"></div>
              </div>"""
    content = content[:grid_match.start(2)] + premium_grid + content[grid_match.end(2):]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
