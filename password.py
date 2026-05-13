import re
import hashlib
import os

DATABASE_FILE = "passwords.txt"


# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to check if password already exists
def is_reused_password(hashed_password):
    if not os.path.exists(DATABASE_FILE):
        return False

    with open(DATABASE_FILE, "r") as file:
        stored_passwords = file.read().splitlines()

    return hashed_password in stored_passwords


# Function to save password hash
def save_password(hashed_password):
    with open(DATABASE_FILE, "a") as file:
        file.write(hashed_password + "\n")


# Password strength checker
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


# Main Program
password = input("Enter Password: ")

# Hash the password
hashed_password = hash_password(password)

# Check reuse
if is_reused_password(hashed_password):
    print("\n⚠ Password already used before!")
    print("Choose a new password.")
else:
    strength, suggestions = check_password_strength(password)

    print("\nPassword Strength:", strength)

    if suggestions:
        print("\nSuggestions:")
        for s in suggestions:
            print("-", s)

    # Save password if not reused
    save_password(hashed_password)

    print("\n✅ Password saved securely.")