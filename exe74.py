import random
from random import randint
sorteados = (random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),)
print(f'Os números sorteados foram ',end=' ')
for n in sorteados:
    print(f'{n}', end=" ")
print(f'\n{max(sorteados)} sendo o maior número')
print(f' E O menor número sorteado foi {min(sorteados)}')

