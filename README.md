# APX Portfolio Scraper

This project is a web scraper designed to extract portfolio of companies from APX websites.

## Installation

1. Clone the repository:
```
git clone https://github.com/karlosmatos/apx-portfolio-scraper
```

2. Navigate to the project directory:
```
cd apx-portfolio-scraper
```

3. Run the following script based on your OS:

#### Windows
```
.\run.ps1
```

#### Linux / MacOS
```
chmod +x run.sh 
./run.sh
```

## Project Structure
    
    . 
    ├── .gitignore                  # Git ignore file 
    ├── LICENSE                     # License file 
    ├── README.md                   # README file 
    ├── apx_portfolio/              # Main project folder 
    │       ├── init.py             # Initialization file 
    │       ├── items.py            # Items definition file 
    │       ├── middlewares.py      # Middlewares file 
    │       ├── pipelines.py        # Pipelines file 
    │       ├── settings.py         # Settings file 
    │       └── spiders/            # Spiders folder 
    │            ├── init.py        # Initialization file 
    │            └── apx_spider.py  # APX spider script 
    ├── companies_script.py         # Script for manipulating company data 
    ├── env/                        # Environment folder 
    ├── member_script.py            # Script for manipulating member data 
    ├── members/                    # Directory where scraped member data is stored 
    ├── requirements.txt            # Contains the Python packages required for this project 
    ├── run.ps1                     # PowerShell script to run the project 
    ├── run.sh                      # Shell script to run the project 
    └── scrapy.cfg                  # Scrapy configuration file 
  
## License
This project is licensed under the terms of the MIT license.
