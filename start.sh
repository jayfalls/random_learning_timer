python -m venv env        # Create a virtual environment
source env/bin/activate   # Activate the virtual environment

pip install -r requirements.txt

xterm -e "python app/study_timer.py"