from datetime import date
ano = int(input("Digite o Ano a analisar"))
bisexto = ano%4 == 0 and ano %100 != 0 or ano % 400 ==0
ano = date.today().year
if bisexto:
    print("Esse O ano {} é Bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))

