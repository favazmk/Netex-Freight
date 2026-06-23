# Netex Freight — Global Carrier Network Hub

> A premium, production-grade logistics web platform for **Netex Freight FZE LLC** — a Dubai-based cargo carrier operating across international sea, air, and land freight corridors.

🔗 **Live Site:** [https://favazmk.github.io/Netex-Freigh/](https://favazmk.github.io/Netex-Freight/)

---

## 📋 Overview

Netex Freight is a multi-page, single-page application (SPA) built as a professional digital hub for a real-world freight logistics company headquartered in Dubai, UAE. The site features an immersive hero experience, interactive global route mapping, real-time cargo tracking powered by Firebase Firestore, and a secure admin portal for shipment dispatch management.

---

## 🛠 Tech Stack

| Layer         | Technology                                                  |
| ------------- | ----------------------------------------------------------- |
| **Structure** | Semantic HTML5                                              |
| **Styling**   | Tailwind CSS (CDN) + Custom CSS with CSS Variables          |
| **Logic**     | Vanilla JavaScript (ES6+)                                   |
| **Mapping**   | Leaflet.js — Interactive tile-based world map               |
| **Icons**     | Lucide Icons (CDN)                                          |
| **Backend**   | Firebase Firestore (real-time database)                     |
| **Auth**      | Firebase Authentication (admin portal)                      |
| **Fonts**     | Inter, JetBrains Mono (Google Fonts)                        |

---

## ✨ Features

### Public-Facing Website
- **Immersive Hero Section** — Full-viewport hero with 3D container imagery, giant background typography, and a custom SVG low-poly world map underlay with animated global route lines and pulsing hub nodes
- **Interactive Global Route Map** — Leaflet.js-powered map with clickable dispatch hub navigation (DXB, NYC, EUR, SIN, TYO, LAX, BOM, PTY) and a live terminal feed overlay
- **Hash-Based SPA Routing** — Client-side page routing (`#home`, `#services`, `#about-us`, `#why-choose-us`, `#tracking`, `#contact-us`) with seamless transitions and no full-page reloads
- **Services Catalog** — Desktop: interactive hub-board with sector selection rail and detail viewport; Mobile: responsive accordion layout
- **Real-Time Cargo Tracking** — Search by AWB, container number, or Netex Tracking ID; displays a horizontal stepper, vertical timeline, origin/destination, and live shipment status pulled from Firestore
- **Contact Inquiry Form** — Direct submission form with field validation and success confirmation
- **Scroll-Reveal Animations** — 3D blur-reveal entrance animations using Intersection Observer with GPU-accelerated `transform: translate3d()` and `will-change` optimizations
- **Sticky Contact Widget** — Floating FAB with expandable quick-access links to Phone and WhatsApp
- **Brochure Modal** — Overlay modal for the company corporate brief document with simulated PDF download
- **Responsive Design** — Fully adaptive layout across mobile, tablet, and desktop breakpoints
- **Active Nav Highlighting** — Scroll-spy-style navigation that highlights the current section

### Admin Dispatch Portal
- **Secure Authentication** — Firebase Auth-gated login with email/password and password visibility toggle
- **Shipment CRUD** — Create new shipments with tracking number, origin, destination, initial status, and checkpoint
- **Live Shipment Table** — Real-time Firestore-synced table of all active shipments with inline status updates and checkpoint additions
- **Search & Filter** — Client-side search across tracking numbers and routes
- **Timeline Management** — Append new milestones to any shipment's tracking history directly from the admin dashboard

---

## 📁 Project Structure

```
Netex-Freigh/
├── index.html              # Main SPA entry point (public website)
├── admin.html              # Secure admin dispatch portal
├── metadata.json           # Project metadata configuration
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
├── assets/                 # Static media assets
│   ├── logo-cropped.png
│   ├── logo-cropped-transparent.png
│   ├── favicon-transparent.png
│   └── blue_container_flat_transparent.png
└── src/                    # Source code
    ├── style.css           # Global styles & Tailwind overrides
    ├── main.js             # Core app logic, routing, map, animations
    ├── tracking.js         # Cargo tracking module (Firestore queries)
    ├── admin.js            # Admin portal logic (auth, CRUD, Firestore)
    └── admin.css           # Admin portal styles
```

---

## 🚀 Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, Edge)
- [Node.js](https://nodejs.org/) (optional — only if using a local dev server)

### Run Locally

Since this is a static site using CDN dependencies, you can serve it with any HTTP server:

```bash
# Clone the repository
git clone https://github.com/favazmk/Netex-Freigh.git
cd Netex-Freigh

# Option 1: VS Code Live Server
# Install the "Live Server" extension and click "Go Live"

# Option 2: Node.js http-server
npx http-server . -p 3000

# Option 3: Python
python -m http.server 3000
```

Then open `http://localhost:3000` in your browser.

### Firebase Configuration

The app connects to a Firebase Firestore backend for real-time tracking data and admin authentication. To use your own Firebase project:

1. Create a project at [Firebase Console](https://console.firebase.google.com/)
2. Enable **Firestore Database** and **Email/Password Authentication**
3. Replace the Firebase config object in `src/main.js` and `src/admin.js` with your project credentials

---

## 📄 License

© 2026 Netex Freight FZE LLC. All rights reserved.
