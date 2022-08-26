resp = 'S'
soma = media = quantidade = maior = menor = 0
while resp in 'Ss' :
    número= int(input( "digite um número"))
    resp = str(input("Quer continuar ?para sim [ S] ou para não [N]")).strip().upper()[0]
    soma += número
    quantidade += 1
    if quantidade == 1:
        maior = menor = número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número
media = soma/quantidade
print(" Você digitou {} e a a média{} foi, maior {} foi e menor {}".format(quantidade,media,maior, menor))
