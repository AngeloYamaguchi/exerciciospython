from random import randint
from time import sleep
computador = randint(0,5)

print("Jogo de adivinhação")
print("********"*7)
print("Vou pensar em um número entre 0 e 5, tente adivinhar")
print("********"*7)
jogador = int(input("Em que número eu pensei?"))
print("Processando......")
sleep(2)
if computador == jogador:
    print("Parabéns você acertou,Eu pensei no número {}".format(computador) )
else:
    print("Vocé errouo nuúmero que eu pesei foi {}".format(computador))


