# ✅ Task 2 – Two-Dashboard AI Feedback System (Web-Based)

This project is a complete **AI-powered user feedback collection and analysis system** built using **Streamlit and Google Gemini AI** as part of the **AI Intern Take-Home Assessment**.

It allows:
- Users to submit feedback and ratings
- AI to generate a response, summary, and admin action
- Admin to view, analyze, and download all feedback

All features are deployed in a **single cloud application** with **real-time synchronization**.

---

## 🚀 Live Deployment Links

✅ **User & Admin Combined Deployment (Final Working App):**  
👉 (https://task2-ai-feedback-system-keviekvszoauecvlncxax4.streamlit.app/) 

_(Single deployment contains both User Feedback page and Admin Dashboard via sidebar navigation.)_

---

## 📌 Problem Statement

Design and deploy an **AI-powered feedback system** where:
- Users can submit ratings and textual feedback
- AI automatically generates:
  - A polite user reply
  - An internal feedback summary
  - A recommended admin action
- Admin can view analytics and export feedback data

---

## 🧠 Deployment Issue Faced & Final Technical Resolution

### ❌ Initial Deployment Approach (Two Separate Apps)

Initially, the project was deployed as two separate Streamlit applications:

- `app_user.py` → User feedback submission app  
- `app_admin.py` → Admin dashboard app  

Both applications worked **perfectly in local execution**.

---

### ⚠️ Issue After Deployment

On **Streamlit Cloud**:

- Each deployed app runs in a **separate isolated container**
- Every container has its **own independent file system**

As a result:

- User app wrote feedback into its own `data.csv`
- Admin app tried to read a **different `data.csv`**
- Therefore, **admin could not see user submissions**

✅ This worked **locally** but failed on **cloud deployment** due to **container isolation**.

---

### ✅ Final Correct Industry-Standard Solution

To permanently solve the issue:

- Merged **User & Admin** into a **single Streamlit application**
- Implemented **sidebar navigation**
- Used **one shared `data.csv` file**

✅ **Final Result:**
- Real-time data synchronization  
- Fully cloud-compatible  
- Stable production deployment  

✅ This fix demonstrates **real-world cloud debugging and deployment architecture handling**.

---

## 🎯 Features

### 👤 User Feedback Page
- 1–5 star rating system  
- Text-based review submission  
- AI-generated:
  - Polite user response  
  - Internal summary  
  - Admin recommended action  
- Feedback stored automatically in CSV  
- Input validation and AI fallback handling  

---

### 👨‍💼 Admin Dashboard
- View all feedback in live table  
- Rating distribution bar chart  
- Download complete feedback CSV  
- Auto-refresh after every submission  

---

### 🤖 AI Intelligence
- Powered by **Google Gemini API**
- Auto-detects supported model
- Structured output parsing:
  - `AI_RESPONSE`
  - `SUMMARY`
  - `ACTION`
- Fail-safe fallback handling if AI fails

---

## 🛠 Technology Stack
- Python  
- Streamlit  
- Google Gemini AI  
- Pandas  
- CSV File System  
- GitHub  
- Streamlit Cloud  
