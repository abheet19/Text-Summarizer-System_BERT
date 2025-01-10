"""
Entry point for the Text Summarizer System.

This script initializes and runs the Flask application.
"""

from app import create_app
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

app = create_app()

if __name__ == '__main__':
    # Retrieve host and port from environment variables with default values
    host = os.getenv('FLASK_RUN_HOST', '0.0.0.0')
    port = int(os.getenv('FLASK_RUN_PORT', 8080))
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't', 'y', 'yes']
    
    # Ensure the downloads directory exists
    os.makedirs(os.path.join(os.getcwd(), 'downloads'), exist_ok=True)
    
    app.run(host=host, port=port, debug=debug_mode)
