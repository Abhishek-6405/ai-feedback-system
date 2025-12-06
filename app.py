import streamlit as st
import pandas as pd
from datetime import datetime
import os
import random

# ---------------- CONFIG ----------------
st.set_page_config(page_title="AI Feedback System", layout="centered")
DATA_FILE = "data.csv"

# ---------------- SIDEBAR ----------------
page = st.sidebar.radio("Navigation", ["User Feedback", "Admin Dashboard"])

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

# ---------------- FAKE AI ENGINE (DEPLOYMENT SAFE) ----------------
def generate_ai_response(review, rating):

    responses = [
        "Thank you for sharing your feedback with us!",
        "We appreciate your time and valuable review.",
        "Thanks for helping us improve our services.",
        "Your feedback means a lot to our team."
    ]

    summaries = [
        "Customer shared general feedback.",
        "User expressed satisfaction level.",
        "Feedback regarding product/service experience.",
        "General customer opinion recorded."
    ]

    actions = [
        "No action required.",
        "Share feedback with team.",
        "Monitor similar feedback.",
        "Follow up if required."
    ]

    return (
        f"AI_RESPONSE: {random.choice(responses)}\n"
        f"SUMMARY: {random.choice(summaries)}\n"
        f"ACTION: {random.choice(actions)}"
    )

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
                ai_raw = generate_ai_response(review, rating)

            # Defaults
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
