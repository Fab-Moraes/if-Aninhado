conta_normal = False
conta_universitaria = False

saldo = 2000
cheque_especial = 600

saque = float(input("Informe o valor do saque: "))


if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com sucesso com o uso do cheque especial!")
    else:
        print("Não foi possivel realizar o saque. SALDO INSUFICIENTE!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

else:
    print("Sua conta está bloqueada!")
    print("Entre em contato com a central, ligue: 0800-0171")