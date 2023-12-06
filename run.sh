#!/bin/bash
echo "Proceeding with the script."

# Create virtual environment
python3 -m venv env

# Activate virtual environment
source env/bin/activate

# Install requirements
pip install -r requirements.txt

# Run scrapy crawl apx_spider
scrapy crawl apx_spider

# Run python companies_script.py
python companies_script.py

# Deactivate virtual environment
deactivate

echo "Script execution completed."