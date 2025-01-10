#!/bin/bash
gunicorn -c gunicorn_config.py run:app
