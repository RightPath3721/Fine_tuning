from openai import OpenAI
client = OpenAI(api_key="enter your api_key")

fine_tuned_model = client.fine_tuning.jobs.list(limit=1).data[0].fine_tuned_model

def main():
    while True:
        print("Enter cold email:")
        prompt = input()

        completion = client.chat.completions.create(
            model=fine_tuned_model,
            messages=[
                {"role": "system", "content": "You are an AI assistant that creates opening lines for cold emails. The output should adhere to grammatical rules without prompting for further information. It should maintain a casual, conversational tone, with a touch of specificity, while remaining concise and clever. It should be simplicity."},
                {"role": "user", "content": prompt}
            ]
        )

        print("Email Opening Line:")
        print(completion.choices[0].message.content)
        print()

if __name__ == "__main__":
    main()

