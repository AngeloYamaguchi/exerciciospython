import random
from time import sleep
import time
from random  import randint
print("{}".format("="*30))
print("Jogo Jan Ken Pô")
print("{}".format("="*30))
print("1 = Pedra")
print("1 = Papel")
print("2 = Tesoura")
itens = ("pedra", "papel" ,"tesoura")
print("#@"*20)
computador = random.randint(0,2)
jogador = int(input("qual sua jogada?"))
print("#@"*20)
sleep(1)
print("JAN")
sleep(1)
print("Ken")
sleep(1)
print("PÔ")
sleep(1)

print("computador jogou {}".format(itens[computador]))
print("Você jogou {}".format(itens[(jogador)]))
if computador == 0:# computador jogou pedra
    if jogador == 0: #jogador jogou pedra
        print("Empate")
    elif jogador == 1:
        print("")
    elif jogador == 2:
        print("você perdeu!")
    else:
        print("Opção invalida!")


elif computador == 1: #jogador jogu papel
    if jogador == 0:  # jogador jogou pedra
        print("Você perdeu")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2:
        print(" você Ganhou")
    else:
        print("opção iválida")

elif computador == 2:
    if jogador == 0:  # jogador jogou pedra
        print("você ganhou")
    elif jogador == 1:
        print(" você perdeu")
    elif jogador == 2:
        print("empate")
    else:
        print("opcão inválida")

else:
    print("Jogada invalida!")








