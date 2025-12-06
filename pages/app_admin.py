import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Admin Dashboard", layout="wide")

DATA_FILE = "data.csv"

st.title("📊 Admin Feedback Dashboard")

if not os.path.exists(DATA_FILE):
    st.warning("No feedback data available yet.")
    st.stop()

df = pd.read_csv(DATA_FILE)

st.metric("Total Submissions", len(df))
st.metric("Average Rating", round(df["user_rating"].mean(), 2))

st.subheader("📋 All Feedback Data")
st.dataframe(df, use_container_width=True)

st.subheader("📈 Ratings Distribution")
st.bar_chart(df["user_rating"].value_counts().sort_index())
