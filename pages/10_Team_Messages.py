# pages/10_Team_Messages.py
import streamlit as st
import datetime

# --- Page Configuration ---
st.set_page_config(page_title="Team Messages", layout="wide")

# --- 🔐 Login Check ---
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please login to access this module.")
    st.stop()

# --- Main Content ---
st.title("💬 Team Messages")

# Message board
st.subheader("📨 Inbox")
messages = [
    {"from": "Prashanth", "msg": "Deployed to staging.", "time": "2025-06-18 10:12"},
    {"from": "Yakob", "msg": "All test cases passed!", "time": "2025-06-18 09:55"},
    {"from": "Sravya", "msg": "Reminder: team sync at 3PM.", "time": "2025-06-18 08:45"}
]

for m in messages:
    st.markdown(f"**{m['from']}** ({m['time']}): {m['msg']}")

st.markdown("---")

# Send new message
st.subheader("✉️ Send a Message")
with st.form("send_message"):
    sender = st.text_input("Your Name")
    message = st.text_area("Message")
    send_btn = st.form_submit_button("Send")

if send_btn:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    st.success(f"✅ Message from {sender} sent at {timestamp}:")
    st.info(message)
