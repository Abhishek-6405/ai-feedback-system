import streamlit as st
import pandas as pd
import time
import os

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Admin Dashboard", layout="wide")
DATA_FILE = "data.csv"

st.title("📊 Admin Dashboard – AI Feedback System")

# ---------------- AUTO REFRESH ----------------
refresh_rate = st.slider("Auto Refresh (seconds)", 5, 60, 10)

# ---------------- LOAD DATA ----------------
def load_data():
    if not os.path.exists(DATA_FILE):
        return pd.DataFrame(columns=[
            "timestamp",
            "user_rating",
            "user_review",
            "ai_response",
            "ai_summary",
            "ai_recommended_action"
        ])
    return pd.read_csv(DATA_FILE)

df = load_data()

# ---------------- ANALYTICS ----------------
st.subheader("📈 Quick Analytics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Feedbacks", len(df))

with col2:
    if len(df) > 0:
        st.metric("Average Rating", round(df["user_rating"].mean(), 2))
    else:
        st.metric("Average Rating", 0)

with col3:
    if len(df) > 0:
        st.metric("Latest Rating", df.iloc[-1]["user_rating"])
    else:
        st.metric("Latest Rating", "N/A")

st.divider()

# ---------------- DATA TABLE ----------------
st.subheader("🗂 All User Submissions")

if len(df) == 0:
    st.warning("No feedback submitted yet.")
else:
    st.dataframe(df, use_container_width=True)

# ---------------- AUTO REFRESH ----------------
time.sleep(refresh_rate)
st.rerun()
