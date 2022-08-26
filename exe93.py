jogador = dict()
patidas = list()
jogador["nome"] = str(input('Nome do Jogador'))
partida = int(input('Quantas partidas ele Jogou?'))
gol = list()
for c in range(0,partida):
       int(input(f'quantos gols na Partida{c +1}?'))
       gol.append(c)
       jogador['gol'] = gol

jogador['total de gols']= sum(gol)
print('=='*30)
print(jogador)
print('=='*30)
for k, v in jogador.items():
    print(f'{k} tem o valor {v}')
print('=='*30)
print(f'O jogador {jogador["nome"]} jogou {len(gol)} partidas ')
print('#'*60)
for i , v in enumerate(jogador['gol']):
    print(f' na partida{i} fez {v} gols')



