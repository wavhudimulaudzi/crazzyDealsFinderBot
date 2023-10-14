#!/bin/bash

# Create a virtual environment named 'venv' (or any other name you prefer)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required packages
pip install -r requirements.txt
