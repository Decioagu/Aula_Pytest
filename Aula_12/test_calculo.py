import pytest
from calcula_total import calculate_total

# teste indireto da função "classifica_idade()"
@pytest.mark.parametrize("a",[1,3,5])
@pytest.mark.parametrize("b",[2])
def test_calculate_total(a,b):
    c = a + b
    d = b - a # <============= ERRO calculate_total() <=> (a - b)
    valor = c + d 
    assert calculate_total(a,b) == valor

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_12\test_calculo.py

'''
PS D:\REPOSITORIO\Aula_Pytest> .\venv\Scripts\activate
(venv) PS D:\REPOSITORIO\Aula_Pytest> pytest .\Aula_12\test_calculo.py
=========================================================== test session starts ============================================================
platform win32 -- Python 3.13.1, pytest-8.3.4, pluggy-1.5.0
rootdir: D:\REPOSITORIO\Aula_Pytest
collected 3 items

Aula_12\test_calculo.py FFF                                                                                                           [100%]

================================================================= FAILURES =================================================================
________________________________________________________ test_calculate_total[2-1] _________________________________________________________

a = 1, b = 2

    @pytest.mark.parametrize("a",[1,3,5])
    @pytest.mark.parametrize("b",[2])
    def test_calculate_total(a,b):
        c = a + b
        d = b - a
        valor = c + d
>       assert calculate_total(a,b) == valor
E       assert 2 == 4
E        +  where 2 = calculate_total(1, 2)

Aula_12\test_calculo.py:11: AssertionError
----------------------------------------------------------- Captured stdout call ----------------------------------------------------------- 
1+2=3
2-1=-1
3 + -1=2
________________________________________________________ test_calculate_total[2-3] _________________________________________________________ 

a = 3, b = 2

    @pytest.mark.parametrize("a",[1,3,5])
    @pytest.mark.parametrize("b",[2])
    def test_calculate_total(a,b):
        c = a + b
        d = b - a
        valor = c + d
>       assert calculate_total(a,b) == valor
E       assert 6 == 4
E        +  where 6 = calculate_total(3, 2)

Aula_12\test_calculo.py:11: AssertionError
----------------------------------------------------------- Captured stdout call ----------------------------------------------------------- 
3+2=5
2-3=1
5 + 1=6
________________________________________________________ test_calculate_total[2-5] _________________________________________________________ 

a = 5, b = 2

    @pytest.mark.parametrize("a",[1,3,5])
    @pytest.mark.parametrize("b",[2])
    def test_calculate_total(a,b):
        c = a + b
        d = b - a
        valor = c + d
>       assert calculate_total(a,b) == valor
E       assert 10 == 4
E        +  where 10 = calculate_total(5, 2)

Aula_12\test_calculo.py:11: AssertionError
----------------------------------------------------------- Captured stdout call ----------------------------------------------------------- 
5+2=7
2-5=3
7 + 3=10
============================================================= warnings summary ============================================================= 
Aula_12\test_calculo.py:16
  D:\REPOSITORIO\Aula_Pytest\Aula_12\test_calculo.py:16: SyntaxWarning: invalid escape sequence '\R'

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
========================================================= short test summary info ========================================================== 
FAILED Aula_12/test_calculo.py::test_calculate_total[2-1] - assert 2 == 4
FAILED Aula_12/test_calculo.py::test_calculate_total[2-3] - assert 6 == 4
FAILED Aula_12/test_calculo.py::test_calculate_total[2-5] - assert 10 == 4
======================================================= 3 failed, 1 warning in 0.15s ======================================================= 
(venv) PS D:\REPOSITORIO\Aula_Pytest> 
'''