# 🔄 SkillSwap — Peer Skill Sharing Network

SkillSwap is a lightweight, responsive web application designed to connect students and peers for mutual skill exchange. Users can list skills they can teach, identify skills they wish to learn, and discover algorithmic peer matches for interactive collaborative learning.

---

## ✨ Features

- **4-Step Onboarding Wizard:** Seamless multi-step registration flow with a real-time progress indicator collecting:
  1. Account Credentials
  2. Personal & Academic Info
  3. Skills to Teach (with instant-add interactive chips)
  4. Skills to Learn
- **Peer Matching Engine:** Displays match percentages and peer recommendations based on user learning interests and skills offered.
- **Dynamic Skill Search:** Instant search filter across available peer skill sets.
- **Profile Management:** View and edit personal profile information, teaching skills, and learning goals in real-time.
- **Session Feedback System:** Interactive 5-star rating and review mechanism for peer learning sessions.
- **Clean Responsive UI:** CSS variables theme, subtle animations, mobile-friendly layouts, and zero external framework dependencies.

---

## 🛠️ Tech Stack

- **HTML5:** Semantic structural layout and form components.
- **CSS3:** Modern CSS with custom properties (variables), Flexbox, CSS Grid layout, and micro-animations.
- **JavaScript (Vanilla JS):** Client-state management, DOM manipulation, interactive step routing, dynamic rendering, and filtering logic.

---

## 📁 Project Structure

```text
skillswap/
├── index.html        # Main single-page application file containing structure, styling, and scripts
└── README.md         # Project documentation
```

---

## 🚀 Getting Started

Since SkillSwap runs as a standalone client-side web application, no build tools or package managers are required.

### Prerequisites
- Any modern web browser (Google Chrome, Mozilla Firefox, Safari, Microsoft Edge).

### Installation & Execution
1. Clone or download this repository:
   ```bash
   git clone https://github.com/your-username/skillswap.git
   ```
2. Navigate to the project folder:
   ```bash
   cd skillswap
   ```
3. Open `index.html` in your web browser:
   - **Option A:** Double-click `index.html` in your file explorer.
   - **Option B:** Serve via VS Code's *Live Server* extension.

---

## ⚙️ How It Works

1. **Onboarding:** Complete the initial 4-step setup. Click the suggestion chips (e.g., `+ Python`, `+ Public Speaking`) to populate skills quickly.
2. **Dashboard Navigation:** Use the sticky top navigation bar to toggle between **Home**, **Find a Skill**, **Matches**, **Profile**, and **Feedback**.
3. **Finding Peers:** Filter through the peer grid on the **Find a Skill** page using the live search bar.
4. **Managing Profile:** Toggle the **Edit Profile** button under the Profile section to adjust contact details or update your skill list.

---

## 📋 Future Enhancements

- [ ] **Backend Integration:** Connect to a Node.js/Express backend with MongoDB or PostgreSQL database support.
- [ ] **Authentication:** JWT-based user login and session management.
- [ ] **Direct Messaging / Chat:** Real-time peer-to-peer chat for scheduling learning sessions using WebSockets/Socket.io.
- [ ] **Calendar Integration:** Schedule exchange sessions with built-in Google Calendar synchronization.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
