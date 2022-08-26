n = str(input("Digite seu Nome Completo")).strip().upper()
nome = n.split()
print("Seu primeiro nome é {}".format(nome[0]))
print("Seu últino nome é {}".format(nome[len(nome)-1]))
