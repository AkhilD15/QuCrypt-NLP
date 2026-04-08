import streamlit as st
import sys
import os

# Adds the current directory to the system path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- UPDATED IMPORTS ---
try:
    # Replace 'encrypt_message' with the actual function name inside encryptor.py
    from utils.encryptor import encrypt_message 
    from quantum.quantum_embedding import embed_text
    modules_loaded = True
except ImportError as e:
    st.error(f"Module Loading Error: {e}")
    modules_loaded = False

st.title("⚛️ QuCrypt NLP")

if modules_loaded:
    user_input = st.text_area("Enter Text", "Hello Quantum")
    
    if st.button("Run"):
        # Use the function name you imported above
        result = encrypt_message(user_input)
        st.success("Text Encrypted!")
        st.write(result)
else:
    st.info("Check your folder names and function names. Ensure '__init__.py' exists in /utils and /quantum.")
