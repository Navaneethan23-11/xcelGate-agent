# 🚀 XcelGATE: Autonomous AI Agent for GATE Aerospace

## 📌 The Problem
Large Language Models (LLMs) are notorious for hallucinating math and physics calculations. For a GATE Aerospace aspirant, an AI making a math error could mean the difference between passing and failing.

## 💡 Our Solution
XcelGATE is not a standard chatbot—it is a native, terminal-based AI Agent. We engineered a custom backend equipped with Python-based physics calculators. 

When a user submits an answer, the Agent does not guess. It routes the variables through our native Python tools (like `calculate_lift_force` and `calculate_mach_number`) to verify the absolute mathematical truth *before* evaluating the student. 

## 🛠️ Features
- **Syllabus Guardrails:** The Agent actively rejects topics outside the official GATE Aerospace syllabus.
- **Autonomous Tool Calling:** Automatically detects which physics formula is needed and runs the math in the background.
- **Rate-Limit Error Handling:** Gracefully handles API quota limits without crashing.
- **Session Report Cards:** Generates a custom performance summary when the user types `exit`.

## ⚙️ How to Run Locally
1. Install dependencies: `pip install -r requirements.txt`
2. Add your Gemini API key inside `agent.py`.
3. Run the agent: `python agent.py`