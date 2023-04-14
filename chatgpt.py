import openai
import os

# Load OpenAI API key from an environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the OpenAI API endpoint
model_engine = "text-davinci-002"

def get_chat_response(prompt):
    # Define the parameters for the GPT-3 request
    params = {
        "engine": model_engine,
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 1024,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    # Send the request to the OpenAI API
    response = openai.Completion.create(**params)

    return response.choices[0].text.strip()



# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Wed Apr 12 18:47:46 2023

# @author: paco
# """

# import openai
# import os

# # Load OpenAI API key from environment variable
# openai.api_key = os.environ["OPENAI_API_KEY"]

# # Define function to generate text from prompt using OpenAI's GPT-3
# def generate_text(prompt, model, length=100, temperature=0.5):
#     response = openai.Completion.create(
#       engine=model,
#       prompt=prompt,
#       max_tokens=length,
#       n=1,
#       stop=None,
#       temperature=temperature,
#     )
#     text = response.choices[0].text.strip()
#     return text


# # Load OpenAI API key from an environment variable
# openai.api_key = "YOUR_OPENAI_API_KEY"

# # Define the OpenAI API endpoint
# endpoint = "https://api.openai.com/v1/engines/davinci-c


# import requests
# import json

# def ask_question(question):
#     url = "https://api.openai.com/v1/engines/davinci-codex/completions"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "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"
#     }
#     data = {
#         "prompt": f"Q: {question}\nA:",
#         "max_tokens": 1024,
#         "temperature": 0.7
#     }
#     response = requests.post(url, headers=headers, data=json.dumps(data))
#     answer = response.json()["choices"][0]["text"].strip()
#     return answer