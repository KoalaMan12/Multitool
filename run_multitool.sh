#!/bin/bash

# Define the directory where multitool.py is located
MULTITOOL_DIR="/home/floppykoala/Downloads/Multitool"

# Check if multitool.py exists in the specified directory
if [ ! -f "$MULTITOOL_DIR/multitool.py" ]; then
    echo "multitool.py not found in $MULTITOOL_DIR!"
    exit 1
fi

# Run multitool.py using Python 3
python3 "$MULTITOOL_DIR/multitool.py"
