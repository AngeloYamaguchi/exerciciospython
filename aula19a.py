brasil= []
estado = {}
for c in range (0,3):
    estado['nome'] = str(input('O nome do estado'))
    estado['sigla'] = str(input('Sigla do Estado'))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f'{v} {e}')