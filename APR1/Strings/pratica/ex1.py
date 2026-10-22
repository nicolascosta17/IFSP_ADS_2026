"""Escreva um programa que remove a primeira ocorrência de uma letra de
uma string. A string e a letra devem ser fornecidas pelo usuário.
"""

string = input("Digite a palavra: ")
letra_eliminada = input("Digite letra que será retirada da palavra (A letra tserá eliminada apenas uma vez): ")
cont = 0
i = 0
print("Palavra: ",string)
print("Letra: ",letra_eliminada)
while i < len(string) and cont == 0:
    if letra_eliminada == string[i]:
        string = string[:i] + string[i+1:]
        cont+=1
    i+=1
print("Palavra: ",string)
