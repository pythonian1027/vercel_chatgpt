import openai
from fastapi import FastAPI, Request
from pydantic import BaseModel
import os

app = FastAPI()

# Define a request body schema using Pydantic
class QuestionPrompt(BaseModel):
    prompt: str

# Load OpenAI API key from an environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define the OpenAI API endpoint
endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

@app.post("/ask")
async def ask(request: Request, question_prompt: QuestionPrompt):
    # Get the question prompt from the request body
    prompt = question_prompt.prompt

    # Set up the OpenAI API request data
    data = {
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 1024,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }

    # Send a POST request to the OpenAI API endpoint
    response = openai.api_request(method="POST", path=endpoint, data=data)

    # Parse the response to get the generated answer text
    answer = response["choices"][0]["text"].strip()

    # Return the answer in a JSON response
    return {"answer": answer}
