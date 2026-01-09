# 🎯 Number Hunt – Smart Guessing Game (Streamlit)

Number Hunt is a **web-based number guessing game** built using **Python and Streamlit**.  
Unlike traditional guessing games that only show *“too high”* or *“too low”*, this project focuses on **user experience, intelligent feedback, and clean UI design**.

The game runs on **localhost in the browser**, supports **multiple difficulty levels**, **hot–cold visual hints**, **theme switching**, and a **rules onboarding system**.

---

## 🚀 Key Features

### 🎮 Difficulty Levels
Choose how challenging you want the game to be:

| Level | Number Range | Attempts |
|------|--------------|----------|
| 🟢 Easy | 1 – 50 | Unlimited |
| 🟡 Medium | 1 – 100 | 10 |
| 🔴 Hard | 1 – 200 | 7 |

---

### 🔥 Smart Hot–Cold Feedback
Instead of generic hints, the game provides **difference-based intelligent feedback**:

- 💥 Correct – You win
- 🔥 Very Hot – Extremely close
- 😍 Hot – Close
- 😐 Warm – A bit far
- 🥶 Cold – Far away

A **visual progress bar** helps users understand how close they are.

---

### 📜 Guess History Panel
All guesses are tracked in a side panel so users can:
- See previous attempts
- Understand patterns
- Improve guessing strategy

---

### 🧾 Rules & Onboarding System
- Rules are shown when the game starts
- Users can **skip rules** if they already know them
- Rules can be **opened anytime** from the sidebar

This mimics real-world application onboarding.

---

### 🎨 Theme Toggle
Users can switch between:
- 💖 Pink Theme (soft & aesthetic)
- 🌙 Dark Theme (professional & clean)

Ensures good readability and accessibility in both modes.

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit**

Only standard Python libraries are used along with Streamlit.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Number-Hunt.git
