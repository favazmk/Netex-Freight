import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Contact Page Text Colors
# Target the block under #contact-form-anchor-wrapper
contact_info_pattern = re.compile(
    r'(<div class="space-y-4">\s*<span class="text-brand-blue uppercase tracking-\[0\.2em\] font-mono text-xs block mb-1 font-semibold">\s*// COLD CHANNEL INQUIRY FLOW\s*</span>\s*<h3 class="text-3xl md:text-4xl font-display font-black text-)zinc-950( tracking-tight uppercase">\s*Connect With <span class="text-)brand-blue(">Us</span>\s*</h3>\s*<p class="text-)zinc-600( text-xs md:text-sm leading-relaxed font-sans">\s*Submit your details and cargo metrics directly to our Dubai operations. Our standard dispatcher desk acts immediately upon routing requests.\s*</p>\s*</div>\s*<div class="p-4 rounded-sm )bg-zinc-50 border border-zinc-200( flex items-center justify-between font-mono text-xs shadow-xs">\s*<span class="text-)zinc-500(">GCC DISPATCH STATUS:</span>\s*<strong class="text-)brand-blue( uppercase tracking-widest">ACTIVE ONLINE</strong>\s*</div>)',
    re.DOTALL
)

def contact_replace(match):
    original = match.group(1)
    # Perform string replacements within the matched block
    replaced = original.replace('text-zinc-950', 'text-white')
    replaced = replaced.replace('text-brand-blue">Us', 'text-white opacity-80">Us')
    replaced = replaced.replace('text-zinc-600', 'text-white opacity-90')
    replaced = replaced.replace('bg-zinc-50 border border-zinc-200', 'bg-white/10 border border-white/20 text-white')
    replaced = replaced.replace('text-zinc-500', 'text-white opacity-70')
    replaced = replaced.replace('text-brand-blue uppercase', 'text-white uppercase')
    # Also change the top label text-brand-blue to text-white
    replaced = replaced.replace('span class="text-brand-blue uppercase', 'span class="text-white opacity-80 uppercase')
    return replaced

content = contact_info_pattern.sub(contact_replace, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Contact page text colors adjusted in index.html.")
