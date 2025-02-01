import pytest
import time

def soma(a , b):
    return a + b

@pytest.mark.lento
def test_soma_lenta():
    time.sleep(4)
    assert soma(2,2) == 4, "Erro ocorreu test_soma_lenta()"

@pytest.mark.rapido
def test_soma_rapida():
    assert soma(2,3) == 5, "Erro ocorreu test_soma_rapida()"

@pytest.mark.lento
@pytest.mark.rapido
def test_soma_l_r():
    time.sleep(2)
    assert soma(2,5) == 7, "Erro ocorreu test_soma_l_r()"

def test_soma():
    assert soma(2,4) == 6,  "Erro ocorreu test_soma()"

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_13\test_marcador.py
# Execute: pytest .\Aula_13\test_marcador.py -m lento
# Execute: pytest .\Aula_13\test_marcador.py -m rapido
# Execute: pytest .\Aula_13\test_marcador.py -m "not rapido and lento"

# Executar na pasta no diretório "D:\REPOSITORIO\Aula_Pytest\Aula_13"
# Execute: pytest -m lento
# Não execute: pytest -m "not lento"
# Execute: pytest -m rapido
# Não execute: pytest -m "not rapido"
