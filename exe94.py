galera = list()
pessoas = dict()
soma = media = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome')).capitalize()
    pessoas['idade'] = int(input('idade'))
    soma += pessoas['idade']
    while True:
        pessoas['sexo'] = str(input('sexo [M/F]')).upper()
        if pessoas['sexo'] in 'FfMm':
            break
        print(f'opção inváila, tente digite M ou F')
    galera.append(pessoas.copy())
    while True:
        resp = str(input("Quer continuar [S/N]")).upper()
        if resp in 'SsNn':
            break
        print("opção inválida! digite S ou N")
    if resp == 'N':
        break
print('-='*30)
print(galera)
print(f'Total de pessoas cadastradas foram {len(galera)}')
media = soma/len(galera)
print(f'A média da idades das pessoas foram {media:5.2f}')
print(f'As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in'Ff':
        print(f'{p["nome"]}',end='')
print()



