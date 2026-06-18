import os

files_to_check = [
    r'c:\Users\favaz\Netex-Freight\Netex-Freigh\index.html',
    r'c:\Users\favaz\Netex-Freight\Netex-Freigh\src\style.css',
    r'c:\Users\favaz\Netex-Freight\Netex-Freigh\src\main.js'
]

for file_path in files_to_check:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Color replacement
        content = content.replace('#0f3a8c', '#011d50')
        content = content.replace('#0F3A8C', '#011D50')
        content = content.replace('15, 58, 140', '1, 29, 80')
        
        # HTML Hero section heading
        hero_target = """              <div class="mb-6">
                <span class="text-brand-blue font-mono text-xs tracking-[0.3em] uppercase block font-semibold">
                  Leading Logistics Solutions // JAFZA Dubai Operator
                </span>
              </div>
              
              
              <p class="text-zinc-600 text-base md:text-lg max-w-lg leading-relaxed mb-10 font-sans">"""
        hero_replacement = """              <div class="mb-6">
                <span class="text-brand-blue font-mono text-xs tracking-[0.3em] uppercase block font-semibold">
                  Leading Logistics Solutions // JAFZA Dubai Operator
                </span>
              </div>
              
              <h2 class="text-4xl md:text-5xl font-display font-black text-zinc-950 uppercase mb-4 tracking-tight">GLOBAL FREIGHT & LOGISTICS</h2>
              
              <p class="text-zinc-600 text-base md:text-lg max-w-lg leading-relaxed mb-10 font-sans">"""
        if hero_target in content:
            content = content.replace(hero_target, hero_replacement)
            
        # HTML Contact section redundancy
        contact_target = """                <div class="space-y-4">
                  <span class="text-white opacity-80 uppercase tracking-[0.2em] font-mono text-xs block mb-1 font-semibold">
                    // SUBMIT YOUR INQUIRY
                  </span>
                  <h3 class="text-3xl md:text-4xl font-display font-black text-white tracking-tight uppercase">
                    Connect With <span class="text-white opacity-80">Us</span>
                  </h3>
                  <p class="text-white opacity-90 text-xs md:text-sm leading-relaxed font-sans">"""
        contact_replacement = """                <div class="space-y-4">
                  <p class="text-white opacity-90 text-xs md:text-sm leading-relaxed font-sans">"""
        if contact_target in content:
            content = content.replace(contact_target, contact_replacement)
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Updated', file_path)
