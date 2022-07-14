class Caneta:
    def __init__(self, marca):
        self.__marca = marca
        
    @property
    def marca(self):
        return self.__marca
    
    def utilizar(self):
        print(f'A caneta {self.marca} esta escrevendo...')