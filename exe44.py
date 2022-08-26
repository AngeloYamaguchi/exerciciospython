print("{:=^40}".format("lojas Leo"))
preço = float(input("Qual o valor das compras?"))

print("         Formas de pagamentos")
print("[1] ávista dinheiro ou cheque 10% de desconto")
print("[2] á vista no cartão 5% de desconto")
print("[3] 2x no cartão sem Juros")
print("[4] 3x ou mais no cartão (20% juros)")
opção = int(input("Escolha opção de pagamento"))
if opção ==1:
    print(" O valor da pagamento será {:.2f}".format(preço*.9))
elif opção == 2:
    print(" O valor da pagamento será {:.2f}".format(preço * .95))
elif opção == 3:
    print(" O valor da pagamento será  2 parcelas iguais de {:.2f}".format(preço/2))
elif opção == 4:
    print(" O valor da pagamento será {:.2f}".format(preço *1.2))