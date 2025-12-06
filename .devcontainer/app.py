import streamlit as st
import pandas as pd
from datetime import datetime
import os
import requests
import json

# ---------------- CONFIG ----------------
st.set_page_config(page_title="User Feedback Dashboard", layout="centered")
DATA_FILE = "data.csv"

# ---------------- API KEY ----------------
API_KEY = os.getenv("GEMINI_API_KEY")

st.write("✅ API Key Loaded:", bool(API_KEY))  # DEBUG

# ------------- CREATE DATA FILE IF NOT EXISTS -------------
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=[
        "timestamp",
        "user_rating",
        "user_review",
        "ai_response",
        "ai_summary",
        "ai_recommended_action"
    ])
    df.to_csv(DATA_FILE, index=False)

# ---------------- AI FUNCTION ----------------
def generate_ai_response(review, rating):

    if not API_KEY:
        st.error("❌ GEMINI_API_KEY missing in Streamlit secrets.")
        return ""

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent?key={API_KEY}"

    prompt = f"""
A user gave a {rating}-star rating and wrote this review:

{review}

Return output strictly as:

AI_RESPONSE: <reply>
SUMMARY: <summary>
ACTION: <action>
"""

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, json=payload)

    # -------- DEBUG OUTPUT --------
    st.write("🔎 Status Code:", response.status_code)

    if response.status_code != 200:
        st.error("❌ Gemini API Error")
        st.code(response.text)
        return ""

    data = response.json()
    st.write("🧠 Raw AI Output:", data)  # DEBUG

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return ""

# ---------------- UI ----------------
st.title("📝 User Feedback Portal")

rating = st.selectbox("Select Rating (1–5)", [1, 2, 3, 4, 5])
review = st.text_area("Write your review")

submit = st.button("Submit")

# ---------------- SUBMISSION ----------------
if submit:

    if review.strip() == "":
        st.warning("⚠️ Please enter a review.")
        st.stop()

    with st.spinner("Generating AI response..."):
        ai_raw = generate_ai_response(review, rating)

    # ✅ DEFAULTS
    ai_response = "Thank you for your feedback!"
    ai_summary = "Summary unavailable."
    ai_action = "Manual review required."

    # ✅ PARSING
    if ai_raw:
        for line in ai_raw.splitlines():
            if line.startswith("AI_RESPONSE:"):
                ai_response = line.replace("AI_RESPONSE:", "").strip()
            elif line.startswith("SUMMARY:"):
                ai_summary = line.replace("SUMMARY:", "").strip()
            elif line.startswith("ACTION:"):
                ai_action = line.replace("ACTION:", "").strip()

    # ✅ SAVE TO CSV
    new_row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "user_rating": rating,
        "user_review": review,
        "ai_response": ai_response,
        "ai_summary": ai_summary,
        "ai_recommended_action": ai_action
    }

    df = pd.read_csv(DATA_FILE)
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

    st.success("✅ Feedback submitted successfully!")
    st.subheader("🤖 AI Response")
    st.write(ai_response)
