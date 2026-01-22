

orçamento =int(input("Digite seu orçamento: "))

if orçamento >= 12:
    print(f"Você pode tomar um cappuccino!")
elif orçamento >= 7:
    print(f"Você pode tomar um café expresso")
else:
    print("Infelizmente você não tem dinheiro o suficiente.")