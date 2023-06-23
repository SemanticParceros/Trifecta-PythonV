from fastapi import FastAPI
from routers import response
from dotenv import load_dotenv

import os
import openai

app = FastAPI()
app.include_router(response.router)

