soma = 0
cont = 0
for c in range(1,7,):
    n = int(input("Digite um número{} primero".format(c)))
    if n % 2 == 0:
        soma += c
        cont += 1
print("Você informou {} númerospares  a soma dos números pares foi {}".format(cont,soma))
