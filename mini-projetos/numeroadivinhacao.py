print("Bem vindo ao jogo de adivinhação!")

numero_secreto = 13
tentativa = 0


while tentativa != numero_secreto:
    tentativa = int(input("Digite um número de 1 a 20: "))
    if tentativa < numero_secreto:
        print(f"O número secreto é maior que {tentativa}")
    elif tentativa > numero_secreto:
        print(f"O número secreto é menor que {tentativa}")
    else:
        print("Parabéns você acertou!")
