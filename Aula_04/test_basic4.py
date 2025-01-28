from funcoes import *

# teste indireto da função "email_valido()"
def test_email_valido():
    assert email_valido("exemplodominio@gmail.com") is True
    assert email_valido("exemplo.com") is False
    # assert email_valido("exemplo.com")

# teste indireto da função "dividir()"
def test_dividir():
    assert dividir(4,2) == 2
    assert dividir(4,0) is None
    # assert dividir(4,0)

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_04\test_basic4.py
