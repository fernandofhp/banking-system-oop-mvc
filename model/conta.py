from .historico import Historico

class Conta:
    def __init__(self, numero, cliente):
        self._agencia = "0001"
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        if valor <= 0 or valor > self._saldo:
            return False
        self._saldo -= valor
        return True

    def depositar(self, valor):
        if valor <= 0:
            return False
        self._saldo += valor
        return True

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    # def sacar(self, valor):
    #     numero_saques = len([
    #         t for t in self.historico.transacoes
    #         if t["tipo"] == "Saque"
    #     ])

    #     if valor > self.limite or numero_saques >= self.limite_saques:
    #         return False

    #     return super().sacar(valor)

    def sacar(self, valor):
        if valor <= 0:
            return False, "VALOR INVÁLIDO"

        if valor > self._saldo:
            return False, "SALDO INSUFICIENTE"

        numero_saques = len([
            t for t in self.historico.transacoes
            if t["tipo"] == "Saque"
        ])

        if valor > self.limite:
            return False, "LIMITE POR SAQUE EXCEDIDO"

        if numero_saques >= self.limite_saques:
            return False, "LIMITE DE SAQUES EXCEDIDO"

        self._saldo -= valor
        return True, "SAQUE REALIZADO"