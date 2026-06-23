// Admin Logic using Firebase Cloud Firestore (Compat Mode for file:// usage)

const firebaseConfig = {
  projectId: "netex-freight-tracking",
  appId: "1:337952360001:web:e9f68838fddbfee425a8c0",
  storageBucket: "netex-freight-tracking.firebasestorage.app",
  apiKey: "AIzaSyB0GYBEHSsoX6ETDH6jErZl9WFNQ-5087o",
  authDomain: "netex-freight-tracking.firebaseapp.com",
  messagingSenderId: "337952360001"
};

let auth = null;
let db = null;

if (firebaseConfig.apiKey && window.firebase) {
  firebase.initializeApp(firebaseConfig);
  auth = firebase.auth();
  db = firebase.firestore();
}

document.addEventListener("DOMContentLoaded", () => {
  const loginSection = document.getElementById("admin-login-section");
  const dashboardSection = document.getElementById("admin-dashboard-section");
  
  if (!auth) {
    // If no config, mock login for demo purposes
    console.warn("Firebase not configured. Running in Mock Admin Mode.");
    loginSection.classList.remove("hidden");
    
    document.getElementById("admin-login-form").addEventListener("submit", (e) => {
      e.preventDefault();
      loginSection.classList.add("hidden");
      dashboardSection.classList.remove("hidden");
      dashboardSection.classList.add("block");
    });
    
    document.getElementById("admin-shipment-form").addEventListener("submit", (e) => {
      e.preventDefault();
      document.getElementById("admin-success-msg").classList.remove("hidden");
      setTimeout(() => document.getElementById("admin-success-msg").classList.add("hidden"), 3000);
    });
    
    return;
  }

  // --- Real Firebase Logic ---
  
  window.activeShipmentsData = {};

  window.updateShipmentRow = async function(id) {
    const statusEl = document.getElementById(`status-${id}`);
    const locationEl = document.getElementById(`location-${id}`);
    const btnEl = document.getElementById(`btn-${id}`);
    
    const status = statusEl.value;
    const locationPlace = locationEl.value.trim();
    
    if (!locationPlace) {
      locationEl.focus();
      return; // Force them to enter a checkpoint
    }

    const eventMsg = `${status} - ${locationPlace}`;
    
    btnEl.innerText = "SAVING...";
    btnEl.disabled = true;

    try {
      const docRef = db.collection("shipments").doc(id);
      const docSnap = await docRef.get();

      const now = new Date();
      const dateStr = now.toISOString().split('T')[0];
      const timeStr = now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});

      if (docSnap.exists) {
        const data = docSnap.data();
        const updates = { status: status };
        updates.timeline = firebase.firestore.FieldValue.arrayUnion({ date: dateStr, time: timeStr, status: eventMsg });
        await docRef.update(updates);
      }
      
      btnEl.classList.replace("bg-[#011d50]", "bg-green-600");
      btnEl.innerText = "SAVED!";
      
      setTimeout(() => {
        fetchActiveShipments();
      }, 1000);

    } catch (error) {
      console.error(error);
      btnEl.innerText = "ERROR";
      btnEl.classList.replace("bg-[#011d50]", "bg-red-600");
      setTimeout(() => {
        btnEl.innerText = "UPDATE";
        btnEl.disabled = false;
        btnEl.classList.replace("bg-red-600", "bg-[#011d50]");
      }, 2000);
    }
  };

  async function fetchActiveShipments() {
    if (!db) return;
    const tableBody = document.getElementById("active-shipments-table-body");
    tableBody.innerHTML = '<tr><td colspan="5" class="p-4 text-center text-xs text-zinc-500 italic">Loading active shipments...</td></tr>';
    
    try {
      const snapshot = await db.collection("shipments").limit(50).get();
      if (snapshot.empty) {
        tableBody.innerHTML = '<tr><td colspan="5" class="p-4 text-center text-xs text-zinc-500 italic">No active shipments found.</td></tr>';
        return;
      }
      
      tableBody.innerHTML = '';
      snapshot.forEach(doc => {
        const data = doc.data();
        if (data.trackingNumber) {
          window.activeShipmentsData[data.trackingNumber] = data;
        }
        
        const timelineArr = data.timeline || [];
        // show latest first
        const historyHtml = timelineArr.slice().reverse().map(t => 
          `<div class="font-bold text-zinc-700">${t.status} <span class="font-normal text-zinc-400 font-mono ml-1">${t.date}</span></div>`
        ).join('');

        const html = `
          <tr class="hover:bg-zinc-50 transition-colors group shipment-row">
            <td class="p-3 align-top border-b border-zinc-100">
              <strong class="text-xs font-mono text-zinc-900 block">${data.trackingNumber}</strong>
              <span class="text-[10px] text-zinc-500 uppercase tracking-widest">${data.origin} &rarr; ${data.destination}</span>
            </td>
            <td class="p-3 align-top border-b border-zinc-100 min-w-[200px]">
              <div class="text-[10px] space-y-1 max-h-16 overflow-y-auto pr-2">
                 ${historyHtml || '<span class="text-zinc-400 italic">No milestones yet</span>'}
              </div>
            </td>
            <td class="p-3 align-top border-b border-zinc-100">
              <select id="status-${data.trackingNumber}" class="w-full border border-zinc-300 rounded px-2 py-1.5 text-[10px] font-bold uppercase focus:ring-1 focus:ring-[#011d50] outline-none">
                 <option value="ORDER RECEIVED" ${data.status === 'ORDER RECEIVED' ? 'selected' : ''}>Order Received</option>
                 <option value="IN TRANSIT" ${data.status === 'IN TRANSIT' ? 'selected' : ''}>In Transit</option>
                 <option value="CUSTOMS CLEARANCE" ${data.status === 'CUSTOMS CLEARANCE' ? 'selected' : ''}>Customs Clearance</option>
                 <option value="OUT FOR DELIVERY" ${data.status === 'OUT FOR DELIVERY' ? 'selected' : ''}>Out for Delivery</option>
                 <option value="DELIVERED" ${data.status === 'DELIVERED' ? 'selected' : ''}>Delivered</option>
                 <option value="ON HOLD" ${data.status === 'ON HOLD' ? 'selected' : ''}>On Hold</option>
              </select>
            </td>
            <td class="p-3 align-top border-b border-zinc-100">
              <input type="text" id="location-${data.trackingNumber}" placeholder="e.g. London Port" class="w-full border border-zinc-300 rounded px-2 py-1.5 text-[10px] focus:ring-1 focus:ring-[#011d50] outline-none">
            </td>
            <td class="p-3 align-top text-center border-b border-zinc-100">
              <button onclick="updateShipmentRow('${data.trackingNumber}')" id="btn-${data.trackingNumber}" class="bg-[#011d50] hover:bg-blue-900 text-white font-bold py-1.5 px-3 rounded text-[10px] uppercase tracking-widest transition-colors w-full">Update</button>
            </td>
          </tr>
        `;
        tableBody.insertAdjacentHTML("beforeend", html);
      });
    } catch (e) {
      console.error("Error fetching shipments:", e);
      tableBody.innerHTML = '<tr><td colspan="5" class="p-4 text-center text-xs text-red-500 italic">Error loading shipments.</td></tr>';
    }
  }

  // Search Filter Logic
  document.getElementById("search-active-shipments").addEventListener("input", (e) => {
    const query = e.target.value.toLowerCase().trim();
    const rows = document.querySelectorAll("#active-shipments-table-body tr.shipment-row");
    
    rows.forEach(row => {
      const text = row.innerText.toLowerCase();
      if (text.includes(query)) {
        row.style.display = "";
      } else {
        row.style.display = "none";
      }
    });
  });

  document.getElementById("refresh-shipments-btn").addEventListener("click", fetchActiveShipments);

  // Auth state listener
  auth.onAuthStateChanged((user) => {
    if (user) {
      document.getElementById("admin-container").classList.replace("max-w-lg", "max-w-6xl");
      loginSection.classList.add("hidden");
      dashboardSection.classList.remove("hidden");
      dashboardSection.classList.add("block");
      fetchActiveShipments();
    } else {
      document.getElementById("admin-container").classList.replace("max-w-6xl", "max-w-lg");
      loginSection.classList.remove("hidden");
      dashboardSection.classList.add("hidden");
      dashboardSection.classList.remove("block");
    }
  });

  // Login Form Submission
  const errorBox = document.getElementById("admin-login-error");
  
  // Clear error on input
  document.getElementById("admin-email").addEventListener("input", () => errorBox.classList.add("hidden"));
  document.getElementById("admin-password").addEventListener("input", () => errorBox.classList.add("hidden"));
  
  // Toggle password visibility
  document.getElementById("toggle-password").addEventListener("click", () => {
    const pwInput = document.getElementById("admin-password");
    const icon = document.getElementById("toggle-password-icon");
    if (pwInput.type === "password") {
      pwInput.type = "text";
      icon.setAttribute("data-lucide", "eye-off");
    } else {
      pwInput.type = "password";
      icon.setAttribute("data-lucide", "eye");
    }
    if (window.lucide) window.lucide.createIcons();
  });

  document.getElementById("admin-login-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const email = document.getElementById("admin-email").value;
    const password = document.getElementById("admin-password").value;
    
    errorBox.classList.add("hidden");

    try {
      await auth.signInWithEmailAndPassword(email, password);
      // Success is handled by auth state listener
    } catch (error) {
      console.error(error);
      errorBox.innerText = "Invalid credentials. Please try again.";
      errorBox.classList.remove("hidden");
    }
  });

  // Logout
  document.getElementById("admin-logout-btn").addEventListener("click", () => {
    auth.signOut();
  });

  // Create New Shipment Data
  document.getElementById("admin-create-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    const successBox = document.getElementById("create-success-msg");
    successBox.classList.add("hidden");

    const id = document.getElementById("create-id").value.trim().toUpperCase();
    const origin = document.getElementById("create-origin").value.trim();
    const destination = document.getElementById("create-destination").value.trim();
    const status = document.getElementById("create-status").value;
    const checkpoint = document.getElementById("create-checkpoint").value.trim();
    
    if (!id || !checkpoint) return;

    try {
      const docRef = db.collection("shipments").doc(id);
      
      const now = new Date();
      const dateStr = now.toISOString().split('T')[0];
      const timeStr = now.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
      const eventMsg = `${status} - ${checkpoint}`;

      const newShipment = {
        trackingNumber: id,
        origin: origin,
        destination: destination,
        status: status,
        timeline: [{ date: dateStr, time: timeStr, status: eventMsg }]
      };
      await docRef.set(newShipment);
      
      successBox.classList.remove("hidden");
      document.getElementById("create-id").value = "";
      document.getElementById("create-origin").value = "";
      document.getElementById("create-destination").value = "";
      document.getElementById("create-checkpoint").value = "";
      document.getElementById("create-status").value = "ORDER RECEIVED";
      
      fetchActiveShipments();
      
      setTimeout(() => successBox.classList.add("hidden"), 3000);

    } catch (error) {
      console.error(error);
      alert("Error creating shipment. See console.");
    }
  });
});
