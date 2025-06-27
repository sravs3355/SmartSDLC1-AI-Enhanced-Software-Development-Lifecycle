# pages/5_Development.py

import streamlit as st

st.set_page_config(page_title="Development", layout="wide")

# 🔐 Authentication check (only alert, no redirect)
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please login to access this page.")
    st.stop()

# ✅ Authenticated users see this
st.title("💻 Development Module")

# Store tasks persistently
if "dev_tasks" not in st.session_state:
    st.session_state.dev_tasks = []

st.subheader("🔗 Link Git Repository")
git_url = st.text_input("Enter GitHub/GitLab repo URL")
if st.button("Save Repository"):
    st.success(f"✅ Repository saved: {git_url}")

st.markdown("---")

st.subheader("📂 Upload Development Files")
code_files = st.file_uploader("Upload code files", type=["py", "js", "html", "css"], accept_multiple_files=True)

if code_files:
    for file in code_files:
        st.markdown(f"**📄 {file.name}** uploaded successfully.")
        code_content = file.read().decode("utf-8")
        st.code(code_content, language="python")

st.markdown("---")

st.subheader("🗂️ Track Dev Tasks")
with st.form("dev_task_form"):
    task = st.text_input("Development Task")
    assignee = st.text_input("Assigned To")
    progress = st.slider("Progress %", 0, 100, 0)
    add_task = st.form_submit_button("Add Task")

if add_task:
    if task and assignee:
        st.session_state.dev_tasks.append({
            "Task": task,
            "Assignee": assignee,
            "Progress": progress
        })
        st.success(f"✅ Task '{task}' assigned to {assignee} with {progress}% progress.")
    else:
        st.error("❗ Please enter both task and assignee.")

st.markdown("---")

st.subheader("📋 Existing Development Tasks")
for task in st.session_state.dev_tasks:
    st.markdown(f"**🛠️ {task['Task']}** — Assigned to *{task['Assignee']}* — Progress: {task['Progress']}%")
