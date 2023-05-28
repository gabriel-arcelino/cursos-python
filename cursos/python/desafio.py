menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Quanto deseja depositar?: "))

        if valor < 0:
            print("Erro! O valor de depósito é inválido.")
        else:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

    elif opcao == "s":
        valor = float(input("Quanto deseja sacar?: "))

        if valor > saldo:
            print("Erro! Saldo insuficiente.")

        elif valor > limite:
            print("Erro! O valor do saque excede o limite.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Erro! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Erro! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")