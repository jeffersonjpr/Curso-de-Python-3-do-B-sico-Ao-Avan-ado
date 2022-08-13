class Teclado:
    def __init__(self, tipo):
        self.__tipo = tipo
        
    @property
    def tipo(self):
        return self.__tipo
    
    def utilizar(self):
        print(f'O teclado {self.tipo} esta sendo utilizado...')
