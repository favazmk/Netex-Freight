import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

style_block = """    <style>
      .edge-tab-white {
        position: relative;
      }
      .edge-tab-white::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 150px;
        height: 30px;
        z-index: 10;
        background-color: #ffffff;
        clip-path: polygon(0 0, 100% 0, calc(100% - 30px) 100%, 0 100%);
      }
      .edge-tab-blue {
        position: relative;
      }
      .edge-tab-blue::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 150px;
        height: 30px;
        z-index: 10;
        background-color: #0f3a8c;
        clip-path: polygon(0 0, 100% 0, calc(100% - 30px) 100%, 0 100%);
      }
      @media (min-width: 768px) {
        .edge-tab-white::before, .edge-tab-blue::before {
          width: 300px;
          height: 50px;
          clip-path: polygon(0 0, 100% 0, calc(100% - 50px) 100%, 0 100%);
        }
      }
    </style>
  </head>"""

if ".edge-tab-white" not in content:
    content = content.replace("  </head>", style_block)

sections = list(re.finditer(r'<section[^>]*>', content))
prev_color = "white"
new_content = ""
last_idx = 0

for m in sections:
    fm = m.group(0)
    start = m.start()
    end = m.end()
    
    new_content += content[last_idx:start]
    cur = "white" if "bg-transparent" in fm else "blue"
    
    if prev_color != cur:
        tab = "edge-tab-white " if cur == "blue" else "edge-tab-blue "
        if 'class="' in fm and tab not in fm:
            fm = fm.replace('class="', f'class="{tab}')
            
    prev_color = cur
    new_content += fm
    last_idx = end

new_content += content[last_idx:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_content)
