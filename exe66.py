numero = soma = quantidade = 0
while True:
        numero = int(input("Digite um número"))
        if numero == 999:
            break
        quantidade += 1
        soma += numero
print(f'aquantidade de numeros digitados  é {quantidade} a soma é do números é {soma} ')