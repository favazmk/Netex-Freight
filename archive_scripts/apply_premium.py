import re

# 1. Update index.html (Font Awesome + HTML block)
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add fontawesome if not exists
if 'font-awesome' not in content and 'fontawesome' not in content:
    head_end = content.find('</head>')
    fa_link = '  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n'
    content = content[:head_end] + fa_link + content[head_end:]

# Replace the HTML block
html_replacement = """          <!-- PREMIUM LOGISTICS FEATURES -->
          <div class="logistics-features w-full relative z-20">
              <div class="route-line"></div>

              <div class="feature-card">
                  <div class="icon-box">
                      <i class="fa-solid fa-shield-halved"></i>
                  </div>
                  <h3>RELIABLE & SAFE</h3>
                  <p>Secure asset handling guaranteed at every step of global transit.</p>
              </div>

              <div class="feature-card">
                  <div class="icon-box">
                      <i class="fa-solid fa-truck-fast"></i>
                  </div>
                  <h3>ON-TIME DELIVERY</h3>
                  <p>Timely priority shipping solutions keeping your supply chain ahead.</p>
              </div>

              <div class="feature-card">
                  <div class="icon-box">
                      <i class="fa-solid fa-globe"></i>
                  </div>
                  <h3>GLOBAL NETWORK</h3>
                  <p>Strong direct alliances with global ocean carriers & air lines.</p>
              </div>

              <div class="feature-card">
                  <div class="icon-box">
                      <i class="fa-solid fa-headset"></i>
                  </div>
                  <h3>DEDICATED SUPPORT</h3>
                  <p>Dubai operations desk available 24/7/365 to manage dispatch.</p>
              </div>
          </div>"""

# Find the start of the block
start_tag = r'          <!-- HERO FLOATING BADGES ROW -->\n          <div class="w-full bg-zinc-50/40 relative z-20 pb-12 pt-6">'
end_tag = r'            </div>\n          </div>'
match = re.search(start_tag + r'.*?' + end_tag, content, re.DOTALL)
if match:
    content = content[:match.start()] + html_replacement + content[match.end():]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("index.html updated successfully.")
else:
    print("Could not find the HTML block to replace.")

# 2. Append CSS
css_code = """
/* Premium Logistics Features Section */
.logistics-features{
    position:relative;
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:30px;
    padding:80px 5%;
    background:linear-gradient(135deg,#07152f,#0d1f4d,#092a7d);
    overflow:hidden;
}

.logistics-features::before{
    content:"";
    position:absolute;
    inset:0;
    background:
    radial-gradient(circle at 20% 30%,rgba(0,102,255,.15),transparent 30%),
    radial-gradient(circle at 80% 70%,rgba(0,102,255,.12),transparent 35%);
    pointer-events:none;
}

.route-line{
    position:absolute;
    top:50%;
    left:10%;
    width:80%;
    height:2px;
    background:linear-gradient(90deg,transparent,#3d7cff,#7fb3ff,transparent);
    animation:moveLine 4s linear infinite;
}

@keyframes moveLine{
    0%{opacity:.4}
    50%{opacity:1}
    100%{opacity:.4}
}

.feature-card{
    position:relative;
    background:rgba(255,255,255,.08);
    backdrop-filter:blur(18px);
    border:1px solid rgba(255,255,255,.15);
    border-radius:24px;
    padding:40px 30px;
    transition:.4s;
    transform-style:preserve-3d;
    overflow:hidden;
}

.feature-card::before{
    content:"";
    position:absolute;
    inset:0;
    padding:1px;
    border-radius:24px;
    background:linear-gradient(135deg,#0A4DFF,#4A90FF,#A8C5FF);
    -webkit-mask:
      linear-gradient(#fff 0 0) content-box,
      linear-gradient(#fff 0 0);
    -webkit-mask-composite:xor;
    mask-composite: exclude;
}

.feature-card:hover{
    transform:translateY(-12px);
    box-shadow:0 25px 60px rgba(0,102,255,.35);
}

.icon-box{
    width:80px;
    height:80px;
    border-radius:20px;
    background:linear-gradient(135deg,#0A4DFF,#4A90FF);
    display:flex;
    align-items:center;
    justify-content:center;
    margin-bottom:25px;
    box-shadow:0 10px 30px rgba(0,102,255,.4);
}

.icon-box i{
    color:#fff;
    font-size:34px;
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

.feature-card h3{
    color:#fff;
    font-size:18px;
    font-weight:700;
    margin-bottom:15px;
    letter-spacing:1px;
}

.feature-card p{
    color:rgba(255,255,255,.8);
    line-height:1.7;
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

with open('src/style.css', 'a', encoding='utf-8') as f:
    f.write(css_code)
print("CSS appended to src/style.css")

# 3. Append JS
js_code = """
// Premium Logistics Features JS
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.feature-card');

    const observer = new IntersectionObserver(entries=>{
        entries.forEach(entry=>{
            if(entry.isIntersecting){
                entry.target.classList.add('reveal');
            }
        });
    },{
        threshold:0.2
    });

    cards.forEach((card,index)=>{
        card.style.transitionDelay=`${index*0.15}s`;
        observer.observe(card);
    });

    // Premium 3D Tilt
    cards.forEach(card=>{
        card.addEventListener('mousemove',(e)=>{
            const rect=card.getBoundingClientRect();
            const x=e.clientX-rect.left;
            const y=e.clientY-rect.top;

            const rotateY=((x/rect.width)-0.5)*12;
            const rotateX=((y/rect.height)-0.5)*-12;

            card.style.transform=
            `perspective(1000px)
            rotateX(${rotateX}deg)
            rotateY(${rotateY}deg)
            translateY(-10px)`;
        });

        card.addEventListener('mouseleave',()=>{
            card.style.transform='perspective(1000px) rotateX(0) rotateY(0)';
        });
    });
});
"""

with open('src/main.js', 'a', encoding='utf-8') as f:
    f.write(js_code)
print("JS appended to src/main.js")
