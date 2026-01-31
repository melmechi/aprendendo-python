#como RECORTAR um intervalo de palavras usando slicing?
#começa no indice x : para antes do indice y

texto = "python"


print(texto[0:4])         #pyth

#sem começo definido, então vai do indice 0 até antes do 3 
print(texto[:3])  #pyt

#sem fim definido então vai do indice indicado até o fim
print(texto[3:])   #hon

#inverter string
print(texto[::-1]) # nohtyp

#pular caracteres
print(texto[::2])  #pula de 1 em 1 letra  = pto
print(texto[::3])  #pula 2 letras         = ph