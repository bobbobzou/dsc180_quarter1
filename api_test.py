import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Say hello!"},
        ],
        max_tokens=5
    )
    print("API response:", response)
except Exception as e:
    print("Error:", e)








import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

def analyze_text(text):
    """Analyzes text using the Perspective API."""
    API_KEY = os.getenv('PERSPECTIVE_API_KEY')
    url = f"https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key={API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {
        'comment': {'text': text},
        'requestedAttributes': {'TOXICITY': {}}
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        toxicity_score = result['attributeScores']['TOXICITY']['summaryScore']['value']
        return toxicity_score
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

text = "fuck."
toxicity_score = analyze_text(text)
if toxicity_score is not None:
    print(f"Toxicity score: {toxicity_score}")