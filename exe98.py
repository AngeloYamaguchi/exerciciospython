from time import sleep
def contador(i,p,f):
    if p < 0:
        p *= -1
    if p == 0:
        p == 1
    print('-='*30)
    print(f'contador com início {i} passo {p} e final {f}')
    cont = i
    if i < f:
        while cont <= f:
            print(f' {cont}',end='')
            sleep(0.2)
            cont += p
        print('Fim')
        print()
    else:
        cont = i
        while cont >= f:
            print(f' {cont}',end='')
            sleep(.2)
            cont -= p
        print(' Fim')



#Programa Principal
contador(0,2,20)
contador(11,1,0)
print('=-'*30)
print("Agora é sua vez de personalizar o contador:")
ini= int(input('Inicio'))
pas = int(input('Passo'))
fin = int(input("Final"))
contador(ini, pas, fin)
