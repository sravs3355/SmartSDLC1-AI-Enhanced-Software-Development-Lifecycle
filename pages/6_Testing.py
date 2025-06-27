# pages/6_Testing.py

import streamlit as st
import sqlite3
from fpdf import FPDF
import tempfile
import os

# --- Page Config ---
st.set_page_config(page_title="Testing", layout="wide")

# --- 🔐 Login Restriction ---
if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please log in to access this module.")
    st.stop()

st.title("🧪 Testing Module")

# --- Database Setup ---
conn = sqlite3.connect("testing_module.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS test_cases (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        expected TEXT,
        actual TEXT,
        result TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bugs (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        priority TEXT
    )
''')
conn.commit()

# --- Add New Test Case ---
with st.form("test_case_form"):
    st.subheader("➕ Add New Test Case")
    title = st.text_input("Test Case Title")
    description = st.text_area("Description")
    expected = st.text_input("Expected Output")
    actual = st.text_input("Actual Output")
    submitted = st.form_submit_button("✅ Save Test Case")

    if submitted:
        if title and expected and actual:
            result = "Pass" if expected == actual else "Fail"
            cursor.execute("INSERT INTO test_cases (title, description, expected, actual, result) VALUES (?, ?, ?, ?, ?)",
                           (title, description, expected, actual, result))
            conn.commit()
            st.success(f"✅ Test case '{title}' added with result: {result}")
        else:
            st.error("❗Please fill in all required fields.")

# --- Display Test Cases ---
st.subheader("📋 Test Case List")
cursor.execute("SELECT * FROM test_cases")
rows = cursor.fetchall()

if rows:
    for r in rows:
        with st.expander(f"🔹 {r[1]}"):
            st.markdown(f"**Description:** {r[2]}")
            st.markdown(f"**Expected:** {r[3]}")
            st.markdown(f"**Actual:** {r[4]}")
            st.markdown(f"**Result:** {'✅ Pass' if r[5] == 'Pass' else '❌ Fail'}")
else:
    st.info("No test cases yet.")

# --- Report Bug Form ---
with st.form("bug_form"):
    st.subheader("🐞 Report Bug")
    bug_title = st.text_input("Bug Title")
    bug_desc = st.text_area("Bug Description")
    bug_priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
    bug_submit = st.form_submit_button("🐛 Report Bug")

    if bug_submit:
        if bug_title and bug_desc:
            cursor.execute("INSERT INTO bugs (title, description, priority) VALUES (?, ?, ?)",
                           (bug_title, bug_desc, bug_priority))
            conn.commit()
            st.success(f"✅ Bug '{bug_title}' reported.")
        else:
            st.error("❗Bug title and description are required.")

# --- Display Bugs ---
st.subheader("🧾 Reported Bugs")
cursor.execute("SELECT * FROM bugs")
bugs = cursor.fetchall()

if bugs:
    for b in bugs:
        with st.expander(f"🔸 {b[1]} (Priority: {b[3]})"):
            st.markdown(b[2])
else:
    st.info("No bugs reported yet.")

# --- PDF Export Function ---
def generate_pdf(test_cases, bug_list):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="🧪 Test Report", ln=True, align="C")

    pdf.set_font("Arial", size=11)
    pdf.ln(10)
    pdf.cell(200, 10, txt="Test Cases:", ln=True)

    for r in test_cases:
        pdf.multi_cell(0, 10, f"Title: {r[1]}\nDescription: {r[2]}\nExpected: {r[3]}\nActual: {r[4]}\nResult: {r[5]}")
        pdf.ln(2)

    pdf.ln(5)
    pdf.cell(200, 10, txt="Reported Bugs:", ln=True)

    for b in bug_list:
        pdf.multi_cell(0, 10, f"Title: {b[1]}\nDescription: {b[2]}\nPriority: {b[3]}")
        pdf.ln(2)

    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(tmp_file.name)
    return tmp_file.name

# --- Export PDF Button ---
if st.button("📤 Export as PDF"):
    pdf_path = generate_pdf(rows, bugs)
    with open(pdf_path, "rb") as f:
        st.download_button("📥 Download Report", f, file_name="test_report.pdf", mime="application/pdf")
    os.remove(pdf_path)  # Clean up temp file
