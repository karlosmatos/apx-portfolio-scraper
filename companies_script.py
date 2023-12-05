import json
import datetime
from re import split
import pandas as pd
import os

def extract_field(company, field, *args):
    try:
        if field != "location_geographic_address":
            return company["_source"][field]
        else:
            return company["_source"][field][*args[0]]
    except Exception:
        return ""

def generate_dataset(company):
    return {
        "company_name": extract_field(company, "name_text"),
        "company_website": extract_field(company, "web_homepage_text"),
        "logo_image": extract_field(company, "logo_image"),
        "team_photo": extract_field(company, "team_photo"),
        "team_count": extract_field(company, "team_count_number"),
        "oneliner": extract_field(company, "oneliner_text"),
        "business_model": extract_field(company, "gtm_option_business_model"),
        "lastround_option_funding_round": extract_field(company, "lastround_option_funding_round"),
        "city": extract_field(company, "city_text"),
        "email": extract_field(company, "email_text"),
        "phone_number": extract_field(company, "phone_number_text"),
        "calendly_link": "https://calendly.com/" + extract_field(company, "calendly_text"),
        "apx_website": "https://apx.network/startup/" + extract_field(company, "Slug"),
        "linkedin": "https://www.linkedin.com/company/"
        + extract_field(company, "linkedin1_text"),
    }

data = json.loads(open('companies.json').read())
output_path = 'apx_portfolio_companies_2.csv'

for company in data["hits"]["hits"]:
    new_dataset = generate_dataset(company)
    print(new_dataset)

    data = pd.DataFrame(new_dataset, index=[0])
    data = data[data['company_name'].notnull()]  # Remove rows where "company_name" is blank

    data.to_csv(output_path, mode='a', header=not os.path.exists(output_path))
    
