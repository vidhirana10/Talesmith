import streamlit as st
import google.generativeai as genai
import pyttsx3
import tempfile
import os
import fitz  # PyMuPDF for PDF processing
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("⚠️ Google API key not found. Check your .env file.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text

# Function to extract text from a URL
def extract_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return " ".join([p.text for p in soup.find_all("p")])
    except Exception as e:
        return f"Error fetching text: {e}"

# Function to generate historical story using Gemini
def generate_story(history_text):
    prompt = f"""
    You are a historian and expert storyteller. Given the following historical text, 
    generate a fictional yet historically accurate narrative featuring a fictional 
    character experiencing the real events of that time. The story should be immersive, 
    engaging, and factually correct.

    Historical Text:
    {history_text}

    Now, create the story:
    """
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    return response.text

# Function to convert text to speech (offline)
def text_to_speech(text):
    engine = pyttsx3.init()
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    engine.save_to_file(text, temp_file.name)
    engine.runAndWait()
    return temp_file.name

# Streamlit UI
st.title("📜 Textbook to storybooks 🎙️")
st.write("Enter a chapter from a history textbook, upload a PDF, or provide a link to generate a historically accurate story.")

# User input options
option = st.radio("Choose input type:", ["📖 Paste Text", "📂 Upload PDF", "🔗 Enter URL"])

history_text = ""

if option == "📖 Paste Text":
    history_text = st.text_area("Paste your history text here:", height=200)

elif option == "📂 Upload PDF":
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    if uploaded_file is not None:
        history_text = extract_text_from_pdf(uploaded_file)
        st.text_area("Extracted Text:", history_text, height=200)

elif option == "🔗 Enter URL":
    url = st.text_input("Enter a URL:")
    if st.button("Fetch Text"):
        if url:
            history_text = extract_text_from_url(url)
            st.text_area("Extracted Text:", history_text, height=200)
        else:
            st.warning("⚠️ Please enter a valid URL.")

if st.button("Generate Story & Audio"):
    if history_text:
        with st.spinner("📝 Generating story..."):
            story = generate_story(history_text)
            audio_file = text_to_speech(story)

        st.subheader("📖 Your Historical Story:")
        st.write(story)

        # Play audio
        st.audio(audio_file, format="audio/mp3", start_time=0)
    else:
        st.warning("⚠️ Please provide historical text.")
