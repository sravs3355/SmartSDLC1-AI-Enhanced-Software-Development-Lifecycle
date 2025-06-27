# pages/12_Admin_Feedback_Analytics.py
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

# Admin access only (optional)
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please login to access this page.")
    st.stop()

st.set_page_config(page_title="📊 Feedback Analytics", layout="wide")
st.title("📊 Feedback & Sentiment Analysis")

# Connect DB
conn = sqlite3.connect("data/smart_sdlc.db", check_same_thread=False)
df = pd.read_sql_query("SELECT * FROM feedback ORDER BY timestamp DESC", conn)

if df.empty:
    st.info("No feedback submitted yet.")
else:
    st.subheader("📋 Recent Feedback")
    st.dataframe(df, use_container_width=True)

    st.subheader("📈 Sentiment Distribution")
    sentiment_counts = df["sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ["Sentiment", "Count"]
    fig = px.pie(sentiment_counts, names="Sentiment", values="Count", title="Sentiment Overview")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📉 Sentiment Polarity Over Time")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    fig2 = px.line(df.sort_values("timestamp"), x="timestamp", y="polarity", markers=True, title="Polarity Trend")
    st.plotly_chart(fig2, use_container_width=True)
