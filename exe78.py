list = []
c = 0

menor = 0
for c in range(0,5):
    list.append(int((input(f" Digite um Número posição  {c}:  "))))
print("="*30)
print(f" Você digitou os seguintes valores {list}")
print()
print(f'o maior valor foi {max(list)} na posição ',end=' ')
for i, v in enumerate(list):
    if v == max(list):
        print(f'{i}....',end='')
print()
print(f'o Menor valor foi {min(list)} na posição ',end=" ")
for i, v in enumerate(list):
    if v== min(list):
        print(f'{i}....',end= "")
print()
