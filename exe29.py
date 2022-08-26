velocidade = float(input("Qual a velocidade atual do carro?"))
vlimite = 80
multa = (velocidade - vlimite)*7
if velocidade > vlimite:
    print("Você foi multado em R${:.2f}".format(multa))
print("Tenha um bom dia dirija com cuidado")