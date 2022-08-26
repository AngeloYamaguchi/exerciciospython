from random import randint
from time import sleep
jogadores = dict()
dado = 0
for c in range(1,5):
    dado = randint(1,6)

    print(f'Jogador{c} jogada foi {dado}')
    sleep(1)

