from src.schemas import Prompt
from fastapi import APIRouter
import openai

router = APIRouter(
    prefix='',
    tags=['chat']
)

@router.post('/chat')
def generate_response(prompt: Prompt):
    text_length = 120
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


