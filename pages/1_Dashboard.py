# pages/1_Dashboard.py
import streamlit as st
from PIL import Image

st.set_page_config(page_title="SmartSDLC Dashboard", layout="wide")

# 🔐 Authentication check (alert-only)
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.error("🔒 Please login first to access the SmartSDLC Dashboard.")
    st.stop()

st.title("📊 SmartSDLC Dashboard")

st.markdown(f"👋 Welcome, **{st.session_state.get('user_email', 'User')}**!")

# --- Logout button ---
if st.button("🔓 Logout", key="logout"):
    st.session_state.authenticated = False
    st.session_state.stage = "login"
    st.success("Successfully logged out.")
    st.switch_page("main.py")

st.markdown("---")

# --- SDLC Module Cards ---
modules = [
    {"name": "Requirements", "emoji": "📝", "file": "2_Requirements.py"},
    {"name": "Design", "emoji": "🎨", "file": "4_Design.py"},
    {"name": "Development", "emoji": "💻", "file": "3_Development.py"},
    {"name": "Testing", "emoji": "✅", "file": "5_Testing.py"},
    {"name": "Deployment", "emoji": "🚀", "file": "6_Deployment.py"},
]

st.info("Tip: You can navigate directly from the left sidebar as well!")
