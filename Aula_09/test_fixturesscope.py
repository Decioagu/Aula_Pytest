import pytest

@pytest.fixture(scope="function")
def recurso_temporario():
    return "dados temporários"

def test_exemplo(recurso_temporario):
    assert recurso_temporario == "dados temporários"

# --------------------------------------------------------------------------------

import pytest

@pytest.fixture(scope="class")
def recurso_da_classe():
    return "dados para a classe"

class TestClasse:
    def test_um(self, recurso_da_classe):
        assert recurso_da_classe == "dados para a classe"

    def test_dois(self, recurso_da_classe):
        assert recurso_da_classe == "dados para a classe"

# --------------------------------------------------------------------------------
 
import pytest

@pytest.fixture(scope="module")
def recurso_do_modulo():
    return "dados para o módulo"

def test_exemplo_um(recurso_do_modulo):
    assert recurso_do_modulo == "dados para o módulo"

def test_exemplo_dois(recurso_do_modulo):
    assert recurso_do_modulo == "dados para o módulo"

# --------------------------------------------------------------------------------

import pytest

@pytest.fixture(scope="session")
def recurso_da_sessao():
    return "dados para a sessão inteira"

def test_um(recurso_da_sessao):
    assert recurso_da_sessao == "dados para a sessão inteira"

def test_dois(recurso_da_sessao):
    assert recurso_da_sessao == "dados para a sessão inteira"


# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_09\test_fixturesscope.py