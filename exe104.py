def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor= int(n)
            ok= True
        else:
            print('\033[0;31m Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


#programa principal
n = leiaint('digite um Número')
print(f'Você digitou o número {n}')
