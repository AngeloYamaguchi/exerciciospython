n = int(input("Digite um número"))
tot = 0
divisores = 0
for c in range(1,n +1):
    if  n % c == 0:
        print("\033[33m",end= " ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print("{}".format(c),end=" ")
print("\\número {} foi divisível {} números".format(n,tot))
if tot == 2:
    print("Por isso ele é Primo")
else:
    print("ele não é primo")





