python -m venv study_timer         # Create a virtual environment
source study_timer/bin/activate   # Activate the virtual environment

pip install -r requirements.txt

xterm -e "python app/study_timer.py"