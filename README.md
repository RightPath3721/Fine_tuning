## Set up environment

You should install python on your PC.

And then install nessessary python modules.

```powershell
pip install openai
```

## Explain

### 1. At Firt, run convert_csv2jsonl.py

This is converting file to get data.jsonl data from .csv.
The data.jsonl is used for fine-tuning.

Note: Confirm .csv file name.

```powershell
python convert_csv2jsonl.py
```

### 2. Second, run fine_tune.py

Before running this file, please enter your openai_api_key.

```py
client = OpenAI(api_key="enter your api_key")
```

This is for creating fine-tuning model

```powershell
python fine_tune.py
```

### 3. Finally, run chatbot.py

After done step 2, please try step 3 after a few mins. Because the creating fine_tuning model need some times.

Before running this file, please enter your openai_api_key.

```py
client = OpenAI(api_key="enter your api_key")
```

Run

```powershell
python chatbot.py
```

Note: If you create fine_tune model(step 2) once, you don't need to repeat step 1 and 2. Only do step 3.
