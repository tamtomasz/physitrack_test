@echo off

set args=%*

py -m venv %~dp0venv123
call %~dp0venv123\Scripts\activate.bat
pip install -r %~dp0requirements.txt
python -m run_all_tests %args%
