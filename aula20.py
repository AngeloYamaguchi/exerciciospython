def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f' A soma A + B = {s}')


#Função Principal
soma(12, 47)

def contador(*num):
    len(num)
    print(f' são  {len(num)} valores')
    for valor in num:
        print(f' {valor}', end='')
    print(' Fim')


contador(1, 2, 3, 4)
contador(1, 2, 3)
contador(1, 2)

