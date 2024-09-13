
class Banco:

    def __init__(self):
        self.__lista_usuarios = []
        self.__lista_contas = []
        self.__saldo = 0
        self.__log = []

    def menu(self):
        menu = '''Bem-vindo ao SacaFacil, Qual operacao deseja:
            1 - Sacar
            2 - Depositar
            3 - Extrato
            4 - Cadastrar usuario
            5 - Cadastrar Conta
            6 - Lista Conta
            7 - Lista Usuario
            8 - Sair
        '''
        return int(input(menu))
    
    def cadastrar_usuario(self, nome, cpf, dt_nascimento, endereco):
        if nome and dt_nascimento and cpf and endereco:
        
            for i in self.__lista_usuarios:
                if i["cpf"] == cpf:
                    print("Usuário já cadastrado")
                    return

            
            usuario = {"nome": nome, "cpf": cpf, "data_de_nascimento": dt_nascimento, "endereco": endereco}
            self.__lista_usuarios.append(usuario)
            print("Usuário cadastrado com sucesso")
        else:
            print("Dados incompletos para cadastro")

    def cadastrar_conta(self, numero_conta, usuario, agencia="0001"):
        if usuario:
            # Verifica se o usuário (CPF) está cadastrado
            for i in self.__lista_usuarios:
                if i["cpf"] == usuario:
                    self.__lista_contas.append({"usuario": usuario, "n_conta": numero_conta, "agencia": agencia})
                    print("Conta cadastrada com sucesso")
                    return
            # Se nenhum usuário for encontrado
            print("Usuário não cadastrado")
        else:
            print("Usuário não fornecido")
    
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

    def depositar(self, valor,/):
        if valor > 0:
            self.__saldo += valor
            self.__log.append({"Deposito realizado": f"{valor:.2f}"})
            print(f"Realizado o deposito no valor de R${valor:.2f}")
        else:
            print("Não foi possivel depositar valor negativo")

    def extrato(self):
        return print(f"transações feitas: {self.__log} \n\n Saldo atual da conta: {self.__saldo}")
    
    def get_lista_usuario(self):
        return print( self.__lista_usuarios)
    
    def get_lista_conta(self):
        return print(self.__lista_contas)



def main():
        
    banco = Banco()    
    count_saque = 0
    numero_conta = 0

    while True:    
        opcao = banco.menu()
        
        if opcao == 1:
            if count_saque <= 3:
                saque = float(input("Informe o valor do Saque: "))
                banco.sacar(saque = saque)
                count_saque += 1
            else:
                print("Já foi feito o numero maximo de saques.")

        elif opcao == 2:
            valor = float(input("Digite o valor que deseja depositar: "))
            banco.depositar(valor)

        elif opcao == 3:
            banco.extrato()

        elif opcao == 4:
            nome = str(input("digite seu nome: "))
            cpf = str(input("digite seu cpf: "))
            dt_nascimento = str(input("digite sua data de nascimento"))        
            endereco = str(input("digite seu endereco"))
            banco.cadastrar_usuario(nome, cpf, dt_nascimento, endereco)

        elif opcao == 5:
            usuario = str(input("informe o cpf do usuario: "))
            banco.cadastrar_conta(numero_conta, usuario)
            numero_conta += 1

        elif opcao == 6:
            banco.get_lista_conta()

        elif opcao == 7:
            banco.get_lista_usuario()

        elif opcao == 8:
            break
        else:
            "Opção invalida"
main()
