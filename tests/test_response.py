import pytest
from unittest import mock
from src.response import generate_response
from src.schemas import Prompt

class TestGenerateResponse:
    @mock.patch('src.response.openai.Completion.create')
    def test_generate_response(self, mock_create):
        prompt = Prompt(text="Test prompt")
        expected_response = "Test response"
        mock_response = {
            'choices': [
                {
                    'text': expected_response
                }
            ]
        }
        mock_create.return_value = mock_response

        # Llamamos a la función generate_response con el prompt
        actual_response = generate_response(prompt)

        # Verificamos que la respuesta sea la esperada
        assert actual_response == expected_response
