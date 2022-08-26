ficha = list()
while True:
    nome = str(input('Nome'))
    nota1 = float(input('Primeira nota'))
    nota2 = float(input('Segunda nota'))
    média = (nota1 + nota2)/2
    ficha.append([nome,[nota1,nota2],média])

    resp= input('Quer continuar?[S/N]')
    if resp not in  "Ss":
        break
print('x='*30)
print(f'{"No.":<4}, {"Nome":<10}, {"Média":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    opc = int(input('Mostar nota de que aluno?(999) interrompe'))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')


