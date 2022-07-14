from carrinho_de_compras import CarrinhoDeCompras
from produto import Produto

carrinho = CarrinhoDeCompras()
carrinho.inserir_produto(Produto("Notebook", 2999.90))
carrinho.inserir_produto(Produto("Mouse", 15.90))
carrinho.inserir_produto(Produto("Teclado", 89.90))
carrinho.inserir_produto(Produto("Suporte para notebook", 50.90))

carrinho.listar_produtos()
print(f"Total: R$ {carrinho.soma_total():.2f}")