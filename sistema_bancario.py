 menu = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
======================================
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print(f"\n✅ Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("\n❌ Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n❌ Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print(f"\n❌ Operação falhou! O limite por saque é R$ {limite:.2f}.")
        elif excedeu_saques:
            print(f"\n❌ Operação falhou! Limite de {LIMITE_SAQUES} saques diários atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\n✅ Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("\n❌ Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:\t\tR$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("\nObrigado por usar nosso banco. Até logo! 👋")
        break

    else:
        print("\n❌ Operação inválida! Por favor, selecione novamente.")
