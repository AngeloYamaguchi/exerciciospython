print("Coversor Binário")
numero = int(input("digite um numero inteiro"))
print('Escolha a conversão a seguir:')
print("[ 1 ]  converter em binario")
print("[ 2 ]  converter em octal")
print("[ 3 ] converter em hexadecimal")
escolha = int(input("escolha um conversor"))

if escolha == 1:
    print("{} convertido em binário é {}".format(numero,bin(numero)[2:]))
elif escolha == 2:
    print("{} convertido em binário é {}".format(numero, oct(numero)[2:]))
elif escolha == 3:
    print("{} convertido em binário é {}".format(numero, hex(numero)[2:]))
else:
    print("opção invalida")



