@echo off
python -m pip install --upgrade pip
python -m pip uninstall -y numpy pandas
python -m pip install -r dashboard\requirements.txt --no-cache-dir
