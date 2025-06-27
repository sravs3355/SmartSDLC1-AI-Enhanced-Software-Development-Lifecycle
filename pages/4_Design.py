# pages/4_Design.py

import streamlit as st
import os

st.set_page_config(page_title="Design", layout="wide")

# 🔐 Authentication check (NO REDIRECT, only alert)
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please login to access this page.")
    st.stop()

# ✅ Authenticated users see this
st.title("🎨 Design Module")

# Directory to save architecture notes
ARCHITECTURE_FILE = "data/architecture_notes.txt"
os.makedirs("data", exist_ok=True)

# Read existing architecture notes from file
def load_architecture_notes():
    if os.path.exists(ARCHITECTURE_FILE):
        with open(ARCHITECTURE_FILE, "r") as file:
            return file.read()
    return ""

# Save architecture notes to file
def save_architecture_notes(notes):
    with open(ARCHITECTURE_FILE, "w") as file:
        file.write(notes)

# --- Upload Section ---
st.subheader("🖼️ Upload UI Mockups / Wireframes")

uploaded_files = st.file_uploader(
    "Upload design images or sketches",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:
    for file in uploaded_files:
        st.image(file, caption=file.name, use_column_width=True)
        st.success(f"✅ {file.name} uploaded")

st.markdown("---")

# --- Architecture Notes Section ---
st.subheader("📝 Describe System Architecture")

# Load notes from file or session
if "architecture_notes" not in st.session_state:
    st.session_state.architecture_notes = load_architecture_notes()

# Text area input
arch_notes = st.text_area("Enter architecture notes", value=st.session_state.architecture_notes, height=200)

# Save notes
if st.button("Save Architecture Notes"):
    st.session_state.architecture_notes = arch_notes
    save_architecture_notes(arch_notes)
    st.success("✅ Architecture notes saved!")

# Show saved notes (optional)
if st.session_state.architecture_notes.strip():
    st.markdown("---")
    st.subheader("📄 Saved Architecture Notes")
    st.info(st.session_state.architecture_notes)
