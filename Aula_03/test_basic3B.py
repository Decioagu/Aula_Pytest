# função testada
def somar(a,b):
    return a + b

# função testada
def comprimento(lista):
    return len(lista)

# teste indireto de função
def test_somar_e_comprimento():
    assert somar(3,2) == 5
    assert comprimento([1,2,3,4,5]) == 5
    # assert somar(3,2) == 0 # erro

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_03\test_basic3B.py