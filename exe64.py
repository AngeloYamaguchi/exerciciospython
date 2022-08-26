n = 0
n = int(input('DIgite um número [Digite 999 para para]'))
n = cont= soma = 0
while n != 999:
    soma += n
    cont += 1
    n =int(input('DIgite um número [Digite 999 para para]'))
print('Você digitou {} números e a soma etre eles foi {}.'.format(cont, soma))