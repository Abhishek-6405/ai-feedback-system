import streamlit as st
import pandas as pd
from datetime import datetime
import os
import google.generativeai as genai

# ---------------- CONFIG ----------------
st.set_page_config(page_title="User Feedback Dashboard", layout="centered")
DATA_FILE = "data.csv"

# ---------------- GEMINI SETUP ----------------
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ GEMINI_API_KEY not set in Streamlit Cloud")
    st.stop()

genai.configure(api_key=api_key)

# ✅ ✅ USE SDK-COMPATIBLE MODEL NAME (NO "models/")
model = genai.GenerativeModel("gemini-pro")

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
    prompt = f"""
A user gave a {rating}-star rating and wrote this review:

"{review}"

Return output in EXACTLY this format:

AI_RESPONSE: <one polite reply to user>
SUMMARY: <one short internal summary>
ACTION: <one admin recommended action>
"""

    response = model.generate_content(prompt)
    return response.text


# ---------------- UI ----------------
st.title("📝 User Feedback Portal")

rating = st.selectbox("Select Rating (1–5)", [1, 2, 3, 4, 5])
review = st.text_area("Write your review")

submit = st.button("Submit")

# ---------------- SUBMISSION ----------------
if submit:
    if review.strip() == "":
        st.warning("⚠️ Please enter a review before submitting.")
    else:
        with st.spinner("Generating AI response..."):
            try:
                ai_raw = generate_ai_response(review, rating)
            except Exception as e:
                st.error(str(e))
                ai_raw = ""

        ai_response = "Thank you for your feedback!"
        ai_summary = "Summary unavailable."
        ai_action = "Manual review required."

        for line in ai_raw.splitlines():
            if line.startswith("AI_RESPONSE:"):
                ai_response = line.replace("AI_RESPONSE:", "").strip()
            elif line.startswith("SUMMARY:"):
                ai_summary = line.replace("SUMMARY:", "").strip()
            elif line.startswith("ACTION:"):
                ai_action = line.replace("ACTION:", "").strip()

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
