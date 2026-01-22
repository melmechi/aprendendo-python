#Simulação de Caixa eletrônico


saldo = 500
menu = -1

while menu != 0: 

    menu = int(input("Bem vindo ao menu inicial!\n1 - Ver saldo\n2 - Fazer saque\n0 - Sair\nEscolha uma opção: "))

    if menu == 1:
        print(f"O seu saldo é de {saldo} reais.") 

    elif menu == 2:
        saque = float(input("Informe o valor do saque (Ou digite 0 para sair): "))
        if saque == 0:
            pass
        elif saque > saldo:
            print("Saldo insuficiente.")
        else:
            saldo -= saque
            print(f"Saque efetuado. Seu saldo agora é {saldo} reais.")
                
    elif menu == 0:
        break

    else:
        print("Opção inválida. Tente novamente")

print("Operação Finalizada.")