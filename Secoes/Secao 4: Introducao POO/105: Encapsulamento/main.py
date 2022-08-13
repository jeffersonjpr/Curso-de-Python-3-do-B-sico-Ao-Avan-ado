"""
COnvenções de visibilidade em python:
_ para privado fraco
__ para privado forte
"""
class BaseDeDados:
    def __init__(self):
        self.__dados = {}
        
    @property
    def dados(self):
        return self.__dados
    
    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})
            
    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(f'{id} - {nome}')
            
    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]
        
bd = BaseDeDados()
bd.inserir_cliente(1, 'João')
bd.inserir_cliente(2, 'Maria')
bd.inserir_cliente(3, 'José')
bd.__dados = "Uma coisa"
bd.dados = "Uma outra coisa"
bd.apagar_cliente(3)

bd.lista_clientes()
print(bd.__dados)
print(bd._BaseDeDados__dados)

