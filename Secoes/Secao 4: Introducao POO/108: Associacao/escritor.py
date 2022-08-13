class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta
        
    def trabalhar(self):
        print(f'O escritor {self.nome} esta trabalhando...')
        self.ferramenta.utilizar()