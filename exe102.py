def fatorial(n, show = False):
    """
    -> Função Fatorial
    :param n: O número fatorial a calcula.
    :param show: (opcional) mostrar ou não a conta.
    :return: retorna o fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f' {c}',end='')
            if c>1:
                print(f" X",end='')
            else:
                print(f" = ",end='')
        f *= c
    return f


print(fatorial(5, show= True))
help(fatorial)