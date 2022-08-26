somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''

for pessoas in range(1,5):
    print("+="*10)
    print('{}° pessoa'.format(pessoas))
    nome = str(input("nome")).strip()
    idade = int(input(" idade").strip())
    sexo = str(input("Sexo[M/F]")).strip().upper()
    somaidade += idade
    totmulher20 = 0
    if pessoas == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomemaisvelho = nome
    if  sexo in 'Mm'and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'F' and idade < 20:
        totmulher20 += 1

mediaidade = somaidade/4
print(" A média de idade do grupo é {} anos".format(mediaidade))
print(" O homem mais velho tem {} anos e se chama {}".format(maioridadehomem,nome))
print("O total mulheres {} tem menos de 20 anos".format(totmulher20,))





