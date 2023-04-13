#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 18:47:46 2023

@author: paco
"""

import requests
import json

def ask_question(question):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "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"
    }
    data = {
        "prompt": f"Q: {question}\nA:",
        "max_tokens": 1024,
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    answer = response.json()["choices"][0]["text"].strip()
    return answer