# pages/3_Requirements.py
import streamlit as st

st.set_page_config(page_title="Requirements", layout="wide")

# 🔐 Inline authentication check
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.error("🔒 Please login first to access this module.")
    st.stop()

st.title("🧾 Requirements Module")

# Initialize session state
if "requirements" not in st.session_state:
    st.session_state.requirements = [
        {
            "Title": "User Login",
            "Type": "Functional",
            "Description": "Allow users to login securely"
        },
        {
            "Title": "System Response Time < 2s",
            "Type": "Non-Functional",
            "Description": "System should respond to user actions within 2 seconds"
        },
        {
            "Title": "Export to PDF",
            "Type": "Functional",
            "Description": "Allow exporting data to PDF format"
        },
    ]

if "req_refresh" not in st.session_state:
    st.session_state.req_refresh = False

st.subheader("➕ Add Requirement")

with st.form("add_requirement"):
    req_title = st.text_input("Requirement Title")
    req_desc = st.text_area("Requirement Description")
    req_type = st.radio("Type", ["Functional", "Non-Functional"])
    submit_req = st.form_submit_button("Add Requirement")

if submit_req:
    if req_title:
        existing_titles = [r["Title"].lower() for r in st.session_state.requirements]
        if req_title.lower() in existing_titles:
            st.warning(f"⚠️ Requirement '{req_title}' already exists.")
        else:
            st.session_state.requirements.append({
                "Title": req_title,
                "Type": req_type,
                "Description": req_desc
            })
            st.success(f"✅ Requirement '{req_title}' added as {req_type} requirement.")
            st.session_state.req_refresh = not st.session_state.req_refresh
    else:
        st.error("❗ Please provide a requirement title.")

st.markdown("---")

st.subheader("📄 Existing Requirements")

for req in st.session_state.requirements:
    st.markdown(f"**{req['Title']}** — *{req['Type']}*")
    if req['Description']:
        st.markdown(f"📌 _{req['Description']}_")
    st.markdown("---")