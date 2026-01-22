print("Bem vindo ao jogo de adivinhação!")

capital_bahia = "Salvador"
tentativa = input("Qual a capital da Bahia? ")


while tentativa != capital_bahia:
    tentativa = input("Não foi dessa vez! Tente novamente: ")
    
   
print("Parabéns, você acertou!")
