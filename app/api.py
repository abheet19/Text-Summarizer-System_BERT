"""
API blueprint for the Text Summarizer System.

This module defines the routes for handling file uploads, URL submissions,
summary generation, and file downloads.
"""

from flask import Blueprint, request, render_template, send_file
from .service import (
    clean_text_and_generate_wordcloud,
    generate_bert_summary,
    summarize_url,
    save_docx_file,
    remove_files,
    process_file,
    generate_docx,
    safe_remove_and_render
)
import pathlib
import os
import logging

# Configure logging for the API module
logging.basicConfig(level=logging.ERROR)

api = Blueprint('api', __name__)

@api.route('/', methods=['GET', 'POST'])
def home():
    """
    Render the home page and remove previous word cloud and DOCX files.

    Returns:
        Response: The rendered home page.
    """
    return safe_remove_and_render('index.html', render_template)

@api.route('/PDF', methods=['GET', 'POST'])
def PDF():
    """
    Render the PDF upload page and remove previous word cloud and DOCX files.

    Returns:
        Response: The rendered PDF upload page.
    """
    return safe_remove_and_render('PDF.html', render_template)

@api.route('/PDF_result', methods=['GET', 'POST'])
def PDF_result():
    """
    Process the uploaded PDF/DOCX/TXT file, generate a summary, and render the result page.

    Returns:
        Response: The rendered result page with the summary or an error message.
    """
    remove_files()
    try:
        if request.method == 'POST':
            uploaded_file = request.files.get('name')
            if not uploaded_file:
                return "<h1>Please provide a file</h1>"

            try:
                uploaded_file.save(uploaded_file.filename)
            except Exception as e:
                logging.error(f"Failed to save file: {e}")
                return "<h1>Error saving file</h1>"

            try:
                file_content = process_file(uploaded_file)
            except ValueError as e:
                os.remove(uploaded_file.filename)
                return f"<h1>{str(e)}</h1>"

            os.remove(uploaded_file.filename)
            cleaned_text = clean_text_and_generate_wordcloud(file_content)
            summary_text = generate_bert_summary(cleaned_text)
            save_docx_file(summary_text)

            return render_template('PDF_result.html', summary=summary_text)
    except Exception as e:
        logging.error(f"Error processing file: {e}")
        return "<h1>Error processing file</h1>"

    return render_template('PDF.html')

@api.route('/RAW', methods=['GET', 'POST'])
def RAW():
    """
    Render the URL input page and remove previous word cloud and DOCX files.

    Returns:
        Response: The rendered URL input page.
    """
    return safe_remove_and_render('RAW.html', render_template)

@api.route('/RAW_result', methods=['GET', 'POST'])
def RAW_result():
    """
    Process the provided URL, generate a summary, and render the result page.

    Returns:
        Response: The rendered result page with the summary or an error message.
    """
    remove_files()
    try:
        if request.method == 'POST':
            url = request.form.get('name')
            summary_text = summarize_url(url)
            if summary_text == "Invalid URL":
                return "<h1>Error! Please upload a correct URL</h1>"
            return render_template('RAW_result.html', summary=summary_text)
    except Exception as e:
        logging.error(f"Error processing URL: {e}")
        return "<h1>Error processing URL</h1>"

    return render_template('RAW.html')

@api.route('/download', methods=['POST'])
def download():
    """
    Allow users to download the generated summary as a DOCX file.

    Returns:
        Response: The DOCX file for download or an error message if unavailable.
    """
    summary = request.form.get('summary')
    if not summary:
        return "No summary available to download.", 400
    file_path = generate_docx(summary)
    return send_file(file_path, as_attachment=True)
