frase = str(input(" Digite uma frase")).strip().upper()
palavra = frase.split()
junta= ''.join(palavra)
inverso = junta[::-1]

if inverso == junta:
    print("Temos um Palindromo!")
else:
    print("a frase não é um palindromo")