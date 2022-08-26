num = (int(input('digite um número')),int(input('digite um número')),
       int(input('digite um número')),int(input('digite um número'),))
print(f' você digitou os Números{ num}')
print(f"o Número 9 apareceu {num.count(9)} vezes")
if 3 in num:
       print(f" o 3 apareceu na posição {num.index(3) +1}")
else:
       print(" O valor 3 não foi digitado")
print("Os valores pares digitados foram ", end= "")
for n in num:
       if n % 2 == 0:
              print(n, end=" ")