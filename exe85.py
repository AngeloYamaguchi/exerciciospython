numeros = [[], []]
n = 0
for c in range(0,7):
   n = int(input(f"Digite {c}° um numero"))
   if n % 2 == 0:
      numeros[0].append(n)
   else:
      numeros[1].append(n)
print('*='*30)
print(numeros)
print(f'ímpares{numeros[1]}')
print(f'pares{numeros[0]}')
print(f'{sorted(numeros[1])}')
