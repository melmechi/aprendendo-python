def menu():
#Menu com a função n recebe valores (por isso n tem return), e so vai mostrar as
#Strings quando for chamada !DEFINIR A FUNCAO N EXECUTA ELA!
    print("CALCULADORA")
    print("1- Somar")                   
    print("2- Subtrair")                 
    print("3- Multiplicar")
    print("4- Dividir")
    print ("0- Sair")


# === FUNÇÕES DAS OPERAÇÕES ===
#Abaixo cada função recebe dois números (a e b)
# e retorna o resultado da operação, calculam mas só dps o menu decide como mostrar

def soma(a, b):
    return a + b

def subtrair (a, b):
    return a - b                                       

def multiplicar(a, b):
    return a * b

#Essa evita erro de execução, e mostra q funções também podem ter lógica interna
def dividir(a, b):
    if b == 0:                                         
        return "Não é possível dividir por 0"
    return a / b

#Aqui o input acontece SÓ quando a função é chamada
#retorna dois valores ao mesmo tempo
def pedir_numero():
    a = float(input("primeiro número: "))
    b = float(input("segundo número: "))
    return a, b 

# ==== DICIONÁRIO DAS OPERAÇÕES ===
# As chaves são as opções digitadas pelo usuário
# Os valores são as funções correspondentes
#deixa o código mais limpo! substitui vários possíveis "elif
operacoes = {
    "1": soma,                             
    "2": subtrair,               
    "3": multiplicar,
    "4": dividir 
}

# === LOOP PRINCIPAL ===
# Cria um loop infinito, só para quando encontrar um break

while True:   
     print()                            
     menu()
     opcao = input("\033[1mEscolha: \033[0m")
     print()

     if opcao == "0":
        print("Fechando...")
        break                                      #INDENTAÇÃO CORRETA!!!!!!!!!!!!!!!!!!!!!!!
    

    #se a opção existir no dicionário
     elif opcao in operacoes:
        a, b = pedir_numero()
        resultado = operacoes[opcao](a,b)                           # desempacota (a, b)
        print(f"\033[32mO resultado é {resultado}\033[0m")
                

     else:
        print()
        print("Opção inválida, tente novamente:")
            

