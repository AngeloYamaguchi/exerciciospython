
from random import randint
from time import sleep
lista = list()
cont = 0
numero = randint(1,60)
while True:
    if numero not in lista:
        lista.append(numero)
        cont += 1
    if cont >= 6:
        break
lista.sort()
print(f'Os números sorteados foram {lista}')



