@echo off
call venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r dashboard\requirements.txt --no-cache-dir
python dashboard\app.py
