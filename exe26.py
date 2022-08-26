Frase= str(input("Digite uma frase")).upper().strip()
print("A letra A aparece {} vezes na frase".format(Frase.count("A")))
print("A Letra A aparece primeira vez na posição {}".format(Frase.find("A")+1))
print("A Letra A aparece pela ultima vez na posição {}".format(Frase.rfind("A")+1))
