# função testada
def soma(a, b):
    return a + b

# teste indireto de função
def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(3, 1) == 0, "O resultado não é igual a 4" # Falha com mensagem

# Ative o ambiente virtual: .\venv\Scripts\activate
# Acesse a pasta: cd .\Aula_02\ 
# Execute: pytest