# 🐱 Neko Chatbot - AI-Powered Emotional Chatbot

**Neko** is an AI-powered chatbot capable of detecting **human emotions** from text and reacting accordingly with animated pixel-art expressions. Built with **React (Frontend)**, **FastAPI (Backend)**, and **Cohere (AI Processing)**.

---

## 🚀 Features
- ✅ AI-powered **sentiment analysis** using NLP  
- ✅ **Dynamically animated cat** reacting to emotions  
- ✅ **Interactive UI** with a **retro pixel-art design**  
- ✅ FastAPI-powered **backend** with **React frontend**  
- ✅ Supports **6 core emotions**: Joy, Sadness, Anger, Fear, Surprise, Neutral  

---

## 🛠️ Installation & Setup  

### **1️⃣ Clone the repository**
```bash
git clone https://github.com/yourusername/neko-chatbot.git
cd neko-chatbot
```

### **2️⃣ Set up the backend (FastAPI)**
1.Navigate to the backend folder:
```bash
cd backend
```
2.Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```
3.Install dependencies:
```bash
pip install -r requirements.txt
```
4.Set up your API key (required for Cohere AI processing):
  - Get a Cohere API Key by signing up at Cohere.com
  - in the backfolder , go to main.py and look for cohere_api_key

5.Start the FastAPI server:
```bash
uvicorn main:app --reload
```

✅ Your backend is now running at http://127.0.0.1:8000

### **3️⃣ Set up the frontend (React)**
1.Navigate to the frontend folder
2.Install dependencies:
```bash
npm install
```
Start the React frontend:
```bash
npm start
```
✅ Your chatbot will now run on http://localhost:3000

## ⚙️ Usage
  - Type a message in the input box.
  - Neko will analyze the sentiment and reply with an emotionally appropriate response.
  - The animated pixel-art cat changes expression based on the detected emotion.

## 📌 Future Improvements
  🎙️ Voice emotion detection (speech-to-text + sentiment analysis)<br>
  🌍 Multi-language support<br>
  📱 Mobile-friendly UI adaptation<br>
  💾 Memory-based conversation tracking<br>

## 🤝 Contributing
Feel free to submit issues or pull requests to improve the chatbot!
Let’s make Neko even smarter and cuter! 🐱💡

## 📝 License
This project is open-source under the MIT License.

