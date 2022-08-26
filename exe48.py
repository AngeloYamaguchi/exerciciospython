soma= 0
cont = 0
for n in range(3,501,2):
    if n  % 3 == 0:
        soma +=  n
        cont += 1
print("A soma de todos os valores {} solicitados é{}.".format(cont,soma))