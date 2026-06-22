import re

# 1. Fix index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the badges section HUGE but centered (py-24)
html = html.replace(
    '<div class="w-full bg-brand-blue relative z-20 py-10" style="background-color: #0f3a8c;">',
    '<div class="w-full bg-brand-blue relative z-20 py-24" style="background-color: #0f3a8c;">'
)

# Remove the relative wrapper and absolute line we added last time
old_timeline_wrapper = '''<div class="relative w-full">
              <div class="hidden md:block absolute top-[28px] left-[10%] right-[10%] h-[3px] bg-white z-0" style="background-color: #ffffff;"></div>
              <div class="relative border-l border-zinc-200 md:border-l-0 md:grid md:grid-cols-5 md:gap-6 pl-4 md:pl-0 space-y-8 md:space-y-0 z-10" id="about-page-workflow-timeline">
                <!-- Generated dynamically by JS -->
              </div>
            </div>'''

new_timeline_wrapper = '''<div class="relative border-l border-zinc-200 md:border-l-0 md:grid md:grid-cols-5 md:gap-6 pl-4 md:pl-0 space-y-8 md:space-y-0" id="about-page-workflow-timeline">
              <!-- Generated dynamically by JS -->
            </div>'''

html = html.replace(old_timeline_wrapper, new_timeline_wrapper)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Fix main.js to restore the line exactly how it was
with open('src/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# We need to inject the line back into pageContainer.innerHTML
old_js_block = '''  if (pageContainer) {
    pageContainer.innerHTML = `
      
      ${pipelineHtml}
    `;
  }'''

# If the previous replacement left a blank line or exactly the pipelineHtml
if "pageContainer.innerHTML = pipelineHtml;" in js:
    js = js.replace(
        "pageContainer.innerHTML = pipelineHtml;",
        "pageContainer.innerHTML = `<div class=\\"hidden md:block absolute top-[28px] left-[10%] right-[10%] h-[2px] z-0\\" style=\\"background-color: rgba(255,255,255,0.4);\\"></div>${pipelineHtml}`;"
    )
elif "pageContainer.innerHTML = `\n      \n      ${pipelineHtml}\n    `;" in js:
    js = js.replace(
        "pageContainer.innerHTML = `\n      \n      ${pipelineHtml}\n    `;",
        "pageContainer.innerHTML = `\n      <div class=\"hidden md:block absolute top-[28px] left-[10%] right-[10%] h-[2px] z-0\" style=\"background-color: rgba(255,255,255,0.4);\"></div>\n      ${pipelineHtml}\n    `;"
    )
else:
    # Let's just use regex to cleanly replace the assignment
    js = re.sub(
        r'if\s*\(pageContainer\)\s*\{\s*pageContainer\.innerHTML\s*=\s*`\s*\$\{pipelineHtml\}\s*`;\s*\}',
        'if (pageContainer) {\n    pageContainer.innerHTML = `\n      <div class="hidden md:block absolute top-[28px] left-[10%] right-[10%] h-[2px] z-0" style="background-color: rgba(255,255,255,0.4);"></div>\n      ${pipelineHtml}\n    `;\n  }',
        js
    )
    # Also handle the case where it has empty spaces
    js = re.sub(
        r'if\s*\(pageContainer\)\s*\{\s*pageContainer\.innerHTML\s*=\s*`\s*\$\{pipelineHtml\}\s*`;\s*\}',
        'if (pageContainer) {\n    pageContainer.innerHTML = `\n      <div class="hidden md:block absolute top-[28px] left-[10%] right-[10%] h-[2px] z-0" style="background-color: rgba(255,255,255,0.4);"></div>\n      ${pipelineHtml}\n    `;\n  }',
        js
    )

with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Restored workflow line and doubled badges padding.")
