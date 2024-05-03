from openai import OpenAI
client = OpenAI(api_key="enter your api_key")

# file upload to openai
file = client.files.create(
  file=open("data.jsonl", "rb"),
  purpose="fine-tune"
)

#Create fine-tuning model
client.fine_tuning.jobs.create(
    training_file=file.id,
    model="gpt-3.5-turbo-0125"
)
