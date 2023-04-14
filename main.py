#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:06:49 2023

@author: paco
"""
from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()

@app.get("/")
async def index():
    return FileResponse("index.html")





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
