def dividir(a,b):
    # test_dividir_por_zero2
    if b == 0: 
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b # test_dividir_por_zero1