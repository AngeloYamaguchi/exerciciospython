class ContaSalario:

    def __str__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        return self._codigo == outro.codigo  and self._saldo == outro._saldo

    def __lt__(self, outro):
        return self._saldo < outro.saldo




    def deposita(self,valor):
        self._saldo += valor

    def _str_(self):
        return "[>>Codigo {} SAldo {} <<]".format(self._codigo, self._saldo)


conta1 = ContaSalario(37)
conta2 = ContaSalario(37)


