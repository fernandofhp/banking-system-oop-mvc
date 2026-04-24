import textwrap
import re
from view.config import LARGURA
from utils.cores import VERDE, VERMELHO, AZUL, NEGRITO, RESET
from utils.foramatadores import formatar_moeda


# ===== HELPERS =====

def remover_ansi(texto):
    return re.sub(r'\033\[[0-9;]*m', '', texto)


# ===== MENU =====

def menu():
    menu = """
    ================ MENU ================
    [1]\tDEPOSITAR
    [2]\tSACAR
    [3]\tEXTRATO
    [4]\tNOVA CONTA
    [5]\tLISTAR CONTAS
    [6]\tNOVO CLIENTE
    [7]\tSAIR
    => """
    return input(textwrap.dedent(menu)).strip()


# ===== INPUTS =====

def pedir_cpf():
    return input("CPF: ")

def pedir_valor():
    return float(input("VALOR: "))


# ===== OUTPUTS =====

def mostrar(msg):
    print(f"\n{msg.upper()}")


# ===== LISTAR CONTAS =====

def mostrar_contas(contas):
    if not contas:
        print("NENHUMA CONTA CADASTRADA.")
        return

    print(f"{' CONTAS ':=^{LARGURA}}")

    for c in contas:
        base = (
            f"{'AGÊNCIA: ':.<12}{c.agencia:<8}  "
            f"{'CONTA: ':.<12}{c.numero:<8}  "
            f"{'TITULAR: ':.<12}"
        )

        restante = LARGURA - len(base)
        nome = c.cliente.nome.upper()[:restante]

        print(base + nome.ljust(restante, "."))

    print("=" * LARGURA)


# ===== EXTRATO =====

def mostrar_extrato(conta):
    if not conta:
        print("CONTA NÃO ENCONTRADA.")
        return

    print(f"{' MEGABANK - EXTRATO ':=^{LARGURA}}")

    base = (
        f"{'AGÊNCIA: ':.<12}{conta.agencia:<8}  "
        f"{'CONTA: ':.<12}{conta.numero:<8}  "
        f"{'TITULAR: ':.<12}"
    )

    restante = LARGURA - len(base)
    nome = conta.cliente.nome.upper()[:restante]

    print(base + nome.ljust(restante, "."))
    print("-" * LARGURA)

    if not conta.historico.transacoes:
        print("NENHUMA MOVIMENTAÇÃO.".center(LARGURA))
    else:
        for t in conta.historico.transacoes:

            if t["tipo"] == "Deposito":
                cor = VERDE
            elif t["tipo"] == "Saque":
                cor = VERMELHO
            else:
                cor = ""

            linha_esquerda = (
                f"{t['data']:<20} - "
                f"{cor}{t['tipo'].upper():<10}{RESET}"
            )

            valor_formatado = f"{cor}{formatar_moeda(t['valor'])}{RESET}"

            # tamanho_real = len(remover_ansi(linha_esquerda))
            # espaco = LARGURA - tamanho_real - len(valor_formatado)
            tamanho_real = len(remover_ansi(linha_esquerda))
            tamanho_valor = len(formatar_moeda(t["valor"]))  # SEM ANSI
            espaco = LARGURA - tamanho_real - tamanho_valor

            if espaco < 1:
                espaco = 1

            print(linha_esquerda + " " * espaco + valor_formatado)

    # ===== SALDO =====

    # saldo_str = f"{AZUL}{formatar_moeda(conta.saldo)}{RESET}"

    # base_saldo = f"{NEGRITO}{AZUL}{'SALDO ':.<32}{RESET}"
    # tamanho_real = len(remover_ansi(base_saldo))
    # espaco = LARGURA - tamanho_real - len(saldo_str)

    # if espaco < 1:
    #     espaco = 1

    # print("\n" + base_saldo + " " * espaco + saldo_str)
    valor_limpo = formatar_moeda(conta.saldo)
    valor_colorido = f"{AZUL}{valor_limpo}{RESET}"

    base_saldo = f"{NEGRITO}{AZUL}{'SALDO ':.<32}{RESET}"

    tamanho_base = len(remover_ansi(base_saldo))
    tamanho_valor = len(valor_limpo)

    espaco = LARGURA - tamanho_base - tamanho_valor

    if espaco < 1:
        espaco = 1

    print("\n" + base_saldo + " " * espaco + valor_colorido)

    print("=" * LARGURA)