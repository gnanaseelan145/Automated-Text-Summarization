from flask import Flask, render_template, request, redirect, url_for
from summarizer import summarize_text
from pdf_extractor import extract_text_from_pdf
from text_cleaner import clean_text
from QA_chatbot import ask_question

app = Flask(__name__)

# Home route to display the form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handling PDF upload
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file and file.filename.endswith('.pdf'):
            raw_text = extract_text_from_pdf(file)
            cleaned_text = clean_text(raw_text)
            return render_template("result.html", text=cleaned_text)
    return render_template("index.html")

# Route for summarization and Q&A
@app.route("/process", methods=["POST"])
def process():
    text = request.form["text"]
    if "summarize" in request.form:
        summary = summarize_text(text)
        return render_template("result.html", text=text, summary=summary)
    elif "ask" in request.form:
        question = request.form["question"]
        answer = ask_question(question, text)
        return render_template("result.html", text=text, answer=answer, question=question)

if __name__ == "__main__":
    app.run(debug=True)


