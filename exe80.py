mumeros = lista = []
for c in range(0,5):
    n = int(input("Digite um Valor"))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado no final da Lista')
    else:
        posi = 0
        while posi < len(lista):
            if n <= lista[posi]:
                lista.insert(posi,n)
                print(f'adicionado na posiõa inicio da lisata {posi}')
                break
            posi += 1
print('=-'*30)
print(f' Os números digitados foram {lista}')





