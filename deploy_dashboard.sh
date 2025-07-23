#!/bin/bash
pip install -r dashboard/requirements.txt
gunicorn --bind 0.0.0.0:8080 dashboard.app:server
