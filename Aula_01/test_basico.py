# teste direto de função
def test_soma_lista():
    assert sum([1,2,3]) == 6
    assert sum([1,2,3]) == 7, "O resultado não é igual a 6" # Falha com mensagem

# Ative o ambiente virtual: .\venv\Scripts\activate
# Acesse a pasta: cd .\Aula_01\ 
# Execute: pytest