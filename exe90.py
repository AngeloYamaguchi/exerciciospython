aluno = {}
aluno['nome'] = str(input('Nome do Aluno'))
aluno['média'] = float(input('qual foi média do aluno?'))
print('=-'*30)
print(f'-- O nome é igual {aluno["nome"]}')
print(f'-- A média de {aluno["nome"]} foi {aluno["média"]}')
if aluno["média"] >= 7:
    print(f'-- A Situção é aprovado')
elif aluno["média"] < 7:
    print(f'-- A situação é igual Recuperação')
elif aluno["média"] < 5:
    print(f'-- Aluno Reprovado')
print()
