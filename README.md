# Task 2 – Two-Dashboard AI Feedback System (Web-Based)

This project is a web-based AI-powered feedback system built as part of the **AI Intern Take-Home Assessment**.  
It consists of two dashboards:
- A **User Dashboard** for submitting feedback
- An **Admin Dashboard** for monitoring and analytics

The system uses **Google Gemini API** to:
- Generate AI replies
- Summarize feedback
- Suggest admin actions

All data is stored in a shared **CSV file (`data.csv`)**.

---

## GitHub Repository
https://github.com/Abhishek-6405/task2-ai-feedback-system

---

## Features

### User Dashboard
- Select star rating (1–5)
- Write a short review
- Submit feedback
- Receive AI-generated response instantly
- Data is saved to CSV

---

### Admin Dashboard
- Live view of all submissions
- Shows:
  - Timestamp
  - User rating
  - User review
  - AI response
  - AI summary
  - AI recommended action
- Basic analytics

Both dashboards use the **same data.csv file**.

---

## Project Structure

task2-ai-feedback-system/
│
├── app_user.py
├── app_admin.py
├── data.csv
├── requirements.txt
├── README.md
├── REPORT.md
└── task2env/   (ignored)

---

## Setup Instructions

### 1. Clone Repository

git clone https://github.com/Abhishek-6405/task2-ai-feedback-system.git  
cd task2-ai-feedback-system

---

### 2. Create Virtual Environment

python -m venv task2env

Activate:

task2env\Scripts\activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Set Gemini API Key

setx GEMINI_API_KEY "YOUR_API_KEY"

Restart terminal after setting the key.

---

### 5. Run User Dashboard

streamlit run app_user.py

---

### 6. Run Admin Dashboard

streamlit run app_admin.py

---

## AI Usage
Google Gemini API is used for:
- User response generation
- Review summarization
- Recommended admin actions

Only **prompt engineering** is used.  
No model fine-tuning.

---

## Data Storage

All feedback is stored in:
data.csv

The file contains:
- Timestamp
- User rating
- User review
- AI response
- AI summary
- AI recommended action

---

## Deployment

Both dashboards are deployed online using platforms like:
- Streamlit Cloud
- Render
- HuggingFace Spaces

Deployment links will be shared in the final submission.

---

## Report

Detailed explanation is available in:
REPORT.md

To create PDF:
- Open REPORT.md
- Copy content to Google Docs / Word
- Export as PDF
- Submit PDF link in Google Form

---

## .gitignore

task2env/  
__pycache__/  
.env  
.ipynb_checkpoints/

---

## Author

Abhishek Maurya  
AI Intern – Take Home Assignment

---

## Notes
- Both dashboards use the same database
- API key is stored using environment variables
- System works end-to-end
