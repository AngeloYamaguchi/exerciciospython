Listagem = ('Lapis','2.00',
            'Borracha','3.00',
            'Caneta',' 2.50',
            'Caderno', '1.50',
            'teclado','20.50',
            'Shampú','9.50',
            'sabonete','3.50',
            'Papel higiênico', '25.50',)
print('='*40)
print(f'{"Listagem de Peços":^40}')
print('='*40)
for pos in range(1,len(Listagem)):
    if pos % 2 == 0 :
        print(f'{Listagem[pos]:.<30}',end='')
    else:
        print(f"R${Listagem[pos]:>7}")
print('=' * 40)