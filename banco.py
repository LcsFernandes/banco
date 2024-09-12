# saca 
# limite de 3 e max de 500 por saque


# deposita
# -so valor positivo

# extrato

# todas as transações serao artmazenadas

class Banco:

    def __init__(self):
        self.__saldo = 0
        self.__log = []
    
    def sacar(self, saque):
        if saque <= self.__saldo and saque <= 500:
            self.__saldo -= saque
            self.__log.append({"Saque realizado": f"R${saque:.2f}"})
            print(f"Realizado o saque no valor de R${saque:.2f}")
        else:
            if saque > self.__saldo:
                print("Seu saldo é insuficiente.")
            elif saque > 500:
                print(f"Seu saque no valor de R${saque:.2f} excede o limite de R$500.00 por saque")

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__log.append({"Deposito realizado": f"{valor:.2f}"})
            print(f"Realizado o deposito no valor de R${valor:.2f}")
        else:
            print("Não foi possivel depositar valor negativo")

    def extrato(self):
        return print(f"transações feitas: {self.__log} \n\n Saldo atual da conta: {self.__saldo}")



banco = Banco()    
count_saque = 0

while True:    
    menu = '''Bem-vindo ao SacaFacil, Qual operacao deseja:
            1 - Sacar
            2 - Depositar
            3 - Extrato
            4 - Sair
        '''
    opcao = int(input(menu))
    
    
    if opcao == 1:
        if count_saque <= 3:
            saque = float(input("Informe o valor do Saque: "))
            banco.sacar(saque)
            count_saque += 1
        else:
            print("Já foi feito o numero maximo de saques.")

    elif opcao == 2:
        valor = float(input("Digite o valor que deseja depositar: "))
        banco.depositar(valor)

    elif opcao == 3:
        banco.extrato()

    elif opcao == 4:
        break

    else:
        "Opção invalida"
