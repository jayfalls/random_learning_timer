# Get the directory of the shell script
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")"

# Set PYTHONPATH to include the app directory
export PYTHONPATH=$PYTHONPATH:$SCRIPT_DIR/app

# Create a virtual environment
python -m venv env       
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
xterm -e "python3 $SCRIPT_DIR/app/study_timer.py"