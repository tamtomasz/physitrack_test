@echo off

set args=%*

py -m venv %~dp0venv
call %~dp0venv\Scripts\activate.bat
pip install -r %~dp0requirements.txt
python -m test_runner %args%
