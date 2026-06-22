import re

with open('src/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add ID to mobile accordion button
content = content.replace(
    "const btn = document.createElement('button');\n    btn.className =",
    "const btn = document.createElement('button');\n    btn.id = `mobile-accordion-${srv.id}`;\n    btn.className ="
)

# 2. Update scroll logic in openServiceHubDivision
old_scroll = """  // Scroll slightly down to the services layout to make it obvious
  setTimeout(() => {
    const servicesSection = document.getElementById('page-services');
    if (servicesSection) {
      servicesSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }, 100);"""

new_scroll = """  // Scroll to the exact interactive section depending on device
  setTimeout(() => {
    if (window.innerWidth < 1024) {
      // Mobile: scroll the specific opened accordion panel into the center of the screen
      const mobileItem = document.getElementById(`mobile-accordion-${id}`);
      if (mobileItem) {
        mobileItem.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    } else {
      // Desktop: scroll the interactive hub board into the center of the screen
      const desktopHub = document.getElementById('services-desktop-hub');
      if (desktopHub) {
        desktopHub.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    }
  }, 100);"""

content = content.replace(old_scroll, new_scroll)

with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated JS scroll logic.")
