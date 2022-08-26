nota1 = float(input("Digite Sua primeira nota"))
nota2 = float(input("Digite sua Segunda nota"))
media = (nota1 + nota2)/2
if media >= 7:
    print("Você foi aprovado Sua Média foi {} ".format(media))
elif media < 7 and media > 5:
    print("Sua média foi {} Você está de recuperação".format(media))
else:
    print("Você foi reprovado")