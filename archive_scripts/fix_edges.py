import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# First, clean up all wrong edge classes and overflow-hidden from sections
content = content.replace("edge-tab-white ", "")
content = content.replace("edge-tab-blue ", "")

# Iterate over all sections
sections = list(re.finditer(r'<section[^>]*>', content))
prev_color = "white"
new_content = ""
last_idx = 0

for m in sections:
    fm = m.group(0)
    start = m.start()
    end = m.end()
    
    new_content += content[last_idx:start]
    
    # Clean overflow-hidden from sections (except hero)
    if 'id="hero"' not in fm:
        fm = fm.replace(' overflow-hidden', '')
        fm = fm.replace('overflow-hidden ', '')
    
    cur = "white" if "bg-transparent" in fm else "blue"
    
    # We want the CURRENT section to project its OWN color UPWARDS into the previous section!
    if prev_color != cur:
        tab = "edge-tab-blue " if cur == "blue" else "edge-tab-white "
        if 'class="' in fm and tab not in fm:
            fm = fm.replace('class="', f'class="{tab}')
            
    prev_color = cur
    new_content += fm
    last_idx = end

new_content += content[last_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)
