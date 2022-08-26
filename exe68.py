from  random import randint
while True:
    jogador = int(input("digite um valor"))
    computador = randint(0,10)
    total = jogador + computador
    tipo = " "
    vitoria = 0
    while tipo not in 'PI':
        tipo = str(input("Par ou impar [P/I]")).strip().upper()
    print(f" Você jogou {jogador} e o computador Jogou {computador} Total de {total}")
    print('Deu Par' if total % 2 == 0 else "Deu Inpar")
    if tipo == 'P':
        if total % 2 == 0:
            print("Você venceu")
            vitoria += 1
        else:
            print(" Você pedeu ")
            break
    elif tipo == 'I' :
        if total % 2 == 1:
            print("Você venceu")
            vitoria += 1
        else:
            print('Você perdeu')
            break
    print("Vamos Jogar novamente")


