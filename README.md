# Personalized AI Agent

A role-based AI assistant that customizes its responses based on the selected
persona: **Marketer**, **Researcher**, or **Ops Assistant**. Built to demonstrate
core skills for the "Build Personalized AI Agents" task in Applied AI roles.

## What it does
- Same question → different answer depending on the selected role
- Each role has its own system prompt (tone, priorities, output style)
- Keeps short-term memory of the last 3 exchanges for context
- Guardrail: each role is instructed to say "I'm not sure" instead of
  inventing facts (basic hallucination control)
- API key is loaded securely from a `.env` file — never typed into the app
  or hardcoded in the code

## Tech stack
- Python
- Streamlit (UI)
- Google Gemini API (`gemini-2.5-flash`) — the model brain
- python-dotenv — for secure key loading

## Project structure
```
personalized_agent_gemini.py   # main Streamlit app
.env                            # your API key goes here (keep private)
README.md                       # this file
```

## How to run
1. Install dependencies:
   ```
   pip install streamlit google-generativeai python-dotenv
   ```
2. Get a free API key from https://aistudio.google.com/app/apikey
3. Open the `.env` file and replace the placeholder with your real key:
   ```
   GOOGLE_API_KEY=your_real_key_here
   ```
4. Run the app:
 
   streamlit google-generativeai python-dotenv request
   ``
   streamlit run personalized_agent_gemini.py
   ```
5. Pick a role in the sidebar and start chatting.

## Example demo flow
1. Select "Marketer" → ask "How do I promote a new coffee shop?"
   → Get punchy ad copy ideas.
2. Switch to "Researcher" → ask the same question
   → Get a structured breakdown (market analysis angle).
3. Switch to "Ops Assistant" → ask the same question
   → Get a step-by-step launch checklist.

This shows the same underlying model behaving as different specialized
agents depending on configuration — the core idea behind "personalized AI
agents" for different workflows/roles.

## Security note
- Never commit the `.env` file to GitHub. Add a `.gitignore` with `.env`
  in it if you push this project to a repository.
- The key stays local to your machine — it is never shown in the UI or
  sent anywhere except directly to Google's API.

## Possible extensions
- Add a retrieval tool (web search) for up-to-date facts
- Persist memory to a file/database instead of session-only
- Add more roles (e.g., Support Agent, Data Analyst)
