from abc import ABCMeta
class Conta:
    def __init__(self,codigo):
        self._codigo = codigo
        self.saldo = 0
        
    def deposita(self,valor): 
        self._saldo += valor
        
    
    def __str__(self):
        return ">>Codigo {} Saldo {}<<".format(self._codigo, self.saldo)


def abstractmethod(args):
    pass


class ContaCorrente(Conta):       
    
    @abstractmethod
    def passa_o_mes(self):
        pass

class Poupanca(Conta) :
    
    def passa_o_mes(self):
        self.saldo *= 1.01
        self.saldo -= 3
class ContaInvestimento:
    pass
        