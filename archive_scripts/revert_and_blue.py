import re

# 1. Revert index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_workflow_html = """        <!-- Workflow pipeline inside About segment too -->
        <section class="edge-tab-blue py-20 px-6 md:px-12 bg-brand-blue relative" style="background-color: #0f3a8c;">
          <div class="absolute left-0 bottom-0 w-96 h-96 bg-white/5 rounded-full blur-3xl pointer-events-none"></div>
          <div class="max-w-7xl mx-auto">
            <div class="text-center mb-16">
              <span class="text-white opacity-80 uppercase tracking-[0.2em] font-mono text-xs block mb-3 font-semibold">
                // OPERATIONS MANAGEMENT
              </span>
              <h2 class="text-4xl font-display font-black text-white uppercase">
                HOW WORKFLOW PIPELINES ACT
              </h2>
              <div class="h-0.5 w-16 bg-brand-blue mx-auto mt-4"></div>
            </div>

            <div class="relative border-l border-zinc-200 md:border-l-0 md:grid md:grid-cols-5 md:gap-6 pl-4 md:pl-0 space-y-8 md:space-y-0" id="about-page-workflow-timeline">
              <!-- Generated dynamically by JS -->
            </div>
          </div>
        </section>"""

start_tag = r'        <!-- PREMIUM LOGISTICS TIMELINE -->\n        <section class="edge-tab-white py-24 px-6 md:px-12 bg-white relative overflow-hidden" id="premium-workflow-section">'
end_tag = r'              </div>\n\n            </div>\n          </div>\n        </section>'
match = re.search(start_tag + r'.*?' + end_tag, content, re.DOTALL)
if match:
    content = content[:match.start()] + old_workflow_html + content[match.end():]
    print("Timeline reverted in index.html.")
else:
    print("Could not find new timeline in index.html.")


# Now we make the RELIABLE & SAFE section blue
# It's currently: <div class="w-full bg-zinc-50/40 relative z-20 pb-12 pt-6">
# Let's change the background to brand-blue, and adjust the cards if necessary
# Wait, if we change the background to brand blue, the cards (which are white) will pop nicely.
# Let's just update the container background.

old_badges_container = '<div class="w-full bg-zinc-50/40 relative z-20 pb-12 pt-6">'
new_badges_container = '<div class="w-full bg-brand-blue relative z-20 pb-12 pt-6 edge-tab-blue" style="background-color: #0f3a8c;">'

if old_badges_container in content:
    content = content.replace(old_badges_container, new_badges_container)
    print("Badges container made blue.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# 2. Revert CSS
with open('src/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

start_idx = css_content.find("/* Premium Corporate Workflow Pipeline */")
if start_idx != -1:
    css_content = css_content[:start_idx]
    with open('src/style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("CSS reverted.")

# 3. Revert JS
with open('src/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Restore timeline JS logic
js_content = js_content.replace(
    '  // Old timeline logic removed for Premium Workflow',
    '  if (pageContainer) {\n    pageContainer.innerHTML = `\n      <div class="hidden md:block absolute top-[28px] left-[10%] right-[10%] h-px bg-white/20 -z-0"></div>\n      ${pipelineHtml}\n    `;\n  }'
)

# Remove the reveal script
start_idx = js_content.find("document.addEventListener('DOMContentLoaded', () => {")
if start_idx != -1:
    # Only remove if it contains 'reveal-step'
    if "'reveal-step'" in js_content[start_idx:]:
        js_content = js_content[:start_idx]
        print("JS reveal script removed.")

with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
