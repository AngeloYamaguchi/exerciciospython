sexo = str(input("Digite o sexo da pessoa [F/M]")).strip().upper()
while sexo not in "MnFf":
    sexo =str(input("Dados inválidos. por favor digite seu sexo")).strip().upper()
print("Sexo {} registrado com sucesso.".format(sexo))
