numeros = lista = []
while True:
    n = int(input("Digite um número"))
    lista.append(n)
    r = str(input('Quer continuar [S/N]').strip().upper())
    if r not in 'Nn':
        n += 1
    else:
        break
print("#@"*30)
print(f"Foram digitados {len(lista)}  valores")
lista.sort(reverse= True)
print(lista)
if 5 in lista:
    print(f"O numero 5 está na posição {len('5')}")
else:
    print(" O 5 não foi digitado")
