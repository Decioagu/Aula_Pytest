from app import Produto,Estoque # Classes

def test_adicionar_novo_produto_estoque():
    ''' Adicionar novos produtos em estoque '''
    estoque = Estoque() # armazenar produto (Classe estoque)

    produto1 = Produto("Mouse",10) # produto (Classe Produto)
    produto2 = Produto("Teclado",5) # produto (Classe Produto)

    estoque.adicionar_produto(produto1) # adicionar em (Classe estoque)
    estoque.adicionar_produto(produto2) # adicionar em (Classe estoque)

    assert estoque.verifica_quantidade("Mouse") == 10 # verificar
    assert estoque.verifica_quantidade("Teclado") == 5 # verificar

def test_adicionar_produto_existente_estoque():
    ''' Adicionar novo produto em estoque e incrementar quantidade do produto em estoque. '''
    estoque = Estoque() # armazenar produto (Classe estoque)

    produto1 = Produto("Monitor",15) # produto (Classe Produto)
    estoque.adicionar_produto(produto1) # adicionar em (Classe estoque)

    produto2 = Produto("Monitor",5) # produto (Classe Produto)
    estoque.adicionar_produto(produto2) # adicionar em (Classe estoque)

    assert estoque.verifica_quantidade("Monitor") == 20 # verificar

# Ative o ambiente virtual: .\venv\Scripts\activate
# Execute: pytest .\Aula_18\test_integration.py
