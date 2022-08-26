def contador(i, f, p):
    """
    ->Faz a contagem e mostra na tela
    :param i: inicio da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem retorno

    """
    c = i
    while c <= f:
        print(f' {c}',end="")
        c += p
    print(f' Fim')
help(contador)






contador(0, 10 ,1)