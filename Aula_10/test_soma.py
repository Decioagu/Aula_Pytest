import pytest
from soma import soma

# teste indireto da função "soma()"
@pytest.mark.parametrize("a,b,resposta",[(1,2,3),(4,5,9),(10,20,30)])
def test_soma(a,b,resposta):
    assert soma(a,b) == resposta

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_10\test_soma.py

'''
@pytest.mark.parametrize("parâmetros",[(tupla),(tupla),(tupla)])
@pytest.mark.parametrize("a,b,resposta",[(1,2,3),(4,5,9),(10,20,30)])
@pytest.mark.parametrize("a,b,resposta",[(a,b,resposta),(a,b,resposta),(a,b,resposta)])
@pytest.mark.parametrize("a,b,resposta",[(a + b = resposta),(a + b = resposta),(a + b = resposta)])
@pytest.mark.parametrize("a+b=resposta",[(1 + 2 = 3),(4 + 5 = 9),(10 + 20 = 30)])
'''