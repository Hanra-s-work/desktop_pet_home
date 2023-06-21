#!/bin/bash
echo "Creating environement"
python3 -m venv lenv
. ./lenv/bin/activate
echo "Upgrading pip"
python3 -m pip install --upgrade pip
echo "Installing requirements"
pip3 install -r ./files/requirements.txt
deactivate
echo "All done"
echo "Activating environement"
. ./lenv/bin/activate
echo "Running script"
cd ./files
python3 ./launch_local.py
cd ..
echo "Deactivating environement"
deactivate
