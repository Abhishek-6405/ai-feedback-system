import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Admin Dashboard", layout="wide")

DATA_FILE = "data.csv"

st.title("🔐 Admin Dashboard – Feedback Monitor")

if not os.path.exists(DATA_FILE):
    st.warning("No feedback data available yet.")
    st.stop()

df = pd.read_csv(DATA_FILE)

st.metric("Total Submissions", len(df))

st.dataframe(df, use_container_width=True)

st.subheader("📊 Rating Distribution")
st.bar_chart(df["user_rating"].value_counts())

st.subheader("📋 Recent Feedback")
st.table(df.tail(10))
