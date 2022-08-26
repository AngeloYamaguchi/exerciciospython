time = list()
jogador = dict()
patidas = list()
while True:
    jogador.clear()
    jogador["nome"] = str(input('Nome do Jogador'))
    partida = int(input('Quantas partidas ele Jogou?'))
    patidas.clear()
    gol = list()
    for c in range(0,partida):
           int(input(f'quantos gols na Partida{c +1}?'))
           gol.append(c)
           jogador['gol'] = gol
    jogador['total de gols']= sum(gol)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]')).upper()
        if resp in 'SN':
            break
        print('Responda apenas S ou N')
    if resp == 'N':
        break
print('-'*60)
print('Cod ',end='')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for k, v in enumerate(time):
    print(f' {k:>4}',end='')
    for d in v.values():
        print(f' {str(d):<15}',end='')
    print()
print('-'*60)
while True:
    busca = int(input('DAdos de Qual jogador quer mostrar? Para parar digite(999)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Jogador não existe código busca {busca}! ')
    else:
        print(f'LEVANTAMETO DO JOGADOR {time[busca]["nome"]} :')
        for i, g in enumerate(time[busca]["gol"]):
            print(f'   no jogo {i+1} fez {g} gols')
    print('-'*60)





