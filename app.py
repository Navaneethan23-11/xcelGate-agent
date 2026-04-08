import streamlit as st
import google.generativeai as genai

# 1. Connect to the AI Brain
# VERY IMPORTANT: Replace the text inside the quotes with the actual API key you saved earlier!
genai.configure(api_key="AIzaSyAhhqAfY7Lc0hlIiB_stsBy7Lc4xihObUE")
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. Build the Website Title and Header
st.title("GATE Aerospace AI Tutor 🚀")
st.write("Adaptive learning for competitive exams.")

# 3. Show a Demo Math Question
st.subheader("Question 1: Aerodynamics")
st.write("Calculate the Lift Force given:")

# st.latex() magically turns code into beautiful math formulas!
st.latex(r"L = \frac{1}{2} \rho V^2 S C_L")

# 4. Create an input box for the user
user_answer = st.text_input("Enter your answer (in Newtons):")

# 5. Create a button and check the answer
if st.button("Submit Answer"):
    
    # We pretend 5000 is the correct answer for this demo
    if user_answer == "5000": 
        st.success("Correct! Moving to Level 2...")
    
    # If they get it wrong, we ask the AI to generate a hint
    else:
        st.error("Incorrect. Asking the AI tutor for help...")
        
        # We send a prompt to the AI
        prompt = "Explain the aerospace lift equation to a student who just made a calculation error. Keep it strictly under 3 sentences."
        response = model.generate_content(prompt)
        
        # We display the AI's answer on the screen
        st.info(response.text)