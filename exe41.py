from datetime import date
nascimento = int(input("Digte o ano de Nascimento do Atleta"))
ano_atual= date.today().year
idade = ano_atual- nascimento
if idade <= 9:
    print("Você tem {} anos, sua categoria é Mirim ".format(idade))
elif idade <=14:
    print("Você tem {} anos, sua categoria é Infantil ".format(idade))
elif idade  <= 19:
    print("Você tem {} anos, sua categoria é Junior ".format(idade))
elif idade  <= 25:
    print("Você tem {} anos, sua categoria é Sênior ".format(idade))
else :
    print("Você tem {} anos, sua categoria é Master ".format(idade))


