"""
Entry point for the Text Summarizer System.

This script initializes and runs the Flask application.
"""

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
