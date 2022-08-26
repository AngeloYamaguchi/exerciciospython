from random import randint
from time import sleep
def sorteio(list):
    print('-='*30)
    print('Sorteando 5 números')
    for cont in range(0,5):
        n= randint(1,10)
        list.append(n)
        print(f' {n}',end='')
        sleep(.3)
    print(" Pronto")
def somapar(lista):
    soma = 0
    for valor in lista :
        if valor % 2 == 0:
          soma += valor
    print(f' Somando os valores os pares  da lista {lista} temos {soma}')





números = list()
sorteio(números)
somapar(números)
