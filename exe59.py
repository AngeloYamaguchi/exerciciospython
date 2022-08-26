n1 = int(input("digite um numero"))
n2 = int(input("digite segundo numero"))
soma = n1 + n2
multiplicar = n1*n2
opção = 0
while opção != 5:
    print("escolha  o  no menu abaixo ")
    print(" [1] somar ")
    print(" [2] multiplicar ")
    print(" [3] maior dos Números ")
    print( "[4] novos números")
    print(" [5] sair do programa ")
    opção = int(input("escolha uma opção"))
    if opção == 1:
        soma = n1 + n2
        print(" a soma {} + {} é = {}".format(n1,n2,soma) )
    elif opção == 2:
        multiplicar = n1*n2
        print(" {} X {} = {}". format(n1,n2, multiplicar))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(" Entre {} e {}   O maior número é {}".format(n1, n2, maior))
    elif opção == 4:
        n1 = int(input("digite um numero"))
        n2 = int(input("digite segundo numero"))
    elif opção == 5:
        print("Finalizando...")
    else:
        print("Opção inválida")



