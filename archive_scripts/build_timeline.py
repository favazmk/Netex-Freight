import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Font Awesome if not present
if 'font-awesome' not in content and 'fontawesome' not in content:
    head_end = content.find('</head>')
    fa_link = '  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n'
    content = content[:head_end] + fa_link + content[head_end:]

premium_workflow_html = """        <!-- PREMIUM LOGISTICS TIMELINE -->
        <section class="edge-tab-white py-24 px-6 md:px-12 bg-white relative overflow-hidden" id="premium-workflow-section">
          <div class="max-w-7xl mx-auto relative z-10">
            <div class="text-center mb-16">
              <span class="text-brand-blue uppercase tracking-[0.2em] font-mono text-xs block mb-3 font-semibold">
                // OPERATIONS MANAGEMENT
              </span>
              <h2 class="text-4xl font-display font-black text-zinc-950 uppercase tracking-tight">
                HOW OUR SHIPPING PROCESS WORKS
              </h2>
              <div class="h-0.5 w-16 bg-brand-blue mx-auto mt-5"></div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-5 gap-8 md:gap-4 relative" id="premium-workflow-timeline">
              <!-- Animated route line (Desktop only) -->
              <div class="hidden md:block absolute top-[56px] left-[10%] right-[10%] h-[2px] bg-zinc-100 z-0 overflow-hidden rounded-full">
                  <div class="absolute top-0 left-0 w-[100px] h-full bg-brand-blue shadow-[0_0_12px_rgba(15,58,140,0.8)] z-10 rounded-full" style="animation: moveCargoLine 4s linear infinite;"></div>
              </div>
              
              <!-- Step 1 -->
              <div class="workflow-step reveal-step flex flex-col items-center text-center p-6 bg-white border border-zinc-100 rounded-[16px] relative shadow-xs cursor-default z-10">
                <div class="step-icon-wrapper w-16 h-16 rounded-full bg-white border border-zinc-200 shadow-sm flex items-center justify-center text-brand-blue mb-5 relative z-10">
                  <i class="fa-solid fa-file-invoice text-xl"></i>
                  <div class="step-number absolute -top-2 -right-2 w-6 h-6 rounded-full bg-brand-blue text-white font-mono text-[10px] font-bold flex items-center justify-center shadow-xs transition-colors">1</div>
                </div>
                <h4 class="font-mono text-[11px] font-bold text-zinc-900 uppercase tracking-wider mb-2">REQUEST QUOTE</h4>
                <p class="font-sans text-[12px] text-zinc-500 leading-relaxed">Submit your cargo details for a competitive transit estimate.</p>
              </div>

              <!-- Step 2 -->
              <div class="workflow-step reveal-step flex flex-col items-center text-center p-6 bg-white border border-zinc-100 rounded-[16px] relative shadow-xs cursor-default z-10">
                <div class="step-icon-wrapper w-16 h-16 rounded-full bg-white border border-zinc-200 shadow-sm flex items-center justify-center text-brand-blue mb-5 relative z-10">
                  <i class="fa-solid fa-clipboard-check text-xl"></i>
                  <div class="step-number absolute -top-2 -right-2 w-6 h-6 rounded-full bg-brand-blue text-white font-mono text-[10px] font-bold flex items-center justify-center shadow-xs transition-colors">2</div>
                </div>
                <h4 class="font-mono text-[11px] font-bold text-zinc-900 uppercase tracking-wider mb-2">CARGO ASSESSMENT</h4>
                <p class="font-sans text-[12px] text-zinc-500 leading-relaxed">Our specialists review compliance and clearance requirements.</p>
              </div>

              <!-- Step 3 -->
              <div class="workflow-step reveal-step flex flex-col items-center text-center p-6 bg-white border border-zinc-100 rounded-[16px] relative shadow-xs cursor-default z-10">
                <div class="step-icon-wrapper w-16 h-16 rounded-full bg-white border border-zinc-200 shadow-sm flex items-center justify-center text-brand-blue mb-5 relative z-10">
                  <i class="fa-solid fa-box-open text-xl"></i>
                  <div class="step-number absolute -top-2 -right-2 w-6 h-6 rounded-full bg-brand-blue text-white font-mono text-[10px] font-bold flex items-center justify-center shadow-xs transition-colors">3</div>
                </div>
                <h4 class="font-mono text-[11px] font-bold text-zinc-900 uppercase tracking-wider mb-2">PACKING PREP</h4>
                <p class="font-sans text-[12px] text-zinc-500 leading-relaxed">Industrial consolidation and secure palletizing procedures.</p>
              </div>

              <!-- Step 4 -->
              <div class="workflow-step reveal-step flex flex-col items-center text-center p-6 bg-white border border-zinc-100 rounded-[16px] relative shadow-xs cursor-default z-10">
                <div class="step-icon-wrapper w-16 h-16 rounded-full bg-white border border-zinc-200 shadow-sm flex items-center justify-center text-brand-blue mb-5 relative z-10">
                  <i class="fa-solid fa-truck-fast text-xl"></i>
                  <div class="step-number absolute -top-2 -right-2 w-6 h-6 rounded-full bg-brand-blue text-white font-mono text-[10px] font-bold flex items-center justify-center shadow-xs transition-colors">4</div>
                </div>
                <h4 class="font-mono text-[11px] font-bold text-zinc-900 uppercase tracking-wider mb-2">TRANSPORTATION</h4>
                <p class="font-sans text-[12px] text-zinc-500 leading-relaxed">Air, Ocean, or Land transit via our global network lines.</p>
              </div>

              <!-- Step 5 -->
              <div class="workflow-step reveal-step flex flex-col items-center text-center p-6 bg-white border border-zinc-100 rounded-[16px] relative shadow-xs cursor-default z-10">
                <div class="step-icon-wrapper w-16 h-16 rounded-full bg-white border border-zinc-200 shadow-sm flex items-center justify-center text-brand-blue mb-5 relative z-10">
                  <i class="fa-solid fa-circle-check text-xl"></i>
                  <div class="step-number absolute -top-2 -right-2 w-6 h-6 rounded-full bg-brand-blue text-white font-mono text-[10px] font-bold flex items-center justify-center shadow-xs transition-colors">5</div>
                </div>
                <h4 class="font-mono text-[11px] font-bold text-zinc-900 uppercase tracking-wider mb-2">DELIVERY SECURE</h4>
                <p class="font-sans text-[12px] text-zinc-500 leading-relaxed">Final mile operational handover and dispatch clearance.</p>
              </div>

            </div>
          </div>
        </section>"""

start_tag = r'        <!-- Workflow pipeline inside About segment too -->\n        <section class="edge-tab-blue py-20 px-6 md:px-12 bg-brand-blue relative" style="background-color: #0f3a8c;">'
end_tag = r'              <!-- Generated dynamically by JS -->\n            </div>\n          </div>\n        </section>'
match = re.search(start_tag + r'.*?' + end_tag, content, re.DOTALL)
if match:
    content = content[:match.start()] + premium_workflow_html + content[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated successfully.")
else:
    print("Could not find Workflow section in index.html")

# 2. Add CSS
css_content = """
/* Premium Corporate Workflow Pipeline */
@keyframes moveCargoLine {
    0% { left: -100px; }
    100% { left: 100%; }
}

.workflow-step {
    transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.workflow-step:hover {
    transform: translateY(-8px);
    border-color: #0f3a8c;
    box-shadow: 0 15px 35px rgba(15, 58, 140, 0.08);
}

.step-icon-wrapper {
    transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.workflow-step:hover .step-icon-wrapper {
    transform: scale(1.08);
    border-color: #0f3a8c;
    background: #0f3a8c;
    color: #fff;
}

.workflow-step:hover .step-icon-wrapper .step-number {
    background: #fff;
    color: #0f3a8c;
    border: 1px solid #0f3a8c;
}

.reveal-step {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s ease-out, transform 0.8s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.reveal-step.revealed {
    opacity: 1;
    transform: translateY(0);
}
"""
with open('src/style.css', 'a', encoding='utf-8') as f:
    f.write(css_content)
print("CSS appended.")

# 3. Add JS & Disable old JS
with open('src/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

# Disable old rendering inside `renderProcessTimeline()`
js_content = js_content.replace(
    '  if (pageContainer) {\n    pageContainer.innerHTML = `\n      <div class="hidden md:block absolute top-[28px] left-[10%] right-[10%] h-px bg-white/20 -z-0"></div>\n      ${pipelineHtml}\n    `;\n  }',
    '  // Old timeline logic removed for Premium Workflow'
)

# Add reveal observer
js_reveal = """
document.addEventListener('DOMContentLoaded', () => {
    const steps = document.querySelectorAll('.reveal-step');
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                entry.target.classList.add('revealed');
            }
        });
    }, { threshold: 0.2 });

    steps.forEach((step, index) => {
        step.style.transitionDelay = `${index * 0.15}s`;
        observer.observe(step);
    });
});
"""
with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(js_content + js_reveal)
print("JS updated.")
