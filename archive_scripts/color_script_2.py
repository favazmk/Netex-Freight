import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Services Catalog in #page-services
services_catalog_pattern = re.compile(
    r'(<!-- Grid Cards block -->\s*)<section class="py-20 px-6 md:px-12 bg-transparent border-t border-zinc-200 relative">(\s*<div class="max-w-7xl mx-auto">\s*<div class="text-center mb-12">\s*)<span class="text-brand-blue uppercase tracking-\[0\.2em\] font-mono text-xs block mb-3 font-semibold">(.*?)</span>(\s*)<h2 class="text-3xl font-display font-black text-zinc-950 uppercase">',
    re.DOTALL
)
services_catalog_rep = r'\1<section class="py-20 px-6 md:px-12 bg-brand-blue border-t border-zinc-200 relative overflow-hidden" style="background-color: #0f3a8c;">\n          <div class="absolute right-0 top-0 w-96 h-96 bg-white/5 rounded-full blur-3xl pointer-events-none"></div>\2<span class="text-white opacity-80 uppercase tracking-[0.2em] font-mono text-xs block mb-3 font-semibold">\3</span>\4<h2 class="text-3xl font-display font-black text-white uppercase">'
content = services_catalog_pattern.sub(services_catalog_rep, content)

# 2. HOW WORKFLOW PIPELINES ACT in #page-about-us
workflow_pattern = re.compile(
    r'(<!-- Workflow pipeline inside About segment too -->\s*)<section class="py-20 px-6 md:px-12 bg-zinc-50 border-t border-zinc-200">(\s*<div class="max-w-7xl mx-auto">\s*<div class="text-center mb-16">\s*)<span class="text-brand-blue uppercase tracking-\[0\.2em\] font-mono text-xs block mb-3 font-semibold">(\s*// OPERATIONS MANAGEMENT\s*)</span>(\s*)<h2 class="text-4xl font-display font-black text-zinc-950 uppercase">',
    re.DOTALL
)
workflow_rep = r'\1<section class="py-20 px-6 md:px-12 bg-brand-blue border-t border-zinc-200 relative overflow-hidden" style="background-color: #0f3a8c;">\n          <div class="absolute left-0 bottom-0 w-96 h-96 bg-white/5 rounded-full blur-3xl pointer-events-none"></div>\2<span class="text-white opacity-80 uppercase tracking-[0.2em] font-mono text-xs block mb-3 font-semibold">\3</span>\4<h2 class="text-4xl font-display font-black text-white uppercase">'
content = workflow_pattern.sub(workflow_rep, content)

# 3. OUR TRADING INDUSTRIES SERVED in #page-why-choose-us
industries_pattern = re.compile(
    r'(<!-- Specialised industries sectors segment -->\s*)<section class="py-20 px-6 md:px-12 bg-zinc-50 border-t border-zinc-200">(\s*<div class="max-w-7xl mx-auto">\s*<div class="text-center mb-16">\s*)<span class="text-brand-blue uppercase tracking-\[0\.2em\] font-mono text-xs block mb-1 font-semibold">(\s*// CLIENT SECTORS IN FOCUS\s*)</span>(\s*)<h2 class="text-3xl md:text-4xl font-display font-black text- zinc-950 uppercase">',
    re.DOTALL
)
# Note: there is a typo in the original HTML: "text- zinc-950". The regex matches it precisely.
industries_rep = r'\1<section class="py-20 px-6 md:px-12 bg-brand-blue border-t border-zinc-200 relative overflow-hidden" style="background-color: #0f3a8c;">\n          <div class="absolute right-0 top-0 w-96 h-96 bg-white/5 rounded-full blur-3xl pointer-events-none"></div>\2<span class="text-white opacity-80 uppercase tracking-[0.2em] font-mono text-xs block mb-1 font-semibold">\3</span>\4<h2 class="text-3xl md:text-4xl font-display font-black text-white uppercase">'
content = industries_pattern.sub(industries_rep, content)

# 4. CONTACT US PAGE Header
contact_pattern = re.compile(
    r'(<!-- ==================== PAGE Stack: CONTACT US ==================== -->\s*<div id="page-contact-us" class="page-view hidden">\s*<!-- Main Form Grid -->\s*)<section class="py-20 px-6 md:px-12 bg-transparent border-t border-zinc-200">(\s*<div class="max-w-7xl mx-auto">\s*<div class="text-center mb-16 space-y-4">\s*)<span class="text-brand-blue uppercase tracking-\[0\.2em\] font-mono text-xs block font-semibold">(// CONNECT CODES)</span>(\s*)<h1 class="text-4xl md:text-5xl font-display font-black text-zinc-950 uppercase">',
    re.DOTALL
)
contact_rep = r'\1<section class="py-20 px-6 md:px-12 bg-brand-blue border-t border-zinc-200 relative overflow-hidden" style="background-color: #0f3a8c;">\n          <div class="absolute left-0 top-0 w-96 h-96 bg-white/5 rounded-full blur-3xl pointer-events-none"></div>\2<span class="text-white opacity-80 uppercase tracking-[0.2em] font-mono text-xs block font-semibold">\3</span>\4<h1 class="text-4xl md:text-5xl font-display font-black text-white uppercase">'
content = contact_pattern.sub(contact_rep, content)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Inverted more sections.")
