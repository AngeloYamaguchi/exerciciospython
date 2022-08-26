import math
print ("Calculo  do triangulo Retângulo")
a = float(input("Digite o valor do cateto Oposto"))
b = float(input(" digite valor cateto adjacente"))
hi = math.hypot(a, b)


print("O valor da hypotenusa é {:.2f}".format(hi))
