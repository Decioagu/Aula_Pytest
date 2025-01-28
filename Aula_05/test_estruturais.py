# teste direto de função
def test_listas_iguais():
    lista_esperada = [1,2,3,4,5]
    lista_resultado = [1,2,3,4,5]
    assert lista_resultado == lista_esperada, "As listas não são iguais." # Falha com mensagem

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_05\test_estruturais.py