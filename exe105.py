def notas(*n, sit = False):
    """
    --> Função Notas
    :param n: as Respectivas notas
    :param sit: Situação que varia de Bom, razoavél, Ruim.
    :return: retorna um dicionário com várias informaçôes das notas dos alunos

    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit:
        if r['Média'] >= 7:
            r['Sitiação'] = 'boa'
        elif r['Média'] >= 5:
            r['Sitiação'] = 'Razoavel'
        else:
            r['Sitiação'] = 'Ruim'
    return r



resp = notas(9.5, 5 ,6 ,5 , 4, sit= True)
print(resp)
