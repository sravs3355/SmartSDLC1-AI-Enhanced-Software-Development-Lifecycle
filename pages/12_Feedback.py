# pages/11_Feedback.py
import streamlit as st
import sqlite3
from textblob import TextBlob
import pandas as pd

# Auth check
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please login to access this page.")
    st.stop()

st.set_page_config(page_title="📣 Feedback", layout="wide")
st.title("📣 Submit Your Feedback")

# SQLite DB setup
conn = sqlite3.connect("data/smart_sdlc.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_email TEXT,
        feedback TEXT,
        sentiment TEXT,
        polarity REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

# Feedback form
st.subheader("📝 Tell us what you think")
feedback = st.text_area("Your feedback", height=150)
if st.button("Submit Feedback"):
    if feedback.strip():
        blob = TextBlob(feedback)
        polarity = blob.sentiment.polarity
        sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
        user_email = st.session_state.get("user_email", "anonymous")

        cursor.execute("INSERT INTO feedback (user_email, feedback, sentiment, polarity) VALUES (?, ?, ?, ?)",
                       (user_email, feedback, sentiment, polarity))
        conn.commit()
        st.success(f"✅ Feedback submitted! Sentiment: {sentiment}")
    else:
        st.warning("⚠️ Please enter some feedback before submitting.")
