import re

with open('src/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the onclick handler
content = content.replace(
    "onclick=\"window.location.hash='#services'; selectServiceHubDivision('${srv.id}')\"",
    "onclick=\"window.openServiceHubDivision('${srv.id}')\""
)

# Append the global openServiceHubDivision function at the end
new_function = """

// Global function to open a service from anywhere
window.openServiceHubDivision = function(id) {
  // Navigate to services page
  window.location.hash = '#services';
  
  // Set desktop active ID
  if (typeof selectServiceHubDivision === 'function') {
    selectServiceHubDivision(id);
  }
  
  // Set mobile active ID to open the accordion
  if (typeof activeMobileServiceId !== 'undefined') {
    activeMobileServiceId = id;
    if (typeof renderServicesMobileAccordion === 'function') {
      renderServicesMobileAccordion();
    }
  }
  
  // Scroll slightly down to the services layout to make it obvious
  setTimeout(() => {
    const servicesSection = document.getElementById('page-services');
    if (servicesSection) {
      servicesSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }, 100);
};
"""

content += new_function

with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated JS with global openServiceHubDivision function.")
