def menu():
    print("1- Somar")                   #Menu com a função n recebe valores, e so vai mostrar as
    print("2- Subtrair")                 #Strings quando for chamada !DEFINIR A FUNCAO N EXECUTA ELA!
    print("3- Multiplicar")
    print("4- Dividir")
    print ("0- Sair")

def soma(a, b):
    return a + b

def subtrair (a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por 0"
    return a / b



while True:                               #while true pro codigo funcionar em loop e so fechar com o break
     menu()
     opcao = input("Escolha: ")

     if opcao == "0":
        break                                      #INDENTAÇÃO CORRETA!!!!!!!!!!!!!!!!!!!!!!!


     if opcao == "1":
         print("Quais números deseja somar? ")
         a = float(input("primeiro número: "))   #Duas variaveis pois a função recebe e retorna 2 números
         b = float(input("segundo número: "))
         print(f"O resultado é {soma(a, b)}")     # { } para colocar a variável dentro de uma fstring, 
                                                            #valores da função sempre em ( )



     elif opcao == "2":
         print("Quais números deseja subtrair? ")
         a = float(input("primeiro número: "))                #Input já printa a string direto
         b = float(input("segundo número: "))
         print(f"O resultado é {subtrair(a, b)}")


     elif opcao == "3":
         print("Quais números deseja multiplicar? ")
         a = float(input("primeiro número: "))
         b = float(input("segundo número: "))
         print(f"O resultado é {multiplicar(a, b)}")


     elif opcao == "4":
         print("Quais números deseja dividir? ")
         a = float(input("primeiro número: "))
         b = float(input("segundo número: "))
         print(f"O resultado é {dividir(a, b)}")

     else:
         print("Opção inválida")

