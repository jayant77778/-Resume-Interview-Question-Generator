
# 🤖 AI Interview Question Generator from Resume (Gemini API + Streamlit)

This is a simple and powerful web application that uses **Google Gemini API** to generate tailored interview questions from an uploaded resume (PDF format). It extracts text from the resume and generates:

- ✅ 10 Technical Questions based on detected skills  
- 💬 5 HR Questions  
- 🎯 3 Scenario-Based Questions  

Built using **Streamlit**, **PyMuPDF**, and **Gemini API (Flash model)**.

---

## 🚀 Features

- Upload any PDF resume.
- Extracts text using `PyMuPDF (fitz)` library.
- Uses Gemini 2.0 Flash model via REST API.
- Displays AI-generated interview questions in a clean UI.
- Fast and responsive – runs locally using Streamlit.

---

## 📂 Project Structure

```

ai-interview-generator/
├── app.py
├── requirements.txt
└── README.md

````

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-interview-generator.git
cd ai-interview-generator
````

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add Your Gemini API Key

Replace this line in `app.py` with your actual API key:

```python
API_KEY = "Use your api key here"
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## 📦 requirements.txt

```txt
streamlit
pymupdf
requests
```

---

## 📸 Demo Screenshot

![screenshot](https://via.placeholder.com/600x400.png?text=Demo+Screenshot+Here)

---

## 🤝 Credits

* Built with ❤️ using [Google Gemini API](https://ai.google.dev/)
* UI Powered by [Streamlit](https://streamlit.io/)
* PDF Parsing via [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/)

---

## 🛡️ Disclaimer

This app is for educational and prototyping purposes only. Please ensure you're using your own Gemini API key and managing quota limits.

---

## 📬 Contact

Made by [Jayant Bhati](https://www.linkedin.com/in/jayantbhati77/).
For feedback or collaboration, feel free to reach out!

```

