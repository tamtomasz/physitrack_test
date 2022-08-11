@echo off

set args=%*

py -m ensurepip --upgrade
py -m pip install virtualenv
py -m virtualenv %~dp0venv
call %~dp0venv\Scripts\activate.bat
pip install -r %~dp0requirements.txt
python -m test_runner %args%
