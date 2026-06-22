import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Shorten About Us
about_us_target = """<p class="text-zinc-650 text-sm leading-relaxed font-sans">
                By building direct relationships with primary global shipping lines and air carriers, we bypass intermediate broker delays to secure competitive transit rates. At Netex Freight, we support your commercial expansion with dependable, round-the-clock dispatch operations.
              </p>

              <div class="flex flex-col sm:flex-row gap-4 pt-2 font-mono text-xs">
                <div class="flex items-center gap-2 text-zinc-700 bg-zinc-50 border border-zinc-200 p-3 rounded-sm">
                  <i data-lucide="check-circle" class="w-4 h-4 text-brand-blue shrink-0"></i>
                  <span>International & Domestic Solutions</span>
                </div>
                <div class="flex items-center gap-2 text-zinc-700 bg-zinc-50 border border-zinc-200 p-3 rounded-sm">
                  <i data-lucide="check-circle" class="w-4 h-4 text-brand-blue shrink-0"></i>
                  <span>Customer-Focused Logistics Care</span>
                </div>
              </div>"""

about_us_replacement = """<div class="mt-8">
                <a href="#about-us" class="px-6 py-3 bg-brand-blue hover:bg-brand-blue-hover text-white font-bold font-mono text-xs uppercase tracking-widest rounded-sm transition-colors shadow-sm inline-block">Read Full Profile</a>
              </div>"""

content = content.replace(about_us_target, about_us_replacement)

# 2. Replace large sections with Previews
sections_pattern = re.compile(
    r'<!-- OPERATIONAL STANDARDS / TAB STAGE BLOCK -->.*?<!-- CTA SECTION IN THE SITE -->',
    re.DOTALL
)

preview_html = '''<!-- CORE SERVICES PREVIEW -->
        <section class="py-20 px-6 md:px-12 bg-zinc-50 border-t border-zinc-200">
          <div class="max-w-7xl mx-auto">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end mb-12 gap-4">
              <div>
                <span class="text-brand-blue uppercase tracking-[0.2em] font-mono text-xs block mb-3 font-semibold">// GLOBAL CAPABILITIES</span>
                <h2 class="text-3xl md:text-4xl font-display font-black text-zinc-950 uppercase">Our Core Services</h2>
              </div>
              <a href="#services" class="px-6 py-3 border border-zinc-200 bg-white hover:bg-zinc-50 text-zinc-700 font-mono text-xs uppercase tracking-widest font-bold rounded-sm transition-colors shadow-sm inline-flex items-center gap-2">
                View All Services <i data-lucide="arrow-right" class="w-4 h-4"></i>
              </a>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6" id="services-summary-grid">
              <!-- Populated by JS -->
            </div>
          </div>
        </section>

        <!-- WHY CHOOSE US PREVIEW -->
        <section class="py-20 px-6 md:px-12 bg-transparent border-t border-zinc-200">
          <div class="max-w-7xl mx-auto">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end mb-12 gap-4">
              <div>
                <span class="text-brand-blue uppercase tracking-[0.2em] font-mono text-xs block mb-3 font-semibold">// OPERATIONAL EXCELLENCE</span>
                <h2 class="text-3xl md:text-4xl font-display font-black text-zinc-950 uppercase">Why Choose Netex</h2>
              </div>
              <a href="#why-choose-us" class="px-6 py-3 border border-zinc-200 bg-zinc-50 hover:bg-zinc-100 text-zinc-700 font-mono text-xs uppercase tracking-widest font-bold rounded-sm transition-colors shadow-sm inline-flex items-center gap-2">
                See Our Standards <i data-lucide="arrow-right" class="w-4 h-4"></i>
              </a>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6" id="why-us-grid-container">
              <!-- Populated by JS -->
            </div>
          </div>
        </section>

        <!-- CTA SECTION IN THE SITE -->'''

content = sections_pattern.sub(preview_html, content)

# 3. Move Contact form
# We will just extract the exact contact inquiry section from #page-home
contact_section_pattern = re.compile(
    r'<!-- CONTACT INQUIRY SECTION -->\s*<section class="py-20 px-6 md:px-12 bg-transparent border-t border-zinc-200 relative">\s*<div class="max-w-7xl mx-auto">\s*(<div id="contact-form-anchor-wrapper".*?)\s*</div>\s*</section>',
    re.DOTALL
)

match = contact_section_pattern.search(content)
if match:
    form_html = match.group(1)
    
    # Remove from #page-home
    content = contact_section_pattern.sub('', content)
    
    # Insert into #page-contact-us
    target_pattern = re.compile(
        r'<div class="grid grid-cols-1 lg:grid-cols-12 gap-10" id="contact-page-layout-grid">\s*<!-- Generated/Adapted with JS mapping elements immediately -->\s*</div>',
        re.DOTALL
    )
    content = target_pattern.sub(form_html, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML Refactoring complete.")
