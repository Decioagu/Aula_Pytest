class Produto:
    def __init__(self,nome, quantidade) :
        self.nome = nome
        self.quantidade = quantidade

class Estoque:
    def __init__(self):
        self.produtos = {} # armazenar produto em dicionário

    def adicionar_produto(self,produto):
        # Se produto não existir
        if produto.nome not in self.produtos:
            self.produtos[produto.nome] = produto.quantidade # criar quantidade
        else:
            self.produtos[produto.nome] += produto.quantidade # somar quantidade
    
    def verifica_quantidade(self,nome_produto):
        return self.produtos.get(nome_produto,0) # buscar
    
if __name__ == '__main__':
    estoque = Estoque()

    produto1 = Produto("Mouse",10) # produto
    produto2 = Produto("Teclado",5) # produto
    produto3 = Produto("Monitor",15) # produto

    estoque.adicionar_produto(produto1) # adicionar
    estoque.adicionar_produto(produto2) # adicionar
    estoque.adicionar_produto(produto3) # adicionar
    print(estoque.produtos)

    produto3 = Produto("Monitor",5) # produto
    estoque.adicionar_produto(produto3) # adicionar
    print(estoque.produtos)
    
    print('Mouse = ', estoque.verifica_quantidade("Mouse"))
    print('Teclado = ', estoque.verifica_quantidade("Teclado"))
    print('Monitor = ', estoque.verifica_quantidade("Monitor"))
    print('Fone = ', estoque.verifica_quantidade("Fone"))