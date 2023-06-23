from fastapi import FastAPI
from src import response
from dotenv import load_dotenv
import os
import openai

app = FastAPI()
app.include_router(response.router)

load_dotenv()

openai.api_key = os.getenv("OPENAI_SECRET_KEY")

@app.get("/")
def index():
    return {"message": "Hello World"}


