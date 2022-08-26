from datetime import date
ano = int(input("Digite o ano do seu nascimento"))
atual = date.today().year
idade = atual - ano
if idade == 18:
    print(" Você deve se alistar aimediatamente")
elif idade < 18:
    saldo = 18 -idade
    print("falta anos {} para seu alistamento".format(saldo))
    print("Seu alistamento será em {}".format(saldo + atual))
elif idade > 18:
    saldo2 = idade-18
    print("Já passou o prazo de alistamento. Era para ter Feito o  alistamento á {} ano(s)".format(saldo2))
    print("seu alistamento foi em {}.".format(atual-saldo2))

