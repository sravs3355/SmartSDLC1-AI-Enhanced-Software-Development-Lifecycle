# utils/auth.py (or auth.py in same directory)

users_db = {}
otp_db = {}

def register_user(email, password):
    if email in users_db:
        return None
    otp = "123456"  # Simulated OTP for testing
    otp_db[email] = otp
    users_db[email] = {"password": password, "verified": False}
    return otp

def verify_otp(email, otp):
    if otp_db.get(email) == otp:
        users_db[email]["verified"] = True
        return True
    return False

def login_user(email, password):
    user = users_db.get(email)
    if user and user["password"] == password and user["verified"]:
        return True
    return False
