import streamlit as st
import re
import hashlib

st.title("🔐 Password Strength Analyzer")

# Hash function (optional future use)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Strength checker
def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search(r"[!@#$%^&*]", password):
        score += 2
    else:
        suggestions.append("Add special characters")

    if score >= 6:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, suggestions


# UI
password = st.text_input("Enter Password", type="password")

if password:
    strength, suggestions = check_password_strength(password)

    st.subheader(f"Password Strength: {strength}")

    if suggestions:
        st.write("### Suggestions:")
        for s in suggestions:
            st.write("•", s)
