'''Faça um programa que simule um jogo da loto. O computador deve gerar 5
números aleatoriamente entre 50 possíveis (0 a 49), armazenando as dezenas
sorteadas em um vetor (dez_sort) de 5 posições. Em seguida, o usuário deverá ler
uma lista com 10 posições, representando a aposta (conforme o exemplo abaixo).
O programa deve, então, verificar e imprimir uma mensagem mostrando quantos
números o usuário acertou. De acordo com o exemplo abaixo o usuário acertou 4
dezenas.'''

import random

dez_sort = []
aposta = []
acertos = []
i=0
sorte = 0
while i < 5:
    num = random.randint(0, 10)
    dez_sort.append(num)
    i+=1

print("Aposte 10 números de 0 a 49:")
while sorte < 10:
    valor = int(input())
    if valor >= 0 and valor <= 49:
        aposta.append(valor)
        sorte += 1
    else: 
        print("Valor não está dentro dos esperados para o sorteio. Insira novamente!")


print("Valores Sorteados: ")
for i in range(len(dez_sort)):
    print(dez_sort[i], end="; ")

print("")
print("Suas apostas: ")
for i in range(len(aposta)):
    print(aposta[i], end="; ")
    for j in range(len(dez_sort)):
        if aposta[i] == dez_sort[j]:
            acertos.append(aposta[i])

print("")
print("Acertos: ")
for i in range(len(acertos)):
    print(acertos[i], end="; ")


