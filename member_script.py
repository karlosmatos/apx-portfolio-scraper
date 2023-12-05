import json
import pandas as pd
import os

def process_member_data(member, rules):
    new_dataset = {}
    for key, value in rules.items():
        try:
            if key == "linkedin":
                new_dataset[key] = "https://www.linkedin.com/in/" + member["_source"][value]
            elif key == "headline":
                new_dataset[key] = member["_source"][value]
                new_dataset["position"], new_dataset["company"] = member["_source"][value].split(" @ ")
            else:
                new_dataset[key] = member["_source"][value]
        except:
            new_dataset[key] = ""
            if key == "headline":
                new_dataset["position"] = ""
                new_dataset["company"] = ""
    return new_dataset

def process_members_data(output_path):
    rules = {
        "first_name": "first_name_text",
        "last_name": "last_name_text",
        "full_name": "full_name_text",
        "email": "email_preferred_text",
        "network_role": "networkrole_option_role",
        "network_reason": "networkreason_text",
        "linkedin": "linkedin_url_text",
        "headline": "text_headlineworkexperience_text",
    }

    with open(output_path, 'w') as file:
        for i in range(1, 4):
            data = json.load(open(f'members/members_{i}.json'))
            for member in data["hits"]["hits"]:
                new_dataset = process_member_data(member, rules)
                print(new_dataset)

                data = pd.DataFrame(new_dataset, index=[0])
                data.to_csv(file, mode='a', header=not os.path.exists(output_path))

output_path = 'apx_members_network_2.csv'
process_members_data(output_path)
