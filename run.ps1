# Check Python version
$pythonVersion = python --version
$requiredVersion = "Python 3.11"

if ($pythonVersion -like "*$requiredVersion*") {
    Write-Host "Python 3.11 detected. Proceeding with the script."

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

    Write-Host "Script execution completed."
} else {
    Write-Host "Python 3.11 is not installed. Please install Python 3.11 to run this script."
}