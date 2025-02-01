from funcoes import *

# def test_email_valido():
#     assert email_valido("exemplo@dominio.com") is True
#     assert email_valido("exemplo.com") is False


def test_dividir():
    assert dividir(4,2) == 2
    assert dividir(4,0) is None


# Ative o ambiente virtual: .\venv\Scripts\activate
# Instalar: pip install pytest-cov
# Execute: pytest --cov=funcoes .\Aula_17\test_funcoes_cov.py