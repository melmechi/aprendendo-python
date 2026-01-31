#remover caracteres do começo ou fim da string
texto= "   Eai Galera   " 
print(texto.strip())  #"Eai galera"(sem os espaços)
#tirar um caractere específico
texto= "***Eai Galera***" 
print(texto.strip("*")) #"Eai galera"

#Deixa só a primeira letra maiúscula e o resto minúsculo
print("pyThon".capitalize()) # Python

#contar quantas vezes algo aparece numa string
print("banana".count("a")) #3

#Verificar se a string termina ou começa com algo
print("python".endswith("on")) #True
print("python".startswith("on")) #False

#procurar um texto dentro de outro (se não encontrar retorna 0)
texto = "Eu amo os minions"
print(texto.find("m")) #4 (O PRIMEIRO M QUE ENCONTROU)
print(texto.find("y"))  #-1, não tem y no texto

#trocar uma parte do texto
novo = texto.replace("minions", "pokémons")
print(novo) #"Eu amo os pokémons"

#divide a string em uma lista
frase = "pera uva acerola caqui"
lista = frase.split()
print(lista)   #['pera', 'uva', 'acerola', 'caqui']

#juntar uma lista numa string
letras = ["M", "E", "L", "O", "D", "Y"]
print("".join(letras))   #MELODY
#pode usar também separador
print("-".join(letras)) #M-E-L-O-D-Y

#deixar tudo em minúsculo
print("PYTHON".lower())   #python
#deixar tudo maiúsculo
print("python".upper())   #PYTHON