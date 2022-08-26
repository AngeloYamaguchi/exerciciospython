import random
from random import randint
print(" Sou o  Computador ,Dige o  número que estou pensando")
computador = random.randint(0,10)
acertou = False
palpites =0
while not acertou:
    jogador = int(input("qual seu palpite?"))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print("Menos. tente de novo")
        elif jogador < computador:
            print(" mais .... tente de novo")


print(" Você acertou em {} palpites".format(palpites))
