from unittest.mock import MagicMock

# Criando um objeto mockado
mock = MagicMock()

# Simulando um método e chamando-o
mock.meu_metodo(10, 20)

# Verificando se o método foi chamado
print(mock.meu_metodo.called)  # True

# Verificando os argumentos com que o método foi chamado
print(mock.meu_metodo.call_args)  # call(10, 20)

# Configurando o retorno do método
mock.meu_metodo.return_value = "Resultado Simulado"
print(mock.meu_metodo(5, 10))  # "Resultado Simulado"

# Simulando exceções
mock.meu_metodo.side_effect = Exception("Erro simulado")
try:
    mock.meu_metodo()
except Exception as e:
    print(e)  # "Erro simulado"
