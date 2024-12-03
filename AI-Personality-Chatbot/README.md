# AI Personality Chatbot

An interactive AI chatbot that adapts its responses based on user-configured personality traits using Google Generative AI (Gemini) and Gradio.

## Project Structure

AI-Personality-Chatbot/
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── google_llm.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── personality_data.py
│   └── ui/
│       ├── __init__.py
│       └── interface.py
├── tests/
│   ├── __init__.py
│   └── test_generate_response.py
└── scripts/
    └── setup.sh