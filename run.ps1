# Create virtual environment
python -m venv env

# Activate virtual environment
. .\env\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt

# Run scrapy crawl apx_spider
scrapy crawl apx_spider

# Run python companies_script.py
python .\companies_script.py

# Deactivate virtual environment
deactivate