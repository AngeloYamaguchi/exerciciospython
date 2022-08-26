pessoas= {'nome': 'Angelo', 'idade': 41,'sexo': 'M'}
print(pessoas)
print(f'{pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('#'*30)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
print('#'*30)
Brasil= []
estado1= {'uf': 'Rio de Janeiro','sigla':'RJ'}
estado2= {'uf': 'São Paulo','sigla':'SP'}

print(estado2)
Brasil.append(estado1)
Brasil.append(estado2)
print(Brasil)
print(Brasil[0]['sigla'])