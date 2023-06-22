from fastapi import FastAPI
from schemas import Prompt
from dotenv import load_dotenv
import os
import openai

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

openai.api_key = os.getenv('SECRET_KEY')


@app.post('/chat')
def generate_response(prompt: Prompt):
    text_length = 1000
    gpt3_model = 'davinci'
    response = openai.Completion.create(
        engine=gpt3_model,
        prompt=prompt.text,
        max_tokens=text_length,
        n=1,
        stop=None,
        temperature=0.5
    )
    return response['choices'][0]['text']
                              