# AI Study Assistant

An AI-powered study helper built with Python, Streamlit, and Google's Gemini API.

## Features

- **Topic Explainer:** Explains a topic in beginner-friendly language.
- **Notes Generator:** Creates structured notes with headings and examples.
- **Quiz Generator:** Creates multiple-choice questions and an answer key.
- **Text Summarizer:** Summarizes pasted study material.
- Learning-level and response-language preferences.
- Download generated content as a text file.

## Tech stack

- Python
- Streamlit
- Google Gen AI Python SDK (`google-genai`)
- Gemini API

## 1. Requirements

- Python 3.11 or newer
- A Gemini API key from Google AI Studio
- Internet connection for Gemini API requests

## 2. Setup on Windows PowerShell

Open PowerShell in this project folder.

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell blocks environment activation, you can install packages without activating:

```powershell
python -m pip install -r requirements.txt
```

## 3. Set your Gemini API key

Create a key at https://aistudio.google.com/apikey.

For the current PowerShell window:

```powershell
$env:GEMINI_API_KEY="PASTE_YOUR_KEY_HERE"
```

Do not paste your real API key into source code, README files, screenshots, or GitHub.

Alternatively, Streamlit secrets can be used. Create `.streamlit/secrets.toml` locally:

```toml
GEMINI_API_KEY = "PASTE_YOUR_KEY_HERE"
```

The `.streamlit/secrets.toml` file is excluded by `.gitignore`.

## 4. Run the application

```powershell
python -m streamlit run app.py
```

Streamlit will open the application in your browser. Select one of the four tools, enter a topic or study material, choose your learning preferences, and click **Generate**.

## 5. Model configuration

The app currently defaults to `gemini-4-hydrogen`, following the Gemini API getting-started documentation available when this project was prepared.

If your Google AI Studio account does not have access to that model, set `GEMINI_MODEL` to a model name currently available to your API key:

```powershell
$env:GEMINI_MODEL="YOUR_AVAILABLE_MODEL_NAME"
```

Model availability and free-tier limits can change.

## 6. Project structure

```text
ai-study-assistant/
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Learning outcomes

- Explored AI assistants and their use cases.
- Connected a Python application to a generative AI API.
- Used prompt instructions to guide model responses.
- Built an interactive web interface with Streamlit.
- Practised secure API-key handling.
- Prepared a project for GitHub sharing.

## Responsible use

AI-generated answers may be inaccurate or incomplete. Verify important information against textbooks, course materials, and trusted sources. Do not enter private or sensitive information into the app.
