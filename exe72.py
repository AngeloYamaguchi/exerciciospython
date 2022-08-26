print("Números Por extenso")
print('-'*25)
nextenso = ('zero',"um", 'dois', "três",'quatro','cinco', 'seis','sete','oito','nove','dez',
            'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito'\
    ,'dezenove','vinte',)
while True:
    n = int(input('digite um numero'))
    if 0 <= n <= 20:
            break
    print("tente novamente", end= " ")
print(f"{nextenso[n]}")
while True:
    continuar= str(input("quer continuar ? [S/N]")).strip().upper()
    if continuar == 'S':
      continuar == n
    if continuar == "N":
        break
print("Fim")






