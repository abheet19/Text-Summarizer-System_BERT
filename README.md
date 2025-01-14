# Text Summarizer System (BERT)

Welcome to the Text Summarizer System powered by a BERT-based extractive summarizer.

## Table of Contents

1. Overview
2. Installation and Requirements
3. How to Run
4. Detailed Theory
5. Usage Workflow
6. Additional Configuration & Deployment
7. Contributing
8. License

---

## 1. Overview

This web application generates short, coherent summaries from textual data, relying on BERT's transformer architecture to identify the most significant parts of the text. It allows:
- Summarizing files (PDF, DOCX, TXT).
- Summarizing text scraped from a URL.
- Saving summaries to DOCX files along with a generated word cloud.

---

## 2. Installation and Requirements

Before proceeding, ensure you have Python 3.x installed and Git available.  
Install the dependencies using:
```
pip install -r requirements.txt
```
All library versions are explicitly listed in the [requirements.txt](requirements.txt) file.

---

## 3. How to Run

1. Clone or download this repository to your local machine.
2. Navigate to the project directory:
   ```
   cd Text-Summarizer-System_BERT
   ```
3. (Optional) Adjust configurations in `config.py` if needed.
4. Install dependencies (step covered above).
5. Start the Flask application:
   ```
   bash start.sh
   ```
   or on Windows:
   ```
   gunicorn -c gunicorn_config.py run:app
   ```
6. Access the app in your browser at:
   ```
   http://127.0.0.1:8000
   ```

---

## 4. Detailed Theory

Under the hood, this system uses an extractive summarization technique. Key highlights:
- Uses the “Summarizer” library, leveraging a pretrained BERT model to rank sentences based on contextual embeddings.
- Extractive, rather than abstractive, meaning it picks crucial sentences from the original text rather than paraphrasing.
- Word cloud generation: Generates a visual representation of term frequencies in the processed text.

---

## 5. Usage Workflow

1. Upload a file under “Upload Document for Summarization” or provide a URL link in “Summarization by scraping a URL link content”.
2. Once the text is processed, you can see the summary and optionally download a DOCX file containing the summary and word cloud.

---

## 6. Additional Configuration & Deployment

- Adjust environment variables in `.env` or `config.py` to set secret keys, debug modes, etc.
- Containerize the application (e.g., using Docker) for consistent deployment across environments.
- Deploy to a cloud platform (Heroku, AWS, Azure, etc.) by following their specific instructions. Ensure you configure all environment variables and port mappings properly.

---

## 7. Contributing

Feel free to open issues, suggest improvements, or submit pull requests. Collaboration is welcome. Ensure you follow conventional commit messages and document your changes clearly.

---

## 8. License

This project is provided “as is” for educational and practice purposes. For official licensing details, consult the LICENSE file (if present) or add a relevant open-source license of your choice.