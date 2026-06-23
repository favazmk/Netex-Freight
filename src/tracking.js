// Tracking Logic using Firebase Cloud Firestore (Compat Mode for file:// usage)

const firebaseConfig = {
  projectId: "netex-freight-tracking",
  appId: "1:337952360001:web:e9f68838fddbfee425a8c0",
  storageBucket: "netex-freight-tracking.firebasestorage.app",
  apiKey: "AIzaSyB0GYBEHSsoX6ETDH6jErZl9WFNQ-5087o",
  authDomain: "netex-freight-tracking.firebaseapp.com",
  messagingSenderId: "337952360001"
};

// Initialize Firebase only if config is provided
let db = null;
if (firebaseConfig.apiKey && window.firebase) {
  // Guard against duplicate initialization (if another script already initialized Firebase)
  if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
  }
  db = firebase.firestore();
}

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("tracking-search-form");
  const input = document.getElementById("tracking-input-number");
  const errorMsg = document.getElementById("tracking-error-msg");
  const resultsContainer = document.getElementById("tracking-results-container");
  
  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    
    const trackingNumber = input.value.trim().toUpperCase();
    if (!trackingNumber) return;

    // Reset UI
    errorMsg.classList.add("hidden");
    resultsContainer.classList.add("hidden");
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.innerText;
    submitBtn.innerText = "SEARCHING...";
    submitBtn.disabled = true;

    try {
      if (!db) {
        // Mock fallback if Firebase is not yet configured
        console.warn("Firebase not configured. Showing mock data for testing.");
        await new Promise(r => setTimeout(r, 800)); // Simulate network
        
        if (trackingNumber === "NETEX10001") {
          renderTrackingData({
            trackingNumber: "NETEX10001",
            status: "IN TRANSIT",
            origin: "Dubai, UAE",
            destination: "London, UK",
            timeline: [
              { date: "2026-06-20", time: "08:00 AM", status: "Cargo Received at Jebel Ali Port" },
              { date: "2026-06-21", time: "14:30 PM", status: "Customs Cleared & Loaded onto Vessel" },
              { date: "2026-06-22", time: "09:15 AM", status: "In Transit - Expected arrival in 12 days" }
            ]
          });
        } else {
          errorMsg.classList.remove("hidden");
        }
      } else {
        // Real Firebase Query (Compat Syntax)
        const shipmentsRef = db.collection("shipments");
        const querySnapshot = await shipmentsRef.where("trackingNumber", "==", trackingNumber).get();

        if (querySnapshot.empty) {
          errorMsg.classList.remove("hidden");
        } else {
          // Get the first matching document
          const shipmentData = querySnapshot.docs[0].data();
          renderTrackingData(shipmentData);
        }
      }
    } catch (error) {
      console.error("Error fetching tracking data:", error);
      errorMsg.innerText = "System error retrieving tracking data. Please try again later.";
      errorMsg.classList.remove("hidden");
    } finally {
      submitBtn.innerText = originalText;
      submitBtn.disabled = false;
    }
  });
});

function renderTrackingData(data) {
  document.getElementById("tracking-display-number").innerText = data.trackingNumber || "N/A";
  document.getElementById("tracking-display-status").innerText = data.status || "UNKNOWN";
  document.getElementById("tracking-display-origin").innerText = data.origin || "N/A";
  document.getElementById("tracking-display-destination").innerText = data.destination || "N/A";

  const timelineList = document.getElementById("tracking-timeline-list");
  timelineList.innerHTML = ""; // Clear existing
  
  // Render Horizontal Stepper
  const globalStatuses = ["ORDER RECEIVED", "IN TRANSIT", "CUSTOMS CLEARANCE", "OUT FOR DELIVERY", "DELIVERED"];
  const currentStatus = data.status || "UNKNOWN";
  
  // If ON HOLD, find the last known status from timeline or just show error state
  // We'll just let the stepper handle standard statuses. If ON HOLD, we'll mark everything up to current as complete, and the current as red.
  let currentIndex = globalStatuses.indexOf(currentStatus);
  const isOnHold = currentStatus === "ON HOLD";
  if (isOnHold) {
     // If it's on hold, it might be stuck at IN TRANSIT or CUSTOMS. 
     // We'll just highlight the whole stepper as red up to the first 3 or whatever we guess.
     // For simplicity, let's just find the last timeline event that wasn't ON HOLD.
     const lastGood = [...(data.timeline||[])].reverse().find(e => !e.status.includes("ON HOLD"));
     // If we can't find one, default to 1 (IN TRANSIT)
     currentIndex = 1; 
  }

  const stepperContainer = document.getElementById("tracking-stepper");
  if (stepperContainer) {
    const totalSteps = globalStatuses.length;
    const progressPercent = currentIndex >= 0 ? (currentIndex / (totalSteps - 1)) * 100 : 0;

    let stepperHTML = '';

    // Background gray line (absolute, behind circles)
    stepperHTML += `<div style="position:absolute; left:48px; right:48px; top:18px; height:4px; background:#e4e4e7; border-radius:9999px;"></div>`;

    // Progress colored line overlay
    if (isOnHold && currentIndex >= 0) {
      stepperHTML += `<div style="position:absolute; left:48px; top:18px; height:4px; background:#ef4444; border-radius:9999px; width:calc((100% - 96px) * ${progressPercent / 100});"></div>`;
    } else if (currentIndex > 0) {
      stepperHTML += `<div style="position:absolute; left:48px; top:18px; height:4px; background:#011d50; border-radius:9999px; width:calc((100% - 96px) * ${progressPercent / 100});"></div>`;
    }

    // Animated moving gradient segment (at leading edge)
    if (!isOnHold && currentIndex >= 0 && currentIndex < totalSteps - 1) {
      const animStart = currentIndex > 0 ? (currentIndex / (totalSteps - 1)) * 100 : 0;
      const segmentWidth = (1 / (totalSteps - 1)) * 100;
      stepperHTML += `<div class="moving-gradient" style="position:absolute; top:18px; height:4px; border-radius:9999px; overflow:hidden; left:calc(48px + (100% - 96px) * ${animStart / 100}); width:calc((100% - 96px) * ${segmentWidth / 100});"></div>`;
    }

    // Circle nodes on top
    globalStatuses.forEach((status, idx) => {
      const isCompleted = idx <= currentIndex;
      const isActive = idx === currentIndex;

      let circleBg = isCompleted ? '#011d50' : '#e4e4e7';
      let circleColor = isCompleted ? '#ffffff' : '#a1a1aa';
      let labelStyle = isCompleted ? 'color:#011d50; font-weight:800;' : 'color:#a1a1aa; font-weight:700;';
      const icon = isActive ? (isOnHold ? 'alert-circle' : 'truck') : (isCompleted ? 'check' : 'circle');

      if (isOnHold && isActive) {
        circleBg = '#ef4444';
        labelStyle = 'color:#dc2626; font-weight:800;';
      }

      const ringStyle = isActive
        ? `box-shadow: 0 0 0 4px ${isOnHold ? 'rgba(239,68,68,0.2)' : 'rgba(1,29,80,0.2)'}, 0 10px 15px -3px rgba(0,0,0,0.1);`
        : '';

      stepperHTML += `
        <div style="flex:1; display:flex; flex-direction:column; align-items:center; position:relative; z-index:10;">
          <div style="width:40px; height:40px; border-radius:50%; display:flex; align-items:center; justify-content:center; background:${circleBg}; color:${circleColor}; ${ringStyle}">
            <i data-lucide="${icon}" style="width:20px; height:20px;"></i>
          </div>
          <span style="font-size:9px; ${labelStyle} text-transform:uppercase; letter-spacing:0.1em; text-align:center; line-height:1.2; margin-top:8px; width:96px;">${status}</span>
        </div>
      `;
    });

    stepperContainer.innerHTML = stepperHTML;
  }

  // Render Vertical Stepper for Mobile
  const verticalStepperContainer = document.getElementById("tracking-stepper-vertical");
  if (verticalStepperContainer) {
    const totalSteps = globalStatuses.length;
    let vStepperHTML = '<div class="relative flex flex-col gap-6 ml-2">';

    // Background gray vertical line
    vStepperHTML += `<div style="position:absolute; left:18px; top:18px; bottom:18px; width:4px; background:#e4e4e7; border-radius:9999px; z-index:0;"></div>`;

    // Progress colored vertical line overlay
    if (currentIndex > 0) {
      const progressPercent = currentIndex >= 0 ? (currentIndex / (totalSteps - 1)) * 100 : 0;
      const lineColor = isOnHold ? '#ef4444' : '#011d50';
      vStepperHTML += `<div style="position:absolute; left:18px; top:18px; width:4px; background:${lineColor}; border-radius:9999px; height:calc((100% - 36px) * ${progressPercent / 100}); z-index:1;"></div>`;
    }

    globalStatuses.forEach((status, idx) => {
      const isCompleted = idx <= currentIndex;
      const isActive = idx === currentIndex;

      let circleBg = isCompleted ? '#011d50' : '#e4e4e7';
      let circleColor = isCompleted ? '#ffffff' : '#a1a1aa';
      let labelStyle = isCompleted ? 'color:#011d50; font-weight:800;' : 'color:#a1a1aa; font-weight:700;';
      const icon = isActive ? (isOnHold ? 'alert-circle' : 'truck') : (isCompleted ? 'check' : 'circle');

      if (isOnHold && isActive) {
        circleBg = '#ef4444';
        labelStyle = 'color:#dc2626; font-weight:800;';
      }

      const ringStyle = isActive
        ? `box-shadow: 0 0 0 4px ${isOnHold ? 'rgba(239,68,68,0.2)' : 'rgba(1,29,80,0.2)'}, 0 10px 15px -3px rgba(0,0,0,0.1);`
        : '';

      vStepperHTML += `
        <div class="relative flex items-center gap-4 z-10">
          <div style="width:40px; height:40px; border-radius:50%; display:flex; align-items:center; justify-content:center; background:${circleBg}; color:${circleColor}; ${ringStyle} flex-shrink-0;">
            <i data-lucide="${icon}" style="width:20px; height:20px;"></i>
          </div>
          <span style="font-size:11px; ${labelStyle} text-transform:uppercase; letter-spacing:0.1em; line-height:1.2;">${status}</span>
        </div>
      `;
    });

    vStepperHTML += '</div>';
    verticalStepperContainer.innerHTML = vStepperHTML;
  }

  if (data.timeline && Array.isArray(data.timeline)) {
    // Reverse timeline so newest is at top, if desired. Or keep chronological.
    // Assuming chronological from DB, we display top-down.
    data.timeline.forEach((event, index) => {
      const isLatest = index === data.timeline.length - 1;
      
      const itemHTML = `
        <div class="relative flex gap-6 group">
          <div class="relative flex flex-col items-center">
            <div class="w-12 h-12 rounded-full flex items-center justify-center shrink-0 ${isLatest ? 'bg-brand-blue text-white shadow-lg ring-4 ring-brand-blue/20 animate-pulse' : 'bg-zinc-100 text-zinc-400 group-hover:bg-zinc-200'} transition-all z-10">
               <i data-lucide="${isLatest ? 'truck' : 'check'}" class="w-5 h-5"></i>
            </div>
            ${!isLatest ? '<div class="w-0.5 bg-zinc-200 absolute top-12 bottom-[-1.5rem] group-hover:bg-brand-blue/30 transition-colors"></div>' : ''}
          </div>
          <div class="flex-grow pt-3 pb-6">
            <div class="flex flex-col md:flex-row md:items-baseline gap-1 md:gap-4 mb-1">
              <span class="text-[12px] font-mono ${isLatest ? 'text-brand-blue font-bold' : 'text-zinc-400'} uppercase tracking-widest min-w-[140px]">${event.date} ${event.time || ''}</span>
              <strong class="font-sans text-lg md:text-xl ${isLatest ? 'text-zinc-900 font-black' : 'text-zinc-600'} uppercase">${event.status}</strong>
            </div>
            <p class="text-zinc-500 text-sm mt-1">${isLatest ? 'Shipment is currently passing through this checkpoint.' : 'Checkpoint successfully cleared.'}</p>
          </div>
        </div>
      `;
      timelineList.insertAdjacentHTML("beforeend", itemHTML);
    });
    
    // Refresh lucide icons
    if (window.lucide && typeof window.lucide.createIcons === 'function') {
      window.lucide.createIcons();
    }
  }

  document.getElementById("tracking-results-container").classList.remove("hidden");
  document.getElementById("tracking-results-container").classList.add("animate-fade-in");
}
