palavras = ('laranja','Sabor', 'noticia',  'relogio',  'garota', 'menino', 'programador',)
for p in palavras:
    print(f'\nNa Palavra {p.upper()} temos as vogais ',end='')
    for letra in p:
        if letra.lower() in "aeiou":
            print( letra,end='')
