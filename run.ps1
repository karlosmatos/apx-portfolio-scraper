# Check created virtual environment
if (Test-Path .\env) {
    Write-Output "Virtual environment exists"
} else {
    Write-Output "Virtual environment does not exist"
    Write-Output "Creating virtual environment"
    python -m venv env
}

# Activate virtual environment
. .\env\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Run scrapy crawl apx_spider
scrapy crawl apx_spider

# Run python companies_script.py
python .\companies_script.py

# Deactivate virtual environment
deactivate