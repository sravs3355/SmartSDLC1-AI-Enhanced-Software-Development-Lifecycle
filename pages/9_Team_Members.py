# pages/9_Team_Members.py
import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Team Members", layout="wide")

# --- 🔐 Login Restriction ---
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please login to access this module.")
    st.stop()

# --- Authenticated Content ---
st.title("👥 Team Members")

st.subheader("Current Members")
team = [
    {"Name": "Sravya Goli", "Role": "Project Manager"},
    {"Name": "Prashanth", "Role": "Backend Developer"},
    {"Name": "Yakob", "Role": "Tester"},
    {"Name": "Sarath", "Role": "Develops"}
]

for member in team:
    st.markdown(f"- **{member['Name']}** — *{member['Role']}*")

st.markdown("---")

st.subheader("➕ Add New Member")
with st.form("add_member_form"):
    name = st.text_input("Full Name")
    role = st.text_input("Role")
    add_member = st.form_submit_button("Add Member")

if add_member:
    if name and role:
        st.success(f"✅ Added {name} as {role}")
    else:
        st.error("❗Please fill in both name and role.")
