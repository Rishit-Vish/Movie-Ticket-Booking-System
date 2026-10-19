<div align="center">

# 🎬 Movie Ticket Booking System

**A web-based ticket booking app with theatre selection, showtimes, a dynamic seat map, and a final ticket summary.**
</div>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Booking Flow](#-booking-flow)
- [Tech Stack](#-tech-stack)
- [Project Evolution](#-project-evolution)
- [Screenshots](#-screenshots)
- [Installation and Setup](#-installation-and-setup)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [What I Learned](#-what-i-learned)
- [Author](#-author)

---

## 📖 Overview

This project simulates the full movie ticket booking experience: choose a theatre, pick a date and showtime, select seats on a visual seat map, pay, and receive a final ticket summary.

It started as a **terminal-based Python program** and was rebuilt as an interactive **Streamlit web application**.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🏛️ **Theatre Selection** | Choose the theatre to book in |
| 📅 **Date and Showtime Booking** | Pick a date and an available showtime |
| 💺 **Dynamic Seat Map** | Visual seat layout with aisle spacing |
| 💰 **Category-Based Pricing** | Ticket price depends on the seat category |
| 💳 **Payment Flow** | Step-by-step payment before confirmation |
| 🎟️ **Final Ticket Summary** | Booking details shown after payment |

---

## 🔄 Booking Flow

```
Select Theatre → Choose Date & Showtime → Pick Seats → Payment → Ticket Summary
```

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| **Language** | Python |
| **Web Framework** | Streamlit |

---

## 🌱 Project Evolution

| Stage | Description |
|---|---|
| **Version 1** | Terminal-based Python program |
| **Version 2** | Rebuilt as a Streamlit web application with a visual seat map and a guided booking flow |

Moving from a terminal program to a web interface meant redesigning how users interact with the app: from typed input to clicking seats, dates, and options.

---

## 📸 Screenshots

<!-- Add screenshots here, for example:

| Theatre Selection | Seat Map |
|:---:|:---:|
| ![Theatre](Screenshots/theatre-selection.png) | ![Seats](Screenshots/seat-map.png) |

| Payment | Ticket Summary |
|:---:|:---:|
| ![Payment](Screenshots/payment.png) | ![Ticket](Screenshots/ticket-summary.png) |
-->

---

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Rishit-Vish/Movie-Ticket-Booking-System.git
cd Movie-Ticket-Booking-System
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

**Windows**
```bash
.venv\Scripts\activate
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install streamlit
```

### 4. Run the app

```bash
streamlit run app.py
```

> 👉 **FILL: replace `app.py` with the name of your main file.**

The app opens in your browser at **http://localhost:8501**.

---

## ⚠️ Limitations

- 👉 **FILL: state whether the payment step is simulated (no real money) or connected to a payment service.**
- 👉 **FILL: state whether bookings are saved after the app closes, or reset each time.**

---

## 🔮 Future Improvements

These are ideas I would add next:

- [ ] Save bookings to a database or file so they persist
- [ ] Prevent double-booking of the same seat across sessions
- [ ] Add user login and booking history
- [ ] Add automated tests for pricing and seat selection
- [ ] Deploy the app online for a live demo

---

## 💡 What I Learned

Rebuilding this project from a terminal program into a web app taught me how to design a **multi-step user flow**, manage state between steps, and present information visually instead of through text prompts.

---

## 👤 Author

**Rishit Vishwakarma**

🔗 GitHub: [Rishit-Vish](https://github.com/Rishit-Vish)
