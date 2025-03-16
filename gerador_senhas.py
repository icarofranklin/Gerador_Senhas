import random #A biblioteca "random" gera números aleatorios

letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%&*()-_=+[]{};:,.<>/?"

caracteres = letras_maiusculas + letras_minusculas + numeros + simbolos
#A senha é composta pela junção dos caracteres indicados acima.

tamanho_senha = int(input("Quantos caracteres deve ter a senha? "))
#Definição do tamanho de senha

senha = [] #Cria uma lista vazia chamada "senha"

for i in range(tamanho_senha): #Loop de repetição que irá rodar "tamanho_senha" vezes.
#Se tamanho_senha = 8, o loop repete 8 vezes.
    caractere_aleatorio = random.choice(caracteres) #Função que escolhe um item aleatório de uma lista
    senha.append(caractere_aleatorio) #append(): Método que adiciona um item ao final da lista


senha_gerada = "" .join(senha)
print("Sua nova senha é: ", senha_gerada)