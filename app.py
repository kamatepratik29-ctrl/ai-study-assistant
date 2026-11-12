import os
import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide",
)
MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

def get_api_key():
    """Read the Gemini API key from environment variables or Streamlit secrets."""
    key = os.getenv("GEMINI_API_KEY")
    if key:
        return key

    try:
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        return None


def generate_with_gemini(prompt: str) -> str:
    api_key = get_api_key()

    if not api_key:
        raise ValueError("Gemini API key not found.")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    answer = response.text

    if not answer:
        raise RuntimeError("Gemini returned an empty response.")

    return answer

def build_prompt(feature: str, content: str, level: str, language: str) -> str:
    """Create a task-specific prompt for the selected study tool."""
    instructions = {
        "Topic Explainer": (
            "Explain the topic in beginner-friendly language. Include a simple "
            "definition, how it works, a real-world example, key points, and a "
            "short recap."
        ),
        "Notes Generator": (
            "Create well-organized study notes with a title, headings, concise "
            "bullet points, important definitions, examples, and a short summary."
        ),
        "Quiz Generator": (
            "Create 5 multiple-choice questions. Give four options (A-D) for each. "
            "After all questions, provide an answer key with a brief explanation "
            "for each correct answer."
        ),
        "Text Summarizer": (
            "Summarize the supplied study material. Start with a short overview, "
            "then list the most important points and key terms. Do not invent "
            "facts that are not present in the supplied material."
        ),
    }

    return f"""
You are a helpful study assistant. Support learning; do not claim that generated
content is guaranteed to be error-free. If the input is ambiguous, say what is
unclear rather than inventing details.

Task: {feature}
Student level: {level}
Response language: {language}

Instructions:
{instructions[feature]}

Student topic or study material:
{content}

Use clear formatting and explain technical terms when needed.
"""


st.title("📚 AI Study Assistant")
st.caption("Learn smarter with AI-powered explanations, notes, quizzes, and summaries.")

with st.sidebar:
    st.header("Study preferences")
    level = st.selectbox(
        "Your learning level",
        ["Beginner", "Intermediate", "Advanced"],
    )
    language = st.selectbox(
        "Response language",
        ["English", "Hindi", "Hinglish"],
    )
    st.divider()
    st.caption(f"Model: {MODEL_NAME}")
    st.caption("Your API key is read from your local environment or Streamlit secrets.")

feature = st.radio(
    "Choose a study tool",
    ["Topic Explainer", "Notes Generator", "Quiz Generator", "Text Summarizer"],
    horizontal=True,
)

placeholders = {
    "Topic Explainer": "Example: Explain photosynthesis in simple words.",
    "Notes Generator": "Example: Operating System – Process Management",
    "Quiz Generator": "Example: Create a quiz on Python loops and functions.",
    "Text Summarizer": "Paste your study material here...",
}

content = st.text_area(
    "Enter a topic or paste your study material",
    height=220,
    placeholder=placeholders[feature],
    max_chars=12000,
)

col1, col2 = st.columns([1, 5])
with col1:
    generate_clicked = st.button("Generate", type="primary", use_container_width=True)
with col2:
    st.caption("Review AI-generated content and verify important facts with your course materials.")

if generate_clicked:
    if not content.strip():
        st.warning("Please enter a topic or study material first.")
    else:
        prompt = build_prompt(feature, content.strip(), level, language)
        with st.spinner("Your study content is being generated..."):
            try:
                result = generate_with_gemini(prompt)
                st.session_state["last_result"] = result
                st.session_state["last_feature"] = feature
            except Exception as exc:
                st.error(f"Could not generate content: {exc}")

if "last_result" in st.session_state:
    st.divider()
    st.subheader(f"✨ {st.session_state.get('last_feature', 'Your result')}")
    st.markdown(st.session_state["last_result"])
    st.download_button(
        "Download result as text",
        data=st.session_state["last_result"],
        file_name="ai_study_result.txt",
        mime="text/plain",
    )

st.divider()
st.caption(
    "Learning project for Module 05. AI responses can contain mistakes; "
    "always verify important information."
)
