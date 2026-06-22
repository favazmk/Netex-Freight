import re

# 1. Revert index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove Font Awesome
content = content.replace('  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n', '')

# Restore the old HTML block
old_html_block = """          <!-- HERO FLOATING BADGES ROW -->
          <div class="w-full bg-zinc-50/40 relative z-20 pb-12 pt-6">
            <div class="w-full max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              
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
              </div>

            </div>
          </div>"""

start_tag = r'          <!-- PREMIUM LOGISTICS FEATURES -->\n          <div class="logistics-features w-full relative z-20">'
end_tag = r'              </div>\n          </div>'
match = re.search(start_tag + r'.*?' + end_tag, content, re.DOTALL)
if match:
    content = content[:match.start()] + old_html_block + content[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html reverted successfully.")

# 2. Revert CSS
with open('src/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()
start_idx = css_content.find("/* Premium Logistics Features Section */")
if start_idx != -1:
    css_content = css_content[:start_idx]
    with open('src/style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("style.css reverted successfully.")

# 3. Revert JS
with open('src/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()
start_idx = js_content.find("// Premium Logistics Features JS")
if start_idx != -1:
    js_content = js_content[:start_idx]
    with open('src/main.js', 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("main.js reverted successfully.")
