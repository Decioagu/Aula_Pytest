import pytest
from divisao import dividir

def test_dividir_por_zero1():
    with pytest.raises(ZeroDivisionError):
        dividir(10,0)

def test_dividir_por_zero2():
    with pytest.raises(ZeroDivisionError) as exec_info: # exec_info = mensagem
        dividir(10,0)
    assert "Não é possível dividir por zero." in str(exec_info)
    
# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_16\test_divisao.py
        