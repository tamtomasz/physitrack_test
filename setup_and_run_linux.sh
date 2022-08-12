#!/bin/sh

while getopts b: flag
do
    case "${flag}" in
        b) browser=${OPTARG};;
    esac
done

python -m venv ./venv
./venv/Scripts/activate
pip install -r ./requirements.txt
python -m test_runner -b "$browser"