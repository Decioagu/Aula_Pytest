# função testada
def soma(a, b):
    return a + b

# teste indireto de função
def test_soma():
    assert soma(2, 3) == 5

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_03\sub_pasta\test_basic3C.py
