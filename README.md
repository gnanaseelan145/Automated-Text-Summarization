
# 🧠 Automated Text Summarization System

An intelligent web application built using **Flask** that allows users to:
- 📄 Upload a PDF
- 🔍 Extract and summarize text content
- ❓ Ask questions about the document using an interactive chatbot

---

## 🚀 Features

- 📁 PDF Upload and Parsing
- ✂️ Automatic Text Extraction
- 📝 Abstractive & Extractive Summarization
- 🤖 Question-Answering on Uploaded PDFs
- 💬 LLM-powered chatbot using LLaMA or similar
- 🧼 Custom Text Preprocessing & Cleaning
- 🎨 Responsive UI with static assets

---

## 📸 Screenshots

### Extracted Text View
![Extracted Text](Image/Capture1.PNG)

### Ask Questions About PDF
![QA Chatbot](Image/Capture2.PNG)

---

## 🛠️ Tech Stack

| Component         | Technology                  |
|------------------|-----------------------------|
| Backend          | Python, Flask               |
| Summarization    | Transformers / Custom Logic |
| QA Model         | LLaMA or Similar LLMs       |
| PDF Processing   | PyMuPDF / PDFMiner          |
| Frontend         | HTML, CSS, JS (basic)       |
| Hosting Ready    | PythonAnywhere / Heroku     |

---

## 📂 Project Structure

```
Summarizer/
├── app.py                  # Flask main app
├── summarizer.py           # Text summarization logic
├── pdf_extractor.py        # PDF parsing code
├── llama_qa.py             # QA model integration
├── QA_chatbot.py           # User question handling
├── templates/              # HTML templates
├── static/                 # Assets & Images
└── Image/                  # UI Screenshots (Capture1.PNG, Capture2.PNG)
```

---

## ⚙️ How to Run Locally

```bash
# Step 1: Clone the repository
git clone https://github.com/gnanaseelan145/Automated-Text-Summarization.git

# Step 2: Navigate into project
cd Automated-Text-Summarization/text/Summarizer

# Step 3: Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate    # On Windows

# Step 4: Install dependencies
pip install -r requirements.txt

# Step 5: Run the Flask app
python app.py

# App will be live at http://127.0.0.1:5000
```

---

## 🌐 Live Demo (Optional)

[🔗 View on PythonAnywhere](#) *(Add your deployment link here)*

---

## ✍️ Author

**Gnanaseelan M**  
🎓 *BSc Computer Technology Graduate – Class of 2025*  
🚀 Quick learner with strong communication, leadership, and adaptability  
🔧 Skilled in Python, Java, Flask, HTML/CSS, and SQL  
🎯 Passionate about real-world problem solving using tech  

📫 **Contact:**  
- 🔗 [Portfolio Website](https://gnanaseelan145.github.io/Gnanaseelan-Portfolio/)  
- 💼 [LinkedIn](https://www.linkedin.com/in/gnanaseelan-m-806b01250)  
- 🧠 [GitHub](https://github.com/gnanaseelan145)  
- 📧 gnanaseelan145@gmail.com  
- 📱 +91 63806 93689  

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
