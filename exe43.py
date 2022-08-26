peso = float(input("Qual seu peso?"))
h = float(input("qual sua altura"
                ""))
imc = peso/h**2
print (" seu imc é{:.2f}".format(imc))
if imc < 18.5:
    print("Abaixo do peso")
elif  18.5 <= imc <25:
    print("Peso ideal")
elif 25 <= imc <30:
    print("Sobre peso")
elif 30 <= imc <40:
    print("Obesidade")
else:
    print("Obesidade Morbida")



