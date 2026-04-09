import streamlit as st
import google.generativeai as genai

# ==========================================
# 1. SETUP & THEME CONFIGURATION
# ==========================================
st.set_page_config(page_title="XcelGATE AI | Aerospace", page_icon="🚀", layout="centered")

# Put your actual API key here
genai.configure(api_key="GOOGLE_API_KEY")

# --- CUSTOM CSS INJECTION (Dark Mode Magic) ---
st.markdown("""
<style>
    /* Force main background to black and standard text to white */
    .stApp, .markdown-text-container, p, span, li, label {
        background-color: #000000 !important;
        color: #FFFFFF !important; 
    }
    
    /* Ensure Streamlit containers don't override the black */
    .stApp > header {
        background-color: transparent !important;
    }

    /* Target Headers (H1, H2, H3) - Bright Neon Aerospace Green */
    h1, h2, h3 {
        color: #2ECC71 !important; 
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        background-color: transparent !important;
    }

    /* Styling the main title container */
    .main-title {
        font-size: 42px;
        color: #2ECC71 !important;
        font-weight: bold;
        margin-bottom: -10px;
        background-color: transparent !important;
    }
    
    .sub-title {
        font-size: 18px;
        color: #CCCCCC !important;
        margin-bottom: 20px;
        font-weight: 500;
        background-color: transparent !important;
    }

    /* Customize the Chat Input Box */
    .stChatInputContainer, .stChatInputContainer > div {
        background-color: #121212 !important;
        border-color: #2ECC71 !important;
        color: white !important;
    }
    
    /* User Message Bubble - Dark Charcoal */
    [data-testid="stChatMessage"]:nth-child(even) {
        background-color: #1A1A1A !important;
        border-radius: 10px;
        padding: 10px;
        color: #FFFFFF !important;
        border: 1px solid #333333 !important;
    }
    
    /* Assistant Message Bubble - Very Dark Green Tint */
    [data-testid="stChatMessage"]:nth-child(odd) {
        background-color: #0B2B19 !important; 
        border-radius: 10px;
        padding: 10px;
        color: #FFFFFF !important;
        border: 1px solid #145A32 !important;
    }

    /* Style the sidebar */
    [data-testid="stSidebar"], [data-testid="stSidebar"] > div:first-child {
        background-color: #0A0A0A !important;
        border-right: 1px solid #333333 !important;
    }
    
    /* Expanders (Study Materials dropdowns) */
    [data-testid="stExpander"] {
        background-color: #121212 !important;
        border-color: #333333 !important;
    }
    
    /* Standard Buttons (MCQ, MSQ, NAT) */
    .stButton>button {
        background-color: #1E8449 !important;
        color: white !important;
        border-radius: 8px;
        border: 1px solid #2ECC71 !important;
        width: 100%;
        transition: all 0.3s;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #2ECC71 !important;
        color: black !important;
        transform: scale(1.02);
    }
    
    /* RED "End Prep" Button */
    [data-testid="baseButton-primary"] {
        background-color: #C0392B !important; 
        color: white !important;
        border-radius: 8px;
        border: none;
        width: 100%;
        transition: all 0.3s;
        font-weight: bold;
    }
    [data-testid="baseButton-primary"]:hover {
        background-color: #E74C3C !important;
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. THE PHYSICS ENGINE (TOOLS)
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
        return f"Yes, '{topic}' is in the syllabus."
    else:
        return f"No, '{topic}' is NOT in the syllabus."

# ==========================================
# 3. INITIALIZE THE AI & CHAT MEMORY
# ==========================================
if "chat_session" not in st.session_state:
    model = genai.GenerativeModel(
        model_name='gemini-2.5-flash',
        tools=[calculate_lift_force, calculate_mach_number, check_syllabus],
        system_instruction="You are XcelGATE, an AI Agent for GATE Aerospace. Always verify math natively before giving solutions. If asked for a final report, analyze the user's answers and list specific weak concepts."
    )
    st.session_state.chat_session = model.start_chat(enable_automatic_function_calling=True)
    st.session_state.messages = []

# ==========================================
# 4. SIDEBAR UI (Materials & Controls)
# ==========================================
with st.sidebar:
    st.markdown("# 🚀 XcelGATE")
    st.markdown("### Specialized AI Tutor")
    st.divider()
    
    st.markdown("### 📚 Study Materials")
    with st.expander("💨 Aerodynamics"):
        st.markdown("- [Inviscid Flow Theory](#)\n- [Viscous Flow & Boundary Layers](#)\n- [Wind Tunnel Testing](#)")
    with st.expander("🔥 Propulsion"):
        st.markdown("- [Gas Turbines & Jet Engines](#)\n- [Thermodynamics Cycles](#)\n- [Rocket Propulsion](#)")
    with st.expander("✈️ Flight Mechanics"):
        st.markdown("- [Aircraft Performance](#)\n- [Static Stability](#)\n- [Dynamic Stability](#)")
    with st.expander("🏗️ Structures"):
        st.markdown("- [Strength of Materials](#)\n- [Flight Vehicle Structures](#)\n- [Vibration Theory](#)")
    with st.expander("🛰️ Space Dynamics"):
        st.markdown("- [Orbital Mechanics](#)\n- [Kepler's Laws](#)\n- [Satellite Trajectories](#)")
        
    st.divider()
    st.markdown("**Status:** 🟢 Physics Engine Active")
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.session_state.chat_session = model.start_chat(enable_automatic_function_calling=True)
        st.rerun()

# ==========================================
# 5. MAIN WEBSITE UI (Header)
# ==========================================
col_title, col_end = st.columns([3.5, 1.5])

with col_title:
    st.markdown('<p class="main-title">XcelGATE</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Zero Hallucinations. 100% Mathematical Precision.</p>', unsafe_allow_html=True)

quick_prompt = None
display_text = None

with col_end:
    st.write("") 
    if st.button("🛑 End Prep & Get Report", type="primary"):
        display_text = "📊 *(System Request): Generating Final Performance & Weakness Report...*"
        quick_prompt = "I am ending my prep session. Please look back at all the questions I answered in this chat history. 1. Verify my answers. 2. Generate a 'Final Subject Report' that outlines my overall performance. 3. Crucially, give me a bulleted list of the EXACT concepts and subjects I am weak in and need to study based on my mistakes."

st.markdown("##### 📝 Generate Practice Question:")
col1, col2, col3 = st.columns(3)

if col1.button("MCQ (Multiple Choice)"): 
    display_text = "*(Generated via Quick Action)*: Generate an MCQ."
    quick_prompt = "Generate a hard GATE Aerospace Multiple Choice Question (MCQ). Give me 4 options where only 1 is correct."
if col2.button("MSQ (Multiple Select)"): 
    display_text = "*(Generated via Quick Action)*: Generate an MSQ."
    quick_prompt = "Generate a GATE Aerospace Multiple Select Question (MSQ). Give me 4 options where multiple answers are correct."
if col3.button("NAT (Numerical Answer)"): 
    display_text = "*(Generated via Quick Action)*: Generate a NAT."
    quick_prompt = "Generate a GATE Aerospace Numerical Answer Type (NAT) question. Give me the variables and ask me to calculate the exact number."

st.divider()

# Draw the past chat history on the screen
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask an Aerospace engineering question or type your answer...")
actual_input = quick_prompt or user_input

# ==========================================
# 6. MESSAGE PROCESSING
# ==========================================
if actual_input:
    final_display = display_text if quick_prompt else actual_input
    
    with st.chat_message("user"):
        st.markdown(final_display)
        
    st.session_state.messages.append({"role": "user", "content": final_display})

    with st.chat_message("assistant"):
        try:
            with st.spinner("🚀 Processing query and verifying math..."):
                response = st.session_state.chat_session.send_message(actual_input)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
        except Exception as e:
            if "429" in str(e) or "Quota" in str(e) or "ResourceExhausted" in str(e):
                st.error("🚦 We are chatting too fast! Google requires a short cooldown on the free tier. Please wait about 60 seconds.")
            else:
                st.error(f"An unexpected error occurred: {e}")