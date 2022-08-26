aluno = {}
aluno['nome'] = str(input('Nome do Aluno'))
aluno['média'] = float(input('qual foi média do aluno?'))
print('=-'*30)
if aluno["média"] >= 7:
    aluno["situação"]= 'Aprovado'
elif aluno["média"] < 7:
    aluno["situação"] = 'Recuperação'
elif aluno["média"] < 5:
    aluno["situação"] = 'Reprovado'
for k,v in aluno.items():
    print(f'--{k} é igual {v}')