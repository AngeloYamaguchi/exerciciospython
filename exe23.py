n = int(input("digite um número com 4 digitos"))
u = n//1%10
d = n//10%10
c = n//100%10
m = n//1000%10

print("O nùmero {}".format(n))
print(" Tem sua undade de milhar é {}".format(m))
print("centena é {}, dezena {} é umidade é {}".format(c,d,u))