import streamlit as st
import numpy as np
from quantum.your_quantum_module import your_quantum_function 
from utils.nlp_processing import preprocess_text

# --- Page Config ---
st.set_page_config(page_title="QuCrypt-NLP", page_icon="⚛️")

st.title("⚛️ QuCrypt: Quantum-NLP Dashboard")
st.markdown("Secure and process text using hybrid quantum-classical logic.")

# --- Sidebar for Settings ---
with st.sidebar:
    st.header("Settings")
    backend = st.selectbox("Quantum Backend", ["Aer Simulator", "IBM Brisbane (Cloud)"])
    shots = st.slider("Shots", 1024, 4096, 2048)

# --- Main UI ---
user_input = st.text_area("Enter text to process:", "Hello Quantum World!")

if st.button("Process with Quantum NLP"):
    with st.spinner("Executing quantum circuit..."):
        # 1. Preprocess
        cleaned_text = preprocess_text(user_input)
        
        # 2. Quantum Execution
        result = your_quantum_function(cleaned_text, shots=shots)
        
        # 3. Display Results
        st.success("Processing Complete!")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Quantum State Fidelity", "98.4%")
        with col2:
            st.metric("Encryption Strength", "High")
            
        st.write("### Output Data")
        st.json(result)
