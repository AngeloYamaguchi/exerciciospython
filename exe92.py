from datetime import datetime
dados = dict()
dados["nome"]= str(input('Nome'))
nasc= int(input("ano de nascimento"))
dados['idade']= datetime.now().year - nasc
dados['carteira']= str(input('Cateira de trabalho (se não tem digite 0)'))
if dados['carteira'] != 0:
    dados['contratração']= int(input('ano de contratação'))
    dados['salário'] = float(input('digite o salário inicial'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratração'] + 35) - datetime.now().year)
print('-='*30)
print()
for v, k in dados.items():
    print(f'{v} é igua {k}')
