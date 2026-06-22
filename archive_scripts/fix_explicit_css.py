import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix the dividers by using an explicit <style> block, avoiding Tailwind compilation issues.
# Remove the old style block
html = re.sub(r'<style>\s*\.premium-badges-grid > div \{ border-color: rgba\(255,255,255,0\.2\) !important; \}\s*<\/style>', '', html)

# Insert the robust style block
new_style = '''<style>
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

html = html.replace(
    '<div class="w-full max-w-7xl mx-auto px-6">',
    new_style + '\n            <div class="w-full max-w-7xl mx-auto px-6">'
)

# 2. Clean up the grid class so it doesn't rely on md:divide-x
html = html.replace(
    'premium-badges-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 md:divide-x py-8',
    'premium-badges-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 py-8'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 3. Clean up main.js so we don't inject the line there anymore, since we use ::before now.
with open('src/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace(
    '<div class="hidden md:block absolute top-[28px] left-[10%] right-[10%] h-[3px] z-0" style="background-color: #ffffff;"></div>',
    ''
)

with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Applied guaranteed explicit CSS fixes.")
