import streamlit as st
import pandas as pd
from datetime import datetime
import os
import google.generativeai as genai

DATA_FILE = "data.csv"

# ---------------- GEMINI SETUP ----------------
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

working_model = None
for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        working_model = m.name
        break

if not working_model:
    st.error("No Gemini model available for your API key.")
    st.stop()

model = genai.GenerativeModel(working_model)

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

# ---------------- UI ----------------
st.title("📝 User Feedback Portal")

rating = st.selectbox("Select Rating (1–5)", [1, 2, 3, 4, 5])
review = st.text_area("Write your review")
submit = st.button("Submit")

# ---------------- AI FUNCTION ----------------
def generate_ai_response(review, rating):
    prompt = f"""
A user gave a {rating}-star rating and wrote this review:

"{review}"

Return output in EXACT format:

AI_RESPONSE: <polite reply>
SUMMARY: <short summary>
ACTION: <recommended action>
"""
    response = model.generate_content(prompt)
    return response.text

# ---------------- SUBMIT ----------------
if submit:
    if review.strip() == "":
        st.warning("Please enter a review.")
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

        st.success("✅ Feedback submitted!")
        st.subheader("🤖 AI Response")
        st.write(ai_response)
