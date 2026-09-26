'''Em geometria analítica, dois vetores podem ser definidos como a=<a1,a2,a3> e
b=<b1,b2,b3>. Escreva um programa que leia dois vetores a e b (duas listas) de
três posições cada e efetue o produto escalar entre eles. O produto escalar é obtido
por ab = a1b1+a2b2+a3b3. De acordo com o exemplo dado abaixo, o calculo a ser
efetuado será: 1x5+4x2+7x3'''


#CRIAÇÃO DAS LISTAS
listaA = []
listaB = []
listaC = []

#ALIMENTANDO AS LISTAS
print("Digite os primeiros 3 números da primeira lista: ")
a = 0
b = 0
while a < 3:
    num = int(input())
    listaA.append(num)
    a+=1
print("Digite os primeiros 3 números da segunda lista: ")
while b < 3:
    num = int(input())
    listaB.append(num)
    b+=1

#FAZENDO OPERAÇÃO
for i in range(len(listaA)):
    valor = listaA[i] * listaB[i]
    listaC.append(valor)

#IMPRIMINDO LISTA
print("Lista A:")
for i in range(len(listaA)):
    print(listaA[i], end="; ")

print("")
print("Lista B:")
for i in range(len(listaB)):
    print(listaB[i], end="; ")

print("")
print("Lista C:")
for i in range(len(listaC)):
    print(listaC[i], end="; ")
