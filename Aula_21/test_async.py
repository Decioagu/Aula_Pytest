import asyncio
import pytest
from fetch_data import fetch_data

@pytest.mark.asyncio # Indica que este teste é assíncrono
async def test_fech_data():
    result = await fetch_data()
    assert result == {'data': 'some data'}

# Ative o ambiente virtual: .\venv\Scripts\activate
# Instalar:  pip install pytest-asyncio
# Execute: pytest .\Aula_21\test_async.py
# Execute: pytest .\Aula_21\test_async.py -m asyncio