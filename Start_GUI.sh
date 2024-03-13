#!/bin/sh

# Check Python version
version=$(python3 -c "import sys; print('{}.{}'.format(sys.version_info.major, sys.version_info.minor))")
if [ "$(printf '3.6\n%s' "$version" | sort -V | head -n1)" != "3.6" ]; then
    echo "Python version 3.6 or later is required"
    exit 1
fi

# Install dependencies
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies"
    exit 1
fi

# Run the script
python3 GUI.py
