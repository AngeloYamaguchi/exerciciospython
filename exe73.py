seriea = ("Palmeiras", "Corinthians","Inter",'Athletico-PR','Atlético-MG','Fluminense',
          'Santos','São Paulo','Red Bull', 'Bragantino','Avaí','Ceará','Flamengo','Coritiba','América-MG','Botafogo',
          'Goiás','Atlético-GO','Cuiabá','Juventude','Fortaleza')
print('+='*30 )
print('Os 5 primeiros Colocados')
print('+='*30 )
print(f'{seriea[1:6]}')
print('+='*30 )
print('Os 4 ultimos Colocados')
print(f"{seriea[-4:]}")
print('+='*30 )
print(f'{sorted(seriea)}')
print('+='*30 )
print("O São Paulo está na {} colocação".format(seriea.index('São Paulo')+ 1))

