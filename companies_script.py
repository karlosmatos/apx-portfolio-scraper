import json
import pandas as pd
import os

def extract_field(company, field):
    return company["_source"].get(field, "")

def generate_dataset(company):
    calendly_text = extract_field(company, "calendly_text")
    linkedin_text = extract_field(company, "linkedin1_text")
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
        "calendly_link": f"https://calendly.com/{calendly_text}" if calendly_text else "",
        "apx_website": f"https://apx.network/startup/{extract_field(company, 'Slug')}",
        "linkedin": f"https://www.linkedin.com/company/{linkedin_text}" if linkedin_text else "",
    }

if __name__ == "__main__":
    # Load data from JSON file
    with open('companies.json', 'r') as file:
        data = json.load(file)

    # Generate dataset for each company and filter out those with empty company_name
    datasets = [generate_dataset(company) for company in data["hits"]["hits"] if company["_source"].get("name_text")]

    # Convert to DataFrame
    df = pd.DataFrame(datasets)

    # Define output path
    output_path = 'apx_portfolio_companies_2.csv'

    # Save DataFrame to CSV
    df.to_csv(output_path, index=False, encoding='utf-8')