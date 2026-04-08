import streamlit as st
import sys
import os

# Adds current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- EXACT IMPORTS MATCHING YOUR CODE ---
try:
    from utils.encryptor import simple_encrypt, redact_text
    from quantum.quantum_embedding import quantum_embed # Changed to quantum_embed
    modules_loaded = True
except ImportError as e:
    st.error(f"Module Loading Error: {e}")
    modules_loaded = False

st.title("⚛️ QuCrypt: Quantum-NLP Bridge")

if modules_loaded:
    user_input = st.text_area("Input Text", "Quantum computing is the future of NLP.")
    
    col1, col2 = st.columns(2)
    with col1:
        action = st.radio("Step 1: NLP Action", ["Simple Encrypt", "Redact Text"])
    
    if st.button("Run Hybrid Process"):
        # Step 1: Run your NLP/Encryptor logic
        if action == "Simple Encrypt":
            processed_text = simple_encrypt(user_input)
            st.info(f"Encrypted Output: {processed_text}")
        else:
            processed_text = redact_text(user_input)
            st.info(f"Redacted Output: {processed_text}")

        # Step 2: Run your BERT-based Quantum Embedding
        with st.spinner("Generating Token Embeddings..."):
            embeddings = quantum_embed(processed_text)
            st.success("Embedding Successful!")
            
            st.write("### BERT Tokenizer Output (Simulated Quantum States)")
            st.write(embeddings)
else:
    st.info("Check your folder names and ensure '__init__.py' exists.")
