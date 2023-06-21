#!/bin/bash
echo "Creating environement"
python3 -m venv lenv
. ./lenv/Scripts/activate
echo "Upgrading pip"
python3 -m pip install --upgrade pip
echo "Installing requirements"
pip install -r files\requirements.txt
deactivate
echo "All done"
