# Talesmith Project(RAG)


## Overview
Talesmith is a Streamlit app that converts historical textbook content into engaging fictional yet historically accurate stories using Google's Gemini AI. It also provides an offline text-to-speech feature to narrate the generated stories.

### Features:
- Extract text from PDF files.
- Extract text from web pages (URLs).
- Accept direct text input.
- Generate an immersive historical story using Google Gemini AI.
- Convert the story into speech (offline TTS with pyttsx3).
- Play the generated audio directly in the app.

## Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/vidhirana10/Talesmith.git
   cd Talesmith
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate   # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up API key:
   - Create a `.env` file in the root directory.
   - Add your Google API key:
   ```plaintext
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Future Enhancements:
- Add language support for multiple languages.
- Improve TTS voice quality with more natural voices.
- Enhance UI/UX with a better design.
- Implement real-time translation for generated stories.

## License:
MIT License - Feel free to modify and distribute!
