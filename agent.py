import google.generativeai as genai

# ==========================================
# 1. CONNECT TO THE AI
# ==========================================
# Look at Step 4 below to see how to paste your key here!
genai.configure(api_key="YOUR_API_KEY_HERE")

# ==========================================
# 2. CREATE THE AGENT'S TOOLS (The Physics Engine)
# ==========================================
def calculate_lift_force(density: float, velocity: float, area: float, lift_coefficient: float) -> float:
    """Calculates aerodynamic lift force in Newtons."""
    return 0.5 * density * (velocity ** 2) * area * lift_coefficient
def calculate_mach_number(velocity: float, speed_of_sound: float) -> float:
    """Calculates the Mach number of an aircraft."""
    return velocity / speed_of_sound

def check_syllabus(topic: str) -> str:
    """Checks if a topic is in the GATE Aerospace syllabus."""
    allowed = ["aerodynamics", "propulsion", "flight mechanics", "structures", "space dynamics"]
    if any(word in topic.lower() for word in allowed):
        return f"Yes, '{topic}' is in the syllabus. Proceed with testing."
    else:
        return f"No, '{topic}' is NOT in the syllabus. Tell the user to pick a valid GATE Aerospace topic."

# ==========================================
# 3. INITIALIZE THE AGENT
# ==========================================
# We hand the Gemini model our tools and strict instructions
model = genai.GenerativeModel(
    model_name='gemini-2.5-flash',
    tools=[calculate_lift_force, calculate_mach_number, check_syllabus],
    system_instruction="You are XcelGATE, a terminal-based autonomous AI Agent for GATE Aerospace. Always use your check_syllabus tool before agreeing to teach a topic. When a student answers a math question, secretly use your calculate_lift_force tool to verify their answer before you grade them."
)

# Start the chat with AUTOMATIC tool calling turned on!
agent_chat = model.start_chat(enable_automatic_function_calling=True)

# ==========================================
# 4. THE COMMAND LINE INTERFACE (CLI) LOOP
# ==========================================
print("======================================================")
print("🚀 XcelGATE: NATIVE AI AGENT INITIALIZED 🚀")
print("GATE Aerospace Specialization Active.")
print("Type 'exit' to end the session.")
print("======================================================\n")

# This loop keeps the Agent running in your terminal forever until you type 'exit'
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("\n[System]: Analyzing session data and generating your GATE Report Card...")
        
        # We send a hidden, final instruction to the Agent
        final_prompt = "The student is ending the session. Look at our chat history. Write a 3-sentence summary of their performance today, and tell them exactly which GATE Aerospace topic they need to study more based on their mistakes."
        
        report = agent_chat.send_message(final_prompt)
        
        print("\n================ 📊 XCELGATE SESSION REPORT ================")
        print(report.text)
        print("==============================================================\n")
        print("Shutting down XcelGATE Agent. Good luck with your exam!")
        break
    
    print("Agent is processing and invoking tools...")
    
    # Send message to the Agent
    response = agent_chat.send_message(user_input)
    
    # Print the Agent's response
    print(f"\nXcelGATE Agent:\n{response.text}\n")
    print("-" * 50)