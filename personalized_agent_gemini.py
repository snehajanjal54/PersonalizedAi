"""
Personalized AI Agent - Role-based Assistant (Gemini version)
 streamlit run personalized_agent_gemini.py
"""

import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import google.generativeai as genai
# ---------------------------
# 0. LOAD API KEY FROM .env
# ---------------------------
load_dotenv()
api_key = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY") 

# ---------------------------
# 1. ROLE-BASED SYSTEM PROMPTS
# ---------------------------
ROLE_PROMPTS = {
    "Marketer": """You are a marketing assistant. 
Your job: give catchy, persuasive, audience-focused answers.
Prioritize: ad copy ideas, captions, hooks, campaign angles.
Tone: energetic, creative, concise.
If you don't have real data (like current trends or stats), 
say so clearly instead of making it up.""",

    "Researcher": """You are a research assistant. 
Your job: give structured, factual, well-organized answers.
Prioritize: clear breakdown of points, logical structure, sources if known.
Tone: neutral, precise, academic.
If you are not certain about a fact, explicitly say 
'I'm not fully certain about this' instead of guessing.""",

    "Ops Assistant": """You are an operations assistant. 
Your job: give step-by-step, actionable, checklist-style answers.
Prioritize: clarity, order of steps, practical execution.
Tone: direct, no fluff, professional.
If a step depends on information you don't have, 
ask for it instead of assuming."""
}

# ---------------------------
# 2. PAGE SETUP
# ---------------------------
st.set_page_config(page_title="Personalized AI Agent", page_icon="🤖")
st.title("🤖 Personalized AI Agent ")
st.caption("Same question → different answer, based on role. Built for AI/ML Internship demo.")

# ---------------------------
# 3. CHECK API KEY (from .env, not user input)
# ---------------------------
if not api_key:
    st.error()
    st.stop()

# ---------------------------
# 4. ROLE SELECTOR
# ---------------------------
role = st.sidebar.selectbox("Choose Agent Role", list(ROLE_PROMPTS.keys()))
st.sidebar.info(f"Current role: **{role}**")

# ---------------------------
# 5. MEMORY (session-based)
# ---------------------------
if "history" not in st.session_state:
    st.session_state.history = []  # list of (role, question, answer)

# ---------------------------
# 6. CHAT INPUT
# ---------------------------
user_input = st.text_input("Ask something:")

if st.button("Ask Agent") and user_input:
    with st.spinner("Thinking..."):
        try:
            genai.configure(api_key=api_key)

            system_prompt = ROLE_PROMPTS[role]

            # Include short memory context (last 3 exchanges) for continuity
            context = ""
            for r, q, a in st.session_state.history[-3:]:
                context += f"\n[Previous - {r}] Q: {q}\nA: {a}\n"

            full_prompt = f"{context}\n\nNew question: {user_input}"

            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash",
                system_instruction=system_prompt
            )

            response = model.generate_content(full_prompt)
            answer = response.text

            st.session_state.history.append((role, user_input, answer))

        except Exception as e:
            st.error(f"Something went wrong: {e}")

# ---------------------------
# 7. DISPLAY CONVERSATION
# ---------------------------
st.subheader("Conversation")
for r, q, a in reversed(st.session_state.history):
    st.markdown(f"**[{r}] You:** {q}")
    st.markdown(f"**Agent:** {a}")
    st.divider()

# ---------------------------
# 8. RESET MEMORY BUTTON
# ---------------------------
if st.sidebar.button("Clear Memory"):
    st.session_state.history = []
    st.rerun()
