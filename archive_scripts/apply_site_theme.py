import re

# 1. Update style.css
with open('src/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

# We will just replace the entire block from /* Premium Logistics Features Section */ to the end
start_idx = css_content.find("/* Premium Logistics Features Section */")
if start_idx != -1:
    css_content = css_content[:start_idx]

new_css = """/* Premium Logistics Features Section */
.logistics-features{
    position:relative;
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:24px;
    padding:80px 5%;
    background:linear-gradient(135deg, #07193f, #0f3a8c, #07193f);
    overflow:hidden;
}

.logistics-features::before{
    content:"";
    position:absolute;
    inset:0;
    background:
    radial-gradient(circle at 20% 30%,rgba(71,130,255,.15),transparent 30%),
    radial-gradient(circle at 80% 70%,rgba(71,130,255,.12),transparent 35%);
    pointer-events:none;
}

.route-line{
    position:absolute;
    top:50%;
    left:10%;
    width:80%;
    height:2px;
    background:linear-gradient(90deg,transparent,#1e56c8,#4782ff,transparent);
    animation:moveLine 4s linear infinite;
}

@keyframes moveLine{
    0%{opacity:.4}
    50%{opacity:1}
    100%{opacity:.4}
}

.feature-card{
    position:relative;
    background:rgba(255,255,255,.04);
    backdrop-filter:blur(18px);
    border:1px solid rgba(255,255,255,.1);
    border-radius:6px;
    padding:30px 24px;
    transition:.4s;
    transform-style:preserve-3d;
    overflow:hidden;
}

.feature-card::before{
    content:"";
    position:absolute;
    inset:0;
    padding:1px;
    border-radius:6px;
    background:linear-gradient(135deg,#0f3a8c,#4782ff,rgba(255,255,255,0.2));
    -webkit-mask:
      linear-gradient(#fff 0 0) content-box,
      linear-gradient(#fff 0 0);
    -webkit-mask-composite:xor;
    mask-composite: exclude;
}

.feature-card:hover{
    transform:translateY(-8px);
    box-shadow:0 20px 40px rgba(8,33,84,.4);
    background:rgba(255,255,255,.08);
}

.icon-box{
    width:56px;
    height:56px;
    border-radius:10px;
    background:linear-gradient(135deg,#0f3a8c,#1e56c8);
    display:flex;
    align-items:center;
    justify-content:center;
    margin-bottom:20px;
    box-shadow:0 10px 20px rgba(8,33,84,.4);
}

.icon-box i{
    color:#fff;
    font-size:24px;
    animation:pulse 2s infinite;
}

@keyframes pulse{
    0%,100%{
        transform:scale(1);
    }
    50%{
        transform:scale(1.12);
    }
}

.reveal{
    opacity:1 !important;
    transform:translateY(0) !important;
}

.feature-card{
    opacity:0;
    transform:translateY(50px);
}

@media(max-width:991px){
    .logistics-features{
        grid-template-columns:repeat(2,1fr);
    }
}

@media(max-width:600px){
    .logistics-features{
        grid-template-columns:1fr;
    }

    .route-line{
        display:none;
    }
}
"""

css_content += new_css

with open('src/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

new_html_block = """          <!-- PREMIUM LOGISTICS FEATURES -->
          <div class="logistics-features w-full relative z-20">
              <div class="route-line"></div>

              <div class="feature-card">
                  <div class="icon-box">
                      <i class="fa-solid fa-shield-halved"></i>
                  </div>
                  <h3 class="font-mono text-[11px] font-bold text-white uppercase tracking-wider mb-2">RELIABLE & SAFE</h3>
                  <p class="font-sans text-[12px] text-white/70 leading-relaxed">Secure asset handling guaranteed at every step of global transit.</p>
              </div>

              <div class="feature-card">
                  <div class="icon-box">
                      <i class="fa-solid fa-truck-fast"></i>
                  </div>
                  <h3 class="font-mono text-[11px] font-bold text-white uppercase tracking-wider mb-2">ON-TIME DELIVERY</h3>
                  <p class="font-sans text-[12px] text-white/70 leading-relaxed">Timely priority shipping solutions keeping your supply chain ahead.</p>
              </div>

              <div class="feature-card">
                  <div class="icon-box">
                      <i class="fa-solid fa-globe"></i>
                  </div>
                  <h3 class="font-mono text-[11px] font-bold text-white uppercase tracking-wider mb-2">GLOBAL NETWORK</h3>
                  <p class="font-sans text-[12px] text-white/70 leading-relaxed">Strong direct alliances with global ocean carriers & air lines.</p>
              </div>

              <div class="feature-card">
                  <div class="icon-box">
                      <i class="fa-solid fa-headset"></i>
                  </div>
                  <h3 class="font-mono text-[11px] font-bold text-white uppercase tracking-wider mb-2">DEDICATED SUPPORT</h3>
                  <p class="font-sans text-[12px] text-white/70 leading-relaxed">Dubai operations desk available 24/7/365 to manage dispatch.</p>
              </div>
          </div>"""

# Find the start of the block
start_tag = r'          <!-- PREMIUM LOGISTICS FEATURES -->\n          <div class="logistics-features w-full relative z-20">'
end_tag = r'              </div>\n          </div>'
match = re.search(start_tag + r'.*?' + end_tag, html_content, re.DOTALL)
if match:
    html_content = html_content[:match.start()] + new_html_block + html_content[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("index.html updated successfully.")
else:
    print("Could not find the HTML block to replace.")
