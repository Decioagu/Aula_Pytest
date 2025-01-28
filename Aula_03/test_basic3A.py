# função testada
def is_positive(numero):
    return numero > 0

# teste indireto de função
def test_eh_positivo():
    assert is_positive(5) is True
    assert is_positive(-5) is False
    # assert is_positive(-5)

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_03\test_basic3A.py