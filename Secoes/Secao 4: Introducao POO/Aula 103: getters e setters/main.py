from xml.sax.handler import property_encoding


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)
    
    # getters
    @property
    def preco(self):
        return self._preco
    
    @property
    def nome(self):
        return self._nome
    
    # setters
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            self._preco = float (valor.replace('R$', '').replace('.', '').replace(',', '.'))
        else:
            self._preco = valor
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

produto1 = Produto("TECLADO gamer", 100)
produto1.desconto(10)

produto2 = Produto("MoUsE multiLUZ", "R$5000,00")
produto2.desconto(10)

print(f"O produto {produto1.nome} custa R$:{produto1.preco}")
print(f"O produto {produto2.nome} custa R$:{produto2.preco}")
