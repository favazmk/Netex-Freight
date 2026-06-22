import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The currently applied white top section
current_top_section = """        <!-- Grid Cards block -->
        <section class="edge-tab-white py-20 px-6 md:px-12 bg-transparent relative">
          <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-brand-blue/5 rounded-full blur-3xl pointer-events-none"></div>
          <div class="max-w-7xl mx-auto">
            <div class="text-center mb-12">
              <span class="text-brand-blue uppercase tracking-[0.2em] font-mono text-xs block mb-3 font-semibold">
                // COMPREHENSIVE CARRIER CAPABILITIES
              </span>
              <h2 class="text-4xl md:text-5xl font-display font-black text-zinc-950 tracking-tight uppercase">
                SERVICES <span class="text-zinc-400 font-medium">& SOLUTIONS</span>
              </h2>
            </div>"""

# Revert to Blue top section
reverted_top_section = """        <!-- Grid Cards block -->
        <section class="py-20 px-6 md:px-12 bg-brand-blue relative" style="background-color: #0f3a8c;">
          <div class="absolute right-0 top-0 w-96 h-96 bg-white/5 rounded-full blur-3xl pointer-events-none"></div>
          <div class="max-w-7xl mx-auto">
            <div class="text-center mb-12">
              <span class="text-white opacity-80 uppercase tracking-[0.2em] font-mono text-xs block mb-3 font-semibold">
                // COMPREHENSIVE CARRIER CAPABILITIES
              </span>
              <h2 class="text-4xl md:text-5xl font-display font-black text-white tracking-tight uppercase">
                SERVICES <span class="text-white/80 font-medium">& SOLUTIONS</span>
              </h2>
            </div>"""

# The currently applied blue bottom section
current_bottom_section = """        <!-- SECTOR SELECTION HUB SYSTEM -->
        <section class="edge-tab-blue py-20 px-6 md:px-12 bg-brand-blue relative w-full" style="background-color: #0f3a8c;">
          <div class="absolute right-0 top-0 w-96 h-96 bg-white/5 rounded-full blur-3xl pointer-events-none"></div>

          <div class="max-w-7xl mx-auto">
            
            <div class="text-center mb-16">
              <span class="text-white opacity-80 uppercase tracking-[0.2em] font-mono text-xs block mb-3 font-semibold">
                // COMPREHENSIVE CARRIER DIVISION
              </span>
              <h2 class="text-3xl font-display font-black text-white uppercase">
                SERVICES CATALOG
              </h2>
              <div class="h-0.5 w-16 bg-brand-blue mx-auto mt-4"></div>
            </div>"""

# Revert to White bottom section
reverted_bottom_section = """        <!-- SECTOR SELECTION HUB SYSTEM -->
        <section class="bg-transparent w-full py-20 px-6 md:px-12 relative">
          <div class="absolute top-0 right-0 w-[500px] h-[500px] bg-brand-blue/5 rounded-full blur-3xl pointer-events-none"></div>

          <div class="max-w-7xl mx-auto">
            
            <div class="text-center mb-16">
              <span class="text-brand-blue uppercase tracking-[0.2em] font-mono text-xs block mb-3 font-semibold">
                // COMPREHENSIVE CARRIER DIVISION
              </span>
              <h2 class="text-3xl font-display font-black text-zinc-950 uppercase">
                SERVICES CATALOG
              </h2>
              <div class="h-0.5 w-16 bg-brand-blue mx-auto mt-4"></div>
            </div>"""

# Regex replacing to ignore edge-tab classes since fix_edges.py might have modified them
import re

content = re.sub(r'        <!-- Grid Cards block -->\n        <section.*?<h2 class="text-4xl md:text-5xl font-display font-black text-zinc-950 tracking-tight uppercase">\n                SERVICES <span class="text-zinc-400 font-medium">& SOLUTIONS</span>\n              </h2>\n            </div>', reverted_top_section, content, flags=re.DOTALL)

content = re.sub(r'        <!-- SECTOR SELECTION HUB SYSTEM -->\n        <section.*?<h2 class="text-3xl font-display font-black text-white uppercase">\n                SERVICES CATALOG\n              </h2>\n              <div class="h-0.5 w-16 bg-brand-blue mx-auto mt-4"></div>\n            </div>', reverted_bottom_section, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Successfully reverted.")
