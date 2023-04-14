from fastapi import FastAPI
from api import ask

app = FastAPI()

@app.post("/ask")
async def ask_question(prompt: str):
    response = ask(prompt)
    return response





# import json
# from chatgpt import ask_question

# def handler(event, context):
#     body = json.loads(event["body"])
#     question = body["question"]
#     answer = ask_question(question)
#     response = {"answer": answer}
#     return {"statusCode": 200, "body": json.dumps(response)}

# import os
# import openai

# openai.api_key = os.environ["OPENAI_API_KEY"]

# def ask_question(prompt):
    # Your code here


# from chatgpt import ask_question


# question = "What is the capital of France?"
# answer = ask_question(question)
# print(answer)
