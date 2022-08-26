from time import sleep
def maior(* num):
    if num not in num:
        print('O Maior valor está vazio')
    print('-='*25)
    cont = 0
    maior = 0
    print(' Analisando os valores')
    print(f'São no total {len(num)} valores')
    for valores in num:
        print(f' {valores}',end='')
    print(f'\nO maior valor é {max(num)}')
    print()

maior(1, 2 ,4 ,5 ,11 ,3 ,22 )
maior(2,-23 ,56 ,12 )
maior(-1,-2,-1,-1,0)
maior(1)
maior()

