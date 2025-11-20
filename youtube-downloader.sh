#!/usr/bin/env bash
set -e

# Path to your venv
VENV_PATH="./venv"

# Python script to run
SCRIPT="./src/main.py"

# Activate the environment
source "$VENV_PATH/bin/activate"

# Execute the script, passing all arguments
python "$SCRIPT" "$@"
