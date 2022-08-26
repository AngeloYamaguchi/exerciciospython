nome = str(input("Digite seu nome completo")).strip()
maiúsculas = nome.upper()
minusculas = nome.lower()
nl= len(nome)-nome.count(" ")
pnome = nome.split()
print("Analisando seu Nome:")
print("Seu nome em Maiúsculas é {}".format(maiúsculas))
print("Seu nome em minusculas é {}".format(minusculas))
print("Seu nome tem {} letras no total".format(nl))
print("Seu Primeiro nome é {} e tem  {} letras".format(pnome[0],len(pnome[0])))


