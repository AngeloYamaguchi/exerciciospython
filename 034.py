salário = float(input ("Digite o valor do salário"))
a1 = salário*1.1
a2 = salário*1.15
if salário > 1250:
    print("O seu seu novo salário será {:.2f}".format(a1))
if salário <= 1250:
    print("O salário era R${} seu novo salário será R${:.2f}".format(salário,a2))




