numeros = lista = []
while True:
    n =  int(input("Digite um numero"))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, não será adicionado')
    resp= str(input("quer continuar [S/N]")).upper().strip()

    if resp in "Nn":
        break
print("=-"*30)
print(f'Os Numeros Digitados foram {sorted(numeros)}')

