from model.cliente import PessoaFisica
from model.conta import ContaCorrente
from model.transacao import Deposito, Saque

class BancoController:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def buscar_cliente(self, cpf):
        return next((c for c in self.clientes if c.cpf == cpf), None)

    def criar_cliente(self, nome, cpf, data, endereco):
        if self.buscar_cliente(cpf):
            return False
        cliente = PessoaFisica(endereco, nome, data, cpf)
        self.clientes.append(cliente)
        return True

    def criar_conta(self, cpf):
        cliente = self.buscar_cliente(cpf)
        if not cliente:
            return None

        conta = ContaCorrente(len(self.contas)+1, cliente)
        cliente.adicionar_conta(conta)
        self.contas.append(conta)
        return conta

    def depositar(self, cpf, valor):
        cliente = self.buscar_cliente(cpf)
        if not cliente or not cliente.contas:
            return False

        return Deposito(valor).registrar(cliente.contas[0]) 

    # def sacar(self, cpf, valor):
    #     cliente = self.buscar_cliente(cpf)
    #     if not cliente or not cliente.contas:
    #         return False

    #     return Saque(valor).registrar(cliente.contas[0]) 

    def sacar(self, cpf, valor):
        cliente = self.buscar_cliente(cpf)
        if not cliente or not cliente.contas:
            return False, "CLIENTE OU CONTA NÃO ENCONTRADO"

        return Saque(valor).registrar(cliente.contas[0])

    def obter_extrato(self, cpf):
        cliente = self.buscar_cliente(cpf)
        if not cliente or not cliente.contas:
            return None

        conta = cliente.contas[0]
        return conta

    def listar_contas(self):
        return self.contas