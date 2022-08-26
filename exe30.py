numero = int(input("digite um número"))
par = numero % 2 == 0
if numero == par:
    print("O número {} é  par".format(numero))
else:
    print("O número {} é impar".format(numero))
