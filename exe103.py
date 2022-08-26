def jogador(n = 'desconhecido', g =0):
    print(f'o Jogador {n} fez {g} gols no campeonato')


#programa principal
n = str(input('Nome do jogador'))
g= str(input('Quantos gols?'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    jogador(g = g)
else:
    jogador(n, g)




