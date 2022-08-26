print("Finaceira")
imóvel = float(input(" Valor do imóvel"))
salário = float(input("Digite o valor do Salário"))
anos = int(input('Em Quantos anos pretende pagar?'))
prestação = imóvel/(anos*12)

if prestação < salário*.30:
    print(" Sendo o seu  salário {;.2f} O um imóvel no valor de R${:.2f} Financiado em {} anos a parcela será de {:.2f}".format(salário,imóvel,anos,prestação))
else:
    print(" O emprestimo não pode ser consedido")
