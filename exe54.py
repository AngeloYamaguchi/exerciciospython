from datetime import date


totmaior = 0
totmenor = 0

for pess in range(1,8):
    nascimento = int(input("Digite o ano de nascimento da {}° pessoa".format(pess)))
    idade = date.today().year - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print("Ao todo tivemos {} pessoas maiores de idade".format(totmaior))
print(" E tivemos  {} menores de idade".format(totmenor))


