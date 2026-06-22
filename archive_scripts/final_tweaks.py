import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Change badges grid to ONLY have vertical lines on desktop
html = html.replace(
    'premium-badges-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 divide-y md:divide-y-0 lg:divide-x py-8',
    'premium-badges-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 md:divide-x py-8'
)

# 2. Add justify-center to vertically centralise the cards
html = html.replace(
    'flex flex-col items-center text-center px-4 py-8 md:py-4 gap-4',
    'flex flex-col justify-center items-center text-center h-full px-4 py-8 md:py-4 gap-4'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


with open('src/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 3. Make the timeline line extremely visible. Maybe it was hidden because 'bg-white/20' wasn't working.
# Let's use an inline style and a higher z-index like z-0, make sure it's absolute within the relative grid container.
old_line = '<div class="hidden md:block absolute top-[28px] left-[10%] right-[10%] h-[2px] z-0" style="background-color: rgba(255,255,255,0.4);"></div>'
new_line = '<div class="hidden md:block absolute top-[28px] left-[10%] right-[10%] h-[3px] z-0" style="background-color: #ffffff;"></div>'

js = js.replace(old_line, new_line)

# Also check if it was still using bg-white/20 in case the earlier replace failed
old_line_fallback = '<div class="hidden md:block absolute top-[28px] left-[10%] right-[10%] h-px bg-white/20 -z-0"></div>'
js = js.replace(old_line_fallback, new_line)


with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Applied final layout tweaks.")
