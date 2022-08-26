from random import randint
from time import sleep
from operator import itemgetter
jogos = {'Jogador1': randint(1,6),
         'Jogador2':randint(1,6),
         'Jogador3': randint(1,6),
         'Jogador4': randint(1,6)}
ranking = list()
print("Valores Sorteados")
for k, v in jogos.items():
    print(f'{k} tirou  no dado {v} ')
    sleep(1)
    ranking = sorted(jogos.items(), key=itemgetter(1), reverse= True)
print('-='*30)
print('Ranking dos Jogadores')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar {v[0]} {v[1]}')
    sleep(1)




