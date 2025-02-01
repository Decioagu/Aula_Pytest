# função testada
def calculate_total(a,b):
    x1 = a + b
    print(f'{a}+{b}={c}')
    x2 = a - b # <============= ERRO
    print(f'{b}-{a}={d}')
    valor = x1 + x2
    print(f'{x1} + {x2}={valor}')
    return valor

'''
@pytest.mark.parametrize("a",[1,3,5])
@pytest.mark.parametrize("b",[2])

O teste consiste em uma atriz conforme exemplo abaixo:

x1 = a + b
x1 = 1 + 2
x1 = 3 + 2
x1 = 5 + 2

x2 = a - b
x2 = 1 - 2
x2 = 3 - 2
x2 = 5 - 2

valor = x1 + x2
'''
