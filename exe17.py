from math import sin, cos,tan,radians
print("Cálculo do Seno, Cosseno e Tangente")
angulo= float(input("Digite o ângulo"))
seno = sin(radians(angulo))
cosseno = cos((angulo))
tangente = tan((angulo))

print("O  valor seno é {:.2f} , cosseno {:.2f} e Tangente {:.2f}".format(seno, cosseno,tangente))
