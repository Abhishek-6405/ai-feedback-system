import streamlit as st
import pandas as pd
import os

DATA_FILE = "data.csv"

st.title("🛠 Admin Dashboard")

if not os.path.exists(DATA_FILE):
    st.warning("No feedback available yet.")
    st.stop()

df = pd.read_csv(DATA_FILE)

st.subheader("📊 All User Feedback")
st.dataframe(df)

st.subheader("📈 Analytics")

col1, col2, col3 = st.columns(3)
col1.metric("Total Reviews", len(df))
col2.metric("Average Rating", round(df["user_rating"].mean(), 2))
col3.metric("Latest Rating", df.iloc[-1]["user_rating"])
