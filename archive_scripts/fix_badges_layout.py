import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the style tag for .premium-badges-grid
html = re.sub(r'<style>\s*\.premium-badges-grid.*?<\/style>\s*', '', html, flags=re.DOTALL)

# 2. Update the main container classes and remove inline background
html = html.replace(
    'class="premium-badges-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 border rounded-xl divide-y md:divide-y-0 lg:divide-x shadow-xl" style="background-color: rgba(255,255,255,0.05); backdrop-filter: blur(4px);"',
    'class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 py-8"'
)

# 3. Update all 4 cards to use flex-col, items-center, text-center
html = html.replace(
    '<div class="bg-transparent py-16 px-8 flex flex-row items-center gap-5 transition-all duration-300 relative overflow-hidden group" style="color: white;">',
    '<div class="bg-transparent flex flex-col items-center text-center gap-4 transition-all duration-300 group" style="color: white;">'
)

# 4. Remove mb-1 from the title if needed, maybe not strictly necessary, but let's make sure it looks good.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Changes applied!")
