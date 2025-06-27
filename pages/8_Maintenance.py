# pages/8_Maintenance.py
import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Maintenance", layout="wide")

# --- 🔐 Login Restriction ---
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please login to access this module.")
    st.stop()

# --- Authenticated Content ---
st.title("🔧 Maintenance Module")

st.subheader("🗓️ Schedule Maintenance")
with st.form("maintenance_form"):
    maint_date = st.date_input("Maintenance Date")
    maint_type = st.selectbox("Type", ["Routine Check", "Bug Fix", "Security Patch", "Upgrade"])
    maint_desc = st.text_area("Description")
    submit_maint = st.form_submit_button("Schedule")

if submit_maint:
    st.success(f"🔧 Maintenance on {maint_date} for '{maint_type}' scheduled successfully.")

st.markdown("---")

st.subheader("🛠️ Log Completed Maintenance")
with st.form("log_form"):
    log_title = st.text_input("Maintenance Title")
    log_notes = st.text_area("Notes")
    completed = st.checkbox("Mark as Completed")
    submit_log = st.form_submit_button("Log Maintenance")

if submit_log:
    st.success(f"🗒️ Maintenance '{log_title}' logged as {'Completed' if completed else 'Pending'}.")
