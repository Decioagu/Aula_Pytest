import pytest
def classifica_idade(idade):
    if idade < 13:
        return 'criança'
    elif idade < 18:
        return 'adolescente'
    elif idade < 60:
        return 'adulto'
    else:
        return 'idoso'

@pytest.mark.crianca
def test_classifica_idade_crianca():
    assert classifica_idade(10) == 'criança', "Deve categorizar como 'criança'"

@pytest.mark.adolescente
def test_classifica_idade_adolescente():
    assert classifica_idade(15) == 'adolescente', "Deve categorizar como 'adolescente'"

@pytest.mark.adulto
def test_classifica_idade_adulto():
    assert classifica_idade(30) == 'adulto', "Deve categorizar como 'adulto'"

@pytest.mark.idoso
def test_classifica_idade_idoso():
    assert classifica_idade(70) == 'idoso', "Deve categorizar como 'idoso'"

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_14\test_classifica_idade.py
# Execute: pytest .\Aula_14\test_classifica_idade.py -m crianca
# Execute: pytest .\Aula_14\test_classifica_idade.py -m adolescente
# Execute: pytest .\Aula_14\test_classifica_idade.py -m adulto
# Execute: pytest .\Aula_14\test_classifica_idade.py -m idoso