from fastapi import FastAPI
from src import response
from dotenv import load_dotenv
import uvicorn

import os
import openai

app = FastAPI()
app.include_router(response.router)

