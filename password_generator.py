import random
import string
import streamlit as st

# Function to generate a password
def generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special_chars, custom_chars):
    chars = ''
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    chars += custom_chars

    if not chars:
        st.error("Please select at least one character set or enter custom characters to generate a password.")
        return ''

    return ''.join(random.choice(chars) for _ in range(length))

# Streamlit interface
st.title("Password Generator")

st.write("""
## Select the criteria for your password:
- Choose the length
- Optionally, add your own custom characters
- Select character sets to include
""")

length = st.slider("Select Password Length", 6, 20, 12)
use_lowercase = st.checkbox("Include Lowercase Letters", value=True)
use_uppercase = st.checkbox("Include Uppercase Letters", value=True)
use_numbers = st.checkbox("Include Numbers", value=True)
use_special_chars = st.checkbox("Include Special Characters", value=True)
custom_chars = st.text_input("Enter Custom Characters (optional)")

if st.button("Generate Password"):
    password = generate_password(length, use_lowercase, use_uppercase, use_numbers, use_special_chars, custom_chars)
    if password:
        st.success(f"Generated Password: {password}")
    else:
        st.error("Failed to generate password. Please check your input.")
