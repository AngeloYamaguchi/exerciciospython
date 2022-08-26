
ex = str(input(" a expressão  matemática")).strip()
Dc = (ex.count("("))
Ec = (ex.count(")"))
if Dc == Ec :
    print('Seu expresão esta correta')
else:
    print( 'Sua expressão esta Errada ! está faltando um Parenteses')
