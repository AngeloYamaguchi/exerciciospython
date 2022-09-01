import abc
class ContaCorrente:
    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita (self,valor):
        self.saldo += valor


    def __str__(self):
        return "[>>codigo {} saldo {}<<]".format(self.codigo, self.saldo)

conta1 = ContaCorrente(15)

conta1.deposita(500)

conta2 = ContaCorrente(21)
conta2.deposita(300)

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta1,conta2]
print(contas[0],contas[1])

contas.insert(0,76)

print(contas[0],contas[1],contas[2])

def deposita (conta) :
    novo_saldo = conta[1] + 100
    cogigo = conta[0]
    return (cogigo,novo_saldo)

deposita(conta1)


