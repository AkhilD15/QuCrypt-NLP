import streamlit as st
import sys
import os

# 1. Add the current directory to the system path so Python can see your folders
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 2. Corrected Imports based on your filenames
try:
    # Assuming the function inside is named 'embed_text' or similar
    # If the function name is different, change 'embed_text' to the correct name
    from quantum.quantum_embedding import embed_text 
    from utils.text_preprocessing import preprocess_text
    st.sidebar.success("✅ Quantum & NLP modules loaded")
except ImportError as e:
    st.sidebar.error(f"⚠️ Connection Error: {e}")
    st.sidebar.info("Double-check the function names inside your .py files.")

# --- Streamlit UI ---
st.set_page_config(page_title="QuCrypt-NLP", page_icon="⚛️")
st.title("⚛️ QuCrypt: Quantum NLP")

user_input = st.text_area("Enter text for Quantum Encryption:", "Quantum computing is the future.")

if st.button("Process"):
    with st.spinner("Executing Quantum Circuit..."):
        # Pre-process text using your utils
        clean_text = preprocess_text(user_input)
        
        # Run quantum embedding
        quantum_result = embed_text(clean_text)
        
        st.write("### Resulting Quantum States")
        st.json(quantum_result)
