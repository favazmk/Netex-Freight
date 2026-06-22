import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the vertical lines logic and keep the centralization CSS
old_style = '''<style>
              @media (min-width: 768px) {
                .premium-badges-grid > div:not(:first-child) {
                  border-left: 1px solid rgba(255,255,255,0.2);
                }
              }
              .premium-badges-grid > div {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100%;
              }
              #about-page-workflow-timeline::before {
                content: '';
                position: absolute;
                top: 28px;
                left: 10%;
                right: 10%;
                height: 3px;
                background-color: #ffffff;
                z-index: 0;
              }
              @media (max-width: 767px) {
                #about-page-workflow-timeline::before {
                  display: none;
                }
              }
            </style>'''

new_style = '''<style>
              .premium-badges-grid > div {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                height: 100%;
              }
            </style>'''

html = html.replace(old_style, new_style)

# 2. Fix the padding of the parent container to perfectly center vertically
html = html.replace(
    '<div class="w-full bg-brand-blue relative z-20 pb-12 pt-6" style="background-color: #0f3a8c;">',
    '<div class="w-full bg-brand-blue relative z-20 py-10" style="background-color: #0f3a8c;">'
)

# 3. Remove the extra py-8 from the grid so padding is purely handled by the parent
html = html.replace(
    '<div class="premium-badges-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 py-8">',
    '<div class="premium-badges-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4">'
)

# 4. Wrap the workflow timeline grid to include the explicit absolute line OUTSIDE the grid
old_timeline_html = '''<div class="relative border-l border-zinc-200 md:border-l-0 md:grid md:grid-cols-5 md:gap-6 pl-4 md:pl-0 space-y-8 md:space-y-0" id="about-page-workflow-timeline">
              <!-- Generated dynamically by JS -->
            </div>'''

new_timeline_html = '''<div class="relative w-full">
              <div class="hidden md:block absolute top-[28px] left-[10%] right-[10%] h-[3px] bg-white z-0" style="background-color: #ffffff;"></div>
              <div class="relative border-l border-zinc-200 md:border-l-0 md:grid md:grid-cols-5 md:gap-6 pl-4 md:pl-0 space-y-8 md:space-y-0 z-10" id="about-page-workflow-timeline">
                <!-- Generated dynamically by JS -->
              </div>
            </div>'''

html = html.replace(old_timeline_html, new_timeline_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied final fixes for centering and workflow line.")
