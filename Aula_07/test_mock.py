import pytest
import requests
from unittest.mock import MagicMock

@pytest.fixture # decorador
def mock_response():
    mock = MagicMock(spec=requests.Response) # spec=requests.Response é comumente utilizado no contexto de testes em Python (HTML)
    mock.status_code = 200 # Simulação status da requisição (ex.: 200, 404)
    mock.json.return_value = {"message": "Success"} # Conteúdo retornado em JSON
    return mock

# teste indireto da função "mock_response"
def test_api_call_with_mock1(mock_response):
    response = mock_response
    assert response.status_code == 200 # Simulação status
    assert response.json() ==  {"message": "Success"} # Conteúdo retornado em JSON

# teste indireto da função "mock_response"
def test_api_call_with_mock2(mock_response):
    response = mock_response
    assert response.status_code == 200 # Simulação status
    assert response.json() ==  {"message": "Success"} # Conteúdo retornado em JSON

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_07\test_mock.py