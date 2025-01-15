#!/bin/bash
gunicorn -c gunicorn_config.py --reload --worker-class sync run:app --bind 0.0.0.0:8080 --timeout 120
