from datetime import datetime
class Pessoa:
    ano_atual = datetime.now().year
    
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        
    def comer(self, alimento):
        if(self.comendo):
            print(f'{self.nome} já está comendo.')
            return
        if(self.falando):
            print(f'{self.nome} não pode comer enquanto está falando.')
            return
        print(f'{self.nome} esta comendo {alimento}.')
        self.comendo = True
        
    def pararComer(self):
        if(not self.comendo):
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False
        
    def falar(self, assunto):
        if(self.comendo):
            print(f'{self.nome} não pode falar enquanto está comendo.')
            return
        if(self.falando):
            print(f'{self.nome} já está falando.')
            return
        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True
    
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return
        print (f'{self.nome} parou de falar.')
        self.falando = False
        
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade