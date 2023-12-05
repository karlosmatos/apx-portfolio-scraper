import json
import pandas as pd
import os

def extract_field(company, field):
    try:
        return company["_source"][field]
    except:
        return ""

def generate_dataset(company):
    new_dataset = {
        "company_name": extract_field(company, "name_text"),
        "web": extract_field(company, "web_homepage_text"),
        "description": extract_field(company, "about_text_text"),
        "business_model": extract_field(company, "gtm_option_business_model"),
        "stage": extract_field(company, "lastround_option_funding_round"),
        "city": extract_field(company, "city_text"),
        "email": extract_field(company, "email_text"),
        "phone_number_text": extract_field(company, "phone_number_text"),
        "linkedin": "https://www.linkedin.com/company/" + extract_field(company, "linkedin1_text")
    }
    return new_dataset

data = json.loads(open('companies1.json').read())
output_path = 'apx_portfolio_network_2.csv'

for company in data["hits"]["companies"]:
    new_dataset = generate_dataset(company)
    print(new_dataset)

    data = pd.DataFrame(new_dataset, index=[0])
    data.to_csv(output_path, mode='a', header=not os.path.exists(output_path))
