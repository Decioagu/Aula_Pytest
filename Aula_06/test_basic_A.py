import pytest

@pytest.fixture # decorador
def sample_list():
    return [1,2,3,4,5]

# teste indireto da função "sample_list()"
def test_sum(sample_list):
    assert sum(sample_list) == 15

# teste indireto da função "sample_list()"
def test_length(sample_list):
    assert len(sample_list) == 5

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_06\test_basic_A.py