from escritor import Escritor
from caneta import Caneta
from teclado import Teclado

escritor = Escritor('Maria')
caneta = Caneta('Caneta azul: azul caneta')
teclado = Teclado('Membrana')

print(escritor.nome)
print(caneta.marca)
print(teclado.tipo)

print("----------------------------------------------------")
escritor.ferramenta = teclado
escritor.trabalhar()
escritor.ferramenta.utilizar()
print("----------------------------------------------------")
escritor.ferramenta = caneta
escritor.trabalhar()
escritor.ferramenta.utilizar()
