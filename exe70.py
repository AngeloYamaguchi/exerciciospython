print("+="*20)
print('Lojas Tudo Barato')
print('+='*20)
cont = total = totalmil  =  menorpreço = preço = 0
while True:
    produto = str(input("Digite o produto comprado")).strip().upper()
    preço:   float(input("digite o valor do produto R$ "))
    cont += 1
    continuar = " "
    total += preço
    if preço > 1000:
        totalmil += 1
    if cont == 1 :
        menorpreço = preço
    else:
        if preço < menorpreço:
         menorpreço = preço
    while continuar not in 'SN':
        continuar = str(input("Quer continuar?  Sim/Não  digite: [S/N] ")).strip().upper()[0]
    if continuar == 'N':
            break
print(" Fim do programa")
print(f'O total de compras foi {total}')
print(f'Produtos acima de mil Reais são {totalmil}')
print(f" o Menor preço foi {menorpreço} o produto mais barato foi")
