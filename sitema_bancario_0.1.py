'''
Operação de depósito
Deve ser possivel depositar valores positivos.

A v1 do projeto trabalha apenas com um usuário,
dessa forma não precisamos nos preocupar em identificar qual
é o número da agência e conta bancária. Todos os depósitos
devem ser armazenados em uma variável e exibidos na 
operação de extrato.
'''
'''
Operação de saque

O sitema deve permitir realizer 3 saques diários com limite
máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo
em conta, o sistema deve exibir uma mensagem informando que
não será possível sacar o dinheiro por falta de saldo. Todos
os saques devem ser armazenados em uma variável e exibidos 
na operaçãode de extrato.
'''

'''
Operação de extrato

Essa operação deve listar todos os depósitos e saques
realizados na conta. No fim da listagem deve ser exibido 
o saldo atual da conta.

Os valores devem ser exibidos utilizando o formato R$ xxx.xxx,
exemplo:
1500.45 = R$1500.45
'''

menu = """

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

saldo = 0
limite = 500
extrato = ''
qtd_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).upper()

    if opcao == 'D':
        # Recebe a entrada do usuário e verifica se é um número
        print('Deposito')
        entrada = input("Quantia a ser depositada:\nR$  ")
        if entrada:
            
            try:
                deposito = float(entrada)
                saldo += deposito

                # Acrescenta um valor na variável extrato todas as vezes que o hover depósito.
                extrato += f'Depósito R$ {deposito:.2f}\n'
                                    
            #Mensagem de erro caso não seja um número ou caso ouver caracteres estranhjos.    
            except ValueError:
                print('Número inválido.')   
            
            print(f'Saldo: R${saldo}')
    # Recece a entrada do usuário verifica se é um número        
    elif opcao == 'S':
        print('Saque')
        saque = input("Quanto deseja sacar?\nR$ ")

        if saque:
            try:
                saques = float(saque)
                #Somente faz o saque se não entrar em um desses requisitos
                if saques > 0 and saques <= limite and saques <=  saldo:
                    if qtd_saques < LIMITE_SAQUES:
                        print(f'Saldo R$: {saldo}')
                        saldo = saldo - saques                    
                        qtd_saques += 1
                        # Acrescenta um valor na variável extrato todas as vezes que o hover saque
                        extrato += f'Saques -R${saques:.2f}\n'
                        # print(qtd_saques)
                        print(f"Valor sacados:  -R$ {saques}")
                        print(f'Saldo atual: R$ {saldo}')
                    else:
                        print(f'Quantia máxima de saques diários atingida {qtd_saques}/{LIMITE_SAQUES}')    
                # Caso o número seja negativo
                elif saques < 0:
                    print("valor inválido.")
                # Caso o usuário tente sacar mais que o limite permitido por saque.
                elif saques > limite:
                    print(f'Limite de R$ {limite} excedido.')
                    print("Tente novamente...")
                # Caso o usuário tente sacar um valor maior que o saldo total da conta.
                elif saques > saldo:
                    print(f"Quantia solicitada maior {saques} que saldo atual R$ {saldo} ")                    
            #Mensagem de erro caso não seja um número ou caso ouver caracteres estranhjos.
            except ValueError:
                print("Valor inválido.")    


    elif opcao == 'E':
        print('Extrato')
        print()
        print(extrato)

    elif opcao == 'Q':
        print('Sair')

        break