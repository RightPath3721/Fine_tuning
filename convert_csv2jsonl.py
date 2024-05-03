import csv
import json

csv_file = "Email Openers Dataset (30) - Sheet1.csv"
jsonl_file = "data.jsonl"

data = []

with open(csv_file, encoding='utf-8') as csvf, open(jsonl_file, 'w', encoding='utf-8') as jsonlf:
    csv_reader = csv.DictReader(csvf)

    for row in csv_reader:

        json_data = {
            "messages": [
                {
                    "role": "system",
                    "content": "You are an AI assistant that creates opening lines for cold emails. The output should adhere to grammatical rules without prompting for further information. It should maintain a casual, conversational tone, with a touch of specificity, while remaining concise and clever."
                }, 
                {
                    "role": "user",
                    "content": row["Personal Bio"],
                }, 
                {
                    "role": "assistant",
                    "content": row["Email Opening Line"],
                }
            ]
        }
        
        jsonlf.write(json.dumps(json_data) + '\n')
