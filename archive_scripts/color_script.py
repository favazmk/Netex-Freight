import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the "Get PDF Brochure" button
brochure_pattern = re.compile(r'<button\s*id="btn-brochure-modal-reveal".*?</button>', re.DOTALL)
content = brochure_pattern.sub('', content)

# 2. Invert the Core Services Preview
services_preview_pattern = re.compile(
    r'(<!-- CORE SERVICES PREVIEW -->\s*)<section class="py-20 px-6 md:px-12 bg-zinc-50 border-t border-zinc-200">\s*(<div class="max-w-7xl mx-auto">)\s*<div class="flex flex-col sm:flex-row justify-between items-start sm:items-end mb-12 gap-4">\s*<div>\s*<span class="text-brand-blue uppercase tracking-\[0\.2em\] font-mono text-xs block mb-3 font-semibold">// GLOBAL CAPABILITIES</span>\s*<h2 class="text-3xl md:text-4xl font-display font-black text-zinc-950 uppercase">Our Core Services</h2>\s*</div>\s*<a href="#services" class="px-6 py-3 border border-zinc-200 bg-white hover:bg-zinc-50 text-zinc-700 font-mono text-xs uppercase tracking-widest font-bold rounded-sm transition-colors shadow-sm inline-flex items-center gap-2">\s*View All Services <i data-lucide="arrow-right" class="w-4 h-4"></i>\s*</a>',
    re.DOTALL
)

services_preview_replacement = r'''\1<section class="py-20 px-6 md:px-12 bg-brand-blue border-t border-zinc-200 relative overflow-hidden" style="background-color: #0f3a8c;">
          <!-- Subtle decorative elements for dark background -->
          <div class="absolute left-0 top-0 w-96 h-96 bg-white/5 rounded-full blur-3xl pointer-events-none"></div>
          
          <div class="max-w-7xl mx-auto relative z-10">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end mb-12 gap-4">
              <div>
                <span class="text-white opacity-80 uppercase tracking-[0.2em] font-mono text-xs block mb-3 font-semibold">// GLOBAL CAPABILITIES</span>
                <h2 class="text-3xl md:text-4xl font-display font-black text-white uppercase">Our Core Services</h2>
              </div>
              <a href="#services" class="px-6 py-3 border border-white/30 bg-white/5 hover:bg-white/10 text-white font-mono text-xs uppercase tracking-widest font-bold rounded-sm transition-colors shadow-sm inline-flex items-center gap-2">
                View All Services <i data-lucide="arrow-right" class="w-4 h-4"></i>
              </a>'''

content = services_preview_pattern.sub(services_preview_replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Inverted Core Services preview and removed Brochure button.")
