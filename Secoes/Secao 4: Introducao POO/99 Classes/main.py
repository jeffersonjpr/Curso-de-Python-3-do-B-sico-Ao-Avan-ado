from pessoa import Pessoa

p1 = Pessoa("luiz", 26)
p2 = Pessoa("João", 32)

p1.comer("Banana")
p1.falar("Maça")
p1.pararComer()
p1.falar("Maça")
p1.comer("Maça")

print("-----------------------------------------------------")

p2.comer("Banana")
p1.falar("Sobre como está o dia?")


print("-----------------------------------------------------")

print(p1.get_ano_nascimento())
print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual) # Pessoa.ano_atual é um atributo da classe Pessoa
# posso usar o atributo da classe Pessoa diretamente