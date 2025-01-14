#!/bin/bash
gunicorn -c gunicorn_config.py --reload --worker-class sync run:app --timeout 120
