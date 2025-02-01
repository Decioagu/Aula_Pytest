import pytest
from classifica_idade import classifica_idade

# teste indireto da função "classifica_idade()"
@pytest.mark.parametrize("idade,categoria_esperada",[
        (10,"Criança"),
        (15,"Adolescente"),
        (30,"Adulto"),
        (70,"Idoso",)
        ])
def test_classifica_idade(idade,categoria_esperada):
    assert classifica_idade(idade) == categoria_esperada

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_11\test_classifica_idade.py