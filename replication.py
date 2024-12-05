import joblib
from better_profanity import profanity
import requests
import json
import os
from dotenv import load_dotenv
import streamlit as st
import openai

load_dotenv()

# Set OpenAI and Perspective API keys from .env
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")
PERSPECTIVE_API_KEY = os.getenv("PERSPECTIVE_API_KEY")

# Function to check for profanity using Google's Perspective API
def check_profanity_perspective(text):
    url = f"https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key={PERSPECTIVE_API_KEY}"
    headers = {'Content-Type': 'application/json'}
    data = {
        "comment": {"text": text},
        "languages": ["en"],
        "requestedAttributes": {
            "TOXICITY": {},
            "INSULT": {},
            "PROFANITY": {},
            "IDENTITY_ATTACK": {}
        }
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json()
        flagged_categories = []
        
        # Threshold for flagging (adjust as needed)
        threshold = 0.3
        
        # Check each attribute
        if result['attributeScores']['TOXICITY']['summaryScore']['value'] >= threshold:
            flagged_categories.append("TOXICITY")
        if result['attributeScores']['INSULT']['summaryScore']['value'] >= threshold:
            flagged_categories.append("INSULT")
        if result['attributeScores']['PROFANITY']['summaryScore']['value'] >= threshold:
            flagged_categories.append("PROFANITY")
        if result['attributeScores']['IDENTITY_ATTACK']['summaryScore']['value'] >= threshold:
            flagged_categories.append("IDENTITY_ATTACK")
        
        return flagged_categories  # Return a list of flagged categories
    else:
        print(f"Perspective API Error: {response.status_code}")
        return None

# Function to perform translation without moderation
def without_guardrails(text):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Translate the following text to English."},
            {"role": "user", "content": text}
        ]
    )
    response_dict = response.to_dict()
    result = response_dict['choices'][0]['message']['content']
    return result


def main():
    st.title("Perspective API Implementation in LLMs")

    text_area = st.text_area("Enter the text to be translated")

    if st.button("Translate"):
        if len(text_area) > 0:
            st.info("Input Text: " + text_area)

            st.warning("Translation Without Moderation")

            without_guardrails_result = without_guardrails(text_area)
            st.success("Translated Text: " + without_guardrails_result)

            st.warning("Translation With Perspective Moderation")

            # Check for flagged categories
            flagged_categories = check_profanity_perspective(without_guardrails_result)
            if flagged_categories:
                for category in flagged_categories:
                    st.error(f"The content is flagged as {category}.")
            else:
                st.success("The content passed all moderation checks.")

if __name__ == "__main__":
    main()
