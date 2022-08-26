lanche = ("Hamburguer","Suco ","pizza", "pudim")
print(lanche)
for comida in lanche:
    print(f"Eu comi pra caraba! eu comi {comida}")
for cont in range (1, len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posiçao {cont}")
for posição, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posiçao {posição}")
    