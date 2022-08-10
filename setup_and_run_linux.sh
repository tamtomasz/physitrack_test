#!/bin/sh

python -m venv ./venv
./venv/Scripts/activate
pip install -r ./requirements.txt
python -m run_all_tests "$0"