import pytest

def dividir(x, y):
    if y == 0:
        raise ZeroDivisionError("Divisão por zero não permitida")
    return x / y

def test_dividir_por_zero():
    with pytest.raises(ZeroDivisionError) as excinfo:
        dividir(10, 0)
    assert "Divisão por zero não permitida" in str(excinfo.value)