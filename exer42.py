print("\033[0;31;42m#######\033[0;m"*10)
print("\033[1;30;45mAnalisando o Triângulo\033[m")
print("\033[7;30;45m#######\033[0;m"*10)
r1 = float( input( "\033[7;31;40mprimeiro seguimento\033[m"))
r2= float(input(" \033[1;30;42msegundo seguimento\033[m"))
r3 = float(input( "\033[4;30;45mterceiro seguimento\033[m"))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2+r1:
    print("\033[4;31;42mSim, os 3 seguimentos forman um Triangulo\033[;m",end="")
    if r1 == r2 == r3:
        print("Triangulo Isoceles")

    elif: r1 != r2!= r3 != r1:
     print("Triangulo escaleno")
    else:
        print("escaleno")
else:
    print("\033[1;30;41mNão é possivel formar um triangulo\033[m")

