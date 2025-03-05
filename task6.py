import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    if length < 8:
        return "⚠️ Please choose a password with at least 8 characters."

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "⚠️ Please select at least one character type!"

    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Secure Password Generator 🔑")
st.write("🚀 **Generate strong and secure passwords easily!**")

# User input for password length
length = st.number_input("📏 Enter password length:", min_value=8, max_value=50, value=12)

# User choices
st.write("🎭 **Choose character types:**")
use_upper = st.checkbox("🔠 Include uppercase letters (A-Z)?")
use_lower = st.checkbox("🔡 Include lowercase letters (a-z)?", value=True)
use_digits = st.checkbox("🔢 Include numbers (0-9)?")
use_symbols = st.checkbox("🔣 Include special characters (@#$%&*! etc.)?")

# Number of passwords
num_passwords = st.slider("🎲 **How many passwords to generate?**", 1, 5, 1)

# Generate passwords on button click
if st.button("✨ Generate Passwords ✨"):
    st.subheader("📋 Generated Passwords:")
    for i in range(num_passwords):
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        st.code(password, language="")

st.write("🔒 **Stay secure! Always use strong passwords.** 💡")
