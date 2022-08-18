class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = [] # Agregação
        
    def inserir_produto(self, produto):
        self.__produtos.append(produto)
        
    def listar_produtos(self):
        for produto in self.__produtos:
            print(f"{produto.nome} - R$ {produto.preco}")
        
    def soma_total(self):
        total = 0
        for produto in self.__produtos:
            total += produto.preco
        return total