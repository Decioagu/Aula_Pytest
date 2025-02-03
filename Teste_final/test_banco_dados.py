import pytest
from database_manager import DatabaseManager, Cliente
from pathlib import Path

# Teste de conexão no banco de dados
@pytest.fixture(scope="module")
def database_connection():
    test_db_path = 'users.db'
    caminho = Path(__file__).parent
    connection = DatabaseManager(caminho / test_db_path)
    yield connection

# Teste indireto da "class Cliente"
@pytest.mark.parametrize("cliente", [
    # Cliente("WWW", "WWW@example.com", "1234567890", "1234 Elm Street", "Springfield", "SP", "12345-678", "2023-03-15", "1990-01-01"),
    Cliente("", "", "1234567890", "1234 Elm Street", "Springfield", "SP", "12345-678", "2023-03-15", "1990-01-01"),
    Cliente("WWW", "WWW@example.com", "1234567890", "1234 Elm Street", "Springfield", "SP", "12345-678", "", "")
])
# 1. Teste para verificar se a inclusão falha com dados inválidos
def test_inclusao_de_clientes_no_banco_de_dados(database_connection, cliente):
    resultado = database_connection.incluir_cliente(cliente)
    assert resultado == "Falha na validação dos dados do cliente."
    

# 2. Teste para verificar se cliente existe no banco de dados
def test_verificar_cliente_existente_no_banco_de_dados(database_connection):
    cliente = database_connection.verificar_cliente(1)  
    assert cliente != None

# 3. Teste para testar a função de atualização de clientes
def test_atualizar_cliente_existente_no_banco_de_dados(database_connection):
    resultado = database_connection.atualizar_cliente(1, "nome", "Atualizar nome")  
    assert resultado == 1

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Teste_final\test_banco_dados.py