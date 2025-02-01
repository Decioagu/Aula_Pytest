import pytest
import sqlalchemy
from sqlalchemy.sql import text

@pytest.fixture # decorador
def database_connection():
    engine = sqlalchemy.create_engine('sqlite:///:memory:') # Criar banco SQLite em memoria (temporário)
    connection = engine.connect() # Abrir conexão
    yield connection # Fornece o recurso para o teste (executa conexão)
    connection.close() # Fechar conexão

# teste indireto da função "database_connection()"
def test_database_connection(database_connection):
    result = database_connection.execute(text("SELECT 1")) # Faz consulta no banco (query)
    assert result.fetchone()[0] == 1 # Retorna a primeira linha do banco

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_08\test_teardown.py

'''
Em Python, o "yield" é uma palavra-chave que é usada para criar geradores. 
Geradores são objetos que podem ser iterados, mas que não armazenam todos 
os seus valores na memória ao mesmo tempo
'''