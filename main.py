import streamlit as st
from auth import register_user, verify_otp, login_user  # 🔐 Your custom auth file
st.set_page_config(page_title="SmartSDLC Login", layout="centered")
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "stage" not in st.session_state:
    st.session_state.stage = "login"
if st.session_state.authenticated:
    st.switch_page("pages/2_project.py")

st.markdown("""
    <style>
    body {
        background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb");
        background-size: cover;
        background-attachment: fixed;
    }
    .stApp {
        background-color: rgba(0, 0, 0, 0.3);
        padding-top: 80px;
    }
    .login-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 40px;
        border-radius: 15px;
        max-width: 420px;
        margin: auto;
        box-shadow: 0 0 15px rgba(0,0,0,0.3);
    }
    .login-title {
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        color: black;
        background-color: white;
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)
st.markdown('<div class="login-title">SmartSDLC – AI-Enhanced Software Development Lifecycle</div>', unsafe_allow_html=True)
if st.session_state.stage == "login":
    st.subheader("🔐 Login")
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login"):
            if login_user(email, password):
                st.success("✅ Login successful!")
                st.session_state.authenticated = True
                st.session_state.user_email = email
                st.switch_page("pages/1_Dashboard.py")  
            else:
                st.error("❌ Invalid email or password.")

    with col2:
        if st.button("Register"):
            st.session_state.stage = "register"
elif st.session_state.stage == "register":
    st.subheader("📝 Register")
    email = st.text_input("Email", key="register_email")
    password = st.text_input("Password", type="password", key="register_password")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Send OTP"):
            otp = register_user(email, password)
            if otp:
                st.session_state.temp_email = email
                st.session_state.temp_password = password
                st.session_state.stage = "otp"
                st.success(f"✅ OTP sent! (Simulated OTP: {otp})") 
            else:
                st.error("⚠️ User already exists.")

    with col2:
        if st.button("Back to Login"):
            st.session_state.stage = "login"
elif st.session_state.stage == "otp":
    st.subheader("📩 OTP Verification")
    otp_input = st.text_input("Enter the OTP sent to your email")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Verify OTP"):
            if verify_otp(st.session_state.temp_email, otp_input):
                st.success("🎉 OTP verified! You can now login.")
                st.session_state.stage = "login"
            else:
                st.error("❌ Invalid OTP.")

    with col2:
        if st.button("Back"):
            st.session_state.stage = "register"

st.markdown("</div>", unsafe_allow_html=True)
