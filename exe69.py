print("+="*20)
print('Cadastro de Pessoas')
print('+='*20)
tot18 = toth = totm20 = 0
while True:
    idade = int(input("Idade Da pessoa"))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == "M" and idade < 20:
        totm20 += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? Sim Ou Não[S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print("Acabou")
print(f"O Total de pesooas Maiores são {tot18}")
print(f"O Total de homens cadastrados são {toth}")
print(f'O total de mulheres menores de 20 anos são {totm20}')




