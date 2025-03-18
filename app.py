





import re
import time
import streamlit as st

import random
import string


def generate_strong_password(length=12):
    """Generate a strong password with a mix of characters."""
    if length < 8:
        st.warning("Password length should be at least 8 characters.")
        return None
    
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*"),
    ]
    password += random.choices(string.ascii_letters + string.digits + "!@#$%^&*", k=length-4)
    random.shuffle(password)
    return ''.join(password)

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if score == 4:
        st.success("✅ Strong Password!")
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.error("❌ Weak Password - Improve it using the suggestions above.")
        for suggestion in feedback:
            st.write(suggestion)

# Streamlit user interface

st.title("🔐 Password Strength Meter")
user_password = st.text_input("Enter your password:", type="password")
if st.button("Check Password Strength"):
    with st.spinner("Analyzing password strength..."):
        time.sleep(1)
    check_password_strength(user_password)

if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    if strong_password:
        st.success(f"Suggested Strong Password: **{strong_password}**")
