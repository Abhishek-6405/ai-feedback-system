import streamlit as st
import pandas as pd
from datetime import datetime
import os
import google.generativeai as genai

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Feedback System", layout="centered")
DATA_FILE = "data.csv"

# ---------------- SIDEBAR ----------------
page = st.sidebar.radio("Navigation", ["User Feedback", "Admin Dashboard"])

# ---------------- GEMINI SETUP ----------------
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# ✅ AUTO-DETECT A WORKING MODEL
working_model = None
try:
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            working_model = m.name
            break
except:
    pass

if not working_model:
    st.warning("⚠️ Gemini model not detected. AI may not work properly.")

model = genai.GenerativeModel(working_model) if working_model else None

# ---------------- CREATE CSV IF NOT EXISTS ----------------
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

# ---------------- AI FUNCTION (REAL AI) ----------------
def generate_ai_response(review, rating):

    if model is None:
        return ""

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

# ============================
# ✅ ✅ USER PAGE
# ============================
if page == "User Feedback":

    st.title("📝 User Feedback Portal")

    rating = st.selectbox("Select Rating (1–5)", [1, 2, 3, 4, 5])
    review = st.text_area("Write your review")

    submit = st.button("Submit")

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

            # Default fallbacks
            ai_response = "Thank you for your feedback!"
            ai_summary = "Summary unavailable."
            ai_action = "Manual review required."

            # Parse AI output
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

# ============================
# ✅ ✅ ADMIN PAGE
# ============================
elif page == "Admin Dashboard":

    st.title("📊 Admin Feedback Dashboard")

    df = pd.read_csv(DATA_FILE)

    if df.empty:
        st.warning("No feedback submitted yet.")
    else:
        st.dataframe(df, use_container_width=True)

        st.subheader("📊 Rating Distribution")
        st.bar_chart(df["user_rating"].value_counts().sort_index())

        st.subheader("⬇️ Download Data")
        st.download_button(
            "Download CSV",
            df.to_csv(index=False).encode("utf-8"),
            "feedback_data.csv",
            "text/csv"
        )
