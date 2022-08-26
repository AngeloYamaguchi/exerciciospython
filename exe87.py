matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = maiorl2 = somacl3 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] =int(input(f'Digite um numero na posição[{l,c} ]'))
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
        if matriz[l][c]%2 == 0:
            somapar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares é {somapar}')
for l in range(0,3):
    somacl3 += matriz[l][2]
s2 = matriz[1][0] + matriz[1][1] + matriz[1][2]
print(f'A soma da linha 2 é {s2}')
for c in range(0,3):
    if c == 0:
        maiorl2 = matriz[1][c]
    elif maiorl2 > matriz[1][c]:
        maiorl2 = matriz[1][c]
print(f" o Maior valor da linha 2 é {maiorl2}")