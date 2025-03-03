# Talesmith

## 📜 Overview
This Streamlit app converts historical textbook content into engaging fictional yet historically accurate stories using Google's Gemini AI. It also provides an offline text-to-speech feature to narrate the generated stories.

## 🚀 Features
- Extract text from **PDF files**.
- Extract text from **web pages (URLs)**.
- Accept **direct text input**.
- Generate an **immersive historical story** using Google Gemini AI.
- Convert the story into **speech (offline TTS with pyttsx3)**.
- Play the generated audio directly in the app.

## 🛠️ Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/textbook-to-storybooks.git
cd textbook-to-storybooks
```

### 2️⃣ Create and Activate a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set Up API Key
- Create a **.env** file in the root directory.
- Add your Google API key:
  ```sh
  GOOGLE_API_KEY=your_google_api_key_here
  ```

## ▶️ Running the App
```sh
streamlit run app.py
```

## 📂 Project Structure
```
📂 textbook-to-storybooks/
├── app.py                 # Main Streamlit app
├── requirements.txt        # Required dependencies
├── .env                    # API Key (not included, add manually)
├── README.md               # Project documentation
```

## 🏗️ Dependencies
- `streamlit`
- `google-generativeai`
- `pyttsx3`
- `PyMuPDF` (for PDF processing)
- `requests` (for web scraping)
- `beautifulsoup4` (for text extraction from URLs)
- `dotenv` (for API key management)

## 🛠️ How It Works
1. **Select input type** (Paste Text, Upload PDF, or Enter URL).
2. **Extract text** using the chosen method.
3. **Generate a historical story** with Gemini AI.
4. **Convert the story to speech** using offline TTS.
5. **Listen to the generated audio**.

## 📌 Future Enhancements
- Add **language support** for multiple languages.
- Improve **TTS voice quality** with more natural voices.
- Enhance **UI/UX** with a better design.
- Implement **real-time translation** for generated stories.

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to improve.

## 📜 License
MIT License - Feel free to modify and distribute!

---
Happy storytelling! 🎙️📖

