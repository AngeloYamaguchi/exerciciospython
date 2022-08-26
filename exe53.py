frase = str(input(" Digite uma frase")).strip().upper()
palavra = frase.split()
junta= ''.join(palavra)
''
inverso ='' #inverso = junta[::-1]
for letra in range( len(junta) -1, -1,-1):
 inverso += junta[letra]

if inverso == junta:
    print("Temos um Palindromo!")
else:
    print("a frase não é um palindromo")