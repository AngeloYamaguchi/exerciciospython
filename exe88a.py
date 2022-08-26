from random import randint
from time import sleep
cont = 0
lista = list()
bol= list()
print("=-"*30)
print("                Jogos da MegaSena       ")
print("=-"*30)
jogos = int(input("        Quantos Jogos Gostaria de fazer?"))
tot = 1
while tot <= jogos:
    cont= 0
    while True:
        num = randint (1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    bol.append(lista[:])
    lista.clear()
    tot += 1
print('<*>'*5, f' Sorteando {jogos} jogos', '<*>'*5)
for i,l in  enumerate(bol):
    print(f'         Jogo{i+1} {l}')
    sleep(1)
print()
print('<>'*8," Boa Sorte",'<>'*8 )



