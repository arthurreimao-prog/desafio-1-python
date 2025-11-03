from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[cu] Cadastrar usuário
[cc] Criar Conta de usuário
[q] Sair

=> """

def deposito (saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + f" Depósito realizado no valor de R$ {valor:.2f}.\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def saque (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques já utilizado.")
    elif valor > 0:
        saldo -= valor
        extrato += str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + f" Saque realizado no valor de R$ {valor:.2f}.\n"
        numero_saques += 1
        print(f"Pegue seu dinheiro no local indicado. Você já efetuou {numero_saques} saques nesse mês.")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def mostrar_extrato (saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_usuario(clientes):
    print ("Vamos começar o seu cadastro. Favor fornecer as informações abaixo:")
    cpf = input("Digite o número do seu CPF (somente números, sem pontos ou traços): ")
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print ("CPF já está cadastrado.")
            return             
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento no formato DD/MM/AAAA: ")
    rua = input("Digite a rua onde mora: ")
    numero = input("Digite o numero do seu prédio ou casa: ")
    bairro = input("Digite o bairro onde mora: ")
    cidade = input("Digite a cidade onde mora: ")
    estado = input("Digite o estado onde mora: ")
    endereco = rua + ", " + numero + " - " + bairro.title() + " - " + cidade.title() + "/" + estado.upper()
    clientes.append({"nome" : nome, "data_nascimento" : data_nascimento, "cpf": cpf, "endereco" : endereco})
    print ("Usuário criado com sucesso!")

def criar_conta(agencia, numero_conta, clientes, contas):
    cpf = input("Digite o número do seu CPF (somente números, sem pontos ou traços): ")
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print ("Conta criada com sucesso.")
            contas.append({"agencia" : agencia, "numero_conta" : numero_conta, "cliente" : cliente})
    print("Usuário não cadastrado.")

AGENCIA = "0001"
LIMITE_SAQUES = 3

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
clientes = []
contas = []


while True:

    opcao = input(menu)
    if opcao == "d":
        saldo, extrato = deposito(saldo, float(input("Informe o valor do depósito: ")), extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = saque(saldo = saldo, valor = float(input("Informe o valor do saque: ")), extrato = extrato, limite = limite, numero_saques = numero_saques, limite_saques = LIMITE_SAQUES)

    elif opcao == "e":
        mostrar_extrato(saldo, extrato = extrato)
    
    elif opcao == "cu":
        cadastrar_usuario(clientes)
    
    elif opcao == "cc":
        numero_conta = len(contas) + 1
        criar_conta(AGENCIA, numero_conta, clientes, contas)
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")