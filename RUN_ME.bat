echo off
color 0A
echo Creating environement
py -m venv wenv
wenv\Scripts\activate &^
echo Upgrading pip &^
python -m pip install --upgrade pip &^
echo Installing requirements &^
pip install -r files\requirements.txt &^
echo All done &^
echo Running script &^
cd files &^
python launch_local.py &^
cd .. &^
echo Deactivating environement &^
deactivate
