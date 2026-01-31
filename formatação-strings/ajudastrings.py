#FORMATAÇÃO DE STRING

nome = "MELODY"

print(f"{nome:=^20}")      # RESULTADO: =======MELODY=======

 #também é possível fazer direto na string, sem usar variável
 #formato:

print(f"{'MELODY':=^20}")    #o RESULTADO será o mesmo


#a ordem é a seguinte:
#{valor:preenchimento alinhamento largura}
#então nesse caso:
#valor (palavra): nome = "MELODY"
# o sinal da formatação é ":"
#preenchimento: caractere que vai se repetir para completar o espaço, nesse caso é o "="
#alinhamento: > alinhar o valor a esquerda, direita <, alinhar ao centro ^ 
#largura total: quantos caracteres a linha inteira vai ter, nesse caso 20


#Também é possível utilizar essa formatação para decidir quantas casas decimais vc quer num float
#Exemplo
print(100 / 73) # sem formatação resultado = 1.36986301369863

#se quero um resultado com somente duas casas decimais:

print(f"{100/73:.2f}")          #RESULTADO = 1.37
#FORMATO: (f"{valor:formato})
# . = casas decimais; 2 = quantidade; f = número float


