nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Parabéns, você passou direto!")
elif nota >= 5:
    print("Você ficou de recuperação!")
else:
    print("Você está reprovado!")