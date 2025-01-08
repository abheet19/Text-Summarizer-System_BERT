from flask import Blueprint, request, render_template, send_file
from service import clean_and_process, BERT, url_validator, dump, remove_files, process_file, summarize_url
import pathlib
import os
import logging

logging.basicConfig(level=logging.ERROR)

api = Blueprint('api', __name__)

@api.route('/', methods=['GET', 'POST'])
def home():
    """
    Render the home page and remove previous word cloud and DOCX files.
    """
    remove_files()
    return render_template('index.html')

@api.route('/PDF', methods=['GET', 'POST'])
def PDF():
    """
    Render the PDF upload page and remove previous word cloud and DOCX files.
    """
    remove_files()
    return render_template('PDF.html')

@api.route('/PDF_result', methods=['GET', 'POST'])
def PDF_result():
    """
    Process the uploaded PDF/DOCX/TXT file, generate a summary, and render the result page.
    """
    remove_files()
    try:
        if request.method == 'POST':
            file = request.files.get('name')
            if not file:
                return "<h1>Please provide a file</h1>"

            file.save(file.filename)
            try:
                text = process_file(file)
            except ValueError as e:
                os.remove(file.filename)
                return f"<h1>{str(e)}</h1>"

            os.remove(file.filename)
            cleaned_text = clean_and_process(text)
            summary = BERT(cleaned_text)
            dump(summary)

            return render_template('PDF_result.html', summary=summary)
    except Exception as e:
        logging.error(f"Error processing file: {e}")
        return "<h1>Error processing file</h1>"

    return render_template('PDF.html')

@api.route('/RAW', methods=['GET', 'POST'])
def RAW():
    """
    Render the URL input page and remove previous word cloud and DOCX files.
    """
    remove_files()
    return render_template('RAW.html')

@api.route('/RAW_result', methods=['GET', 'POST'])
def RAW_result():
    """
    Process the provided URL, generate a summary, and render the result page.
    """
    remove_files()
    try:
        if request.method == 'POST':
            url = request.form.get('name')
            summary = summarize_url(url)
            if summary == "Invalid URL":
                return "<h1>Error! Please upload a correct URL</h1>"
            return render_template('RAW_result.html', summary=summary)
    except Exception as e:
        logging.error(f"Error processing URL: {e}")
        return "<h1>Error processing URL</h1>"

    return render_template('RAW.html')

@api.route('/download', methods=['GET', 'POST'])
def download():
    """
    Allow users to download the generated summary as a DOCX file.
    """
    file = pathlib.Path("static/download/file.docx")
    if file.is_file():
        return send_file(file, as_attachment=True)
    return "<h1>No file available for download</h1>"
