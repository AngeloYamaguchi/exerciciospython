viagem = float(input("Qual a distância percorrida?"))
if viagem <=200:
    print("Seu Valor a pagar é R${} ".format(viagem*0.50))
else:
    print("Seu Valor a pagar é R${} ".format(viagem * 0.45))
