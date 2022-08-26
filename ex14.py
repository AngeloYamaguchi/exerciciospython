print('Exercício: Locação de carros')

dias = int(input("qual o numero de dias alugados?"))
km = float(input("Qual a quilometragem percorrida?"))
v = (dias*60)+(km*.15)
print("Sendo o carro alugado por {}dias e percorrido {:.2f} km, o  valor a pagar será {:.2f}".format(dias,km,v))
