dados = []
dados12 = []
maior = menor = 0
while True:
    nome = str(input('Nome')).strip().capitalize()
    dados.append(nome)
    peso = int(input('peso'))
    dados.append(peso)
    if len(dados12) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
           maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    dados12.append(dados[:])
    dados.clear()

    resposta = str(input("Posso Contiunar? [S/N]")).strip()
    if resposta not in 'Ss':
        break

print(f' foram cadastradas  {len(dados12)} pessoas')
print(f' O mais pesado tem {maior} e se chama' ,end='')
for p in dados12:
    if p[1] == maior:
        print(f' {p[0]}')
print(f" A Pesoa mais leve tem {menor} kg e se chama", end='')
for p in dados12:
    if p[1] == menor:
        print(f' {p[0]}',end='')







