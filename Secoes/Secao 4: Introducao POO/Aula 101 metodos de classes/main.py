class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)
    
p1 = Pessoa('João', 22)
p2 = Pessoa.por_ano_nascimento('Jão', 1999)

print("Idade de {} é {}".format(p1.nome, p1.idade))
print("Idade de {} é {}".format(p2.nome, p2.idade))


