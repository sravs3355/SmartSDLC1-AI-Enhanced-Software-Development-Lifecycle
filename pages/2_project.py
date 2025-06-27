# pages/2_project.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Projects", layout="wide")

# 🔐 LOGIN GUARD — only alert, no redirection or login UI
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please login first to access this module.")
    st.stop()

# ✅ Authenticated users will see this content
st.title("📁 Projects")

# ✅ Initialize projects (once)
if "projects" not in st.session_state:
    st.session_state.projects = [
        {"Project": "AI Chatbot", "Status": "In Progress", "Owner": "Sravya", "Progress": 75},
        {"Project": "Smart Waste Tracker", "Status": "Pending", "Owner": "Prashanth", "Progress": 40},
        {"Project": "Exam Prep App", "Status": "Completed", "Owner": "Yakob", "Progress": 100},
    ]

# ✅ Display projects
df = pd.DataFrame(st.session_state.projects)
st.dataframe(df, use_container_width=True)

st.markdown("---")
st.subheader("➕ Add New Project")

# ✅ Form to add a new project
with st.form("new_project_form"):
    name = st.text_input("Project Name")
    owner = st.text_input("Owner")
    status = st.selectbox("Status", ["Pending", "In Progress", "Completed"])
    progress = st.slider("Progress %", 0, 100, 0)
    submitted = st.form_submit_button("Add Project")

if submitted:
    if name and owner:
        st.session_state.projects.append({
            "Project": name,
            "Status": status,
            "Owner": owner,
            "Progress": progress
        })
        st.success(f"✅ Project '{name}' added successfully!")
    else:
        st.error("❗ Please enter both project name and owner.")
