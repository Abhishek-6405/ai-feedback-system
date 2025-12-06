import streamlit as st
import pandas as pd

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Admin Feedback Dashboard", layout="wide")
DATA_FILE = "data.csv"

# ---------------- LOAD DATA ----------------
st.title("📊 Admin Feedback Dashboard")

try:
    df = pd.read_csv(DATA_FILE)
except:
    st.error("❌ data.csv not found. Please submit at least one feedback first.")
    st.stop()

# ---------------- FILTER SECTION ----------------
st.sidebar.header("🔍 Filters")

rating_filter = st.sidebar.selectbox(
    "Filter by Rating",
    ["All", 1, 2, 3, 4, 5]
)

if rating_filter != "All":
    df = df[df["user_rating"] == int(rating_filter)]

# ---------------- METRICS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Feedback", len(df))

with col2:
    avg_rating = round(df["user_rating"].mean(), 2) if len(df) > 0 else 0
    st.metric("Average Rating", avg_rating)

with col3:
    low_ratings = len(df[df["user_rating"] <= 2])
    st.metric("Low Ratings (≤2)", low_ratings)

# ---------------- TABLE ----------------
st.subheader("🗂 All Feedback Records")
st.dataframe(df, use_container_width=True)

# ---------------- DOWNLOAD BUTTON ----------------
st.subheader("⬇ Download Data")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download CSV",
    data=csv,
    file_name="feedback_data.csv",
    mime="text/csv"
)

# ---------------- SIMPLE ANALYTICS ----------------
st.subheader("📈 Rating Distribution")

rating_counts = df["user_rating"].value_counts().sort_index()
st.bar_chart(rating_counts)

# ---------------- AI SUMMARY VIEW ----------------
st.subheader("🤖 AI Insights")

for _, row in df.iterrows():
    with st.expander(f"Feedback at {row['timestamp']} (Rating: {row['user_rating']})"):
        st.write(f"**User Review:** {row['user_review']}")
        st.write(f"**AI Response:** {row['ai_response']}")
        st.write(f"**AI Summary:** {row['ai_summary']}")
        st.write(f"**Recommended Action:** {row['ai_recommended_action']}")
