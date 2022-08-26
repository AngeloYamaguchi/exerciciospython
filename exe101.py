def voto(nasc):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual- nasc
    if idade < 16:
        return f'  com {idade} anos Não é permitido votar'
    elif 16 <= idade < 18 or idade> 65:
        return f'com {idade} o  Voto é facultativo'
    else:
        return f' tem {idade} anosVoto obrigatorio'



nasc = int(input(' Que ano vc nasceu?'))
print(voto(nasc))