"""
Entry point for the Text Summarizer System.

This script initializes and runs the Flask application.
"""

from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # Retrieve host and port from environment variables with default values
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', 8080))
    debug_mode = os.getenv('FLASK_DEBUG', 'False') == 'True'
    
    app.run(host=host, port=port, debug=debug_mode)
