#!/bin/sh

python -m venv ./venv
./venv/Scripts/activate
pip install -r ./requirements.txt
python -m test_runner -b "$0"