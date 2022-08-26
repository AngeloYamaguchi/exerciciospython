valores = lista = []
pares = listpares = []
impar = listaimpar = []
while True:
    valores = int(input("Digite um número"))
    lista.append(valores)
    if valores % 2 == 0:
        listpares.append(valores)
    elif valores % 2 == 1:
        listaimpar.append(valores)
    resp = str(input("Quer continuar?[S/N]"))
    if resp not in "Nn":
        valores += 1
    else:
        break
print('=-'*30)
print(f'Os Números digitados foram {lista}')
print(f'Os pares sao  { listpares}')
print(f'OS ´Impares são { listaimpar}')