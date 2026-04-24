from controller.banco_controller import BancoController
import view.terminal_view as view

def main():
    controller = BancoController()

    while True:
        op = view.menu()

        if op == "1":
            cpf = view.pedir_cpf()
            valor = view.pedir_valor()
            if controller.depositar(cpf, valor):
                view.mostrar("DEPÓSITO REALIZADO")
            else:
                view.mostrar("ERRO")

        # elif op == "2":
        #     cpf = view.pedir_cpf()
        #     valor = view.pedir_valor()
        #     if controller.sacar(cpf, valor):
        #         view.mostrar("SAQUE REALIZADO")
        #     else:
        #         view.mostrar("ERRO")
        elif op == "2":
            cpf = view.pedir_cpf()
            valor = view.pedir_valor()

            sucesso, msg = controller.sacar(cpf, valor)

            if sucesso:
                view.mostrar(msg)
            else:
                view.mostrar(f"⚠️  {msg} ⚠️")

        elif op == "3":
            cpf = view.pedir_cpf()
            conta = controller.obter_extrato(cpf)
            view.mostrar_extrato(conta)

        elif op == "4":
            cpf = view.pedir_cpf()
            if controller.criar_conta(cpf):
                view.mostrar("CONTA CRIADA")
            else:
                view.mostrar("CLIENTE NÃO ENCONTRADO")

        elif op == "5":
            contas = controller.listar_contas()
            view.mostrar_contas(contas)

        elif op == "6":
            nome = input("NOME: ")
            cpf = input("CPF: ")
            data = input("NASCIMENTO: ")
            endereco = input("ENDEREÇO: ")

            if controller.criar_cliente(nome, cpf, data, endereco):
                view.mostrar("CLIENTE CRIADO")
            else:
                view.mostrar("CLIENTE JÁ EXISTE")

        elif op == "7":
            print(" OBRIGADO POR USAR O MEGABANK ".center(60, "="))
            break

        else:
            view.mostrar("OPÇÃO INVÁLIDA")

if __name__ == "__main__":
    main()